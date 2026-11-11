# R3 — Critic: Usability (Krug)

- **Anchor used:** *Don't Make Me Think* (Krug): the five-second test, the trunk test, obviously clickable signifiers.
- **Observed:** Live page. 1280x800: "Learn Java" in header and h1; "Start lesson 01 →" pill (top 405); latte glass with four arrowed layers (Ecosystem, Versions, Inside the JVM, The lessons); chalkboard menu of 13 lessons. 390x844: h1, pill (top 275), full glass; menu below the fold. Clicking the JVM layer opens jvm.html: "Inside the JVM", pipeline "Hello.java → javac → Hello.class → java", four numbered steps, the 417-byte hex dump with three colour-keyed callouts (magic number, version, constant pool).
- **Findings:**
  - F1 [claim] Five seconds, both widths: site = Learn Java; topics = lessons, Inside the JVM, Versions; first action = the dark "Start lesson 01" pill.
  - F2 [claim] Layers read as links (title + "→" + one plain line), and the JVM layer delivers its promise, "Hello.class, all 417 bytes of it".
  - F3 [claim] Trunk test on jvm.html passes: site name, highlighted nav tab, page name, pipeline line.
  - F4 [defect] At 1280, menu row 09 "Records, sealed types and patterns" wraps; "patterns" sits on row 10's divider.
  - F5 [premise] The glass repeats the top nav: three routes to lesson 01 on one screen. Noted, not objected.
- **Verdict:** PASS
- **Requested change:** F4: let row 09 grow to two lines, or shorten it to "Records and patterns". Others: none.
