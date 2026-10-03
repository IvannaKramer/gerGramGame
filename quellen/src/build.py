"""Setzt die sechs Spiele eines Themas aus gemeinsamen Bausteinen zu je einer HTML-Datei zusammen.
Aufruf: python3 build.py <thema-ordner>   (z. B. einzahl-mehrzahl)"""
import json, pathlib, re, sys

SRC = pathlib.Path(__file__).resolve().parent
TOPIC = SRC / sys.argv[1]
REPO = SRC.parent.parent

ref = (REPO / 'games' / 'artikel-match.html').read_text(encoding='utf-8').split('\n')
def lines(a, b):
    return '\n'.join(ref[a - 1:b])

# Gestaltung aus dem Artikel-Match übernehmen (Zeilenbereiche der Vorlage)
GAME_RANGES = [(11, 98), (99, 121), (140, 147), (149, 166), (168, 186), (188, 193), (195, 196), (213, 213),
               (218, 218), (221, 225), (227, 251), (254, 254), (263, 264), (354, 356)]
INDEX_RANGES = [(11, 98), (99, 103), (123, 147), (350, 356)]
assert ref[10].startswith(':root{') and ref[353].startswith('@media (prefers-reduced-motion')
base_css = '\n'.join(lines(a, b) for a, b in GAME_RANGES)
extra_css = (SRC / 'extra.css').read_text(encoding='utf-8')
shared_js = (SRC / 'shared.js').read_text(encoding='utf-8')
drag_js = (SRC / 'drag.js').read_text(encoding='utf-8')
tpl = (SRC / 'shared.html').read_text(encoding='utf-8')

def parse(path):
    parts, cur = {}, None
    for ln in path.read_text(encoding='utf-8').split('\n'):
        if ln.startswith('@@'):
            cur = ln[2:].strip(); parts[cur] = []
        else:
            parts[cur].append(ln)
    parts = {k: '\n'.join(v).strip('\n') for k, v in parts.items()}
    meta = dict(l.split(': ', 1) for l in parts['meta'].split('\n') if l.strip())
    return meta, parts

def fill(html, values):
    for key, val in values.items():
        html = html.replace('{{' + key + '}}', val)
    assert '{{' not in html, re.findall(r'\{\{\w+\}\}', html)
    return html

topic, tp = parse(TOPIC / 'topic.txt')
slug = topic['slug']
OUT = REPO / 'games' / slug
OUT.mkdir(parents=True, exist_ok=True)

games = []
for n in range(1, 7):
    meta, p = parse(TOPIC / f'g{n}.txt')
    assert meta['nr'] == str(n) and f"id: '{meta['id']}'" in p['data'], f'g{n}: nr/id passt nicht'
    js = shared_js.replace('/*SLUG*/', slug).replace('/*DATA*/', p['data']).replace('/*GAME*/', (drag_js + '\n' if meta['drag'] == 'yes' else '') + p['js'])
    html = fill(tpl, {
        'TITLE': meta['title'], 'TOPIC': topic['title'], 'SUBTITLE': meta['subtitle'], 'LEVEL': meta['level'], 'NR': meta['nr'],
        'TOTAL': meta['total'], 'LEAD': meta['lead'], 'TIPP': p['tipp'], 'EXAMPLES': p['examples'],
        'HOWTO': p['howto'], 'BOARD': p['board'], 'TRAY': p['tray'],
        'CSS': base_css + '\n' + extra_css + '\n' + p['css'], 'JS': js,
    })
    (OUT / meta['file']).write_text(html, encoding='utf-8')
    games.append(meta)
    print('ok', meta['file'], len(html))

ids = [g['id'] for g in games]
index = fill((SRC / 'index.tpl.html').read_text(encoding='utf-8'), {
    'CSS': '\n'.join(lines(a, b) for a, b in INDEX_RANGES) + '\n' + extra_css,
    'TOPIC': topic['title'], 'SUBTITLE': topic['subtitle'], 'TIPP': tp['tipp'], 'SLUG': slug, 'SHEETS': topic['sheets'],
    'LEAD1': topic['lead1'], 'LEAD2': topic['lead2'], 'LEAD3': topic['lead3'],
    'IDS1': ','.join(ids[:3]), 'IDS2': ','.join(ids[3:5]), 'IDS3': ids[5],
    'GAMES': json.dumps({g['id']: {'nr': int(g['nr']), 'href': g['file'], 'name': g['title'], 'desc': g['desc'], 'sample': g['sample']} for g in games}, ensure_ascii=False, indent=2),
})
(OUT / 'index.html').write_text(index, encoding='utf-8')
print('ok index.html')
