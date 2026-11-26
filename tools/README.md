# How the TLC posters are made

- `make.py`: poster template (1080x1350) + the `days` list (one dict per day: lead colour, eyebrow, headline, body, items, CTA).
  Colours: purple #8C28E9, green #33FF12, yellow #F9CC15 (from the TLC logo). Rotate `lead` per day.
- `render.py`: turns each poster into PNGs (feed 1080x1350 and vertical 1080x1920) with headless Chrome + Playwright.
  Fonts: `npm i` in this folder (installs @fontsource/syne and @fontsource/inter). Logo: tlc-logo.png.
  Paths in these scripts point at /home/claude/gen and /home/claude/render: copy the files there, or edit the paths.
- Images go in a folder per week (e.g. `2026-week2/`) and are used by Buffer via
  https://raw.githubusercontent.com/dionpather-afk/tlc-social-posts/main/<folder>/<file>.png
- Captions: see week1-captions.json for tone. Facebook gets the clickable link; Instagram/TikTok get "link in bio".
- Audience (Dion, 25 Nov 2026): think big. TLC serves businesses, schools and organisations of every size, in South Africa and beyond. Never say "small business" or use #SmallBusinessSA; use tags like #BusinessWebsites #WebDesign #SEO #AEO #TalentLearnConsult.
- Rules: no prices on posters; no invented stats or claims; only list client sites that are live (Power Tech Link Solutions is excluded).

## Brief: business email now included (Dion, 26 Nov 2026)
- New: every TLC hosted website package includes a professional email on the client's own domain (you@yourbusiness, not a free Gmail).
- Every website package includes: their own web address (domain), hosting, and a professional email on their domain.
- Use this in some posters in every batch (about 2 or 3 of the 9), rotating these wordings:
  - "Look professional from day one. Every TLC website comes with your own web address, hosting and a business email."
  - "You@yourbusiness beats yourbusiness@gmail. Every TLC website includes a professional email."
  - "Domain. Hosting. Business email. All included with your TLC website."
- Call to action: talentlearnconsult.com/website, "tell us what you need".
- On these email posters (poster small print or caption), say: "Your email works while your monthly service is active."
- Don't: say how many email addresses come with it; quote prices or discounts; promise "free forever".
