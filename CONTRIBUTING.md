# Contributing

1. Add or fix a program in `examples/`. A new lesson also needs an entry in `LESSONS` in `_src/content.py`, including the oldest Java version it compiles under.
2. Run `python3 _src/build.py`. It fails on a warning, a failed run, a wrong minimum version or a dead link.
3. Commit the program, the rebuilt `site/` and `_src/runs.json` together.

To report a wrong fact, open an issue that quotes the sentence and cites the Java Language Specification, the JVM Specification or the JDK documentation.
