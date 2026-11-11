"""Every word on the site that the build does not generate."""

# (class name in examples/, slug, title, one line, notes html, Java version that introduced the newest feature used)
LESSONS = [
    ("Hello", "hello", "Hello, World",
     "A class, a main method, one line printed.",
     """<p>Java code lives in <em>classes</em>: a class is a named bundle of data and the
     methods (named blocks of code) that work on it. A class named <code>Hello</code> goes in a file
     named <code>Hello.java</code>. The program starts at <code>main</code>:
     <code>public</code> (anyone may call it), <code>static</code> (no object is needed to
     call it), and <code>void</code> (it returns nothing). <code>String[] args</code> holds
     any words typed after the program's name.</p>
     <p>The text “Hello, World!” is stored inside the compiled file, in a part called the
     <em>constant pool</em>: the table of every name and piece of text a class uses.</p>
     <p><code>javac</code> compiles the file into <code>Hello.class</code>, and <code>java</code>
     runs it on the Java Virtual Machine (the JVM). The <a href="../index.html">home page</a> is
     that very <code>.class</code> file, byte for byte; <a href="../jvm.html">Inside the JVM</a>
     walks through it.</p>""", "1.0"),
    ("Variables", "variables", "Variables and types",
     "Eight primitive types, var, and what happens past the largest int.",
     """<p>A <em>type</em> says what kind of value a variable holds. Java has eight
     <em>primitive</em> types, which hold a plain value directly:
     <code>byte</code>, <code>short</code>, <code>int</code>, <code>long</code>,
     <code>float</code>, <code>double</code>, <code>char</code> and <code>boolean</code>.
     Their sizes are the same on every machine: an <code>int</code> is always 4 bytes (32
     bits). A floating-point type such as
     <code>double</code> holds numbers with a fractional part. Everything else, a
     <code>String</code> included, is an <em>object</em>: the variable holds a
     <em>reference</em>, the address where the object lives.</p>
     <p><code>var</code> (Java 10) lets the compiler infer a local variable's type; the type is
     still fixed. The last line shows overflow: one more than the largest <code>int</code>
     wraps around to the most negative one, silently.</p>""", "10"),
    ("Strings", "strings", "Strings",
     "== compares objects, equals compares text, and strings never change.",
     """<p><code>==</code> asks whether two references point at the <em>same object</em>;
     <code>equals</code> asks whether the text is the same. Use <code>equals</code> for
     strings.</p>
     <p>A <code>String</code> is <em>immutable</em>: <code>toUpperCase</code> returns a new
     string and leaves the old one alone. To build text piece by piece, use a
     <code>StringBuilder</code>: the <code>for</code> loop (explained in lesson 04) runs three
     times, and each <code>append</code> adds to the end and hands back the same builder, so
     two can be chained. Text blocks (three double quotes, <code>&quot;&quot;&quot;</code>, Java 15) keep line breaks.</p>""", "15"),
    ("ControlFlow", "control-flow", "Control flow",
     "if, a switch that returns a value, and a while loop.",
     """<p>The <code>switch</code> here is an <em>expression</em> (Java 14): each arrow
     <code>-&gt;</code> gives a value, there is no fall-through, and the result goes straight
     into <code>kind</code>. The <code>while</code> loop follows the Collatz rule from 27;
     nobody can say in advance how many steps it takes, which is what <code>while</code> is
     for.</p>""", "14"),
    ("Methods", "methods", "Methods",
     "Static methods, overloading by type, and recursion.",
     """<p>A <code>static</code> method belongs to the class, so <code>main</code> can call it
     without making an object. Two methods may share a name if their parameter types differ
     (<em>overloading</em>); the compiler picks one from the arguments. <code>factorial</code>
     uses <code>long</code> because 20! is larger than the biggest <code>int</code>.</p>""", "1.0"),
    ("ArraysDemo", "arrays", "Arrays",
     "A fixed-length row of values, sorted, and checked at every index.",
     """<p>An array's length is fixed when it is created and read with <code>.length</code>.
     The enhanced <code>for</code> loop visits each element. Unlike C, Java checks every index:
     reading past the end throws an <code>ArrayIndexOutOfBoundsException</code> instead of
     reading whatever memory follows. The program catches it to print the message; the
     <a href="11-exceptions.html">exceptions lesson</a> explains catching.</p>""", "5.0"),

    ("Classes", "classes", "Classes and objects",
     "Fields, a constructor, private state and toString.",
     """<p>A class describes objects; <code>new Account("Ada")</code> makes one.
     <code>private</code> fields can only be changed by the class's own methods, so
     <code>deposit</code> can refuse a bad amount. <code>final</code> means the field is set
     once. Money is kept in whole cents as a <code>long</code>, because a
     <code>double</code> cannot hold 0.10 exactly.</p>
     <p><code>@Override</code> on <code>toString</code> tells the compiler to check that it
     really replaces the method every object inherits from <code>Object</code>; that is the
     method <code>println</code> calls.</p>""", "5.0"),

    ("Interfaces", "interfaces", "Interfaces and polymorphism",
     "A contract, two classes that keep it, one loop over both.",
     """<p>An <code>interface</code> lists methods without bodies; a class that
     <code>implements</code> it must provide them. The loop holds a <code>List&lt;Shape&gt;</code>
     and calls <code>area()</code>; which body runs is decided at run time by the actual object.
     That is <em>polymorphism</em>.</p>""", "9"),

    ("Records", "records", "Records, sealed types and patterns",
     "Modern Java: data classes in one line, closed hierarchies, and switch on shape.",
     """<p>A <code>record</code> (Java 16) is a class for plain data: the compiler writes the
     constructor, the accessors, <code>equals</code>, <code>hashCode</code> and
     <code>toString</code>, which is why two <code>Square(2)</code> are equal.</p>
     <p><code>sealed</code> (Java 17) fixes the list of subtypes, so the <code>switch</code> in
     <code>area</code> can cover every case with no <code>default</code>; add a fourth shape
     and it stops compiling. <code>case Rect(double w, double h)</code> is a <em>record
     pattern</em> (Java 21): it checks the type and unpacks the fields in one step.</p>""", "21"),
    ("CollectionsDemo", "collections", "Collections and generics",
     "List, Map and Set, and one method that works for any comparable type.",
     """<p><code>List</code> keeps order, <code>Map</code> pairs keys with values
     (<code>TreeMap</code> keeps the keys sorted), and <code>Set</code> drops duplicates.
     The type in angle brackets, <code>List&lt;String&gt;</code>, is a <em>generic</em>
     parameter: the compiler then refuses to put anything but a <code>String</code> in.</p>
     <p><code>largest</code> is generic too. It works for any <code>T</code> that can be
     compared, so the same code finds the last word alphabetically and the biggest number.</p>""", "9"),

    ("Exceptions", "exceptions", "Exceptions",
     "try, catch and finally; checked and unchecked; try-with-resources.",
     """<p>Read the output in order: both calls to <code>parse</code> run, each printing its own
     lines, before <code>println</code> prints their sum, 42. <code>finally</code> runs whether
     or not an exception was thrown.</p>
     <p>A <em>checked</em> exception such as <code>IOException</code> must be caught or
     declared with <code>throws</code>, or the program does not compile. An
     <em>unchecked</em> one such as <code>NumberFormatException</code> need not be.
     <code>try (…)</code> closes the reader automatically, even after an error.</p>""", "11"),

    ("Streams", "streams", "Lambdas and streams",
     "Filter, map, sort and join a list in one expression.",
     """<p>A <em>lambda</em>, <code>l -&gt; l.year() &gt; 2000</code>, is a function written in
     place. A <em>method reference</em>, <code>Lang::name</code>, names an existing method
     instead. A <em>stream</em> passes each element through the steps in order; nothing
     happens until <code>collect</code> asks for the result. Lambdas and streams arrived in
     Java 8; this program also declares a <code>record</code>, which is why it needs Java
     16.</p>""", "16"),

    ("Threads", "threads", "Virtual threads",
     "Ten thousand tasks, each with its own thread, all waiting at once.",
     """<p>A <em>thread</em> runs code at the same time as other threads. Platform threads are
     expensive, so programs used to share a few among many tasks. Virtual threads (Java 21) are
     cheap enough to give every task its own: here 10,000 tasks each sleep 10 milliseconds,
     and they all wait at the same time. One after another, they would take 100 seconds.</p>
     <p><code>AtomicInteger</code> counts safely from many threads at once; a plain
     <code>int</code> would lose updates. Leaving the <code>try</code> block waits for every
     task, so the count is always 10,000.</p>""", "21"),
]

VERSIONS = [
    # (year, version, note, lts)
    (1996, "1.0", "Sun Microsystems releases Java: “write once, run anywhere” on the JVM.", False),
    (1998, "1.2", "The Collections framework: List, Map, Set.", False),
    (2004, "5.0", "Generics, enums, annotations and the enhanced for loop.", False),
    (2006, "6", "Sun begins releasing Java as open source: OpenJDK.", False),
    (2010, "—", "Oracle acquires Sun, and with it Java.", False),
    (2011, "7", "try-with-resources, the diamond <code>&lt;&gt;</code>, strings in switch.", False),
    (2014, "8", "Lambdas, streams and the java.time dates.", True),
    (2017, "9", "Modules, and JShell for trying code line by line.", False),
    (2018, "10", "<code>var</code>, and a new release every six months, in March and September.", False),
    (2018, "11", "Run a source file directly: <code>java Hello.java</code>.", True),
    (2020, "14", "Switch expressions, with <code>-&gt;</code> and a value.", False),
    (2020, "15", "Text blocks: strings in three double quotes that keep their line breaks.", False),
    (2021, "16", "Records: a one-line class for plain data.", False),
    (2021, "17", "Sealed classes.", True),
    (2023, "21", "Virtual threads, record patterns and pattern matching for switch.", True),
    (2025, "25", "The current long-term-support release.", True),
]

ECOSYSTEM = [
    ("Build tools", "Compile, test and package a project, and fetch its libraries.",
     [("Apache Maven", "https://maven.apache.org/guides/getting-started/"), ("Gradle", "https://docs.gradle.org/current/userguide/userguide.html")]),
    ("Frameworks", "Widely used frameworks for server-side Java.",
     [("Spring Boot", "https://docs.spring.io/spring-boot/"), ("Jakarta EE", "https://jakarta.ee/learn/"), ("Quarkus", "https://quarkus.io/guides/")]),
    ("Testing", "Write a test beside every class.",
     [("JUnit 5", "https://junit.org/junit5/docs/current/user-guide/")]),
    ("Other languages on the JVM", "They compile to the same class files, so they can call Java and be called by it.",
     [("Kotlin", "https://kotlinlang.org/docs/home.html"), ("Scala", "https://docs.scala-lang.org/"), ("Learn Groovy (hands-on)", "https://learngroovy.shadw.app/"), ("Clojure", "https://clojure.org/guides/getting_started")]),
    ("Android", "Android apps are written in Java or Kotlin, against the Android SDK.",
     [("Android developers", "https://developer.android.com/guide")]),
    ("The JDK and its documentation", "Free builds of the Java Development Kit, and the reference for its library.",
     [("OpenJDK", "https://openjdk.org/"), ("Eclipse Temurin", "https://adoptium.net/"), ("Java SE API documentation", "https://docs.oracle.com/en/java/javase/21/docs/api/")]),
]

# Sentences in the prose above that quote a program's output; the build checks each as a whole line.
QUOTED_OUTPUTS = [
    ("ControlFlow", "27 reaches 1 in 111 steps"),
    ("Records", "true"),
    ("Exceptions", "42"),
    ("Threads", "tasks finished: 10000"),
    ("Variables", "int is 4 bytes, long is 8 bytes"),
]
