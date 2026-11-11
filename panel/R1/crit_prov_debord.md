# Critic: Provocateur (Debord), R1

- **Anchor used:** *Society of the Spectacle*, Thesis 1 (the lived becomes representation). Unrecorded sentences are images of claims.
- **Observed:** content.py, build.py (`release_ok`, `check_runs`), runs.json, footer, jvm, versions, ecosystem. I recompiled Hello with `--release 8` (major 52) and timed Threads (0.21 s). Footer, quoted outputs, dump, trademark lines hold.

**Findings**
- F1 [claim] jvm.html: "417 bytes of bytecode, the same on every machine." The bytes depend on the JDK and `--release`, not the machine: JDK 25, which About recommends, writes major 69. And 417 is the whole file; main's bytecode is 9 bytes.
- F2 [claim] Home: "the same .class files, which is why Java runs … Android apps." Android converts class files to DEX for ART, not a JVM. Nothing backs "bank back ends".
- F3 [defect] The pages say the build "checks/proves" the minimum with `javac --release`, but `release_ok` skips minimums below 8, so lessons 01, 05, 06 and 07 are never checked.
- F4 [claim] Versions: "every two years one is LTS." The timeline shows 11 to 17: three years.
- F5 [claim] Ecosystem meta: "official links." Learn Groovy is a third-party site.
- F6 [claim] "The last bytes of every class file name its source file." SourceFile is optional (`-g:none`).
- F7 [premise] Streams is badged 16+ but the note says "All of this arrived in Java 8". The record that forces 16 is never named.
- F8 [premise] Threads: "a fraction of a second" is true here but the build never measures it.

**Verdict:** OBJECT

**Requested change:** F1 "the same file wherever it runs"; F2 drop "which is why" and the Android/bank items; F3 test `--release 8` or reword; F4 "since 17"; F5 drop "official"; F6 "usually"; F7 name the record; F8 measure the time, or drop the phrase.
