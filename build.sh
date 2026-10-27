#!/bin/sh
# Builds the installable plugin zip into dist/
set -eu
cd "$(dirname "$0")"
version=$(python3 -c "import re; print('.'.join(re.search(r'version = \((\d+), (\d+), (\d+)\)', open('__init__.py').read()).groups()))")
mkdir -p dist
out="dist/restart-servers-$version.zip"
rm -f "$out"
for po in translations/*.po; do msgfmt --check -o "${po%.po}.mo" "$po"; done
zip -q "$out" __init__.py ui.py plugin-import-name-restart_servers.txt LICENSE translations/*.mo
echo "$out"
