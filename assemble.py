#!/usr/bin/env python3
"""Build the whole course page from the lesson content files, in one step.

  python3 assemble.py            -> dist/course.html + site/index.html (GitHub Pages)
  python3 assemble.py --check    -> list the lessons it would build, and their quiz lengths

Each lesson in course.json is matched to a lessons/*.py file by its storage key,
rendered by build.py, and embedded in the course page. Nothing is written to disk
in between.
"""
import argparse, glob, html, json, os, runpy, sys

import build

HERE = os.path.dirname(os.path.abspath(__file__))
SKELETON_HEAD = ('<!doctype html><html><head><meta charset=utf8><meta name=viewport '
    'content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;'
    'box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
    'html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,'
    'BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}'
    '[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')

def lesson_sources():
    """Storage key -> content file, for every lessons/*.py."""
    out = {}
    for path in sorted(glob.glob(os.path.join(HERE, "lessons", "*.py"))):
        try:
            L = runpy.run_path(path)["L"]
        except Exception as e:
            raise SystemExit(f"{path}: {e}")
        out[L["key"]] = path
    return out

# In an iframe srcdoc, href="#section" resolves against the course page's URL and would
# load the whole course inside the frame. This keeps in-page links scrolling in place.
ANCHOR_FIX = ('<script>document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest(\'a[href^="#"]\');'
    'if(!a)return;e.preventDefault();var t=document.getElementById(a.getAttribute("href").slice(1));'
    'if(t)t.scrollIntoView({behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"})});</script>\n')

def full_document(text):
    if not text.lstrip().lower().startswith("<!doctype"):
        text = SKELETON_HEAD + text + "\n</body></html>\n"
    i = text.rfind("</body>")
    return text[:i] + ANCHOR_FIX + text[i:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", default=os.path.join(HERE, "course.json"))
    ap.add_argument("--out", default=os.path.join(HERE, "dist", "course.html"))
    ap.add_argument("--template", default=os.path.join(HERE, "course_template.html"))
    ap.add_argument("--site", default=os.path.join(HERE, "site"),
                    help="also write a standalone index.html here for GitHub Pages (pass --site '' to skip)")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    course = json.load(open(a.course, encoding="utf8"))
    sources = lesson_sources()
    missing, lessons, docs = [], [], {}
    for unit in course["units"]:
        for L in unit["lessons"]:
            path = sources.get(L["key"])
            if not path:
                missing.append(f'{L["label"]} {L["title"]}  (no lessons/*.py with key "{L["key"]}")')
                continue
            data, text = build.render(path)
            docs[L["id"]] = full_document(text)
            L = dict(L, unit=unit["name"], quiz=len(data["quiz"]))
            lessons.append(L)
            if a.check:
                print(f'ok  {L["label"]:<9} {L["title"]:<42} quiz={L["quiz"]}  {os.path.relpath(path, HERE)}')
    if missing:
        print("MISSING (fetch these, then run again):\n  " + "\n  ".join(missing), file=sys.stderr)
        sys.exit(1)
    if a.check:
        return

    meta = {"title": course["title"], "subtitle": course["subtitle"], "storage_key": course["storage_key"],
            "units": [u["name"] for u in course["units"]],
            "lessons": [{k: L.get(k) for k in ("id", "label", "title", "key", "unit", "quiz", "tag")} for L in lessons]}
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
