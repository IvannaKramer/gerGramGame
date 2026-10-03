"""Übungsblätter: Aus Verben und Adjektiven werden Nomen (Großschreibung von Nominalisierungen).
Die Sätze werden direkt aus g1.txt … g6.txt gelesen, damit Spiel und Blatt immer zusammenpassen."""
import sys, pathlib, re, ast
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from ws_common import *

def load(n):
    block = (HERE / f'g{n}.txt').read_text(encoding='utf-8').split('const SENTENCES = [')[1].split('\n];')[0]
    return [ast.literal_eval(l.strip().rstrip(',')) for l in block.split('\n') if l.strip().startswith('[')]
def order(rows, idx):
    assert sorted(idx) == list(range(len(rows))), 'Reihenfolge unvollständig'
    return [rows[i] for i in idx]

T = re.compile(r'\[([^\]]+)\]')
S, GR, KL = (lambda s: f'<span class="sg">{s}</span>'), (lambda s: f'<span class="gr">{s}</span>'), (lambda s: f'<span class="kl">{s}</span>')
G = '<span class="g"></span>'
big = lambda w: w[0].isupper()
low = lambda w: w[0].lower() + w[1:]
cap = lambda w: w[0].upper() + w[1:]
word = lambda s: T.search(s).group(1)
plain = lambda s: T.sub(lambda m: m.group(1), s)
caps = lambda s: T.sub(lambda m: f'<b class="cp">{m.group(1).upper()}</b>', s)
gap = lambda s: T.sub(G, s)

def solved(s, hints):
    """Satz in Farbe: Signalwort lila, großes Wort blau, kleines Wort türkis."""
    toks, out, n = s.split(' '), [], 0
    sig = set()
    for i, t in enumerate(toks):
        if '[' in t:
            w = word(t)
            if big(w):
                for j in range(i - 1, -1, -1):
                    if toks[j].strip('.,!?') == hints[n]: sig.add(j); break
                else: raise AssertionError(f'Signalwort fehlt: {s}')
            n += 1
    for i, t in enumerate(toks):
        if '[' in t: out.append(T.sub(lambda m: (GR if big(m.group(1)) else KL)(m.group(1)), t))
        elif i in sig: out.append(S(t))
        else: out.append(t)
    return ' '.join(out)
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def dots(items): return ' · '.join(items)

SIGNAL = f'{S("das, ein")} (Artikel), {S("beim, zum, im, vom, ans")} (versteckte Artikel), {S("etwas, nichts, viel, wenig, alles")} (Mengenwörter)'
MERK = f'Verben und Adjektive können zu <b>Nomen</b> werden. Dann schreibst du sie {GR("groß")}. Du erkennst das am <b>Signalwort</b> davor: {SIGNAL}.'

EXTRA = '''
.sg{color:#6A3FC8;font-weight:700}.gr{color:#1F57C3;font-weight:700}.kl{color:#086169;font-weight:700}
.cp{letter-spacing:.04em;background:#FFF2CF;border-radius:1.5mm;padding:0 1.2mm}
.g{display:inline-block;border-bottom:.45mm solid #56657F;width:30mm;height:1.1em;margin:0 .8mm;vertical-align:baseline}
.list p{margin:0;height:9.2mm;display:flex;align-items:flex-end;gap:3mm;font-size:13.5pt;white-space:nowrap}
.list .line{flex:1;width:auto;min-width:24mm;max-width:52mm;margin-left:auto}
.list.t20 p{height:8.3mm;font-size:12.5pt}
.list .opt{color:#56657F;font-size:11.5pt;margin-left:auto}
.o{display:inline-block;width:3.6mm;height:3.6mm;border:.45mm solid #22304A;border-radius:50%;vertical-align:-.5mm;margin-right:1.2mm}
.pool{border:.7mm dashed #56657F;border-radius:4mm;padding:1.5mm 5mm;display:grid;grid-template-columns:1fr 1fr;gap:0 6mm;font-size:13pt;margin-bottom:4mm}
.pool p{margin:0;height:7.3mm;display:flex;align-items:center;white-space:nowrap}
.kb{width:100%;border-collapse:separate;border-spacing:0;font-size:14pt}
.kb th{font-family:'Grandstander',sans-serif;font-size:13pt;color:#fff;padding:1.2mm 4mm;text-align:left;width:50%}
.kb th small{font-family:'Andika',sans-serif;font-weight:400;font-size:10pt;margin-left:2mm}
.kb .gh{background:#2B6BE0;border-radius:3mm 0 0 0}.kb .kh{background:#0B8791;border-radius:0 3mm 0 0}
.kb td{height:8.4mm;border-bottom:.45mm solid #56657F}
.kb td + td{border-left:.45mm solid #56657F}
.count{display:flex;gap:12mm;font-size:13.5pt;align-items:flex-end;height:10mm}
.count .line{width:16mm}
.own .wr{height:10mm}
.pl p{margin:0 0 .9mm;font-size:12.5pt;line-height:1.7}
.nw{white-space:nowrap}
.pl .g{width:27mm}
.pl .cp{font-size:10.5pt;background:none;padding:0;color:#56657F}
.base{color:#56657F;font-size:11.5pt}
.sol .solb p{margin-bottom:1mm}
'''

# ---------------- Blatt 1: Signalwörter-Jagd ----------------
g1 = order(load(1), [0, 8, 5, 10, 2, 12, 1, 9, 6, 3, 13, 4, 11, 7, 14])
t1 = '<div class="list">' + ''.join(f'<p><span>{caps(s)}</span>{L()}</p>' for s, *_ in g1) + '</div>'
t1b = L('f')
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Signalwörter-Jagd', 'Signalwörter-Jagd', MERK,
  task(1, 'Ein Wort steht in GROSSBUCHSTABEN. Schau auf das Wort davor. Ist es ein Signalwort? Dann kreise es ein. Schreibe das Wort in Großbuchstaben richtig auf die Linie: mit Signalwort groß, ohne Signalwort klein.', t1) +
  task(2, 'Welche Signalwörter hast du eingekreist? Schreibe sie auf.', t1b))

# ---------------- Blatt 2: Zwei Körbe ----------------
g2 = order(load(2), [0, 3, 7, 11, 8, 1, 5, 12, 9, 2, 13, 4, 6, 10, 14])
pool = '<div class="pool">' + ''.join(f'<p>{caps(s)}</p>' for s, *_ in g2) + '</div>'
tab = f'<table class="kb"><tr><th class="gh">groß <small>Signalwort davor</small></th><th class="kh">klein <small>kein Signalwort</small></th></tr>' + '<tr><td></td><td></td></tr>' * 8 + '</table>'
own = f'<div class="own"><div class="wr"><span>{S("beim")}:</span> {L()}</div><div class="wr"><span>{S("etwas")}:</span> {L()}</div></div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Zwei Körbe', 'Zwei Körbe', MERK,
  task(1, 'Lies die Sätze. In welchen Korb gehört das Wort in GROSSBUCHSTABEN? Schreibe es richtig in die Tabelle: groß oder klein.', pool + tab) +
  task(2, 'Schreibe zwei eigene Sätze mit diesen Signalwörtern.', own))

# ---------------- Blatt 3: Groß oder klein? ----------------
g3 = order(load(3), [8, 0, 5, 11, 2, 9, 6, 12, 1, 13, 4, 10, 3, 14, 7])
def opts(s):
    w = word(s); return f'<span class="opt">{low(w)} / {cap(w)}</span>'
t3 = '<div class="list">' + ''.join(f'<p><span>{gap(s)}</span>{opts(s)}</p>' for s, *_ in g3) + '</div>'
cnt = f'<div class="count"><span>{GR("groß")}: {L()} -mal</span><span>{KL("klein")}: {L()} -mal</span></div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Groß oder klein?', 'Groß oder klein?', MERK,
  task(1, 'Unterstreiche das Wort vor der Lücke. Ist es ein Signalwort? Setze dann das richtige Wort ein: klein oder groß.', t3) +
  task(2, 'Zähle nach: Wie oft hast du groß geschrieben und wie oft klein?', cnt))

# ---------------- Blatt 4: Fehler-Detektiv ----------------
g4 = order(load(4), [0, 14, 8, 3, 17, 11, 1, 9, 15, 4, 12, 18, 2, 10, 6, 16, 13, 5, 19, 7])
def shown(s, mode):
    w = word(s)
    return T.sub((low(w) if big(w) else cap(w)) if mode == 'falsch' else w, s)
t4 = '<div class="list t20">' + ''.join(f'<p><span>{shown(s, m)}</span>{L()}</p>' for s, _, m in g4) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Fehler-Detektiv', 'Fehler-Detektiv',
  f'Ein Signalwort muss zu dem Wort <b>gehören</b>. In „das {KL("alte")} Haus“ gehört „das“ zum Nomen „Haus“, darum bleibt „alte“ klein. Und: Nur {S("zum")} ist ein Signalwort, „zu“ nicht (zum {GR("Lesen")}, aber: Lust zu {KL("lesen")}).',
  task(1, 'In vielen Sätzen ist ein Wort falsch geschrieben: klein statt groß oder groß statt klein. Streiche es durch und schreibe es richtig auf die Linie. Ist alles richtig? Dann mache einen Haken auf die Linie.', t4))

# ---------------- Blatt 5: Adjektiv-Werkstatt ----------------
g5 = order(load(5), [0, 10, 1, 11, 4, 14, 2, 12, 5, 15, 3, 16, 6, 13, 8, 17, 7, 18, 9, 19])
t5 = '<div class="list t20">' + ''.join(f'<p><span>{gap(s)}</span><span class="opt">({b})</span></p>' for s, _, b, _ in g5) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Adjektiv-Werkstatt', 'Adjektiv-Werkstatt',
  f'Nach {S("etwas, nichts, viel, wenig")} wird ein Adjektiv zum Nomen: groß und mit der Endung -es (etwas {GR("Neues")}). Nach {S("alles")} hat es die Endung -e (alles {GR("Gute")}). Kommt nach dem Adjektiv noch ein Nomen, bleibt es klein: etwas {KL("warme")} Milch.',
  task(1, 'Setze das Adjektiv aus der Klammer in die Lücke ein. Achte auf die Endung und überlege: groß oder klein?', t5))

# ---------------- Blatt 6: Großschreib-Profi ----------------
g6 = load(6)
def pro(s): return T.sub(lambda m: f'<span class="nw">{G}<b class="cp">({m.group(1).upper()})</b></span>', s)
t6 = '<div class="pl">' + ''.join(f'<p>{pro(r[0])}</p>' for r in g6) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Großschreib-Profi', 'Großschreib-Profi', '',
  task(1, f'Schreibe das Wort aus der Klammer richtig in die Lücke: groß oder klein? Pass auf die Fallen auf: {S("das")} laute {GR("Bellen")}, aber das {KL("schöne")} Haus. Ich will etwas {KL("trinken")}, aber etwas {GR("Kaltes")}.', t6))

# ---------------- Lösungen ----------------
def sigs(rows): return dots(S(r[1].lower()) for r in rows if big(word(r[0])))
l1 = sol(1, 'Signalwörter-Jagd', '<p><b>Aufgabe 1:</b> ' + dots(solved(s, [h]) for s, h, _ in g1) + '</p>' +
  f'<p><b>Aufgabe 2:</b> {sigs(g1)}</p>')
l2 = sol(2, 'Zwei Körbe', '<p><b>groß:</b> ' + dots(solved(s, [h]) for s, h, _ in g2 if big(word(s))) + '</p>' +
  '<p><b>klein:</b> ' + dots(solved(s, [h]) for s, h, _ in g2 if not big(word(s))) + '</p>' +
  f'<p><b>Aufgabe 2:</b> Eigene Sätze, zum Beispiel: {S("Beim")} {GR("Spielen")} vergesse ich die Zeit. · Ich habe {S("etwas")} {GR("Schönes")} gemalt.</p>')
n_gr = sum(big(word(r[0])) for r in g3)
l3 = sol(3, 'Groß oder klein?', '<p><b>Aufgabe 1:</b> ' + dots(solved(s, [h]) for s, h, _ in g3) + '</p>' +
  f'<p><b>Aufgabe 2:</b> {GR("groß")}: {n_gr}-mal · {KL("klein")}: {len(g3) - n_gr}-mal</p>')
l4 = sol(4, 'Fehler-Detektiv', '<p><b>Falsch geschrieben war das farbige Wort:</b> ' + dots(solved(s, [h]) for s, h, m in g4 if m == 'falsch') + '</p>' +
  '<p><b>Alles richtig (Haken):</b> ' + dots(solved(s, [h]) for s, h, m in g4 if m == 'richtig') + '</p>')
l5 = sol(5, 'Adjektiv-Werkstatt', '<p>' + dots(solved(s, [h]) for s, h, *_ in g5) + '</p>')
l6 = sol(6, 'Großschreib-Profi', '<p>' + dots(solved(r[0], r[1:]) for r in g6) + '</p>')
note = f'<p class="clue">Farben wie im Spiel: {S("Signalwort")} · {GR("groß geschrieben")} · {KL("klein geschrieben")}</p>'
psA = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 4', '', '', note + l1 + l2 + l3 + l4, solution=True)
psB = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 5 und 6', '', '', note + l5 + l6, solution=True)

write('nominalisierungen', 'Übungsblätter: Aus Verben und Adjektiven werden Nomen (Klasse 4)', [p1, p2, p3, p4, p5, p6, psA, psB], extra_css=EXTRA)
