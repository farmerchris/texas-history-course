#!/bin/bash
# Build everything, then run every check and test.
#   tools/test.sh           full run
#   tools/test.sh --fast    skip the browser tests
#
# Exits non-zero if any step fails, and prints a summary at the end.
set -o pipefail
cd "$(dirname "$0")/.."
FAST=0; [ "$1" = "--fast" ] && FAST=1

PASS=(); FAIL=(); SKIP=()
step() {  # step <name> <command...>
  local name="$1"; shift
  printf '\n=== %s\n' "$name"
  if "$@"; then PASS+=("$name"); else FAIL+=("$name"); fi
}
have_playwright() { python3 -c "import playwright" 2>/dev/null; }

# 1. the course page, and a page per lesson for the browser tests to drive
step "build course page" python3 assemble.py
step "build lesson pages" python3 build.py lessons/*.py

# 2. every page's script must parse
syntax() {
  local tmpd; tmpd=$(mktemp -d); trap 'rm -rf "$tmpd"' RETURN
  local bad=0
  for h in out/*.html dist/course.html site/index.html; do
    [ -f "$h" ] || continue
    python3 -c "
import sys;h=open(sys.argv[1]).read();s=h[h.rfind('<script>')+8:h.rfind('</script>')];open(sys.argv[2],'w').write(s)" \
      "$h" "$tmpd/s.js"
    node --check "$tmpd/s.js" || { echo "JS FAIL: $h"; bad=1; }
  done
  [ $bad -eq 0 ] && echo "Scripts OK"
  return $bad
}
step "JS syntax" syntax

if [ $FAST -eq 1 ]; then
  SKIP+=("browser tests (--fast)")
elif ! have_playwright; then
  SKIP+=("browser tests (playwright not installed: pip install playwright && python3 -m playwright install chromium)")
else
  # 3. quizzes answer correctly, phone width, no page errors
  step "smoke test: lessons"     python3 tools/smoke_test.py out/*.html
  step "smoke test: course page" python3 tools/smoke_test.py --course dist/course.html
  # 4. every practice activity type solves to full marks and the lesson completes
  step "practice activities"     python3 tools/practice_test.py out/*.html
  # 5. reordering works by dragging, with a mouse and with touch
  step "drag to reorder"         python3 tools/drag_test.py out/*.html
fi

printf '\n========================================\n'
for s in "${PASS[@]}"; do printf 'PASS  %s\n' "$s"; done
for s in "${SKIP[@]}"; do printf 'SKIP  %s\n' "$s"; done
for s in "${FAIL[@]}"; do printf 'FAIL  %s\n' "$s"; done
printf '%d passed, %d failed, %d skipped\n' "${#PASS[@]}" "${#FAIL[@]}" "${#SKIP[@]}"
[ ${#FAIL[@]} -eq 0 ] || exit 1
