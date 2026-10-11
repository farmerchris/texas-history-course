#!/bin/bash
# Build every generated lesson and syntax-check the scripts in out/ and dist/course.html.
# Usage: tools/check.sh            (all lessons)
#        tools/check.sh lessons/l07.py   (just one)
set -e
cd "$(dirname "$0")/.."
files=("$@"); [ ${#files[@]} -eq 0 ] && files=(lessons/*.py)
for f in "${files[@]}"; do python3 build.py "$f"; done
# mktemp --suffix is GNU-only, so make a temp dir and name the file inside it.
tmpd=$(mktemp -d); tmp="$tmpd/script.js"
trap 'rm -rf "$tmpd"' EXIT
for h in out/*.html dist/course.html; do
  [ -f "$h" ] || continue
  python3 -c "
import sys;h=open(sys.argv[1]).read();s=h[h.rfind('<script>')+8:h.rfind('</script>')];open(sys.argv[2],'w').write(s)" "$h" "$tmp"
  node --check "$tmp" || { echo "JS FAIL: $h"; exit 1; }
done
echo "Scripts OK"
