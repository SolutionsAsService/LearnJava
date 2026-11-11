// Usage: node _src/measure.cjs <base-url> <outdir>
// Enumerates every page in site/ (never a typed list), screenshots key pages, and measures
// overflow, the smallest text, the hero's bottom edge and targets under 44px.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [base, outdir] = process.argv.slice(2);
const root = path.join(__dirname, '..', 'site');
const walk = d => fs.readdirSync(path.join(root, d), { withFileTypes: true }).flatMap(e =>
  e.isDirectory() ? (e.name === 'examples' || e.name === 'fonts' ? [] : walk(path.join(d, e.name))) : e.name.endsWith('.html') ? [path.join(d, e.name)] : []);
const pages = walk('').sort((a, b) => (a === 'index.html' ? -1 : b === 'index.html' ? 1 : a.localeCompare(b)));
const shots = new Set(['index.html', 'lessons/index.html', 'lessons/01-hello.html', 'lessons/09-records.html', 'jvm.html', 'versions.html', 'ecosystem.html', 'about.html']);
(async () => {
  const b = await chromium.launch(); const report = [];
  for (const scheme of ['light', 'dark']) for (const [w, h] of [[1280, 800], [375, 812], [390, 844]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, colorScheme: scheme, hasTouch: w < 500 });
    const p = await ctx.newPage();
    for (const pg of pages) {
      await p.goto(base + pg, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
      const m = await p.evaluate(() => {
        let minFont = 99, minEl = '';
        for (const el of document.querySelectorAll('body *')) {
          if (el.closest('[aria-hidden="true"]')) continue;
          if (![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
          const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
          const r = el.getBoundingClientRect(); if (!r.width) continue;
          const fs = parseFloat(cs.fontSize); if (fs < minFont) { minFont = fs; minEl = el.tagName + '.' + el.className + ' "' + el.textContent.trim().slice(0, 24) + '"'; }
        }
        const small = [...document.querySelectorAll('a, button, summary')].filter(a => { const r = a.getBoundingClientRect(); if (!r.width) return false;
          const inline = getComputedStyle(a).display === 'inline' && a.closest('p, li, figcaption') && !a.closest('nav, .legend, .strip, .chips, .lessons, .pager'); return !inline && (r.height < 44 || r.width < 24); }).map(a => a.textContent.trim().slice(0, 20));
        const hero = document.querySelector('.hero'); let heroBottom = null, parts = {};
        if (hero) { for (const s of ['.hero h1', '.start', '.glass', '.saucer', '.menu']) { const e = document.querySelector(s); if (e) parts[s] = Math.round(e.getBoundingClientRect().bottom); } heroBottom = Math.max(...Object.values(parts)); }
        return { scrollW: document.documentElement.scrollWidth, minFont, minEl, small: small.slice(0, 5), nSmall: small.length, heroBottom, parts };
      });
      report.push({ scheme, w, h, page: pg, ...m, overflow: m.scrollW > w });
      if (shots.has(pg) && (scheme === 'light' || pg === 'index.html')) await p.screenshot({ path: `${outdir}/${pg.replace(/\//g, '_')}-${w}-${scheme}.png`, fullPage: pg !== 'index.html' });
    }
    await ctx.close();
  }
  await b.close();
  console.log(JSON.stringify(report).replace(/},{/g, '},\n{'));
})();
