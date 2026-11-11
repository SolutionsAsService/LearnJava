# Critic: Evidence (Tufte), R2

- Anchor used: Visual Display of Quantitative Information, graphical integrity. The lie factor (shown effect / data effect) must stay within 0.95–1.05.
- Observed: I recompiled all 13 programs and parsed each class file myself. All 13 ribbon captions match my counts. Playwright measured every .seg at 1280, 390 and 375 px. On the home and JVM dumps, badge-to-byte overlaps = 0 at all widths. The caption is now "Hello.class · 417 bytes". Region 4 is relabelled.
- Findings:
  1. F1 [claim] The captions are true. The pool, methods and attributes segments have a lie factor of 0.98–1.00.
  2. F2 [defect] `.seg{min-width:3px}` inflates the small parts. On Streams at 375 px, magic and version reach a lie factor of 6.25 (3 px drawn, 0.48 px due); at 1280 they reach 2.87. Header reaches 2.5.
  3. F3 [claim] R1 F2 (badges cover bytes) is resolved.
  4. F4 [premise] I accept the R1 F3 overrule. jvm.html's .rng headings keep the ranges on phones.
  5. F5 [defect] R1 F4 is unaddressed and worse: bytes are 8.6 px at 375 (they were 9.2), still 16 per row.
  6. F6 [premise] Lesson 07's ribbon shows Classes.class (header 10). The class with fields is Classes$Account (header 26).
- Verdict: OBJECT (on F2)
- Requested change: F2: drop the floor, or merge magic and version into one true-width 8-byte run, or say so in the caption. F5: 8 bytes per row on phones, or log the decision. F6: show Account, or reword the text. Otherwise none.
