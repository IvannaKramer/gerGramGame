"""Übungsblätter Wortbausteine."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

EXTRA = '''
.vs,.ws,.ns{white-space:nowrap}
.vs{color:#1F57C3;font-weight:700}.ws{color:#157A41;font-weight:700}.ns{color:#C22A63;font-weight:700}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 6mm}
.grid2{grid-template-columns:repeat(2,minmax(0,1fr))}
.bws{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4mm 4mm;justify-items:center}
.bw{display:inline-flex}
.bk{border:.6mm solid #22304A;padding:1.6mm 2.6mm 2mm;font-size:16pt;font-weight:700;margin-left:-.6mm;line-height:1.1}
.bk:first-child{border-radius:2.5mm 0 0 2.5mm;margin-left:0}.bk:last-child{border-radius:0 2.5mm 2.5mm 0}
.tab3{width:100%;border-collapse:separate;border-spacing:0;font-size:14pt}
.tab3 th{font-family:'Grandstander',sans-serif;font-size:12.5pt;color:#fff;padding:1.2mm 3mm;text-align:left}
.tab3 th.w0{background:#56657F;border-radius:3mm 0 0 0}.tab3 th.h1{background:#2B6BE0}.tab3 th.h2{background:#1A8C4B}.tab3 th.h3{background:#DE3A76;border-radius:0 3mm 0 0}
.tab3 td{height:10.5mm;border-bottom:.45mm solid #56657F;border-left:.45mm solid #56657F;padding:0 3mm;width:24%}
.tab3 td:first-child{border-left:none;font-weight:700;width:28%}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.cols4{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}
.cols3 .c,.cols4 .c{border:.6mm solid var(--c);border-radius:3mm;padding:0 2.5mm 3mm;background:#fff}
.cols3 h3,.cols4 h3{margin:0 -2.5mm 0;background:var(--c);color:#fff;font-size:13pt;padding:1mm 2mm;text-align:center;border-radius:2.2mm 2.2mm 0 0}
.cols3 h3 small{font-family:'Andika',sans-serif;font-weight:400;font-size:10pt;margin-left:2mm}
.kw{--c:#1A8C4B}.kn{--c:#DE3A76}
.g{display:inline-block;width:7mm;border-bottom:.5mm solid #22304A;margin-right:.5mm}
.g2{display:inline-block;width:15mm;border-bottom:.5mm solid #22304A;margin:0 .3mm 0 1.6mm}
.wr .w{font-weight:700}
.wr.fix .line{flex:none;width:30mm}
.sents.v p{height:10.6mm;font-size:13.5pt;gap:0;white-space:nowrap}
.sents.v .clue{margin-left:auto;font-size:12pt;color:#22304A;font-weight:700}
.sents.fill .line{width:40mm;margin:0 1.5mm}
.sents.fill p{height:11.5mm;gap:0;font-size:13.5pt;white-space:nowrap}
.sents.fill .clue{margin-left:2mm}
.trios{display:grid;grid-template-columns:auto auto;justify-content:space-between;gap:0 6mm}
.trio{height:9.6mm;display:flex;align-items:center;gap:2mm;font-size:11.5pt;font-weight:700;white-space:nowrap}
.trio i{font-style:normal;color:#56657F;font-weight:400}
.rule .wr .line{min-width:14mm}
'''
V, W, N = (lambda s: f'<span class="vs">{s}</span>'), (lambda s: f'<span class="ws">{s}</span>'), (lambda s: f'<span class="ns">{s}</span>')
store = lambda ws: '<div class="store"><b>Wortspeicher</b>' + ''.join(f'<span>{w}</span>' for w in ws) + '</div>'

# ---------------- Blatt 1 ----------------
blocks = ['Ver·pack·ung', 'un·glaub·lich', 'Vor·name', 'Be·stell·ung', 'Schön·heit', 'Ent·spann·ung', 'Krank·heit', 'Zer·stör·ung', 'Er·find·ung']
bw = '<div class="bws">' + ''.join('<span class="bw">' + ''.join(f'<span class="bk">{p}</span>' for p in w.split('·')) + '</span>' for w in blocks) + '</div>'
rows = ['Erzählung', 'Verkauf', 'unfreundlich', 'Wohnung', 'Belohnung', 'Wildnis']
tb = '<table class="tab3"><tr><th class="w0">Wort</th><th class="h1">Vorsilbe</th><th class="h2">Wortstamm</th><th class="h3">Nachsilbe</th></tr>' + ''.join(
  f'<tr><td>{w}</td><td></td><td></td><td></td></tr>' for w in rows) + '</table>'
rel = [('pack', 'packen'), ('kauf', ''), ('wohn', ''), ('freund', '')]
rl = '<div class="grid2">' + ''.join(f'<div class="wr">{W(s)} <span class="arr">→</span> ' + (f'<span class="w">{ex}</span>, {L()}' if ex else L()) + '</div>' for s, ex in rel) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Baustein-Detektiv', 'Baustein-Detektiv',
  f'Wörter bestehen aus Bausteinen. Der {W("Wortstamm")} ist der wichtigste Baustein. Die {V("Vorsilbe")} steht davor, die {N("Nachsilbe")} dahinter: {V("Ver")}{W("pack")}{N("ung")}.',
  task(1, f'Male die Bausteine an: Vorsilbe {V("blau")}, Wortstamm {W("grün")}, Nachsilbe {N("rot")}. Achtung: Nicht jedes Wort hat alle drei Bausteine!', bw) +
  task(2, 'Zerlege die Wörter in ihre Bausteine. Fehlt ein Baustein, machst du einen Strich.', tb) +
  task(3, 'Der Wortstamm steckt auch in verwandten Wörtern. Schreibe zu jedem Wortstamm ein Wort auf.', rl))

# ---------------- Blatt 2 ----------------
words2 = ['der Bäcker', 'losfahren', 'der Wettlauf', 'die Fähre', 'das Gebäck', 'der Läufer', 'das Fahrrad', 'der Backofen', 'verlaufen',
          'die Abfahrt', 'die Bäckerei', 'der Laufschuh', 'der Fahrer', 'das Backblech', 'weglaufen']
houses = [('🚗', 'fahr', 'fahren'), ('🏃', 'lauf', 'laufen'), ('🥨', 'back', 'backen')]
hs = '<div class="cols3">' + ''.join(f'<div class="c kw"><h3>{e} {s}<small>{b}</small></h3>' + ''.join(L('f') for _ in range(5)) + '</div>' for e, s, b in houses) + '</div>'
circ = ['Abfahrt', 'Läufer', 'Bäckerei', 'verlaufen', 'Fähre', 'Gebäck', 'losfahren', 'Backofen']
cb = '<div class="boxes">' + ''.join(f'<span class="box">{b}</span>' for b in circ) + '</div>'
own = '<div class="grid3">' + ''.join(f'<div class="wr">{L()}</div>' for _ in range(3)) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Wortfamilien-Häuser', 'Wortfamilien-Häuser',
  f'Wörter mit dem gleichen {W("Wortstamm")} gehören zu einer <b>Wortfamilie</b>: {W("fahr")}en, der {W("Fahr")}er, die Ab{W("fahr")}t. Manchmal wird aus a ein ä oder aus au ein äu: die {W("Fähr")}e, der {W("Läuf")}er.',
  task(1, 'Welches Wort wohnt in welchem Haus? Schreibe jedes Wort in das Haus seiner Wortfamilie.', store(words2) + hs) +
  task(2, f'Kreise in jedem Wort den Wortstamm {W("grün")} ein.', cb) +
  task(3, f'Finde drei Wörter zur Wortfamilie {W("spiel")}.', own))

# ---------------- Blatt 3 ----------------
gk = [('Z', 'eitung'), ('L', 'ustig'), ('K', 'indheit'), ('G', 'efährlich'), ('S', 'auberkeit'), ('Z', 'eugnis'), ('W', 'indig'), ('K', 'reuzung'),
      ('E', 'ssbar'), ('D', 'unkelheit'), ('S', 'parsam'), ('Ü', 'belkeit'), ('P', 'ünktlich'), ('E', 'reignis'), ('W', 'underbar')]
gg = '<div class="grid3">' + ''.join(f'<div class="wr fix"><span class="clue">{a}/{a.lower()}</span> <span class="w"><span class="g"></span>{r}</span></div>' for a, r in gk) + '</div>'
nl = '<div class="grid2">' + ''.join(f'<div class="wr">{L()}</div>' for _ in range(8)) + '</div>'
endings = ['-ig', '-ung', '-lich', '-heit', '-bar', '-keit', '-sam', '-nis']
eb = '<div class="boxes">' + ''.join(f'<span class="box" style="min-width:26mm">{b}</span>' for b in endings) + '</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Groß oder klein?', 'Groß oder klein?',
  f'Wörter mit {N("-ung")}, {N("-heit")}, {N("-keit")} und {N("-nis")} sind <b>Nomen</b>. Nomen schreibst du <b>groß</b>. Wörter mit {N("-ig")}, {N("-lich")}, {N("-bar")} und {N("-sam")} sind <b>Adjektive</b>. Adjektive schreibst du <b>klein</b>.',
  task(1, f'Groß oder klein? Setze den richtigen Anfangsbuchstaben ein. Unterstreiche die Nachsilbe {N("rot")}.', gg) +
  task(2, 'Schreibe die acht Nomen aus Aufgabe 1 mit Artikel auf (die oder das).', nl) +
  task(3, 'Welche Nachsilben machen ein Wort zum Nomen? Male diese Kästchen an.', eb))

# ---------------- Blatt 4 ----------------
words4 = ['üben', 'klug', 'fröhlich', 'erleben', 'landen', 'dumm', 'traurig', 'erlauben', 'warnen', 'frech', 'höflich', 'geheim',
          'prüfen', 'klar', 'dankbar', 'wagen', 'mischen', 'blind', 'einsam', 'ärgern']
ct = '<div class="cols4">' + ''.join(f'<div class="c kn"><h3>{h}</h3>' + ''.join(L('f') for _ in range(5)) + '</div>' for h in ['-ung', '-heit', '-keit', '-nis']) + '</div>'
sent4 = [('Morgen schreiben wir eine', 'in Mathe.', 'prüfen'), ('Das Flugzeug setzt zur', 'an.', 'landen'), ('Ich verrate dir ein', '.', 'geheim'),
         ('Der Ausflug war ein tolles', '.', 'erleben'), ('Lisa hüpft vor', 'durch den Garten.', 'fröhlich')]
sn4 = '<div class="sents fill">' + ''.join(f'<p>{a}{L()}{b} <span class="clue">({w})</span></p>' for a, b, w in sent4) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Baustein-Werkstatt', 'Baustein-Werkstatt',
  f'Mit {N("-ung")}, {N("-heit")}, {N("-keit")} und {N("-nis")} baust du aus Verben und Adjektiven <b>Nomen</b>: heilen → die Heil{N("ung")}, frei → die Frei{N("heit")}. Nach -ig, -lich, -sam und -bar steht immer {N("-keit")}. Nomen schreibst du groß.',
  task(1, 'Baue aus jedem Wort ein Nomen. Schreibe es mit Artikel in die richtige Spalte. In jede Spalte gehören fünf Nomen.', store(words4) + ct) +
  task(2, 'Mache aus dem Wort in der Klammer ein Nomen und setze es ein.', sn4))

# ---------------- Blatt 5 ----------------
sent5 = [('Die Vase fällt vom Tisch und ', 'bricht.', 'be- · zer- · un-'), ('Ich habe meine Hausaufgaben ', 'gessen.', 'ver- · be- · zer-'),
         ('Am Sonntag ', 'suchen wir Oma und Opa.', 'zer- · ent- · be-'), ('Die Detektivin ', 'deckt eine Spur.', 'ent- · zer- · er-'),
         ('Ich ', 'kläre dir die Aufgabe.', 'zer- · er- · be-'), ('Kannst du mir den Handstand ', 'machen?', 'zer- · ent- · vor-'),
         ('Das schafft niemand. Es ist ', 'möglich.', 'un- · ent- · zer-'), ('Der Hund hat meinen Schuh ', 'bissen.', 'ent- · zer- · vor-'),
         ('Tim hat seinen Schlüssel ', 'loren.', 'ver- · ent- · be-'), ('Ich habe mich ', 'kältet und muss husten.', 'zer- · ent- · er-')]
sn5 = '<div class="sents v">' + ''.join(f'<p>{a}<span class="g2"></span>{b}<span class="clue">{o}</span></p>' for a, b, o in sent5) + '</div>'
trios = [('bereißt', 'zerreißt', 'erreißt'), ('verstecken', 'zerstecken', 'entstecken'), ('zerkomme', 'erkomme', 'bekomme'), ('entzahlt', 'bezahlt', 'zerzahlt'),
         ('entschuldige', 'vorschuldige', 'erschuldige'), ('befernt', 'zerfernt', 'entfernt'), ('beinnern', 'erinnern', 'zerinnern'), ('vorbereiten', 'erbereiten', 'entbereiten'),
         ('beführen', 'zerführen', 'vorführen'), ('unordentlich', 'beordentlich', 'verordentlich')]
tr = '<div class="trios">' + ''.join(f'<div class="trio">{a} <i>–</i> {b} <i>–</i> {c}</div>' for a, b, c in trios) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Vorsilben-Lücke', 'Vorsilben-Lücke',
  f'Eine {V("Vorsilbe")} steht vor dem Wortstamm und verändert die Bedeutung: {V("ver")}-, {V("be")}-, {V("ent")}-, {V("er")}-, {V("zer")}-, {V("vor")}-, {V("un")}-. Aus brechen wird {V("zer")}brechen.',
  task(1, 'Welche Vorsilbe passt? Probiere alle drei leise aus und schreibe die richtige in die Lücke.', sn5) +
  task(2, 'Nur ein Wort in jeder Reihe gibt es wirklich. Kreise es ein.', tr))

# ---------------- Blatt 6 ----------------
rules = [('-ung', 'Manchmal fällt ein e weg.', [('sammeln', 'die'), ('zeichnen', 'die'), ('rechnen', 'die'), ('öffnen', 'die'), ('hoffen', 'die')]),
         ('-heit', 'Manchmal fällt ein Buchstabe weg.', [('zufrieden', 'die'), ('vergangen', 'die'), ('selten', 'die'), ('weise', 'die'), ('einzeln', 'die')]),
         ('-keit und -igkeit', '', [('tapfer + keit', 'die'), ('müde + igkeit', 'die'), ('schnell + igkeit', 'die'), ('genau + igkeit', 'die'), ('hell + igkeit', 'die')]),
         ('-nis', 'Achtung: nur ein s!', [('finster', 'die'), ('hindern', 'das'), ('ergeben', 'das'), ('kennen', 'die'), ('gefangen', 'das')])]
rb = '<div class="rules">' + ''.join(f'<div class="rule k3"><h3>{h}<small>{s}</small></h3>' + ''.join(f'<div class="wr"><span class="w">{w}</span> <span class="arr">→</span> {a} {L()}</div>' for w, a in ws) + '</div>' for h, s, ws in rules) + '</div>'
det = '<div class="grid2">' + ''.join(f'<div class="wr"><s>{w}</s> <span class="arr">→</span> {L()}</div>' for w in ['die sammlung', 'die Müdekeit', 'das Hinderniss', 'die Hoffung']) + '</div>'
sent6 = [('Im Keller herrscht tiefe', '.', 'finster'), ('Das', 'der Aufgabe ist 12.', 'ergeben'), ('Oma erzählt aus der', '.', 'vergangen')]
sn6 = '<div class="sents fill">' + ''.join(f'<p>{a}{L()}{b} <span class="clue">({w})</span></p>' for a, b, w in sent6) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Nomen-Meister', 'Nomen-Meister', '',
  task(1, f'Baue Nomen mit der Nachsilbe. Aufgepasst: Manchmal fällt ein Buchstabe weg oder es kommt einer dazu. Nomen schreibst du groß!', rb) +
  task(2, 'Fehler-Detektiv: Diese Wörter sind falsch geschrieben. Schreibe sie richtig auf.', det) +
  task(3, 'Mache aus dem Wort in der Klammer ein Nomen und setze es ein.', sn6))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def cw(s):
    """Färbt ein Wort: v:Ver|s:pack|n:ung"""
    f = {'v': V, 's': W, 'n': N}
    return ''.join(f[p[0]](p[2:]) for p in s.split('|'))
l1 = sol(1, 'Baustein-Detektiv', '<p><b>Aufgabe 1</b> (Vorsilbe blau, Wortstamm grün, Nachsilbe rot): ' + ' · '.join(cw(x) for x in [
  'v:Ver|s:pack|n:ung', 'v:un|s:glaub|n:lich', 'v:Vor|s:name', 'v:Be|s:stell|n:ung', 's:Schön|n:heit', 'v:Ent|s:spann|n:ung', 's:Krank|n:heit', 'v:Zer|s:stör|n:ung', 'v:Er|s:find|n:ung']) + '</p>'
  '<p><b>Aufgabe 2:</b> Er – zähl – ung · Ver – kauf – (kein Baustein) · un – freund – lich · (kein Baustein) – Wohn – ung · Be – lohn – ung · (kein Baustein) – Wild – nis</p>'
  '<p><b>Aufgabe 3:</b> Eigene Wörter, zum Beispiel: packen, das Paket, einpacken · kaufen, der Käufer, einkaufen · wohnen, die Wohnung, der Bewohner · der Freund, freundlich, die Freundschaft</p>')
l2 = sol(2, 'Wortfamilien-Häuser', '<p><b>Aufgabe 1:</b> <b>fahr:</b> losfahren, die Fähre, das Fahrrad, die Abfahrt, der Fahrer · <b>lauf:</b> der Wettlauf, der Läufer, verlaufen, der Laufschuh, weglaufen · <b>back:</b> der Bäcker, das Gebäck, der Backofen, die Bäckerei, das Backblech</p>'
  f'<p><b>Aufgabe 2:</b> Ab{W("fahr")}t · {W("Läuf")}er · {W("Bäck")}erei · ver{W("lauf")}en · {W("Fähr")}e · Ge{W("bäck")} · los{W("fahr")}en · {W("Back")}ofen</p>'
  '<p><b>Aufgabe 3:</b> Eigene Wörter, zum Beispiel: spielen, der Spieler, das Spielzeug, der Spielplatz, mitspielen, verspielt, das Spiel</p>')
l3 = sol(3, 'Groß oder klein?', f'<p><b>Aufgabe 1:</b> Zeit{N("ung")} · lust{N("ig")} · Kind{N("heit")} · gefähr{N("lich")} · Sauber{N("keit")} · Zeug{N("nis")} · wind{N("ig")} · Kreuz{N("ung")} · ess{N("bar")} · Dunkel{N("heit")} · spar{N("sam")} · Übel{N("keit")} · pünkt{N("lich")} · Ereig{N("nis")} · wunder{N("bar")}</p>'
  '<p><b>Aufgabe 2:</b> die Zeitung · die Kindheit · die Sauberkeit · das Zeugnis · die Kreuzung · die Dunkelheit · die Übelkeit · das Ereignis</p>'
  '<p><b>Aufgabe 3:</b> -ung, -heit, -keit und -nis machen ein Wort zum Nomen.</p>')
l4 = sol(4, 'Baustein-Werkstatt', '<p><b>Aufgabe 1:</b> <b>-ung:</b> die Übung, die Landung, die Warnung, die Prüfung, die Mischung · <b>-heit:</b> die Klugheit, die Dummheit, die Frechheit, die Klarheit, die Blindheit · '
  '<b>-keit:</b> die Fröhlichkeit, die Traurigkeit, die Höflichkeit, die Dankbarkeit, die Einsamkeit · <b>-nis:</b> das Erlebnis, die Erlaubnis, das Geheimnis, das Wagnis, das Ärgernis</p>'
  '<p><b>Aufgabe 2:</b> Prüfung · Landung · Geheimnis · Erlebnis · Fröhlichkeit</p>')
l5 = sol(5, 'Vorsilben-Lücke', f'<p><b>Aufgabe 1:</b> {V("zer")}bricht · {V("ver")}gessen · {V("be")}suchen · {V("ent")}deckt · {V("er")}kläre · {V("vor")}machen · {V("un")}möglich · {V("zer")}bissen · {V("ver")}loren · {V("er")}kältet</p>'
  f'<p><b>Aufgabe 2:</b> {V("zer")}reißt · {V("ver")}stecken · {V("be")}komme · {V("be")}zahlt · {V("ent")}schuldige · {V("ent")}fernt · {V("er")}innern · {V("vor")}bereiten · {V("vor")}führen · {V("un")}ordentlich</p>')
l6 = sol(6, 'Nomen-Meister', '<p><b>Aufgabe 1:</b> <b>-ung:</b> die Sammlung, die Zeichnung, die Rechnung, die Öffnung, die Hoffnung · <b>-heit:</b> die Zufriedenheit, die Vergangenheit, die Seltenheit, die Weisheit, die Einzelheit · '
  '<b>-keit und -igkeit:</b> die Tapferkeit, die Müdigkeit, die Schnelligkeit, die Genauigkeit, die Helligkeit · <b>-nis:</b> die Finsternis, das Hindernis, das Ergebnis, die Kenntnis, das Gefängnis</p>'
  '<p><b>Aufgabe 2:</b> die Sammlung · die Müdigkeit · das Hindernis · die Hoffnung</p>'
  '<p><b>Aufgabe 3:</b> Finsternis · Ergebnis · Vergangenheit</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

write('wortbausteine', 'Übungsblätter: Wortbausteine (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps], extra_css=EXTRA)
