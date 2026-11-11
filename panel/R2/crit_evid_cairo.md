# Critic: Evidence (Cairo), R2

- **Anchor used:** *How Charts Lie* (Cairo): a figure can be accurate and still mislead by what it leaves out.
- **Observed:** I recompiled all 13 programs with javac 21.0.12.1. Every ribbon matches to the byte. For example, Hello is 417 = 4/4/293/10/96/10 and Records is 2,076 with a 1,453-byte pool. The JVM ranges (0–3, 4–7, 8–300, 301–310, 311–406, 407–416), the 28 entries, the 9-byte main and the pool's 293 of 417 are correct. `--release` passes at each minimum and fails one version below, for all 11 minimums of 8 and later. measure.json matches EVIDENCE.
- **R1 check:** F1–F5 are fixed: rows for 14, 15 and 16, the scope of the check stated, "417-byte class file", "since then one every two years", and Streams names its record. On F6, the legend now ends at 778 < 812.
- **Findings:**
  - F1 [claim] The ribbons on lessons 07, 08, 09 and 12 show only the outer class, but javac writes 2, 4, 5 and 2 files. Records totals 6,011 B. The 09 ribbon holds none of the record or sealed bytes the lesson teaches. On 07, the 611-byte Classes.class shows "header 10" (no fields), while Classes$Account (1,317 B) holds both fields that the JVM page promises ("Lesson 07 builds a class with fields").
  - F2 [defect] "lessons[13]" (build.py:216, 338) is out of range in the site's own zero-indexed notation (lesson 9 = lessons[8], build.py:349).
- **Verdict:** OBJECT
- **Requested change:**
  - F1: caption it "one of N class files, X bytes in all", or ribbon the class the lesson is about.
  - F2: write "lessons[0–12]", or drop it.
