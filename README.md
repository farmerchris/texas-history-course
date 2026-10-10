# Texas History Course

Interactive lesson pages for a 7th-grade Texas History course (18 sessions, 2022 Grade 7 TEKS), plus one combined course page with a lesson picker and progress tracker.

Each lesson page runs Read → Practice → Quiz → Exit claim → Results. Students turn in work by tapping **Copy my answers** and pasting it into a message to a parent, who grades the exit claim. Work saves in the browser.

## Layout

| Path | What it is |
|---|---|
| `lessons/*.py` | Content for Lessons 5–17 and Celebrate Freedom Week: reading, practice activities, quiz, exit-claim prompt, sources |
| `build.py` | Turns a lesson file into a page, using `published/lesson04.html` as the layout template |
| `published/` | Snapshot of every lesson page as published, including Lessons 1–4, which were made separately and have no file in `lessons/` |
| `course.json` | Lesson order, units, titles, storage keys, and each page's published URL |
| `course_template.html` | Shell of the combined course page |
| `assemble.py` | Bakes every lesson page into `dist/course.html`, plus a standalone `site/index.html` for GitHub Pages |
| `dist/course.html` | The combined course page, for publishing as a Claude artifact |
| `.github/workflows/pages.yml` | Rebuilds the course page and deploys it to GitHub Pages on every push to `main` |
| `tools/check.sh` | Builds all lessons and syntax-checks every page's script |
| `tools/smoke_test.py` | Headless-browser test: answers each quiz, checks phone width and errors, exercises the course page |

`out/`, `pub/` and `site/` are build output and are ignored by git.

## Common tasks

**Change a generated lesson (5–17, CFW)**

```
# edit lessons/l07.py
python3 build.py lessons/l07.py      # out/lesson07.html to test, pub/lesson07.html to publish
python3 tools/smoke_test.py out/lesson07.html
```

Publish `pub/lesson07.html` to that lesson's URL in `course.json`, copy the published page into `published/lesson07.html`, then rebuild the course page.

**Rebuild the course page**

```
python3 assemble.py --check          # lists every lesson found and its quiz length
python3 assemble.py                  # writes dist/course.html
python3 tools/smoke_test.py --course dist/course.html
```

Publish `dist/course.html` to `course_url` in `course.json` so the link stays the same. Lessons are matched by their page `<title>` (`page_title` in `course.json`), and the newest copy wins, so keep that field in sync if a lesson is renamed.

**Edit Lessons 1–4**

These have no content file. Edit the published page itself, then save the new version into `published/` and rebuild the course page. Lesson 4 is also the layout template for `build.py`, so rebuild all lessons after changing it (`tools/check.sh`).

## GitHub Pages

The workflow in `.github/workflows/pages.yml` runs `assemble.py` and publishes `site/index.html`, a standalone copy of the course page.

1. Push this folder to a GitHub repo on the `main` branch.
2. In the repo, open **Settings → Pages**, and under **Build and deployment** set **Source** to **GitHub Actions**.
3. Open the **Actions** tab. The first run starts on your next push, or start it with **Run workflow**. When it finishes, the site is at `https://<username>.github.io/<repo>/`.

After that, every push to `main` rebuilds and redeploys the site, so updating a lesson is: replace its page in `published/`, commit, push. To preview locally: `python3 assemble.py`, then `python3 -m http.server -d site` and open http://localhost:8000.

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
