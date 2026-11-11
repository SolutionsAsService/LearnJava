# Critic: Inclusion (Holmes), R1

**Anchor used:** Holmes, *Mismatch*: exclusion is a person-design mismatch. Solve for one excluded person (a never-programmed newcomer on a phone) and extend to many.

**Observed:** Home at 390x844 and 1280 (aria snapshots, shots/index.html-390-light.png); lessons 01–03; about.html#setup; site.css lines 67, 102, 119.

**Findings:**
- F1 [defect] At 390 the first screen is CA FE BA BE, the title and hex. The explaining kicker is `display:none` under 999px and the lede starts at y=837, below the fold.
- F2 [defect] Under 999px `.lg-l` is hidden, so legend links read only "1 The magic number"… At 1280 each one carries a plain sentence.
- F3 [defect] Legend 3 "constant pool" goes to lesson 01 and legend 6 "attributes" goes to ecosystem.html. Neither page uses the term (grep: 0).
- F4 [defect] Zero-indexed `lessons[1] →` in pager names means lesson 2. That is an in-joke for people who already code.
- F5 [defect] Unglossed terms: "object" (lesson 01), "primitive", "reference", "32-bit", "floating point", "UTF-16 code unit", "Unlike C" (02), "bytecode", "compile time" (home).
- F6 [claim] The JDK path works: every lesson links to #setup, and JDK and terminal are glossed. But "open a terminal in the folder" never says how, and Windows gets no command.
- F7 [claim] The strip names ("Lesson 1: Hello, World") and the landmarks are sound.

**Verdict:** OBJECT

**Requested change:**
- F1: plain one-line lede above the dump on phones.
- F2: keep the description at every width (or aria-describedby).
- F3: link to jvm.html sections that name the parts.
- F4: visible and accessible "Lesson 2", with the index as decoration.
- F5: inline gloss at first use.
- F6: add a `cd` step and a Windows winget line.
- F7: none.
