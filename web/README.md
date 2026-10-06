# Web version

`power-system-basics.html` is the single source of the course web page. It is published in two places:

- **GitHub Pages (public):** https://taio11k.github.io/Power-System-Basics/
- **claude.ai:** https://claude.ai/artifact/CNg9KrHXyNkaiGcmMBEQQq

The file has no `<!doctype>`, `<html>`, `<head>` or `<body>` tags on purpose, because claude.ai adds them when it publishes the page. For GitHub Pages, `build_pages.sh` wraps the file into a complete HTML document.

## How updates work

1. Edit `power-system-basics.html`.
2. Commit and push to `main`. The **Deploy GitHub Pages** workflow (`.github/workflows/pages.yml`) runs `build_pages.sh` and publishes the site within a minute or two. You can watch it in the repo's **Actions** tab.
3. Republish the same file to the claude.ai link so both copies match.

To preview the GitHub Pages build locally:
```bash
bash web/build_pages.sh _site
```
Then open `_site/index.html` in a browser. (`_site/` is git-ignored.)
