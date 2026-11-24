# How the TLC posters are made

- `make.py`: poster template (1080x1350) + the `days` list (one dict per day: lead colour, eyebrow, headline, body, items, CTA).
  Colours: purple #8C28E9, green #33FF12, yellow #F9CC15 (from the TLC logo). Rotate `lead` per day.
- `render.py`: turns each poster into PNGs (feed 1080x1350 and vertical 1080x1920) with headless Chrome + Playwright.
  Fonts: `npm i` in this folder (installs @fontsource/syne and @fontsource/inter). Logo: tlc-logo.png.
  Paths in these scripts point at /home/claude/gen and /home/claude/render: copy the files there, or edit the paths.
- Images go in a folder per week (e.g. `2026-week2/`) and are used by Buffer via
  https://raw.githubusercontent.com/dionpather-afk/tlc-social-posts/main/<folder>/<file>.png
- Captions: see week1-captions.json for tone. Facebook gets the clickable link; Instagram/TikTok get "link in bio".
- Rules: no prices on posters; no invented stats or claims; only list client sites that are live (Power Tech Link Solutions is excluded).
