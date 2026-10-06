#!/usr/bin/env bash
# Builds the GitHub Pages site from the claude.ai page source.
# The source has no <!doctype>/<html>/<head> tags (claude.ai adds them),
# so this wraps it into a complete document: its <title>, <link> and <style>
# land in <head>, and the first <div> opens the body.
set -euo pipefail

out="${1:-_site}"
src="$(dirname "$0")/power-system-basics.html"
mkdir -p "$out"

{
  cat <<'HTML'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="A guided 26-week course from AC fundamentals to a junior power systems engineer portfolio using IEC standards, PowerFactory, pandapower and PSCAD.">
<style>html{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
HTML
  cat "$src"
  printf '\n</html>\n'
} > "$out/index.html"

touch "$out/.nojekyll"
echo "Built $out/index.html"
