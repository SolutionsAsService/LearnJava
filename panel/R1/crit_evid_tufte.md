# Critic: Evidence (Tufte), R1

- Anchor used: Visual Display of Quantitative Information: graphical integrity (lie factor) and data-ink.
- Observed: I compiled Hello.java fresh and parsed it on my own: 417 bytes, and the served dump matches byte for byte. The regions 0–3, 4–7, 8–300, 301–310, 311–406 and 407–416 all match. javap gives 28 entries, major 65, 2 methods, main code 9 bytes. Cells sit in a fixed 16-column grid. The pool's 293/417 = 70.3% fills about 70% of the block, so the lie factor is 1.0. Shots index.html-1280/375-light; site.css:67, 88, 102, 119.
- Findings:
  - F1 [claim] The encoding is true: every boundary, count and version checks out.
  - F2 [defect] The badges (absolute, -.55em/-.6em) cover data. At 1280, badge 4 hides byte 300, badge 6 hides byte 406, and badge 1 clips "CA".
  - F3 [defect] Below 999px, .lg-b, .lg-l and .off are hidden. The phone legend is six names with no ranges, counts or offsets, so the colour has nothing to read it by.
  - F4 [defect] 9.2px bytes at 375 read as texture, not data.
  - F5 [premise] "CA FE BA BE" appears four times. The dump caption's copy is redundant ink.
  - F6 [premise] Region 4 includes interfaces_count and fields_count (bytes 307–310), so it covers more than "class header".
- Verdict: OBJECT
- Requested change: F1 none. F2: move the badges into the gutter. F3: show the byte ranges on phones. F4: wrap at 8 bytes per row on phones, or accept this. F5: trim the caption. F6: relabel region 4, or leave it.
