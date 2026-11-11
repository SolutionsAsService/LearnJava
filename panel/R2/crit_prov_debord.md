# Critic: Provocateur (Debord), R2

- **Anchor used:** *Society of the Spectacle*, Thesis 1: what was lived becomes a representation. A setup step nobody ran is an image of a working install.
- **Observed:** all 20 pages as text; build.py (`release_ok`, the tight check), runs.json, all 13 ribbon captions (the parts add up to each class size), the JVM byte ranges, javap facts (`ldc #13`, 9 bytes), the Versions rows. R1 fixes hold.

**Findings**
- F1 [defect] About → lessons: Windows readers are sent to PowerShell, then told to paste `javac … && java X`. Windows PowerShell 5.1, the default, rejects `&&`. The first step fails.
- F2 [claim] About: "brew install openjdk@21", then "Check it with javac -version". The formula is keg-only and is not linked, so macOS's `/usr/bin/javac` stub reports that no Java runtime is installed.
- F3 [claim] "Debian or Ubuntu: openjdk-21-jdk". Debian 12 does not have that package.
- F4 [claim] Ecosystem: "Most server-side Java is written on one of these." There is no source. The section heading "Free builds of the JDK" also lists the API documentation.
- F5 [claim] JVM: "count up from 45 (Java 1.1)". Java 1.0 also wrote 45, and Versions starts at 1.0.

**Verdict:** OBJECT

**Requested change:** F1 give a PowerShell line (`javac …; java X`) or say "PowerShell 7"; F2 add the symlink step from brew's caveat, or point macOS readers to Temurin; F3 "Ubuntu 22.04+, Debian 13"; F4 "Widely used server frameworks", and move the API docs out of that heading; F5 "45 (Java 1.0 and 1.1)".
