# R3 evidence: the café home page (moves M8, M9)

The owner graded the previous home page (the Hello.class hex dump) B+, in these words: "more coffee type theme … colors too similar keep that code chart somewhere". The hex dump now lives on the JVM page. The home page is a latte glass whose four layers link the site, plus a chalkboard menu of all 13 lessons. Read DESIGN-LOG.md, sections "Human grade" and "Move M8".

Site: http://localhost:8767/. Source: /home/user/learnjava (`_src/build.py`, the `hero()` function; `site/css/site.css`).

## Measured after the last edit (20 pages × 1280x800, 375x812, 390x844 × light and dark)
- Overflow: none. Smallest text outside aria-hidden: 12 px. Targets under 44 px (excluding inline links): 0.
- Hero parts (bottom edges, px): light 1280x800: {'.hero h1': 280, '.start': 453, '.glass': 407, '.saucer': 477, '.menu': 746}; light 375x812: {'.hero h1': 264, '.start': 323, '.glass': 665, '.saucer': 735, '.menu': 1446}; light 390x844: {'.hero h1': 264, '.start': 323, '.glass': 665, '.saucer': 735, '.menu': 1431}; dark 1280x800: {'.hero h1': 280, '.start': 453, '.glass': 407, '.saucer': 477, '.menu': 746}; dark 375x812: {'.hero h1': 264, '.start': 323, '.glass': 665, '.saucer': 735, '.menu': 1446}; dark 390x844: {'.hero h1': 264, '.start': 323, '.glass': 665, '.saucer': 735, '.menu': 1431}
- Layer contrast (light): foam text on espresso 13.98:1; ink on caramel 5.73:1; ink on milk 12.09:1. Dark: foam on espresso 8.55:1; espresso layer against the page 1.83:1, separated by a drop-shadow rim.
- Every figure in the layers is computed by the build: 6 families of tools with 14 links (content.ECOSYSTEM), Java 1.0 to 25 (content.VERSIONS), 417 bytes (javac), 13 programs.

Screenshots: panel/shots/index.html-1280-light.png, -1280-dark, -375-light, -375-dark, -390-light, -390-dark; jvm.html-1280-light.png (the chart's new home); lessons_09-records.html-1280-light.png (the ribbon over every class file).
