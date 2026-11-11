# Critic: Evidence (Cairo), R1

- **Anchor used:** *How Charts Lie* (Cairo): omission misleads as surely as scale.
- **Observed:** The scratch builds, `--no-run` and a full JDK run, are byte-identical to site/ and runs.json. `javap -v` agrees: 417 B, 28 entries, major 65, 2 methods, main 9 B. The byte ranges are correct. Threads and Exceptions, downloaded over HTTP into empty folders and run with the printed command, match; Threads took 0.78 s. First screen: at 1280 the legend ends at 595. At 375 the dump ends at 638 and the legend at 799. 20!, Collatz 111 and the VERSIONS dates are correct.
- **Findings:**
  - F1 [defect] Versions omits lessons 03 (15), 04 (14) and 12 (16): VERSIONS has no rows for them (content.py:120-135, build.py:381). This contradicts the page's "lessons that cannot compile under anything older".
  - F2 [claim] "The build checks it with javac --release" (build.py:307, 389) is vacuous for 01, 05, 06 and 07, because `need < 8` returns True unchecked (build.py:70-71).
  - F3 [claim] "417 bytes of bytecode" (build.py:353): the bytecode is 14 B. The legend itself says main is 9 B.
  - F4 [claim] "Every two years one is LTS" since 2018 (build.py:387) is wrong: 11 to 17 was three years.
  - F5 [claim] Streams is badged 16+, but its notes say "All of this arrived in Java 8" (content.py:107). The record that needs 16 is unnamed.
  - F6 [premise] At 375, the legend hides every figure (ranges, counts), and it ends 13 px above the fold.
- **Verdict:** OBJECT
- **Requested change:**
  - F1: add rows for 14, 15 and 16.
  - F2: say the check starts at Java 8.
  - F3: say "a 417-byte class file".
  - F4: say "since 2021".
  - F5: name the record.
  - F6: none required.
