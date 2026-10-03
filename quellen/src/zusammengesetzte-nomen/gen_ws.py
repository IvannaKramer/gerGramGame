"""Übungsblätter Zusammengesetzte Nomen. Das Wortmaterial ist dasselbe wie in den sechs Spielen."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

ART = dict(der='ad', die='ai', das='as')
A = lambda a: f'<b class="{ART[a]}">{a}</b>'                      # Artikel in seiner Farbe
W = lambda a, w: f'<b class="{ART[a]}">{a} {w}</b>'               # Artikel + Wort in der Artikel-Farbe
emo = lambda e: f'<span class="emo">{e}</span>'
PLUS, EQ, ARR = '<span class="op">+</span>', '<span class="op">=</span>', '<span class="arr">→</span>'
BW, GW = '<b class="cbw">Bestimmungswort</b>', '<b class="cgw">Grundwort</b>'

EXTRA = '''
.ad{color:#1F57C3}.ai{color:#C22A63}.as{color:#157A41}
.cbw{color:#5B34B0}.cgw{color:#086169}
.op{color:#56657F;margin:0 1.2mm;font-weight:700}
.grid2{grid-template-columns:repeat(2,minmax(0,1fr))}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 7mm}
.wr b{font-weight:700}
.wr.one{height:11mm}
.p1 .wr.one{height:10.2mm}
.connect .l{width:50mm}.connect .r{width:50mm;padding-left:4mm}
.connect .row{height:10.6mm;font-weight:700}
.cutb{border:.6mm solid #D5E3F1;border-radius:3.5mm;height:15mm;display:grid;place-items:center;font-size:19pt;font-weight:700;letter-spacing:.32em;padding-left:.32em;margin-bottom:3mm}
.wr .line.h{flex:1;min-width:0}
.wr .line.a{flex:none;width:15mm;min-width:0}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.cols3 .c{border:.6mm solid var(--c);border-radius:3mm;padding:0 3mm 3mm;background:#fff}
.cols3 h3{margin:0 -3mm 0;background:var(--c);color:#fff;font-size:13pt;padding:1mm 2mm;text-align:center;border-radius:2.2mm 2.2mm 0 0}
.kd{--c:#2B6BE0}.ki{--c:#DE3A76}.ks{--c:#1A8C4B}
.opt{display:inline-block;border:.5mm solid #56657F;border-radius:2.5mm;padding:0 2.5mm;margin-right:1.5mm;font-size:13pt;line-height:1.45}
.pick{height:11mm;display:flex;align-items:flex-end;gap:1mm;font-size:14pt;white-space:nowrap}
.pick b{font-weight:700}
.pick .line{flex:1;width:auto;min-width:30mm;margin-left:2mm}
.pair{border:.6mm solid #D5E3F1;border-radius:3.5mm;padding:1mm 4mm 2.5mm;margin-bottom:2.2mm}
.pair .hd{font-family:'Grandstander',sans-serif;font-weight:800;font-size:12pt;color:#5B34B0}
.pair .hd small{font-family:'Andika',sans-serif;font-weight:400;color:#56657F;font-size:10.5pt;margin-left:3mm}
.pair p{margin:0;height:9.2mm;display:flex;align-items:flex-end;gap:2mm;font-size:13pt;white-space:nowrap}
.pair .line{flex:1;width:auto;min-width:40mm}
.fu{background:#FFB627;border-radius:1mm;padding:0 .6mm}
.rule .wr{height:9.6mm;font-size:13pt}
.sol .fu{padding:0 .4mm}
'''

# ---------------- Blatt 1: Wörter-Puzzle ----------------
left = [('🍎', 'Apfel'), ('✉️', 'Brief'), ('👮', 'Polizei'), ('🚪', 'Tür'), ('🌧️', 'Regen'), ('🌙', 'Mond'), ('🐑', 'Schaf'), ('❄️', 'Schnee')]
right = [('🚗', 'Auto'), ('🧶', 'Wolle'), ('🥤', 'Saft'), ('⚽', 'Ball'), ('🔔', 'Klingel'), ('🕊️', 'Taube'), ('🚀', 'Rakete'), ('🧥', 'Mantel')]
connect = '<div class="connect">' + ''.join(
    f'<div class="row"><span class="l">{emo(e)}{w}</span><span class="dot"></span><span class="gap"></span><span class="dot"></span><span class="r">{emo(e2)}{w2}</span></div>'
    for (e, w), (e2, w2) in zip(left, right)) + '</div>'
write1 = [('🦷', 'der Zahn', 'der Arzt'), ('🧀', 'der Käse', 'das Brot'), ('☀️', 'der Sommer', 'das Kleid'), ('🐄', 'die Kuh', 'die Glocke'),
          ('🍝', 'die Nudel', 'der Salat'), ('📖', 'das Buch', 'die Seite'), ('🍯', 'der Honig', 'das Glas')]
wr1 = '<div class="p1">' + ''.join(f'<div class="wr one">{emo(e)}{a} {PLUS} <b>{b}</b> {EQ} {L()}</div>' for e, a, b in write1) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Wörter-Puzzle', 'Wörter-Puzzle',
  f'Aus zwei Nomen kannst du ein neues Nomen bauen: Apfel + Saft = <b>Apfelsaft</b>. Vorne steht das {BW}, hinten das {GW}. Das Grundwort bestimmt den Artikel: <b class="ad">der</b> Saft → <b class="ad">der</b> Apfelsaft.',
  task(1, 'Welche zwei Wörter ergeben zusammen ein neues Wort? Verbinde sie mit einer Linie.', connect) +
  task(2, 'Baue das neue Wort. Schreibe es mit Artikel auf. Der Artikel kommt vom <b>fett</b> gedruckten Grundwort.', wr1))

# ---------------- Blatt 2: Wort-Schere ----------------
cut = ['Fischsuppe', 'Wasserball', 'Vogelhaus', 'Autotür', 'Nusskuchen', 'Zirkuszelt', 'Feldmaus', 'Seestern']
cb = '<div class="grid2">' + ''.join(f'<div class="cutb">{w}</div>' for w in cut) + '</div>'
split = ['der Tigerhai', 'die Kinokarte', 'das Würfelspiel', 'der Eisberg', 'die Schatzkiste', 'das Tierbuch', 'das Abendessen']
sp = ''.join(f'<div class="wr one"><b>{w}</b> {EQ} {L("h")} {PLUS} {L("h")}</div>' for w in split)
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Wort-Schere', 'Wort-Schere',
  f'Ein zusammengesetztes Nomen hat zwei Teile. Hinten steht das {GW}. Es sagt, was es ist: Eine Fischsuppe ist eine <b>Suppe</b>. Vorne steht das {BW}. Es sagt es genauer: eine Suppe mit <b>Fisch</b>.',
  task(1, 'Wo hört das erste Nomen auf? Zeichne einen Strich zwischen die beiden Nomen.', cb) +
  task(2, 'Zerlege das Wort. Schreibe beide Nomen mit Artikel auf und kreise das Grundwort ein.', sp))

# ---------------- Blatt 3: Artikel-Chef ----------------
art1 = [('das Haus', 'der Schlüssel', 'Hausschlüssel'), ('der Tisch', 'die Lampe', 'Tischlampe'), ('der Wind', 'das Rad', 'Windrad'),
        ('die Stadt', 'der Bus', 'Stadtbus'), ('das Telefon', 'die Nummer', 'Telefonnummer'), ('der Garten', 'das Tor', 'Gartentor'),
        ('das Papier', 'der Korb', 'Papierkorb'), ('die Hand', 'das Tuch', 'Handtuch')]
a1 = ''.join(f'<div class="wr one">{a} {PLUS} {b} {EQ} {L("a")} <b>{c}</b></div>' for a, b, c in art1)
store3 = ['Dachboden', 'Handyhülle', 'Sternbild', 'Strohhut', 'Waldhütte', 'Luftschiff', 'Fußspur']
st3 = '<div class="store"><b>Wortspeicher</b>' + ''.join(f'<span>{w}</span>' for w in store3) + '</div>'
c3 = '<div class="cols3">' + ''.join(f'<div class="c {k}"><h3>{h}</h3>' + ''.join(L('f') for _ in range(3)) + '</div>' for h, k in [('der', 'kd'), ('die', 'ki'), ('das', 'ks')]) + '</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Artikel-Chef', 'Artikel-Chef',
  f'Das {GW} ist der Chef. Es steht <b>hinten</b> und bestimmt den Artikel: das Haus + <b class="ai">die</b> Tür = <b class="ai">die</b> Haustür. Der Artikel vom vorderen Wort fällt weg.',
  task(1, 'Welcher Artikel gehört zum neuen Wort? Unterstreiche das Grundwort und schreibe den Artikel auf die Linie.', a1) +
  task(2, 'Überlege: Wie heißt das Grundwort? Welchen Artikel hat es? Schreibe jedes Wort mit Artikel in die richtige Spalte.', st3 + c3))

# ---------------- Blatt 4: Wörter-Baukasten ----------------
pick4 = [('Garten', None, ['Löffel', 'Zwerg', 'Wolke']), (None, 'Bank', ['Nase', 'Pilz', 'Fenster']), ('Taxi', None, ['Fahrer', 'Teller', 'Zahn']),
         (None, 'Brei', ['Stuhl', 'Kartoffel', 'Brief']), ('Fahrrad', None, ['Suppe', 'Blatt', 'Helm']), (None, 'Burg', ['Ritter', 'Apfel', 'Hose']),
         ('Märchen', None, ['Schuh', 'Buch', 'Wiese']), (None, 'Dose', ['Lampe', 'Vogel', 'Zucker'])]
def pickrow(bw, gw, opts):
    o = ''.join(f'<span class="opt">{x}</span>' for x in opts)
    inner = f'<b>{bw}</b> {PLUS} {o}' if bw else f'{o} {PLUS} <b>{gw}</b>'
    return f'<div class="pick">{inner} {ARR} {L()}</div>'
pk = ''.join(pickrow(*r) for r in pick4)
fuge4 = [('Blume', 'n', 'strauß'), ('Hund', 'e', 'hütte'), ('König', 's', 'schloss'), ('Tasche', 'n', 'lampe'), ('Ei', 'er', 'becher'), ('Kind', 'er', 'zimmer')]
fg = '<div class="grid3">' + ''.join(f'<div class="wr">{L("a")} <b>{a}{f}{b}</b></div>' for a, f, b in fuge4) + '</div>'
own4 = [('Topf', 'Pflanze'), ('Pony', 'Hof'), ('Gemüse', 'Beet'), ('Bus', 'Haltestelle'), ('Zelt', 'Lager'), ('Geld', 'Stück')]
ow = '<div class="grid2">' + ''.join(f'<div class="wr">{a} {PLUS} {b} {EQ} {L()}</div>' for a, b in own4) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Wörter-Baukasten', 'Wörter-Baukasten',
  f'Das {GW} steht hinten und bestimmt den Artikel. Manchmal steht zwischen den beiden Wörtern noch ein <b>Verbindungs-Buchstabe</b>: Tasche + <span class="fu">n</span> + Lampe = <b class="ai">die</b> Tasche<span class="fu">n</span>lampe.',
  task(1, 'Welcher Baustein passt? Kreise ihn ein. Schreibe das neue Wort mit Artikel auf.', pk) +
  task(2, 'Hier steckt ein Verbindungs-Buchstabe im Wort. Kreise ihn ein und schreibe den Artikel davor.', fg) +
  task(3, 'Baue das Wort zusammen. Schreibe es mit Artikel auf.', ow))

# ---------------- Blatt 5: Wort-Dreher ----------------
pairs5 = [('Milch', 'Kuh', 'eine Kuh, die Milch gibt:', 'die Milch von einer Kuh:', ''),
          ('Reise', 'Bus', 'ein Bus für lange Reisen:', 'eine Reise mit dem Bus:', ''),
          ('Haus', 'Boot', 'ein Boot, in dem man wohnen kann:', 'ein Haus am Wasser, in dem Boote stehen:', 'Achtung: einmal mit <span class="fu">s</span> dazwischen!'),
          ('Honig', 'Biene', 'eine Biene, die Honig macht:', 'Honig, den Bienen gemacht haben:', 'Achtung: einmal mit <span class="fu">n</span> dazwischen!')]
pr = ''.join(f'<div class="pair"><span class="hd">{a} + {b}<small>{note}</small></span><p>{r1} {L()}</p><p>{r2} {L()}</p></div>' for a, b, r1, r2, note in pairs5)
turn = ['der Fingerring', 'der Lederschuh', 'das Ballspiel', 'der Obstbaum', 'die Steinmauer', 'das Kuchenblech']
tn = '<div class="grid2">' + ''.join(f'<div class="wr"><b>{w}</b> {ARR} {L()}</div>' for w in turn) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Wort-Dreher', 'Wort-Dreher',
  f'Die Reihenfolge verändert die Bedeutung! Das {GW} steht hinten und sagt, <b>was es ist</b>: Eine Milch<b>kuh</b> ist eine Kuh. Kuh<b>milch</b> ist Milch.',
  task(1, 'Was ist gesucht? Baue aus den zwei Wörtern das passende Nomen. Schreibe es mit Artikel auf.', pr) +
  task(2, 'Drehe das Wort um. Schreibe das neue Wort mit Artikel auf. Achtung: Der Artikel kann sich ändern!', tn))

# ---------------- Blatt 6: Profi-Werkstatt ----------------
f6 = [('Sonne', 'Schirm'), ('Straße', 'Bahn'), ('Banane', 'Schale'), ('Geburtstag', 'Geschenk'), ('Übung', 'Heft'), ('Liebling', 'Essen'), ('Pferd', 'Stall'), ('Bild', 'Rahmen')]
v6 = [('schreiben', 'Tisch'), ('kochen', 'Löffel'), ('turnen', 'Halle'), ('waschen', 'Maschine'), ('schwimmen', 'Bad'), ('springen', 'Seil')]
a6 = [('blau', 'Wal'), ('frisch', 'Käse'), ('groß', 'Stadt'), ('süß', 'Kartoffel'), ('hoch', 'Haus'), ('klein', 'Kind')]
row6 = lambda a, b: f'<div class="wr">{a} {PLUS} {b} {EQ} {L()}</div>'
t61 = '<div class="store"><b>Diese Verbindungs-Buchstaben brauchst du</b><span>3-mal <b>n</b></span><span>3-mal <b>s</b></span><span>1-mal <b>e</b></span><span>1-mal <b>er</b></span></div>' + \
      '<div class="grid2">' + ''.join(row6(a, b) for a, b in f6) + '</div>'
t62 = '<div class="rules"><div class="rule k4"><h3>Verb + Nomen<small>schreib<s>en</s> → Schreib-</small></h3>' + ''.join(row6(a, b) for a, b in v6) + '</div>' + \
      '<div class="rule k5"><h3>Adjektiv + Nomen<small>hoch → Hoch-</small></h3>' + ''.join(row6(a, b) for a, b in a6) + '</div></div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Profi-Werkstatt', 'Profi-Werkstatt',
  'Vorne kann auch ein <b>Verb</b> oder ein <b>Adjektiv</b> stehen: turnen + Halle = <b class="ai">die Turnhalle</b>, hoch + Haus = <b class="as">das Hochhaus</b>. Das neue Wort ist immer ein Nomen: Du schreibst es groß, und das Grundwort bestimmt den Artikel.',
  task(1, 'Nomen + Nomen: Hier fehlt immer ein Verbindungs-Buchstabe. Schreibe das neue Wort mit Artikel auf.', t61) +
  task(2, 'Vorne steht ein Verb oder ein Adjektiv. Schreibe das neue Nomen mit Artikel auf.', t62))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
fu = lambda a, f, b: f'{a}<span class="fu">{f}</span>{b}'
D = ' · '
l1 = sol(1, 'Wörter-Puzzle', '<p><b>Aufgabe 1:</b> ' + D.join(['Apfel – Saft (der Apfelsaft)', 'Brief – Taube (die Brieftaube)', 'Polizei – Auto (das Polizeiauto)', 'Tür – Klingel (die Türklingel)',
     'Regen – Mantel (der Regenmantel)', 'Mond – Rakete (die Mondrakete)', 'Schaf – Wolle (die Schafwolle)', 'Schnee – Ball (der Schneeball)']) + '</p>' +
     '<p><b>Aufgabe 2:</b> ' + D.join([W('der', 'Zahnarzt'), W('das', 'Käsebrot'), W('das', 'Sommerkleid'), W('die', 'Kuhglocke'), W('der', 'Nudelsalat'), W('die', 'Buchseite'), W('das', 'Honigglas')]) + '</p>')
l2 = sol(2, 'Wort-Schere', '<p><b>Aufgabe 1:</b> ' + D.join(['Fisch | suppe', 'Wasser | ball', 'Vogel | haus', 'Auto | tür', 'Nuss | kuchen', 'Zirkus | zelt', 'Feld | maus', 'See | stern']) + '</p>' +
     '<p><b>Aufgabe 2</b> (das Grundwort ist unterstrichen): ' + D.join(f'{a} + <u>{b}</u>' for a, b in [('der Tiger', 'der Hai'), ('das Kino', 'die Karte'), ('der Würfel', 'das Spiel'),
     ('das Eis', 'der Berg'), ('der Schatz', 'die Kiste'), ('das Tier', 'das Buch'), ('der Abend', 'das Essen')]) + '</p>')
l3 = sol(3, 'Artikel-Chef', '<p><b>Aufgabe 1:</b> ' + D.join([W('der', 'Hausschlüssel'), W('die', 'Tischlampe'), W('das', 'Windrad'), W('der', 'Stadtbus'), W('die', 'Telefonnummer'), W('das', 'Gartentor'), W('der', 'Papierkorb'), W('das', 'Handtuch')]) +
     '. Das Grundwort ist immer das hintere Wort.</p><p><b>Aufgabe 2:</b> <b>der:</b> der Dachboden, der Strohhut · <b>die:</b> die Handyhülle, die Waldhütte, die Fußspur · <b>das:</b> das Sternbild, das Luftschiff</p>')
l4 = sol(4, 'Wörter-Baukasten', '<p><b>Aufgabe 1:</b> ' + D.join([W('der', 'Gartenzwerg'), W('die', 'Fensterbank'), W('der', 'Taxifahrer'), W('der', 'Kartoffelbrei'), W('der', 'Fahrradhelm'), W('die', 'Ritterburg'), W('das', 'Märchenbuch'), W('die', 'Zuckerdose')]) + '</p>' +
     '<p><b>Aufgabe 2:</b> ' + D.join([f'{A("der")} {fu("Blume", "n", "strauß")}', f'{A("die")} {fu("Hund", "e", "hütte")}', f'{A("das")} {fu("König", "s", "schloss")}', f'{A("die")} {fu("Tasche", "n", "lampe")}',
     f'{A("der")} {fu("Ei", "er", "becher")}', f'{A("das")} {fu("Kind", "er", "zimmer")}']) + '</p>' +
     '<p><b>Aufgabe 3:</b> ' + D.join([W('die', 'Topfpflanze'), W('der', 'Ponyhof'), W('das', 'Gemüsebeet'), W('die', 'Bushaltestelle'), W('das', 'Zeltlager'), W('das', 'Geldstück')]) + '</p>')
l5 = sol(5, 'Wort-Dreher', '<p><b>Aufgabe 1:</b> ' + D.join(['die Milchkuh, die Kuhmilch', 'der Reisebus, die Busreise', f'das Hausboot, das {fu("Boot", "s", "haus")}', f'die Honigbiene, der {fu("Biene", "n", "honig")}']) + '</p>' +
     '<p><b>Aufgabe 2:</b> ' + D.join(['der Ringfinger', 'das Schuhleder', 'der Spielball', 'das Baumobst', 'der Mauerstein', 'der Blechkuchen']) + '</p>')
l6 = sol(6, 'Profi-Werkstatt', '<p><b>Aufgabe 1:</b> ' + D.join([f'der {fu("Sonne", "n", "schirm")}', f'die {fu("Straße", "n", "bahn")}', f'die {fu("Banane", "n", "schale")}', f'das {fu("Geburtstag", "s", "geschenk")}',
     f'das {fu("Übung", "s", "heft")}', f'das {fu("Liebling", "s", "essen")}', f'der {fu("Pferd", "e", "stall")}', f'der {fu("Bild", "er", "rahmen")}']) + '</p>' +
     '<p><b>Aufgabe 2:</b> <b>Verb + Nomen:</b> der Schreibtisch, der Kochlöffel, die Turnhalle, die Waschmaschine, das Schwimmbad, das Springseil · ' +
     '<b>Adjektiv + Nomen:</b> der Blauwal, der Frischkäse, die Großstadt, die Süßkartoffel, das Hochhaus, das Kleinkind</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

write('zusammengesetzte-nomen', 'Übungsblätter: Zusammengesetzte Nomen (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps], extra_css=EXTRA)
