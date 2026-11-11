#!/usr/bin/env python3
"""Build the Learn Java site.

1. Compile every program in examples/ with javac -Xlint:all, run it, and record the output, the JDK
   version, and the oldest --release each one compiles under. Results go to _src/runs.json, which is
   reused when no JDK is installed (--no-run).
2. Parse the real Hello.class and capture `javap -c`, for the home page and the JVM page.
3. Write site/, then fail on a dead local link, a warning, a failed run, a quoted output the program
   did not print, a wrong minimum version, or missing deploy config.

Standard-library Python only.   python3 _src/build.py [--no-run]
"""
import html
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, EX, OUT = ROOT / "_src", ROOT / "examples", ROOT / "site"
sys.path.insert(0, str(SRC))
import content as K  # noqa: E402

SITE_URL = "https://learnjava.shadw.app"
JAVAC = "javac -Xlint:all"
BUILT = ""


def sh(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, timeout=120)
    clean = lambda s: "\n".join(l for l in s.splitlines() if not l.startswith("Picked up JAVA_TOOL_OPTIONS"))
    return p.returncode, clean(p.stdout), clean(p.stderr)


def release_ok(cls, release, tmp):
    code, _, _ = sh(f"javac --release {release} -d {tmp}/r{release} {EX / (cls + '.java')}", tmp)
    return code == 0


# --------------------------------------------------------------------------- run
def run_all(do_run):
    cache_path = SRC / "runs.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    if not do_run or not shutil.which("javac"):
        if do_run:
            print("  no JDK found: using the cached results in _src/runs.json")
        return cache
    tmp = tempfile.mkdtemp()
    _, out, err = sh("javac -version", tmp)
    cache = {"jdk": (out or err).strip(), "built": time.strftime("%Y-%m-%d", time.gmtime()), "runs": {}}
    for L in K.LESSONS:
        cls = L[0]
        d = Path(tmp) / cls
        d.mkdir()
        code, so, se = sh(f"{JAVAC} -d {d} {EX / (cls + '.java')}", tmp)
        warnings = [l for l in (so + se).splitlines() if "warning" in l]
        r = {"command": f"{JAVAC} {cls}.java && java {cls}", "compiled": code == 0, "warnings": warnings}
        if code == 0:
            cb = (d / f"{cls}.class").read_bytes()
            r["class_size"] = len(cb)
            r["regions"] = [[n, a, z] for n, a, z, _ in parse_class(cb)]
            rc, so, se = sh(f"java -cp {d} {cls}", tmp)
            r.update(stdout=so + ("\n" + se if se else ""), exit=rc)
        else:
            r.update(stdout="", exit=code, error=se[-1500:])
        # the oldest release it compiles under, checked both ways where the JDK can (8 and newer)
        need = K_min(L)
        r["min_release_ok"] = need < 8 or release_ok(cls, max(need, 8), tmp)
        r["min_release_tight"] = need <= 8 or not release_ok(cls, need - 1, tmp)
        cache["runs"][cls] = r
    # the class file the home page is drawn from
    hello = Path(tmp) / "Hello" / "Hello.class"
    cache["hello_class"] = hello.read_bytes().hex()
    _, jp, _ = sh(f"javap -c -p -cp {hello.parent} Hello", tmp)
    cache["javap"] = jp
    shutil.rmtree(tmp, ignore_errors=True)
    cache_path.write_text(json.dumps(cache, indent=1, ensure_ascii=False) + "\n")
    return cache


def K_min(L):
    v = L[5]
    return int(v.split(".")[1]) if v.startswith("1.") else int(float(v))


# ------------------------------------------------------------- the class file
def parse_class(b):
    """Return the regions of a class file: (name, start, end, facts)."""
    regions, p = [], 0
    u2 = lambda o: struct.unpack(">H", b[o:o + 2])[0]
    u4 = lambda o: struct.unpack(">I", b[o:o + 4])[0]
    regions.append(("magic", 0, 4, {"hex": b[0:4].hex().upper()}))
    minor, major = u2(4), u2(6)
    regions.append(("version", 4, 8, {"major": major, "minor": minor, "java": major - 44}))
    count, p = u2(8), 10
    pool, i = [None], 1
    while i < count:
        tag = b[p]
        if tag == 1:
            n = u2(p + 1); pool.append(("utf8", b[p + 3:p + 3 + n].decode("utf-8", "replace"))); p += 3 + n
        elif tag in (3, 4):
            pool.append(("num", None)); p += 5
        elif tag in (5, 6):
            pool.append(("wide", None)); pool.append(None); p += 9; i += 1
        elif tag in (7, 8, 16, 19, 20):
            pool.append((tag, u2(p + 1))); p += 3
        elif tag == 15:
            pool.append(("mh", None)); p += 4
        else:  # 9, 10, 11, 12, 17, 18
            pool.append((tag, u2(p + 1), u2(p + 3))); p += 5
        i += 1
    texts = [e[1] for e in pool if e and e[0] == "utf8"]
    regions.append(("pool", 8, p, {"entries": count - 1, "has_hello": "Hello, World!" in texts}))
    head = p
    p += 6  # access flags, this class, super class
    p += 2 + 2 * u2(p)  # interfaces

    # fields
    p = skip_fields(b, p)
    regions.append(("header", head, p, {"access": hex(u2(head))}))
    mstart = p
    nmeth = u2(p); p += 2
    main_code = 0
    for _ in range(nmeth):
        name = pool[u2(p + 2)][1]
        nattr = u2(p + 6); p += 8
        for _ in range(nattr):
            aname = pool[u2(p)][1]; length = u4(p + 2)
            if aname == "Code" and name == "main":
                main_code = u4(p + 2 + 4 + 4)
            p += 6 + length
    regions.append(("methods", mstart, p, {"methods": nmeth, "main_code": main_code}))
    regions.append(("attributes", p, len(b), {}))
    assert regions[-1][2] == len(b)
    return regions


def skip_fields(b, p):
    u2 = lambda o: struct.unpack(">H", b[o:o + 2])[0]
    u4 = lambda o: struct.unpack(">I", b[o:o + 4])[0]
    n = u2(p); p += 2
    for _ in range(n):
        nattr = u2(p + 6); p += 8
        for _ in range(nattr):
            p += 6 + u4(p + 2)
    return p


REGION_TEXT = {
    "magic": ("The magic number", "Every class file starts with CA FE BA BE. The JVM checks it before anything else.", "jvm.html#magic", "Inside the JVM"),
    "version": ("The version", "major {major}: compiled for Java {java}, so it needs Java {java} or later to run.", "versions.html", "Versions"),
    "pool": ("The constant pool", "{entries} entries: every name and piece of text the class uses, “Hello, World!” among them.", "lessons/01-hello.html", "Lesson 01"),
    "header": ("The class header", "public class Hello, which extends Object; with no interfaces and no fields.", "lessons/07-classes.html", "Lesson 07"),
    "methods": ("The methods", "{methods} methods; main is {main_code} bytes of bytecode.", "jvm.html#bytecode", "Inside the JVM"),
    "attributes": ("The attributes", "The source file’s name, Hello.java, for stack traces and debuggers.", "ecosystem.html", "Ecosystem"),
}
SHORT = {"magic": "magic", "version": "version", "pool": "constant pool", "header": "header", "methods": "methods", "attributes": "attributes"}


def dump_rows(b, regs, gutter=True):
    owner = {}
    for n, (name, s0, e, _) in enumerate(regs, 1):
        for i in range(s0, e):
            owner[i] = n
    starts = {s0: n for n, (_, s0, _, _) in enumerate(regs, 1)}
    rows = []
    for off in range(0, len(b), 16):
        marks = "".join(f'<i class="badge g{n}">{n}</i>' for i, n in starts.items() if off <= i < off + 16)
        cells = "".join(f'<span class="by r{owner[i]}{" st" if i in starts else ""}">{b[i]:02X}</span>' for i in range(off, min(off + 16, len(b))))
        rows.append(f'<span class="row"><span class="gut">{marks}</span><span class="off">{off:04X}</span>{cells}</span>')
    return "".join(rows)


def legend_items(regs):
    out = []
    for n, (name, s0, e, facts) in enumerate(regs, 1):
        t, line, href, cta = REGION_TEXT[name]
        out.append(f'<li class="lg r{n}"><a href="{href}"><span class="num">{n}</span>'
                   f'<span class="lg-t">{html.escape(t)} <span class="lg-b">bytes {s0}–{e - 1}</span></span>'
                   f'<span class="lg-l">{html.escape(line.format(**facts))}<span class="lg-go">{html.escape(cta)} →</span></span>'
                   f'<span class="lg-go lg-go-m" aria-hidden="true">{html.escape(cta)} →</span></a></li>')
    return "".join(out)


def ribbon(cls, runs, up=""):
    """A lesson's own class file as a strip of six tinted runs, sized by bytes."""
    r = runs["runs"][cls]
    size = r["class_size"]
    names = [n for n, _, _ in r["regions"]]
    segs = "".join(f'<span class="seg r{names.index(n) + 1}" style="flex-grow:{z - a}"></span>' for n, a, z in r["regions"])
    parts = ", ".join(f'{SHORT[n]} {z - a}' for n, a, z in r["regions"])
    return (f'<figure class="ribbon"><div class="segs" aria-hidden="true">{segs}</div>'
            f'<figcaption><code>{cls}.class</code> is {size} bytes: {parts}. '
            f'<a href="{up}jvm.html">What these parts are</a></figcaption></figure>')


def hero(runs):
    b = bytes.fromhex(runs["hello_class"])
    regs = parse_class(b)
    strip = "".join(f'<li><a href="{lesson_href(i)}" title="{html.escape(L[2])}" aria-label="Lesson {i + 1}: {html.escape(L[2])}">{i + 1:02d}</a></li>'
                    for i, L in enumerate(K.LESSONS))
    return f"""<section class="hero" aria-labelledby="h1">
  <p class="kicker">Every compiled Java class begins with the same four bytes:</p>
  <div class="magic-row"><p class="magic" aria-label="C A F E B A B E"><span>CA</span><span>FE</span><span>BA</span><span>BE</span></p>
    <a class="start" href="lessons/01-hello.html">Start lesson 01 →</a></div>
  <h1 id="h1">Learn Java, from the bytes up</h1>
  <p class="plain">Below is lesson 01, compiled: the file every Java program becomes.</p>
  <figure class="dump" aria-hidden="true"><div class="dump-h">Hello.class · {len(b)} bytes</div><div class="rows">{dump_rows(b, regs)}</div></figure>
  <ol class="legend" aria-label="The six parts of Hello.class">{legend_items(regs)}</ol>
  <p class="lede">That is <code>Hello.class</code>, the whole of it: the {len(b)} bytes <code>javac</code> made from lesson 01. Each coloured run is one part of the file, and each part leads to the page that explains it.</p>
  <nav class="strip" aria-label="Lessons"><p class="strip-h">All {len(K.LESSONS)} lessons <span class="idx">lessons[{len(K.LESSONS)}]</span> · titles below</p><ol>{strip}</ol></nav>
</section>"""


# ------------------------------------------------------------------ highlight
KW = set("""abstract assert boolean break byte case catch char class continue default do double else enum extends final
finally float for if implements import instanceof int interface long native new package permits private protected public
record return sealed short static super switch this throw throws try var void volatile while yield true false null""".split())
TOKEN = re.compile(r'(?P<com>//[^\n]*|/\*.*?\*/)|(?P<tb>""".*?""")|(?P<str>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')'
                   r'|(?P<ann>@\w+)|(?P<num>\b\d[\d_]*(?:\.\d+)?[Ll]?\b)|(?P<word>[A-Za-z_]\w*)', re.S)


def highlight(src):
    out, pos = [], 0
    for m in TOKEN.finditer(src):
        out.append(html.escape(src[pos:m.start()]))
        t, k = m.group(0), m.lastgroup
        e = html.escape(t)
        cls = {"com": "tc", "tb": "ts", "str": "ts", "ann": "tp", "num": "tn"}.get(k)
        if k == "word":
            cls = "tk" if t in KW else ("tt" if t[0].isupper() else None)
        out.append(f'<span class="{cls}">{e}</span>' if cls else e)
        pos = m.end()
    out.append(html.escape(src[pos:]))
    return "".join(out)


# ------------------------------------------------------------------ layout
NAV = [("index.html", "Home"), ("lessons/index.html", "Lessons"), ("jvm.html", "Inside the JVM"),
       ("versions.html", "Versions"), ("ecosystem.html", "Ecosystem"), ("about.html", "About")]
PROTECT = re.compile(r"(<pre.*?</pre>|<code.*?</code>|<samp.*?</samp>|<[^>]+>)", re.S)


def typeset(markup):
    markup = re.sub(r"<code>([^<]{25,}?)</code>", r'<code class="w">\1</code>', markup)
    parts = PROTECT.split(markup)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"(?<=\w)(?:'|&#x27;)(?=\w)", "\u2019", parts[i])
        if i and (parts[i - 1].startswith("<code") or parts[i - 1] == "</code>"):
            parts[i] = re.sub(r"^(?:'|&#x27;)(?=\w)", "\u2019", parts[i])
    return "".join(parts)


def page(path, title, body, desc, active=None):
    up = "../" * path.count("/")
    links = "".join(f'<li><a href="{up}{h}"{" aria-current=\"page\"" if h == active else ""}>{l}</a></li>' for h, l in NAV)
    full = "Learn Java" if title is None else f"{title} · Learn Java"
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(full)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE_URL}/og.png">
<meta name="theme-color" content="#f2ead9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#17100b" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{up}fonts/ibm-plex-mono-normal-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{up}css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <a class="mark" href="{up}index.html"><span class="mark-hex" aria-hidden="true">CAFE</span><span>Learn Java</span></a>
  <nav aria-label="Site"><ul>{links}</ul></nav>
</header>
<main id="main">
{typeset(body)}
</main>
<footer class="foot">
  <p>Every program on this site was compiled with <code>{html.escape(JAVAC)}</code> on {BUILT} and run; the output shown is what it printed. <a href="{up}about.html">How</a> · <a href="https://github.com/SolutionsAsService/LearnJava">Source</a> · MIT licence.</p>
  <p>An unofficial guide. Java is a trademark of Oracle and/or its affiliates.</p>
</footer>
</body>
</html>
"""
    dest = OUT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc)


def lesson_href(i, up=""):
    L = K.LESSONS[i]
    return f"{up}lessons/{i + 1:02d}-{L[1]}.html"


def code_block(cls, runs, up=""):
    src = (EX / f"{cls}.java").read_text()
    r = runs["runs"][cls]
    out = html.escape(r["stdout"].rstrip("\n"))
    return f"""<figure class="ex">
  <figcaption><span class="fname">{cls}.java</span><span class="fmeta">{sum(1 for l in src.splitlines() if l.strip())} lines</span></figcaption>
  <pre class="code"><code class="b">{highlight(src)}</code></pre>
  <div class="out"><div class="out-h"><span>Output</span><span>exit {r["exit"]} · {len(r["warnings"])} warnings</span></div><pre><samp>{out}</samp></pre></div>
  <div class="cmd"><p class="cmd-h">Compile and run it yourself</p><pre><code class="b">{html.escape(r["command"])}</code></pre>
  <p class="setup"><a download href="{up}examples/{cls}.java">Download {cls}.java</a>, open a terminal in the folder you saved it to, and paste the command. No JDK yet? <a href="{up}about.html#setup">How to get one</a>.</p></div>
</figure>"""


# ------------------------------------------------------------------ hero
# ------------------------------------------------------------------ pages
def build_home(runs):
    items = "".join(f'<li><a href="{lesson_href(i)}"><span class="ln">{i + 1:02d}</span><span class="lt">{html.escape(L[2])}</span>'
                    f'<span class="ll">{html.escape(L[3])}</span><span class="lv">Java {L[5]}+</span></a></li>' for i, L in enumerate(K.LESSONS))
    body = f"""{hero(runs)}
<section class="wrap">
  <h2>What Java is</h2>
  <p>Java is a general-purpose language. Its compiler, <code>javac</code>, turns your code into <em>bytecode</em>: instructions for the Java Virtual Machine (the JVM), not for one kind of processor. So the same <code>.class</code> file runs unchanged on any computer with a JVM of the right version. Java manages memory for you, checks every array index, and catches many mistakes before the program runs, when it is compiled.</p>
  <h2>The course</h2>
  <ol class="lessons">{items}</ol>
  <p class="small">“Java 21+” is the oldest version the lesson compiles under. For Java 8 and later the build proves it with <code>javac --release</code>; the older minimums (1.0, 5.0) come from the language's history, because JDK 21 cannot compile for them.</p>
</section>"""
    page("index.html", None, body, "Learn Java from the bytes up: thirteen lessons, every program compiled and run, and the class file the compiler makes.", active="index.html")


def build_lessons(runs):
    items = "".join(f'<li><a href="{i + 1:02d}-{L[1]}.html"><span class="ln">{i + 1:02d}</span><span class="lt">{html.escape(L[2])}</span>'
                    f'<span class="ll">{html.escape(L[3])}</span><span class="lv">Java {L[5]}+</span></a></li>' for i, L in enumerate(K.LESSONS))
    body = f"""<article class="wrap">
  <p class="kicker"><code>lessons[{len(K.LESSONS)}]</code></p>
  <h1>The course</h1>
  <p class="lede">Thirteen programs, from <code>main</code> to virtual threads. Each was compiled with every warning switched on and run; its page shows what it printed.</p>
  <ol class="lessons">{items}</ol>
</article>"""
    page("lessons/index.html", "Lessons", body, "Thirteen Java lessons, each a program compiled and run.", active="lessons/index.html")
    for i, L in enumerate(K.LESSONS):
        cls, slug, title, line, notes, ver = L
        prev = (f"{i:02d}-{K.LESSONS[i - 1][1]}.html", K.LESSONS[i - 1][2], f"lesson {i} · <span class='idx'>lessons[{i - 1}]</span>") if i else ("index.html", "All lessons", "the course")
        nxt = (f"{i + 2:02d}-{K.LESSONS[i + 1][1]}.html", K.LESSONS[i + 1][2], f"lesson {i + 2} · <span class='idx'>lessons[{i + 1}]</span>") if i + 1 < len(K.LESSONS) else ("../jvm.html", "Inside the JVM", "next")
        body = f"""<article class="wrap">
  <p class="kicker"><a href="index.html">Lessons</a> · lesson {i + 1} of {len(K.LESSONS)} <span class="idx">lessons[{i}]</span> · Java {ver}+</p>
  <h1>{html.escape(title)}</h1>
  <p class="lede">{html.escape(line)}</p>
  {ribbon(cls, runs, up="../")}
  {code_block(cls, runs, up="../")}
  <div class="notes">{notes}</div>
  <nav class="pager" aria-label="Lessons">
    <a class="prev" href="{prev[0]}"><span>← {prev[2]}</span>{html.escape(prev[1])}</a>
    <a class="next" href="{nxt[0]}"><span>{nxt[2]} →</span>{html.escape(nxt[1])}</a>
  </nav>
</article>"""
        page(f"lessons/{i + 1:02d}-{slug}.html", f"{title} (lesson {i + 1})", body, f"Java lesson {i + 1}: {line}", active="lessons/index.html")


def build_jvm(runs):
    b = bytes.fromhex(runs["hello_class"])
    regs = parse_class(b)
    R = {name: (s0, e, f) for name, s0, e, f in regs}
    v = R["version"][2]
    javap = runs["javap"]
    main = javap[javap.index("public static void main"):]
    main = main[:main.index("}")].rstrip()
    rng = lambda n: f"bytes {R[n][0]}–{R[n][1] - 1}"
    body = f"""<article class="wrap">
  <p class="kicker">Hello.java → javac → Hello.class → java</p>
  <h1>Inside the JVM</h1>
  <p class="lede">What happens between typing <code>javac Hello.java</code> and seeing “Hello, World!”, shown with the real file the compiler made.</p>
  <ol class="pipe" aria-label="The four steps">
    <li><strong>You write source</strong>, <code>Hello.java</code>: text a person can read.</li>
    <li><strong><code>javac</code> compiles it</strong> to <code>Hello.class</code>, a {len(b)}-byte class file. It runs unchanged on any JVM of version {v["java"]} or later.</li>
    <li><strong><code>java</code> starts a JVM</strong>, which loads the class, checks that it is safe, and runs it.</li>
    <li><strong>The JIT compiler</strong> turns code that runs often into the processor's own instructions while the program runs.</li>
  </ol>
</article>
<div class="jvm-file">
  <figure class="dump" aria-hidden="true"><div class="dump-h">Hello.class · {len(b)} bytes</div><div class="rows">{dump_rows(b, regs)}</div></figure>
  <ol class="legend" aria-label="The six parts of Hello.class">{legend_items(regs).replace('href="jvm.html#', 'href="#').replace('href="lessons/', 'href="lessons/')}</ol>
</div>
<article class="wrap">
  <h2 id="magic"><span class="num-h r1">1</span> The magic number <span class="rng">{rng("magic")}</span></h2>
  <p>The first four bytes of every class file are <code>CA FE BA BE</code>. A JVM that reads anything else refuses the file.</p>
  <h2 id="version"><span class="num-h r2">2</span> The version <span class="rng">{rng("version")}</span></h2>
  <p>Minor {v["minor"]}, major {v["major"]}. Major versions count up from 45 (Java 1.1), so {v["major"]} means Java {v["java"]}, and an older JVM will not run the file. See <a href="versions.html">Versions</a>.</p>
  <h2 id="pool"><span class="num-h r3">3</span> The constant pool <span class="rng">{rng("pool")}</span></h2>
  <p>{R["pool"][2]["entries"]} entries: the class's own name, <code>java/lang/Object</code>, <code>System.out</code>, <code>println</code> and the text “Hello, World!”. Instructions refer to them by number, like <code>#13</code> below. At {R["pool"][1] - R["pool"][0]} of {len(b)} bytes, the pool is most of the file.</p>
  <h2 id="header"><span class="num-h r4">4</span> The class header <span class="rng">{rng("header")}</span></h2>
  <p>Who may use the class (<code>public</code>), its own name, its superclass (<code>Object</code>), and its interfaces and fields, of which Hello has none. <a href="lessons/07-classes.html">Lesson 07</a> builds a class with fields.</p>
  <h2 id="bytecode"><span class="num-h r5">5</span> The methods and their bytecode <span class="rng">{rng("methods")}</span></h2>
  <p>Hello has {R["methods"][2]["methods"]} methods: the constructor the compiler adds, and <code>main</code>. This is what <code>javap -c Hello</code> prints for <code>main</code>'s {R["methods"][2]["main_code"]} bytes of <em>bytecode</em>. Each line is one instruction for the JVM, which is a <em>stack machine</em>: instructions push values onto a stack and take them off.</p>
  <pre class="code"><code class="b">{html.escape(main)}</code></pre>
  <ul class="ops">
    <li><code>getstatic</code> pushes <code>System.out</code>, the object that prints.</li>
    <li><code>ldc</code> pushes the string “Hello, World!” from the constant pool.</li>
    <li><code>invokevirtual</code> calls <code>println</code> on them.</li>
    <li><code>return</code> ends <code>main</code>, and with it the program.</li>
  </ul>
  <h2 id="attributes"><span class="num-h r6">6</span> The attributes <span class="rng">{rng("attributes")}</span></h2>
  <p>Extra facts about the class. Here there is one: <code>SourceFile</code>, naming <code>Hello.java</code>, which stack traces and debuggers use to point back at your code. A compiler can be told to leave it out. See <a href="ecosystem.html">Ecosystem</a>.</p>
  <h2>Memory you do not free</h2>
  <p>Objects live on the <em>heap</em>. When nothing refers to an object any more, the <em>garbage collector</em> reclaims it; there is no <code>free</code> and no <code>delete</code>. The price is that you do not decide exactly when memory comes back.</p>
  <p class="docs">Further: <a href="https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html">JVM specification, chapter 4: the class file format</a> · <a href="https://docs.oracle.com/en/java/javase/21/docs/specs/man/javap.html">javap</a></p>
</article>"""
    page("jvm.html", "Inside the JVM", body, "From Hello.java to bytecode: the real class file, its six parts, and the bytecode of main.", active="jvm.html")


def build_versions(runs):
    by_ver = {}
    for i, L in enumerate(K.LESSONS):
        by_ver.setdefault(L[5], []).append(f'<a href="{lesson_href(i)}">{i + 1:02d}</a>')
    rows = "".join(f"<li{' class=\"lts\"' if lts else ''}><span class='yr'>{y}</span><span class='vn'>{v}</span>"
                   f"<span class='vt'>{t}{' <em class=\"tag\">LTS</em>' if lts else ''}"
                   f"{(' <span class=\"uses\">Lessons that need it: ' + ', '.join(by_ver[v]) + '</span>') if v in by_ver else ''}</span></li>"
                   for y, v, t, lts in K.VERSIONS)
    v = parse_class(bytes.fromhex(runs["hello_class"]))[1][3]
    body = f"""<article class="wrap">
  <p class="kicker">major {v["major"]} = Java {v["java"]}</p>
  <h1>Versions</h1>
  <p class="lede">Java has kept almost every old program running while it changed. Since 2018 a new version arrives every six months. Some are long-term-support (LTS) releases that companies stay on for years: 11 in 2018, 17 in 2021, and since then one every two years.</p>
  <ul class="versions">{rows}</ul>
  <p class="small">This site is built with <code>{html.escape(runs["jdk"])}</code>. The lesson numbers beside a version are the lessons that cannot compile under anything older. For Java 8 and later the build proves each one with <code>javac --release</code>.</p>
</article>"""
    page("versions.html", "Versions", body, "Java's versions from 1.0 to 25, and which lessons need which.", active="versions.html")


def build_ecosystem():
    secs = "".join(f'<section class="eco"><h2>{html.escape(t)}</h2><p>{html.escape(d)}</p><ul class="chips">'
                   + "".join(f'<li><a href="{u}">{html.escape(n)}</a></li>' for n, u in links) + "</ul></section>"
                   for t, d, links in K.ECOSYSTEM)
    body = f"""<article class="wrap">
  <p class="kicker">SourceFile: Hello.java</p>
  <h1>Ecosystem</h1>
  <p class="lede">The tools, frameworks and languages built around the JVM. A class file's last part, its <em>attributes</em>, usually names its source file, so these tools can point back to your code.</p>
  {secs}
</article>"""
    page("ecosystem.html", "Ecosystem", body, "Java's build tools, frameworks, testing, JVM languages, Android and JDKs, with links to their documentation.", active="ecosystem.html")


def build_about(runs):
    n = len(runs["runs"])
    nw = sum(len(r["warnings"]) for r in runs["runs"].values())
    body = f"""<article class="wrap">
  <p class="kicker">java -version</p>
  <h1>About this site</h1>
  <p class="lede">One Python script, <code>_src/build.py</code>, compiles every program in <code>examples/</code>, runs it, reads the class file it makes, and writes these pages from the results.</p>
  <h2>The last build</h2>
  <p>On {BUILT}, with <code>{html.escape(runs["jdk"])}</code>: {n} programs compiled with <code>{html.escape(JAVAC)}</code>, {nw} warnings, and every one ran and exited 0. With <code>--no-run</code>, or without a JDK, the build reuses those stored results, and this date says when they were made.</p>
  <h2 id="setup">Getting a JDK</h2>
  <p>A <em>JDK</em> (Java Development Kit) gives you <code>javac</code> to compile and <code>java</code> to run. You type both in a <em>terminal</em> (Terminal on macOS, a Linux shell, or Windows Terminal).</p>
  <ul>
    <li><strong>Any system:</strong> download a free JDK 21 or newer from <a href="https://adoptium.net/">Eclipse Temurin</a> and run its installer.</li>
    <li><strong>macOS with Homebrew:</strong> <code>brew install openjdk@21</code>.</li>
    <li><strong>Debian or Ubuntu:</strong> <code>sudo apt install openjdk-21-jdk</code> (<code>sudo</code> asks for your password).</li>
    <li><strong>Windows:</strong> in PowerShell, <code>winget install EclipseAdoptium.Temurin.21.JDK</code>, then open a new window.</li>
  </ul>
  <p>Check it with <code>javac -version</code>. Then download any program from its lesson. In the terminal, move to the folder it saved to with <code>cd</code> (for example <code>cd Downloads</code>), paste the command printed under the program, and compare what it prints with the dark output box.</p>
  <h2>Design</h2>
  <p>The home page is the real <code>Hello.class</code>, parsed byte by byte at build time. The design decisions and the critique rounds are in <code>DESIGN-LOG.md</code> in the repository. Type: Fraunces and IBM Plex Mono (SIL Open Font Licence), self-hosted.</p>
  <p>This is an unofficial guide. Java and OpenJDK are trademarks of Oracle and/or its affiliates.</p>
</article>"""
    page("about.html", "About", body, "How Learn Java is built, and how to get a JDK.", active="about.html")


def build_404():
    page("404.html", "Not found", """<article class="wrap"><p class="kicker">java.lang.ClassNotFoundException</p><h1>404</h1>
<p class="lede">No class by that name. <a href="index.html">Load the home page instead.</a></p></article>""", "Page not found.")


# ------------------------------------------------------------------ checks
def check_links():
    bad = []
    for f in OUT.rglob("*.html"):
        for href in re.findall(r'href="([^"#]+)(?:#[^"]*)?"', f.read_text()):
            if not href.startswith(("http", "mailto:")) and not (f.parent / href).resolve().exists():
                bad.append(f"{f.relative_to(OUT)} -> {href}")
    return bad


def check_deploy():
    try:
        root = json.loads((ROOT / "vercel.json").read_text())
        inner = json.loads((OUT / "vercel.json").read_text())
        fluid = json.loads((ROOT / "fluid.json").read_text())
    except (OSError, ValueError) as e:
        return [f"deploy config: {e}"]
    bad = []
    if root.get("outputDirectory") != "site" or inner.get("outputDirectory") != "." or not root.get("fluid"):
        bad.append("deploy config: vercel.json must serve site/ with fluid on, and site/vercel.json must serve .")
    if fluid.get("static_dir") != "site" or not SITE_URL.endswith(".shadw.app"):
        bad.append("deploy config: fluid.json static_dir must be site; SITE_URL must be the shadw.app address")
    return bad


def check_runs(runs):
    bad = []
    for cls, r in runs["runs"].items():
        if not r["compiled"] or r["exit"] != 0 or r["warnings"]:
            bad.append(f"{cls}: compiled={r['compiled']} exit={r['exit']} warnings={len(r['warnings'])}")
        if not r.get("min_release_ok") or not r.get("min_release_tight"):
            bad.append(f"{cls}: its stated minimum Java version is wrong (ok={r.get('min_release_ok')}, tight={r.get('min_release_tight')})")
    for cls, expect in K.QUOTED_OUTPUTS:
        if expect not in runs["runs"][cls]["stdout"].splitlines():
            bad.append(f"{cls}: prose quotes {expect!r}, not a line of its output")
    return bad


def main():
    global BUILT
    runs = run_all("--no-run" not in sys.argv)
    BUILT = runs["built"]
    for f in OUT.rglob("*.html"):
        f.unlink()
    shutil.rmtree(OUT / "examples", ignore_errors=True)
    shutil.copytree(EX, OUT / "examples")
    build_home(runs)
    build_lessons(runs)
    build_jvm(runs)
    build_versions(runs)
    build_ecosystem()
    build_about(runs)
    build_404()
    problems = check_links() + check_deploy() + check_runs(runs)
    print(f"built {len(list(OUT.rglob('*.html')))} pages from {len(runs['runs'])} compiled programs; Hello.class is {len(runs['hello_class']) // 2} bytes")
    if problems:
        print("problems:", *problems, sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
