# R1 · Critic: Provocateur (Shklovsky)

- Anchor used: Art as Technique (Shklovsky). Habit swallows things ("automatization"); the device makes the stone stony by making perception difficult and slow.

- Observed: Home at 1280 (index.html-1280-light.png) shows the real 417-byte Hello.class, tinted into six regions with numbered pins and a legend. "Hello, World" arrives as bytes before source. CA FE BA BE is not "huge": `.magic` is clamp(34px, 4.3vw, 66px), about 55px at 1280 and roughly h1 size, and 30px below 1000px. Only the conductor's prompt claims "huge"; the evidence file does not. The inner pages (lessons_01-hello, lessons index, jvm, versions) are one centred column each: code box, output bar, prose, ruled lists. Only index.html carries the dump (grep). jvm.html gives CA FE BA BE as inline code.

- Findings:
  - F1 [claim] The home dump defeats automatic perception. "Hello, World" made strange.
  - F2 [defect] The magic number is headline-sized, not monumental. It ties with the h1 instead of dominating it.
  - F3 [defect] The device is buried after one screen. Thirteen lessons fall back to habitual documentation, and only `lessons[13]` labels and the CAFE chip remain.
  - F4 [defect] jvm.html "walks through" the file without ever showing its bytes. It gives only javap text.
  - F5 [claim] Versions is a competent timeline table, which is the habitual form.

- Verdict: OBJECT

- Requested change:
  - F2: lift the 66px cap so the magic number is the largest thing on the first screen at every width.
  - F3: give each lesson a strip of its own compiled .class bytes, tinted by region, above the source.
  - F4: put the tinted dump on jvm.html and pin each section to its byte range.
  - F1, F5: none.
