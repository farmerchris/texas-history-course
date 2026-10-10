#!/usr/bin/env python3
"""Assemble every lesson page into one course page with a lesson picker and progress tracker.

How to repeat after editing any lesson:
  1. Get the latest copy of every lesson listed in course.json into published/
     (or let Claude fetch them: Artifact "read" with path "index.html" for each url,
     which lands copies in artifact-files/<uuid>/index.html; both folders are scanned).
  2. python3 assemble.py            -> dist/course.html (artifact) + site/index.html (GitHub Pages)
     python3 assemble.py --check    -> only report which lessons were found

Lessons are matched by their <title> (course.json "page_title"), newest file wins,
so it doesn't matter which folder a copy landed in. Use --src DIR [DIR...] to scan
other folders instead (any *.html under them is scanned).
"""
import argparse, glob, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKELETON_HEAD = ('<!doctype html><html><head><meta charset=utf8><meta name=viewport '
    'content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;'
    'box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
    'html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,'
    'BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}'
    '[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')

def page_title(text):
    m = re.search(r"<title>(.*?)</title>", text[:10000], re.S)
    return html.unescape(m.group(1).strip()) if m else None

def find_pages(src):
    found = {}
    for path in glob.glob(os.path.join(src, "**", "*.html"), recursive=True):
        try:
            text = open(path, encoding="utf8").read()
        except OSError:
            continue
        t = page_title(text)
        if not t:
            continue
        mt = os.path.getmtime(path)
        if t not in found or mt > found[t][0]:
            found[t] = (mt, path, text)
    return found

# In an iframe srcdoc, href="#section" resolves against the course page's URL and would
# load the whole course inside the frame. This keeps in-page links scrolling in place.
ANCHOR_FIX = ('<script>document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest(\'a[href^="#"]\');'
    'if(!a)return;e.preventDefault();var t=document.getElementById(a.getAttribute("href").slice(1));'
    'if(t)t.scrollIntoView({behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"})});</script>\n')

def full_document(text):
    """Published copies already carry the skeleton; local drafts may not."""
    if not text.lstrip().lower().startswith("<!doctype"):
        text = SKELETON_HEAD + text + "\n</body></html>\n"
    i = text.rfind("</body>")
    return text[:i] + ANCHOR_FIX + text[i:]

def quiz_total(text):
    m = re.search(r"window\.LESSON=(\{.*?\});\n", text, re.S)
    if m:
        try:
            return len(json.loads(m.group(1))["quiz"])
        except Exception:
            pass
    m = re.search(r"const QUIZ=(\[.*?\]);", text, re.S)
    if m:
        try:  # older pages: evaluate the array literal with node
            out = subprocess.run(["node", "-e", "process.stdout.write(String((" + m.group(1) + ").length))"],
                                 capture_output=True, text=True, timeout=20)
            return int(out.stdout)
        except Exception:
            pass
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", nargs="+", default=[os.path.join(HERE, "published"), os.path.join(HERE, "artifact-files")],
                    help="folders of lesson pages to scan (newest copy of each title wins)")
    ap.add_argument("--course", default=os.path.join(HERE, "course.json"))
    ap.add_argument("--out", default=os.path.join(HERE, "dist", "course.html"))
    ap.add_argument("--template", default=os.path.join(HERE, "course_template.html"))
    ap.add_argument("--site", default=os.path.join(HERE, "site"),
                    help="also write a standalone index.html here for GitHub Pages (pass --site '' to skip)")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    course = json.load(open(a.course, encoding="utf8"))
    pages = {}
    for src in a.src:
        for t, v in find_pages(src).items():
            if t not in pages or v[0] > pages[t][0]:
                pages[t] = v
    missing, lessons, docs = [], [], {}
    for unit in course["units"]:
        for L in unit["lessons"]:
            hit = pages.get(L["page_title"])
            if not hit:
                missing.append(f'{L["label"]} {L["title"]}  (page title "{L["page_title"]}", {L["url"]})')
                continue
            text = hit[2]
            docs[L["id"]] = full_document(text)
            L = dict(L, unit=unit["name"], quiz=quiz_total(text))
            lessons.append(L)
            if a.check:
                print(f'ok  {L["label"]:<9} {L["title"]:<42} quiz={L["quiz"]}  {os.path.relpath(hit[1], HERE)}')
    if missing:
        print("MISSING (fetch these, then run again):\n  " + "\n  ".join(missing), file=sys.stderr)
        sys.exit(1)
    if a.check:
        return

    meta = {"title": course["title"], "subtitle": course["subtitle"], "storage_key": course["storage_key"],
            "units": [u["name"] for u in course["units"]],
            "lessons": [{k: L.get(k) for k in ("id", "label", "title", "key", "unit", "quiz", "tag", "url")} for L in lessons]}
    def js(o):  # safe to place inside <script>
        return json.dumps(o, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\!--")
    blobs = "\n".join(f'<script type="application/json" id="doc-{i}">{js(d)}</script>' for i, d in docs.items())
    tpl = open(a.template, encoding="utf8").read()
    out = tpl.replace("/*__COURSE__*/null", js(meta)).replace("<!--__LESSON_DOCS__-->", blobs)
    out = out.replace("__TITLE__", html.escape(course["title"]))
    assert "__COURSE__" not in out and "__LESSON_DOCS__" not in out
    open(a.out, "w", encoding="utf8").write(out)
    print(f"wrote {a.out}: {len(lessons)} lessons, {len(out)//1024} KB")
    if a.site:
        write_site(out, a.site)

def write_site(body, site_dir):
    """Standalone copy for static hosting (GitHub Pages): add the document skeleton
    the artifact host normally supplies, moving the title, font links and styles into <head>."""
    split = body.index("</style>") + len("</style>")
    head, rest = body[:split], body[split:]
    page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + head + '\n</head>\n<body>\n' + rest.strip() + '\n</body>\n</html>\n')
    os.makedirs(site_dir, exist_ok=True)
    dst = os.path.join(site_dir, "index.html")
    open(dst, "w", encoding="utf8").write(page)
    open(os.path.join(site_dir, ".nojekyll"), "w").close()  # serve files as-is
    print(f"wrote {dst} (standalone, for GitHub Pages)")

if __name__ == "__main__":
    main()
