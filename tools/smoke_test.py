"""Open pages in headless Chromium at phone width and exercise them.

  python3 tools/smoke_test.py out/lesson07.html ...   # answer each quiz correctly, report width and errors
  python3 tools/smoke_test.py --course dist/course.html  # open a lesson inside the course page, check the tracker

Needs: pip install playwright && python3 -m playwright install chromium
"""
import asyncio, os, sys
from playwright.async_api import async_playwright

ANSWER_QUIZ = """()=>{const C=window.LESSON;if(!C)return "no LESSON config (older page)";
  C.quiz.forEach((q,i)=>{const r=document.querySelector(`input[name=qz${i}][value="${q.a}"]`);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}))});
  document.getElementById('submitQuiz').click();return document.getElementById('fbQuiz').textContent}"""

async def lessons(paths):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for f in paths:
            pg = await b.new_page(viewport={"width": 390, "height": 844})
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.goto("file://" + os.path.abspath(f))
            await pg.wait_for_timeout(400)
            quiz = await pg.evaluate(ANSWER_QUIZ)
            width = await pg.evaluate("document.documentElement.scrollWidth")
            print(f"{f} | quiz: {quiz} | width: {width}{' (TOO WIDE)' if width > 390 else ''} | errors: {errs}")
            await pg.evaluate("localStorage.clear()")
            await pg.close()
        await b.close()

async def course(path):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 390, "height": 844})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://" + os.path.abspath(path))
        await pg.wait_for_timeout(400)
        print("home width:", await pg.evaluate("document.documentElement.scrollWidth"))
        await pg.click('button.row[data-id="lesson-5"]')
        await pg.wait_for_timeout(800)
        f = pg.frames[1]
        print("lesson 5 quiz in frame:", await f.evaluate(ANSWER_QUIZ))
        await f.click("#nav-check")
        await pg.wait_for_timeout(300)
        print("in-lesson link stays in frame:", f.url == "about:srcdoc")
        await pg.click("#next")
        await pg.wait_for_timeout(400)
        print("next ->", await pg.evaluate("location.hash"))
        await pg.click("#back")
        await pg.wait_for_timeout(400)
        print("tracker row 5:", await pg.text_content("#st-lesson-5"))
        print("errors:", errs)
        await pg.evaluate("localStorage.clear()")
        await b.close()

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--course"]:
        asyncio.run(course(args[1] if len(args) > 1 else "dist/course.html"))
    else:
        asyncio.run(lessons(args))
