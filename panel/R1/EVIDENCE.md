# R1 evidence: Learn Java (moves M1 to M4), the first WHOLE round

The site is served at http://localhost:8767/. Source: /home/user/learnjava (`_src/build.py`, `_src/content.py`, `site/css/site.css`, `examples/`). Rebuild with `python3 _src/build.py --no-run`. Measure with `node _src/measure.cjs http://localhost:8767/ <outdir>`; it enumerates every page in site/.
This is a from-scratch run: the repo was empty, so there was no R0. The design log is `DESIGN-LOG.md`.

## Build
- javac 21.0.12.1. 13 programs compiled with `javac -Xlint:all`: 0 warnings, 0 non-zero exits.
- Each lesson's stated minimum Java version is checked with `javac --release N`, which must pass, and `--release N-1`, which must fail (for N above 8). All 13 hold.
- Hello.class: 417 bytes, parsed into 6 regions. Cross-checked against `javap -v`: 28 constant-pool entries, major 65, and main's code is 9 bytes (last instruction at offset 8).
- Output lines quoted in the prose are checked as whole lines of the output; all pass.

## Measured after the last edit (20 pages × 1280x800, 375x812, 390x844 × light and dark)
- Horizontal overflow: none. Smallest text outside aria-hidden: 12 px. Links and buttons under 44 px tall, excluding inline links in sentences: 0.
- The hex dump is `aria-hidden` (decorative; the six-part legend carries its meaning). On phones its bytes are 9.2 px, which the Mobile Floor's M4 decorative exemption allows.
- Hero bottom edges (the largest of .magic, h1, .dump, .legend, .strip):
  - light 1280x800: {'.magic': 193, 'h1': 363, '.dump': 576, '.legend': 595, '.strip': 635}
  - light 375x812: {'.magic': 188, 'h1': 272, '.dump': 638, '.legend': 799, '.strip': 1097}
  - light 390x844: {'.magic': 188, 'h1': 272, '.dump': 649, '.legend': 810, '.strip': 1108}
  At 375x812 the lessons strip (and the lede) sit below the fold; the six-part legend, which links every page, ends at 799.

## Screenshots (panel/shots/)
index.html-1280-light.png, index.html-1280-dark.png, index.html-375-light.png, index.html-375-dark.png, index.html-390-light.png, lessons_01-hello.html-1280-light.png, lessons_09-records.html-375-light.png, jvm.html-1280-light.png, versions.html-1280-light.png, ecosystem.html-1280-light.png, about.html-375-light.png.
