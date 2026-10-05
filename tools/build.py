#!/usr/bin/env python3
"""Build the static study pages.  Run from the repo root:  python3 tools/build.py
Content lives in tools/content/*.py (each exposes PAGES = [...]).
Output is plain HTML next to assets/, ready for GitHub Pages."""
import os, sys, importlib, pkgutil
sys.path.insert(0, os.path.dirname(__file__))
from lib import b, bd, esc

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

VB = {
    'ok': ('Checked against a scanned edition', 'स्कैन किए गए संस्करण से मिलान किया'),
    'pend': ('Proofread pending', 'प्रूफ़-पठन शेष'),
}

def unit_html(u, sec_id):
    uid = u.get('id') or f"{sec_id}-{u['no']}"
    kind = u.get('kind', 'sa')
    cls = {'sa': '', 'pk': ' pk', 'hi': ' hi-txt'}[kind]
    if u.get('small'):
        cls += ' fx'
    lines = '<br>'.join(esc(l) for l in u['text'].split('\n'))
    v = u.get('v', 'pend')
    vb = f'<span class="vbadge {v}">{b(*VB[v])}</span>'
    title = ''
    if u.get('title'):
        title = f'<span class="unit-title">{b(*u["title"])}</span>'
    terms = ''
    if u.get('terms'):
        terms = '<div class="terms">' + ''.join(
            f'<span><b>{t}</b> = {b(e, h)}</span>' for t, e, h in u['terms']) + '</div>'
    note = ''
    if u.get('note'):
        note = f'<div class="src">{b(*u["note"])}</div>'
    mean_lbl = {'sa': ('Meaning', 'अर्थ'), 'pk': ('Meaning', 'अर्थ'), 'hi': ('Meaning', 'अर्थ')}[kind]
    return f'''<article class="unit" id="{uid}">
<div class="unit-head"><span class="num">{esc(str(u['no']))}</span>{title}{vb}</div>
<div class="orig{cls}">{lines}</div>
<span class="lbl">{b(*mean_lbl)}</span>
<div class="meaning">{bd(*u['mean'])}</div>
{terms}
<details class="ex" open><summary>{b('Explanation', 'व्याख्या')}</summary><div class="body">{bd(*u['ex'])}</div></details>
{note}
</article>'''

def page_html(p):
    depth = p['path'].count('/')
    up = '../' * depth
    sections = p['sections']
    toc = ''.join(f'<a href="#{s["id"]}">{b(*s["nav"])}</a>' for s in sections)
    body = []
    for s in sections:
        intro = f'<p class="sub">{b(*s["intro"])}</p>' if s.get('intro') else ''
        units = ''.join(unit_html(u, s['id']) for u in s.get('units', []))
        body.append(f'<section id="{s["id"]}"><h2>{b(*s["title"])}</h2>{intro}{s.get("diagram", "")}{units}</section>')
    crumbs = ' <span>›</span> '.join(
        f'<a href="{up}{href}">{b(*lab)}</a>' for href, lab in p.get('crumbs', []))
    pager = ''
    if p.get('prev') or p.get('next'):
        l = f'<a href="{p["prev"][0]}">← {b(*p["prev"][1])}</a>' if p.get('prev') else '<span></span>'
        r = f'<a href="{p["next"][0]}">{b(*p["next"][1])} →</a>' if p.get('next') else '<span></span>'
        pager = f'<div class="pager">{l}{r}</div>'
    foot = b(*p['foot']) if p.get('foot') else ''
    expand = ('<button id="bExpand">' + b('Collapse all', 'सब समेटें') + '</button>') if any(
        s.get('units') for s in sections) else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-en="{esc(p['title'][0])} – Jindharma" data-hi="{esc(p['title'][1])} – जिनधर्म">{esc(p['title'][0])} – Jindharma</title>
<meta name="description" content="{esc(p.get('desc', p['title'][0]))}">
<link rel="stylesheet" href="{up}assets/site.css">
<script src="{up}assets/site.js"></script>
</head>
<body>
<div class="wrap">
<div class="topbar">
  <div class="crumbs"><a href="{up}">{b('Home', 'मुख पृष्ठ')}</a> <span>›</span> {crumbs}</div>
  <div class="tools"><button data-l="en">English</button><button data-l="hi">हिन्दी</button>{expand}<button id="bTheme" aria-label="Theme">◐</button></div>
</div>
<header class="page"><h1>{b(*p['title'])}</h1><p class="by">{b(*p['by'])}</p></header>
<nav class="toc">{toc}</nav>
{p.get('intro', '')}
{''.join(body)}
{pager}
<footer class="page">{foot}</footer>
</div>
</body>
</html>
'''

def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(text)
    print('wrote', path, len(text))

def main():
    import content
    for m in pkgutil.iter_modules(content.__path__):
        mod = importlib.import_module('content.' + m.name)
        for p in getattr(mod, 'PAGES', []):
            write(p['path'], page_html(p))

if __name__ == '__main__':
    main()
