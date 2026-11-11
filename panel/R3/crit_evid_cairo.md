# Critic: Evidence (Cairo), R3

- **Anchor used:** *How Charts Lie* (Cairo): a true figure can still mislead by what sits beside it.
- **Observed:** I rebuilt in a scratch copy (javac 21.0.12.1). site/ and runs.json are identical apart from the date. I reran measure.cjs: 0 overflow, 12 px minimum, 0 small targets, and every hero edge equals EVIDENCE. The glass ends at 407 (1280x800) and 665 (375x812); the saucer ends at 735. Nothing in the glass or menu scrolls sideways. The menu runs from 753 to 1446 on the phone, as M8 logs. The glass and menu figures match content.py and runs.json: 6 families, 14 links, Java 1.0 to 25, 417 bytes, 13 lessons, 13 prices.
- **R2 check:** both fixed. The ribbons sum every class file (Records: 5 files, 6,011 bytes, recompiled). No `lessons[` index remains. Two-line commands appear on all 13 lessons, and About says why (build.py:481).
- **Findings:**
  - F1 [claim] The four menu prices "1.0+" and "5.0+" are never compiled (build.py:78, `need < 8`) but look the same as the proven ones. The caveat sits at y=1077 (1280) and y=1837 (375), below the menu.
  - F2 [defect] The kicker "Thirteen small programs" is a literal (build.py:227), not `len(K.LESSONS)`.
- **Verdict:** PASS
- **Requested change:** F1: mark the prices below Java 8 on the menu (for example "1.0+†") and link the mark to the caveat. F2: compute the kicker.
