"""Solve every practice activity on a lesson page and check it scores full marks.

Covers all five activity types (match, order, sort, mc, compare), which the quiz-only
smoke test does not. Also confirms the page reaches "Lesson complete".

  python3 tools/practice_test.py out/lesson02.html ...
"""
import asyncio, os, sys
from playwright.async_api import async_playwright

SOLVE = """() => {
  const C = window.LESSON;
  if (!C) return {skip: 'no LESSON config'};
  const out = [];
  C.practice.forEach((t, ti) => {
    if (t.type === 'match')
      t.items.forEach((c, i) => { const s = document.getElementById(`ms${ti}_${i}`);
        s.value = c[1]; s.dispatchEvent(new Event('change', {bubbles: true})); });
    if (t.type === 'sort')
      t.items.forEach((s, i) => document.querySelector(
        `#body${ti} button[data-i="${i}"][data-v="${s[1]}"]`).click());
    if (t.type === 'mc')
      t.items.forEach((q, i) => { const r = document.querySelector(`input[name=c${ti}_${i}][value="${q.a}"]`);
        r.checked = true; r.dispatchEvent(new Event('change', {bubbles: true})); });
    if (t.type === 'compare')
      t.items.forEach((r, i) => t.columns.forEach((p, k) => {
        const s = document.getElementById(`cs${ti}_${i}_${k}`);
        s.value = String(r.a[k]); s.dispatchEvent(new Event('change', {bubbles: true})); }));
    if (t.type === 'order') {
      // selection sort via the move buttons, the way a student would
      for (let target = 0; target < t.items.length; target++) {
        for (let guard = 0; guard < t.items.length * 2; guard++) {
          const lis = [...document.querySelectorAll(`#ol${ti} li`)];
          // a correctly placed item also shows " · <year>"; strip it before matching,
          // and match exactly - "World War I" is a prefix of "World War II"
          const cur = lis.map(li => li.querySelector('.t').textContent.replace(/\\s*·\\s*\\S+$/, '').trim());
          const want = t.items[target][0].replace(/<[^>]+>/g, '').trim();
          const at = cur.findIndex((x, idx) => idx >= target && x === want);
          if (at < 0 || at === target) break;
          lis[at].querySelector('button[data-d="-1"]').click();
        }
      }
    }
    document.getElementById('chk' + ti).click();
    out.push({type: t.type, fb: document.getElementById('fb' + ti).textContent});
  });
  C.quiz.forEach((q, i) => { const r = document.querySelector(`input[name=qz${i}][value="${q.a}"]`);
    r.checked = true; r.dispatchEvent(new Event('change', {bubbles: true})); });
  document.getElementById('submitQuiz').click();
  const cl = document.getElementById('claim');
  cl.value = 'Spain and the people of Texas shaped this era, and the evidence above shows how that happened over a long period of time.';
  cl.dispatchEvent(new Event('input', {bubbles: true}));
  ['ck1','ck2','ck3'].forEach(k => { const b = document.getElementById(k);
    b.checked = true; b.dispatchEvent(new Event('change', {bubbles: true})); });
  return {tasks: out, quiz: document.getElementById('fbQuiz').textContent,
          status: document.getElementById('status').textContent,
          stamp: document.getElementById('stamp').textContent};
}"""


async def main(paths):
    bad = 0
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for f in paths:
            pg = await b.new_page(viewport={"width": 390, "height": 844})
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.goto("file://" + os.path.abspath(f))
            await pg.wait_for_timeout(400)
            await pg.evaluate("localStorage.clear()")
            await pg.reload()
            await pg.wait_for_timeout(400)
            r = await pg.evaluate(SOLVE)
            if r.get("skip"):
                print(f"{f}: SKIP ({r['skip']})")
                await pg.close()
                continue
            await pg.wait_for_timeout(200)
            fails = [t for t in r["tasks"] if not t["fb"].startswith("All ")]
            ok = not fails and r["quiz"].startswith("All ") and r["stamp"] == "Lesson complete" and not errs
            bad += not ok
            marks = ", ".join(f"{t['type']}:{'ok' if t['fb'].startswith('All ') else 'FAIL'}" for t in r["tasks"])
            print(f"{'PASS' if ok else 'FAIL'} {f}  [{marks}]  quiz:{r['quiz'][:22]!r}  {r['stamp']!r}")
            for t in fails:
                print(f"       {t['type']} -> {t['fb']!r}")
            if errs:
                print(f"       page errors: {errs}")
            await pg.evaluate("localStorage.clear()")
            await pg.close()
        await b.close()
    print("practice_test:", "OK" if not bad else f"{bad} page(s) failed")
    return bad


sys.exit(1 if asyncio.run(main(sys.argv[1:])) else 0)
