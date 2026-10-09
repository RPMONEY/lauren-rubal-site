#!/bin/sh
# Usage: sh tools/bump.sh <BUILD>  - stamps build number in footer, CSS header, stylesheet cache-buster, version.txt
B="$1"; [ -z "$B" ] && echo "usage: sh tools/bump.sh <BUILD>" && exit 1
cd "$(dirname "$0")/.."
for f in site/*.html; do sed -i -E "s/Build [0-9]+\b/Build $B/g; s#href=\"styles\.css(\?v=[0-9]+)?\"#href=\"styles.css?v=$B\"#" "$f"; done
sed -i -E "s#/\* Lauren Rubal, MD \| Build [0-9]+ \*/#/* Lauren Rubal, MD | Build $B */#" site/styles.css
echo "$B" > site/version.txt
