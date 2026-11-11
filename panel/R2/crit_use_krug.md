# Critic: Usability (Krug), R2

- Anchor used: Don't Make Me Think (Krug): five-second test, trunk test, obvious clickability, omit needless words.
- Observed: live home at 1280x800 and 390x844; card 5 clicked; trunk test on lessons/09-records.html.
- Five seconds, 1280: "Learn Java, from the bytes up", huge CA FE BA BE, dark "Start lesson 01 →" beside it (y 137). Cards end in blue "Inside the JVM →". Clear.
- Five seconds, 390: button at y 147, plain line "Below is lesson 01, compiled…" at y 235, six cards with destinations end at 773. Fixed.
- Legibility probe: card 5 lands on jvm.html#bytecode, "The methods and their bytecode, bytes 311–406", javap output, one bullet per instruction. Promise kept.
- Trunk test, lesson 9: site ID, h1, Lessons underlined, "lesson 9 of 13", breadcrumb, titled prev/next. Pass.

Findings:
- F1 [defect, resolved] Cards carry destination and arrow.
- F2 [defect, resolved] Start button on the first screen at both widths.
- F3 [claim] Tiles 01–13 are still numbers; "titles below" points off-screen at 1280. Mild mystery meat, honestly labelled.
- F4 [claim] "lessons[13]", "lessons[8]" survive as grey asides. Harmless, still needless.
- F5 [defect, minor] The javap box on jvm.html clips its comments at 1280 ("Ljava/io/Pri…").
- F6 [premise] The dump hero is strangeness; my blind spot.

Verdict: PASS

Requested change:
- F3: optional: short titles under tiles on desktop.
- F4: optional: drop the array labels.
- F5: wrap or trim the javap comments.
- F1, F2, F6: none.
