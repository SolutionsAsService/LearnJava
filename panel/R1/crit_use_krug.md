# Critic: Usability (Krug), R1

- Anchor used: Don't Make Me Think (Krug): the five-second test, the trunk test, obviously clickable things, omit needless words.
- Observed: home at 1280x800 and 390x844 (shots plus live Playwright); card 5 traced; trunk test on lessons/05-methods.html.
- Five seconds, 1280: name "Learn Java". Topics: lessons (13 tiles), inside the JVM (the dump), versions. First action: "start with 01" (y about 515), small, set beside "lessons[13]".
- Five seconds, 390: name and nav are clear. The lede and "start with 01" are below the fold (strip ends at 1108). The only actions on screen are the six legend cards, titles only.
- Legibility probe: card 5 ("The methods ... main is 9 bytes of bytecode") goes to jvm.html#bytecode, "The bytecode of main". That section shows javap -c (getstatic, ldc, invokevirtual, return) and explains each line. The promise matches the page. Pass.
- Trunk test, lesson 5: site ID, page name, sections, "you are here" (Lessons underlined, "lesson 5 of 13") and previous/next all present. No search, which is fine at 20 pages.

Findings:
- F1 [defect] The legend cards are links with no signifier (no underline, arrow or link colour). They read as captions.
- F2 [defect] At 390 nothing on the first screen says "start here".
- F3 [defect] Tiles 01-13 are numbers with no titles (mystery meat).
- F4 [claim] "lessons[13]" and "lessons[4]" next to "lesson 5 of 13" are needless words that make the visitor decode.
- F5 [premise] The dump as hero is deliberate strangeness, which is my blind spot.

Verdict: OBJECT

Requested change:
- F1: add an arrow and the destination page name to each card.
- F2: put a "Start lesson 01" button above the dump on phones.
- F3: show each lesson's title on its tile.
- F4: drop the array labels, or keep them as decoration beside plain words.
- F5: none.
