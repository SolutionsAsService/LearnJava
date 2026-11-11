# Critic: Inclusion (Holmes), R2

**Anchor used:** Holmes, *Mismatch*: solve for one excluded person (a never-programmed newcomer on a phone, or using a screen reader or voice control) and the fix extends to many.

**Observed:** aria snapshots of home, lessons 01–03 and about at 390x844; the home legend at 1280; index.html legend markup.

**Findings:**
- F1 [claim] R1 F1–F3, F5 and F6 are fixed: a plain line above the dump, full legend sentences at 390, the constant pool named in lesson 01, `cd Downloads` and winget.
- F2 [defect] At 390 the card's visible "Inside the JVM →" is `aria-hidden`, so the link name lacks its visible destination (WCAG 2.5.3, Label in Name).
- F3 [defect] At 1280 the name runs together: "…anything else.Inside the JVM →".
- F4 [defect] "lessons[13]" (strip) and "lessons[1]" (pager) are still in the accessible names, which a screen reader reads out with brackets.
- F5 [defect] Lesson 03 uses a `for` loop and chained `.append` without explaining them. Loops come in lesson 04.
- F6 [premise] Lesson 02 still assumes the reader knows C ("where in C it depends").
- F7 [claim] The ribbon is aria-hidden and its caption carries the counts and a link, which is sound. "magic" and "header" are unglossed there.

**Verdict:** OBJECT

**Requested change:**
- F2: drop `aria-hidden` on the phone destination.
- F3: add a separator before `.lg-go`.
- F4: `aria-hidden` on `.idx`.
- F5: add one sentence on the loop.
- F6: cut the C clause.
- F1, F7: none.
