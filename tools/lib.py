"""Tiny helpers for building bilingual (EN/HI) static pages.
Every bilingual snippet is emitted as <x class="en">..</x><x class="hi">..</x>;
CSS hides the inactive language, so pages work without JavaScript rendering."""
import html as _h

def b(en, hi, tag='span', cls=''):
    c = (' ' + cls) if cls else ''
    return f'<{tag} class="en{c}">{en}</{tag}><{tag} class="hi{c}">{hi}</{tag}>'

def bd(en, hi, cls=''):
    return b(en, hi, 'div', cls)

def bp(en, hi):
    return b(en, hi, 'p')

def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

def bul(items):
    """items = [(en,hi),...] -> bilingual bullet list"""
    return (f'<div class="en">{ul([e for e, h in items])}</div>'
            f'<div class="hi">{ul([h for e, h in items])}</div>')

def fbox(en, hi, cls='', sub=None):
    s = ''
    if sub:
        s = '<small>' + b(*sub) + '</small>'
    return f'<div class="fbox {cls}"><b>{b(en, hi)}</b>{s}</div>'

def arrow(kind='r'):
    return f'<div class="farrow {kind}"></div>'

def flow(parts, col=False):
    return f'<div class="flow{" col" if col else ""}">' + ''.join(parts) + '</div>'

def panel(title, body, cls=''):
    return f'<div class="panel {cls}"><h4>{title}</h4>{body}</div>'

def chips(items):
    return '<div class="chips">' + ''.join(f'<span class="chip">{i}</span>' for i in items) + '</div>'

def table(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<div class="tw"><table><tr>{h}</tr>{r}</table></div>'

def callout(en, hi, cls=''):
    return f'<div class="callout {cls}">{b(en, hi)}</div>'

def svgtext(x, y, en, hi, cls='t', anchor='middle'):
    return (f'<text class="en {cls}" x="{x}" y="{y}" text-anchor="{anchor}">{en}</text>'
            f'<text class="hi {cls}" x="{x}" y="{y}" text-anchor="{anchor}">{hi}</text>')

def esc(s):
    return _h.escape(s, quote=False)
