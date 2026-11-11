# R2 evidence: Learn Java after the R1 fixes (moves M5 to M7)

The site is served at http://localhost:8767/. Source: /home/user/learnjava. Read your own R1 report in `panel/R1/` and the R1 resolution table in `DESIGN-LOG.md` ("Resolutions, round R1"). Then judge the site as it is now.

## Measured after the last edit (20 pages × 1280x800, 375x812, 390x844 × light and dark; `_src/measure.cjs` enumerates site/)
- Build: 13 programs, 0 warnings, 0 failures; quoted outputs and the minimum-version checks (Java 8 and later) pass.
- Horizontal overflow: none. Smallest text outside aria-hidden: 12 px. Targets under 44 px, excluding inline links in sentences and captions: 0.
- Hero bottom (the largest of .magic, h1, .dump, .legend, .strip): 1280x800: 772 (legend 772, strip 546); 375x812: 1024 (legend 778, strip 1024); 390x844: 1019 (legend 773, strip 1019).
  On phones the strip and the long lede sit below the fold; the start button, plain line, dump and legend (with destinations) are above it.
- All programs now fit in 74 columns.

## Screenshots (panel/shots/, refreshed after the last edit)
index.html-1280-light/dark, index.html-375-light/dark, index.html-390-light/dark, lessons_01-hello.html-*, lessons_09-records.html-*, jvm.html-*, versions.html-*, ecosystem.html-*, about.html-*.
