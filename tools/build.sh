#!/bin/bash
# Build the course from the lesson content files.
#   tools/build.sh            -> dist/course.html + site/index.html
#   tools/build.sh --lessons  -> also write out/<slug>.html for each lesson, to view one on its own
set -e
cd "$(dirname "$0")/.."

python3 assemble.py

if [ "$1" = "--lessons" ]; then
  python3 build.py lessons/*.py
fi
