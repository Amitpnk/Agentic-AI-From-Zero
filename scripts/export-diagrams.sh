#!/usr/bin/env bash
# Re-export every .drawio file to an .svg next to it (needs draw.io desktop).
# The SVG embeds the diagram, so it can also be opened and edited in draw.io.
# Usage: bash scripts/export-diagrams.sh
set -euo pipefail
cd "$(dirname "$0")/.."

DRAWIO="${DRAWIO:-}"
if [ -z "$DRAWIO" ]; then
  for c in "/c/Program Files/draw.io/draw.io.exe" "/Applications/draw.io.app/Contents/MacOS/draw.io" "$(command -v drawio || true)"; do
    if [ -n "$c" ] && [ -x "$c" ]; then DRAWIO="$c"; break; fi
  done
fi
[ -n "$DRAWIO" ] || { echo "draw.io desktop not found; set DRAWIO=/path/to/draw.io"; exit 1; }

find . -name '*.drawio' -not -path './.git/*' | while read -r f; do
  "$DRAWIO" -x -f svg --embed-diagram -b 10 -o "${f%.drawio}.svg" "$f"
done
