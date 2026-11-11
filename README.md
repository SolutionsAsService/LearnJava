# Learn Java, from the bytes up

A static website that teaches Java in thirteen programs, from `main` to virtual threads. Its home page is a café: a latte glass whose four layers link the site, and a chalkboard menu of the lessons. The *Inside the JVM* page draws the real `Hello.class` that `javac` makes from lesson 01, byte by byte, in its six parts. Every lesson shows a ribbon of the class files its program becomes.

The earlier home page, the hex dump of `Hello.class`, is kept on the branch `design/hexdump-b-plus`.

Every program is compiled with `javac -Xlint:all` and run when the site is built, and each lesson shows the output it actually printed. The build also proves each lesson's stated minimum Java version with `javac --release`.

**Live:** https://learnjava.shadw.app

## Layout

```
examples/      the thirteen programs (Hello.java … Threads.java)
_src/
  content.py   every sentence on the site that is not generated
  build.py     compiles, runs and javap's the examples, parses Hello.class, writes site/, checks it
  runs.json    stored results, reused with --no-run or when no JDK is installed
  measure.cjs  screenshots and layout measurements of every page (Playwright)
site/          the deployable static site (committed)
```

## Run one program yourself

```bash
cd examples
javac -Xlint:all Hello.java && java Hello
```

Requires JDK 21 or newer (lessons 09 and 13 use Java 21 features).

## Rebuild

```bash
python3 _src/build.py          # compile, run, write site/
python3 _src/build.py --no-run # reuse _src/runs.json
```

The build fails if any program warns, fails or exits non-zero; if a lesson's stated minimum version is wrong; if a quoted output is not a line the program printed; if a local link is dead; or if the deploy config is missing.

## Deploy

Shadw and Vercel, with no build step on the host:

- `vercel.json` serves `site/`, and `site/vercel.json` serves `.` when the Root Directory is `site`.
- `fluid.json` points Shadw at `site`.
- The root `index.html` redirects to `site/` on any other static host.
- `.vercelignore` keeps the sources out of the upload.

## Design

The design decisions and the critique rounds are in [DESIGN-LOG.md](DESIGN-LOG.md), and the critics' reports are in `panel/`.

## Licence

MIT. An unofficial guide: Java and OpenJDK are trademarks of Oracle and/or its affiliates. Fonts: Fraunces and IBM Plex Mono, SIL Open Font Licence.
