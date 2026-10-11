# Texas History Course

**Live course: <https://farmerchris.github.io/texas-history-course>**

Interactive lesson pages for a 7th-grade Texas History course (18 sessions, 2022 Grade 7 TEKS), plus one combined course page with a lesson picker and progress tracker.

Each lesson page runs Read → Practice → Quiz → Exit claim → Results. Students turn in work by tapping **Copy my answers** and pasting it into a message to a parent, who grades the exit claim. Work saves in the browser.

## Layout

| Path | What it is |
|---|---|
| `lessons/*.py` | Content for all 18 sessions: reading, practice activities, quiz, exit-claim prompt, sources |
| `lesson_template.html` | Page skeleton, styles and the lesson engine that every lesson is built with |
| `build.py` | Renders one lesson file into a lesson page |
| `course.json` | Lesson order, units, titles and storage keys |
| `course_template.html` | Shell of the combined course page |
| `assemble.py` | Builds every lesson and bakes them into `dist/course.html`, plus `site/index.html` for GitHub Pages |
| `dist/course.html` | The combined course page |
| `.github/workflows/pages.yml` | Rebuilds the course page and deploys it to GitHub Pages on every push to `main` |
| `tools/build.sh` | Builds the course page (add `--lessons` to also write a page per lesson) |
| `tools/test.sh` | Builds everything, then runs every check and test below |
| `tools/smoke_test.py` | Answers each quiz, checks phone width and page errors, exercises the course page |
| `tools/practice_test.py` | Solves every practice activity and checks it scores full marks |
| `tools/drag_test.py` | Checks the reordering activity can be solved by dragging, with a mouse and with touch |

`out/` and `site/` are build output and are ignored by git. Lessons are matched to
`course.json` by their storage key, so renaming a lesson's title is safe.

## Common tasks

**Change a lesson**

```
# edit lessons/l07.py
tools/build.sh                       # rebuild the course page from source
tools/test.sh                        # build everything and run all checks
```

To look at one lesson on its own, `python3 build.py lessons/l07.py` writes
`out/lesson07.html`; that file is only for testing, nothing is published from it.

**Rebuild the course page**

```
python3 assemble.py --check          # list the lessons it will build and their quiz lengths
python3 assemble.py                  # writes dist/course.html and site/index.html
```

**Change the look or the lesson engine**

Edit `lesson_template.html` (styles, page skeleton, the JavaScript that runs the
practice activities, quiz and results), then rebuild. Every lesson picks it up.

## GitHub Pages

The workflow in `.github/workflows/pages.yml` runs `assemble.py` and publishes `site/index.html`, a standalone copy of the course page.

1. Push this folder to a GitHub repo on the `main` branch.
2. In the repo, open **Settings → Pages**, and under **Build and deployment** set **Source** to **GitHub Actions**.
3. Open the **Actions** tab. The first run starts on your next push, or start it with **Run workflow**. When it finishes, the site is at `https://<username>.github.io/<repo>/`.

After that, every push to `main` rebuilds and redeploys the site, so updating a lesson is: edit its file in `lessons/`, commit, push. To preview locally: `python3 assemble.py`, then `python3 -m http.server -d site` and open http://localhost:8000.

Deep links open a lesson directly, e.g. `https://<username>.github.io/<repo>/#lesson-7`.

## Requirements

- Python 3.9+
- Node.js (syntax checks, and reading quiz lengths from Lessons 1–2)
- For `tools/smoke_test.py`: `pip install playwright` and `python3 -m playwright install chromium`

## Notes

- Each lesson saves under its own browser key (`tx-lessonN-v1`, `tx-cfw-v1`). Changing a key resets saved work for that lesson.
- The combined page and the single-lesson pages are separate sites, so progress in one does not appear in the other.
- Checkpoints 1–3 are the five extra review questions at the end of the Lesson 5, 10 and 16 quizzes. Mastery is 80% of the quiz.
- Lesson 10 quotes the 1861 Declaration of Causes and shows a parent note first.
