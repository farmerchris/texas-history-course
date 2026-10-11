"""Build lesson pages from the Lesson 4 page used as a template.
Usage: python3 build.py lessons/l05.py [more...]
  -> out/<slug>.html  full page for local testing
  -> pub/<slug>.html  page body to publish as an Artifact
"""
import json, re, sys, os, runpy, math

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "published", "lesson04.html")  # layout template: the published Lesson 4 page
lines = open(SRC, encoding="utf8").read().split("\n")

def find(prefix):
    for i, l in enumerate(lines):
        if l.startswith(prefix):
            return i
    raise SystemExit("missing " + prefix)

i_main = find('<main class="wrap">')
i_lesson = find("window.LESSON=")
head = "\n".join(lines[:i_main + 1])
engine = "\n".join(lines[i_lesson + 1:])

# engine tweaks: mastery threshold scales with quiz length
engine = engine.replace(
    'if(all) st=S.qzScore>=8?"Lesson complete. Mastery reached (8/10 or better on the quiz).":',
    'const need=Math.ceil(QUIZ.length*0.8);\n  if(all) st=S.qzScore>=need?`Lesson complete. Mastery reached (${need}/${QUIZ.length} or better on the quiz).`:')
assert "const need=" in engine
engine = engine.replace('fb("fbQuiz",S.qzScore,QUIZ.length,"correct")', 'fb("fbQuiz",S.qzScore,QUIZ.length,"correct")')
engine = engine.replace('const L=[`Texas History Lesson ${C.n}: ${C.title}`];', 'const L=[`Texas History ${C.label}: ${C.title}`];')
assert "C.label" in engine

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

PATTERN = [1, 3, 0, 2, 2, 0, 3, 1, 0, 2, 1, 3, 3, 1, 0, 2]

def spread(qs, offset=0):
    """Move each correct answer to a varied position so keys aren't guessable."""
    for i, q in enumerate(qs):
        if q.get("fixed"):
            continue
        o = list(q["o"])
        right = o.pop(q["a"])
        tgt = PATTERN[(i + offset) % len(PATTERN)] % (len(o) + 1)
        o.insert(tgt, right)
        q["o"], q["a"] = o, tgt

def build(path):
    L = runpy.run_path(path)["L"]
    spread(L["quiz"])
    for k, t in enumerate(L["practice"]):
        if t["type"] == "mc":
            spread(t["items"], offset=5 + k)
    label = L["label"]  # e.g. "Lesson 5"
    eyebrow = L.get("eyebrow", f"{label} of 17")
    title_tag = L.get("title_tag") or (f'{L["short"]} {label}' if L.get("short") else f'{L["title"]} {label}')
    h = head.replace("<title>Spanish Colonial Texas Lesson 4</title>", f"<title>{esc(title_tag)}</title>")
    teks = L.get("teks_text") or ("TEKS " + ", ".join("7." + t for t in L["teks"]))
    nq = len(L["quiz"])
    h = h.replace("</style>\n\n<nav", "/* long words and URLs wrap instead of widening the page */\n.t,.excerpt p,.card p,.callout{overflow-wrap:anywhere}\n</style>\n\n<nav", 1)
    assert "overflow-wrap:anywhere}" in h
    out = [h, f'''<header class="hero">
  <p class="eyebrow">Texas History · {esc(eyebrow)}</p>
  <h1>{esc(L["title"])}</h1>
  <p class="q">Big question: <b>{esc(L["question"])}</b></p>
  <div class="meta"><span>About {L.get("minutes", 90)} minutes</span><span>{teks}</span><span>Your work saves on this device</span></div>
</header>
''']
    if L.get("note"):
        out.append(f'<div class="callout" style="margin-bottom:8px"><b>For parents:</b> {L["note"]}</div>\n')
    out.append(f'''<section class="step" id="read">
  <p class="eyebrow">Step 1 · Read</p>
{L["read"]}
</section>

<section class="step" id="practice">
  <p class="eyebrow">Step 2 · Practice</p>
  <h2>Do the work</h2>
  <div id="practiceTasks" style="display:grid;gap:18px"></div>
</section>

<section class="step" id="check">
  <p class="eyebrow">Step 3 · {esc(L.get("quiz_label", "Quiz"))}</p>
  <h2>Show what you know</h2>
  <p class="small">{nq} questions.{" " + L["quiz_note"] if L.get("quiz_note") else ""} You can scroll up to review, but try it from memory first.</p>
  <form class="quiz" id="quiz"></form>
  <div class="row"><button class="btn" id="submitQuiz">Submit quiz</button><span class="fb" id="fbQuiz" aria-live="polite"></span></div>
</section>

<section class="step" id="reflect">
  <p class="eyebrow">Step 4 · Exit claim</p>
  <h2>{esc(L.get("reflect_h", "Answer the big question"))}</h2>
  <div class="prose"><p>{L["prompt"]}</p></div>
  <label for="claim" class="small">Your answer</label>
  <textarea id="claim" placeholder="{esc(L["placeholder"])}"></textarea>
  <p class="small" id="wc">0 words</p>
  <div class="checks">
    <p><b>Check your own work before you finish:</b></p>
    <label><input type="checkbox" id="ck1"> {L.get("ck1", "I made a clear <b>claim</b> that answers the question.")}</label>
    <label><input type="checkbox" id="ck2"> {L.get("ck2", "I gave specific <b>evidence</b> (a place, a date, a person, or an event).")}</label>
    <label><input type="checkbox" id="ck3"> {L.get("ck3", "I explained <b>how</b> my evidence supports my claim.")}</label>
  </div>
</section>

<section class="step" id="results">
  <p class="eyebrow">Results</p>
  <h2>{esc(label)} report</h2>
  <div class="cert" id="cert">
    <div class="cert-top"><span class="eyebrow">Texas History · {esc(label)}</span><span class="stamp" id="stamp">In progress</span></div>
    <h3 id="certTitle">{esc(L["title"])}</h3>
    <div class="score" id="score"></div>
    <p class="small" id="status"></p>
    <p class="certdate yr" id="certDate"></p>
  </div>
  <div class="shot" id="shot" hidden>
    <h3>Last step: turn in your work</h3>
    <ol>
      <li>Tap <b>Copy my answers</b> below.</li>
      <li>Paste the answers into a message to your parents.</li>
      <li>Send it. A parent will read and grade your exit claim.</li>
    </ol>
  </div>
  <div class="row">
    <button class="btn" id="copy">Copy my answers</button>
    <span class="fb" id="fbCopy" aria-live="polite"></span>
  </div>
  <textarea id="reportText" readonly hidden aria-label="Report text"></textarea>
  <div class="confirm" id="resetBox">
    <button class="btn ghost" id="reset">Start this lesson over</button>
  </div>
  <p class="small">Sources: <a href="https://www.law.cornell.edu/regulations/texas/19-Tex-Admin-Code-SS-113-19" target="_blank" rel="noopener">19 TAC §113.19 (Grade 7 TEKS)</a> · {L["sources"]}</p>
</section>
</main>

<script>''')
    cfg = {"key": L["key"], "n": L.get("n"), "label": label, "title": L["title"],
           "practice": L["practice"], "quiz": L["quiz"], "review": L["review"]}
    out.append("window.LESSON=" + json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/") + ";")
    out.append(engine)
    html = "\n".join(out)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    dst = os.path.join(HERE, "out", L["slug"] + ".html")
    open(dst, "w", encoding="utf8").write(html)
    # publish copy: drop the skeleton the publish step adds back
    pub = html.split("<body>", 1)[1]
    pub = pub.rsplit("</body></html>", 1)[0].strip() + "\n"
    assert pub.startswith("<title>")
    os.makedirs(os.path.join(HERE, "pub"), exist_ok=True)
    open(os.path.join(HERE, "pub", L["slug"] + ".html"), "w", encoding="utf8").write(pub)
    check(L, path)
    print("built", dst, len(html))

def check(L, path):
    errs = []
    for ti, t in enumerate(L["practice"]):
        assert t["type"] in ("match", "order", "sort", "mc", "compare"), path
        for k in ("title", "intro", "button", "word", "items"):
            if k not in t: errs.append(f"practice {ti} missing {k}")
        if t["type"] == "match":
            for it in t["items"]:
                if not (0 <= it[1] < len(t["options"])): errs.append(f"match bad idx {it}")
        if t["type"] == "sort":
            codes = [c[0] for c in t["choices"]]
            for it in t["items"]:
                if it[1] not in codes or len(it) != 3: errs.append(f"sort bad {it}")
        if t["type"] == "mc":
            for q in t["items"]:
                if not (0 <= q["a"] < len(q["o"])) or "e" not in q: errs.append(f"mc bad {q['q']}")
        if t["type"] == "compare":
            for r in t["items"]:
                if len(r["a"]) != len(t["columns"]):
                    errs.append(f"compare {r['row']}: {len(r['a'])} answers for {len(t['columns'])} columns")
                for a in r["a"]:
                    if not (0 <= a < len(r["o"])): errs.append(f"compare bad idx in {r['row']}")
    for q in L["quiz"]:
        if not (0 <= q["a"] < len(q["o"])) or "e" not in q: errs.append(f"quiz bad {q['q']}")
    # answer-position balance in quiz
    pos = [q["a"] for q in L["quiz"]]
    from collections import Counter
    c = Counter(pos)
    if max(c.values()) > len(pos) * 0.5: errs.append(f"quiz answers bunched: {dict(c)}")
    if errs:
        raise SystemExit(path + ": " + "; ".join(errs))

if __name__ == "__main__":
    for p in sys.argv[1:]:
        build(p)
