#!/bin/bash
# Build everything and run every check and smoke test.
# Usage: tools/checkall.sh            (full run)
#        tools/checkall.sh --fast     (skip the browser tests)
#
# Exits non-zero if any step fails, and prints a summary at the end.
cd "$(dirname "$0")/.."
FAST=0; [ "$1" = "--fast" ] && FAST=1

PASS=(); FAIL=(); SKIP=()
step() {  # step <name> <command...>
  local name="$1"; shift
  printf '\n=== %s\n' "$name"
  if "$@"; then PASS+=("$name"); else FAIL+=("$name"); fi
}
have_playwright() { python3 -c "import playwright" 2>/dev/null; }

# 1. build every lesson from its content file, and syntax-check the scripts
step "build + JS syntax (tools/check.sh)" bash tools/check.sh

# 2. assemble the combined course page and the standalone site
step "assemble course page" python3 assemble.py

# 3. syntax-check the pages check.sh does not cover
check_published() {
  local tmpd; tmpd=$(mktemp -d); trap 'rm -rf "$tmpd"' RETURN
  local bad=0
  for h in published/*.html pub/*.html site/index.html; do
    [ -f "$h" ] || continue
    python3 -c "
import sys;h=open(sys.argv[1]).read();s=h[h.rfind('<script>')+8:h.rfind('</script>')];open(sys.argv[2],'w').write(s)" \
      "$h" "$tmpd/s.js"
    node --check "$tmpd/s.js" || { echo "JS FAIL: $h"; bad=1; }
  done
  [ $bad -eq 0 ] && echo "Scripts OK (published, pub, site)"
  return $bad
}
step "JS syntax (published/ pub/ site/)" check_published

if [ $FAST -eq 1 ]; then
  SKIP+=("browser tests (--fast)")
elif ! have_playwright; then
  SKIP+=("browser tests (playwright not installed: pip install playwright && python3 -m playwright install chromium)")
else
  # 4. quizzes answer correctly, phone width, no page errors
  step "smoke test: generated lessons" python3 tools/smoke_test.py out/*.html
  step "smoke test: published lessons" python3 tools/smoke_test.py published/*.html
  step "smoke test: course page"       python3 tools/smoke_test.py --course dist/course.html
  # 5. every practice activity type solves to full marks and the lesson completes
  step "practice activities: generated" python3 tools/practice_test.py out/*.html
  step "practice activities: published" python3 tools/practice_test.py published/*.html
  # 6. reordering works by dragging, with a mouse and with touch
  step "drag to reorder" python3 tools/drag_test.py out/*.html
fi

printf '\n========================================\n'
for s in "${PASS[@]}"; do printf 'PASS  %s\n' "$s"; done
for s in "${SKIP[@]}"; do printf 'SKIP  %s\n' "$s"; done
for s in "${FAIL[@]}"; do printf 'FAIL  %s\n' "$s"; done
printf '%d passed, %d failed, %d skipped\n' "${#PASS[@]}" "${#FAIL[@]}" "${#SKIP[@]}"
[ ${#FAIL[@]} -eq 0 ] || exit 1
