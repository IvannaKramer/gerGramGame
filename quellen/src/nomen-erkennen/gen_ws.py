"""Übungsblätter Nomen erkennen."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

N = lambda s: f'<span class="ez">{s}</span>'   # Nomen blau
V = lambda s: f'<span class="mz">{s}</span>'   # Verb pink
A = lambda s: f'<span class="aj">{s}</span>'   # Adjektiv grün

EXTRA = '''
.aj{color:#157A40;font-weight:700}
.ko{--c:#C2570C}
.cols5.three{grid-template-columns:repeat(3,1fr);gap:5mm}
.cols5.three h3{font-size:13pt}
.cols5.three h3 small{display:block;font-family:'Andika',sans-serif;font-weight:400;font-size:9.5pt}
.box.caps{letter-spacing:.05em;min-width:30mm}
.gk3{display:grid;grid-template-columns:repeat(3,1fr);gap:0 7mm}
.gk{height:12mm;display:flex;align-items:flex-end;font-size:15pt;white-space:nowrap}
.gk .emo{align-self:center}
.gk .gap{display:inline-block;width:7.5mm;height:1.2em;border-bottom:.45mm solid #56657F;margin-right:.7mm}
.gk .clue{margin-left:auto;font-size:11.5pt}
.jagd p{margin:0;height:9.6mm;display:flex;align-items:center;font-size:13pt;font-weight:700;letter-spacing:.06em;border-bottom:.3mm dotted #B7C3D3}
.copy{display:grid;gap:1mm}
.copy .src{font-size:12.5pt;font-weight:700;letter-spacing:.05em}
.copy.low .src{font-size:13.5pt;letter-spacing:.02em}
.famr{display:grid;grid-template-columns:repeat(3,41mm) 1fr;align-items:end;height:9.6mm;font-size:12pt;gap:0 2mm}
.famr b{letter-spacing:.04em}
.famr .to{display:flex;align-items:flex-end;gap:1.5mm}
.famr .to .line{flex:1;width:auto}
.own{display:grid;grid-template-columns:30mm 1fr 1fr;gap:0 6mm;align-items:end;height:11mm;font-size:13.5pt}
.own .line{width:auto}
.low p{margin:0;height:10.6mm;display:flex;align-items:flex-end;font-size:14.5pt;letter-spacing:.03em;border-bottom:.3mm dotted #B7C3D3;padding-bottom:1mm}
.store.caps span{letter-spacing:.05em;font-weight:700}
.foot{font-size:9.4pt}
.copy .line.xl{height:8mm}
'''
def boxes(words): return '<div class="boxes">' + ''.join(f'<span class="box caps">{w.upper()}</span>' for w in words) + '</div>'
def cols(heads, n): return '<div class="cols5 three">' + ''.join(f'<div class="c {k}"><h3>{h}</h3>' + ''.join(L('f') for _ in range(n)) + '</div>' for h, k in heads) + '</div>'
def lines2(n, pre=''): return '<div class="grid2">' + ''.join(f'<div class="wr">{pre}{L()}</div>' for _ in range(n)) + '</div>'
def copy(sents, cls=''): return f'<div class="copy {cls}">' + ''.join(f'<div><div class="src">{s}</div>{L("xl")}</div>' for s in sents) + '</div>'

# ---------------- Blatt 1 ----------------
w1 = ['Katze', 'lacht', 'Ball', 'kalt', 'Angst', 'Bruder', 'schläft', 'Buch', 'Freude', 'lecker', 'Pferd', 'schwimmt', 'Uhr', 'krank', 'Idee']
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Nomen oder kein Nomen?', 'Nomen oder kein Nomen?',
  '<b>Nomen</b> sind Namen für Lebewesen, Dinge, Gefühle und Gedanken. Mach die Artikelprobe: Passt <b class="ez">der</b>, <b class="ez">die</b> oder <b class="ez">das</b> davor? Dann ist es ein Nomen. Nomen schreibst du groß.',
  task(1, 'Mach die Artikelprobe. Male alle Kästchen mit einem Nomen <b class="ez">blau</b> an. Es sind neun.', boxes(w1)) +
  task(2, 'Schreibe die neun Nomen mit Artikel in die richtige Spalte. Denk an den großen Anfangsbuchstaben!',
       cols([('Lebewesen', 'k5'), ('Dinge', 'k4'), ('Gefühle und Gedanken', 'ko')], 3)) +
  task(3, 'Sechs Wörter sind keine Nomen. Schreibe sie klein auf.', lines2(6)))

# ---------------- Blatt 2 ----------------
w2 = [('🐦', 'Vogel'), ('🎤', 'singt'), ('👜', 'Tasche'), ('😢', 'traurig'), ('👵', 'Oma'), ('🏃', 'rennt'), ('🚲', 'Fahrrad'), ('🍭', 'süß'),
      ('💭', 'Traum'), ('🎨', 'malt'), ('🧒', 'Kind'), ('🤤', 'hungrig'), ('🔑', 'Schlüssel'), ('🥤', 'trinkt'), ('😡', 'Wut')]
gk = '<div class="gk3">' + ''.join(f'<div class="gk"><span class="emo">{e}</span><span class="gap"></span>{w[1:]}<span class="clue">({w[0].upper()} / {w[0].lower()})</span></div>' for e, w in w2) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Groß oder klein?', 'Groß oder klein?',
  '<b class="ez">Nomen</b> schreibst du immer <b>groß</b>. <b class="mz">Verben</b> sagen, was jemand tut. <b class="aj">Adjektive</b> sagen, wie etwas ist. Verben und Adjektive schreibst du <b>klein</b>.',
  task(1, 'Der erste Buchstabe fehlt. Schreibe ihn in die Lücke: groß bei einem Nomen, sonst klein.', gk) +
  task(2, 'Acht Wörter aus Aufgabe 1 sind Nomen. Schreibe sie mit Artikel auf.', lines2(8)) +
  task(3, 'Finde selbst drei Nomen und schreibe sie mit Artikel auf: ein Lebewesen, ein Ding und ein Gefühl.',
       '<div class="grid2" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div class="wr">{L()}</div>' for _ in range(3)) + '</div>'))

# ---------------- Blatt 3 ----------------
s3 = [('🐕', 'Der Hund frisst einen Knochen.'), ('📰', 'Das Mädchen liest eine Zeitung.'), ('🧀', 'Die Maus riecht den Käse.'),
      ('🌞', 'Die Sonne scheint am Himmel.'), ('🚌', 'Der Bus hält an der Schule.'), ('🍎', 'Der Apfel liegt auf dem Teller.'),
      ('👶', 'Das Baby hat Hunger.'), ('🎂', 'Opa kauft einen Kuchen.'), ('🐸', 'Der Frosch springt in den Teich.'),
      ('🌠', 'Meine Schwester hat einen Wunsch.'), ('🐣', 'Das Küken sitzt im Nest.')]
c3 = ['Die Freunde spielen im Garten.', 'Das Auto steht vor der Garage.', 'Der Regen tropft auf das Dach.', 'Der Lehrer wünscht uns Glück.']
jg = '<div class="jagd">' + ''.join(f'<p><span class="emo">{e}</span>{s.upper()}</p>' for e, s in s3) + '</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Nomen-Jagd', 'Nomen-Jagd',
  'Vor einem Nomen steht oft ein <b>Artikel</b>: der, die, das, ein oder eine. Manchmal steht ein Nomen aber auch ganz allein: Das Baby hat <b class="ez">Hunger</b>.',
  task(1, 'In jedem Satz verstecken sich zwei Nomen. Kreise sie <b class="ez">blau</b> ein.', jg) +
  task(2, 'Schreibe die Sätze richtig auf. Nur der Satzanfang und die Nomen sind groß!', copy([s.upper() for s in c3])))

# ---------------- Blatt 4 ----------------
w4 = ['hüpft', 'Onkel', 'leise', 'Zeit', 'kocht', 'mutig', 'Fenster', 'tanzt', 'rund', 'Mut', 'fliegt', 'Ente', 'dünn', 'weint',
      'Geheimnis', 'freundlich', 'klettert', 'Koffer', 'gesund', 'flüstert']
st = '<div class="store caps"><b>Wortspeicher</b>' + ''.join(f'<span>{w.upper()}</span>' for w in w4) + '</div>'
own = ''.join(f'<div class="own">{lab}{L()}{L()}</div>' for lab in [N('Nomen:'), V('Verben:'), A('Adjektive:')])
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Wortarten-Körbe', 'Wortarten-Körbe',
  'Drei Proben: <b class="ez">Nomen</b> – Passt der, die oder das davor? <b class="mz">Verb</b> – Sagt das Wort, was jemand tut? <b class="aj">Adjektiv</b> – Sagt das Wort, wie etwas ist?',
  task(1, 'Sortiere die Wörter in die drei Körbe. Schreibe die Nomen groß und mit Artikel, die Verben und Adjektive klein.',
       st + cols([('Nomen <small>der, die, das?</small>', 'k1'), ('Verben <small>Was tut jemand?</small>', 'k3'), ('Adjektive <small>Wie ist etwas?</small>', 'k2')], 7)) +
  task(2, 'Finde zu jeder Wortart zwei eigene Wörter.', own))

# ---------------- Blatt 5 ----------------
f5 = [('ärgert', 'Ärger', 'ärgerlich'), ('hilfsbereit', 'hilft', 'Hilfe'), ('Sturm', 'stürmisch', 'stürmt'), ('zauberhaft', 'Zauber', 'zaubert'),
      ('erschrickt', 'schrecklich', 'Schreck'), ('Farbe', 'färbt', 'farbig'), ('wunderbar', 'wundert', 'Wunder'), ('fürchtet', 'Furcht', 'furchtbar'),
      ('Schmerz', 'schmerzhaft', 'schmerzt'), ('nachdenklich', 'denkt', 'Gedanke')]
fr = ''.join('<div class="famr">' + ''.join(f'<b>{w.upper()}</b>' for w in row) + f'<span class="to"><span class="arr">→</span>{L()}</span></div>' for row in f5)
a5 = [('gefühlvoll', 'das'), ('neidisch', 'der'), ('sprachlos', 'die'), ('musikalisch', 'die'), ('ordentlich', 'die'),
      ('frei', 'die'), ('siegreich', 'der'), ('rätselhaft', 'das'), ('salzig', 'das'), ('beweglich', 'die')]
ar = '<div class="grid2">' + ''.join(f'<div class="wr">{A(a)} <span class="arr">→</span> {N(art)} {L()}</div>' for a, art in a5) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Wortfamilien-Detektiv', 'Wortfamilien-Detektiv',
  'Wörter einer Familie sehen sich ähnlich. Aber nur vor das <b class="ez">Nomen</b> passt ein Artikel: <b class="ez">der Fleiß</b>, aber nicht „der fleißig“. Viele Nomen kann man nicht anfassen.',
  task(1, 'Drei Wörter aus einer Familie. Kreise das Nomen ein und schreibe es mit Artikel richtig auf.', fr) +
  task(2, 'Zu jedem Adjektiv gehört ein Nomen aus derselben Familie. Schreibe es auf.', ar))

# ---------------- Blatt 6 ----------------
def low(s):
    ws = s.split(' ')
    return ' '.join([ws[0]] + [w[0].lower() + w[1:] for w in ws[1:]])
s6 = ['Nach dem Gewitter riecht die Luft ganz frisch.', 'Meine kleine Cousine hat heute Geburtstag.', 'Ohne Licht finde ich die Tür nicht.',
      'Vor Aufregung kann ich kaum schlafen.', 'Die neue Lehrerin erzählt eine spannende Geschichte.', 'Mit viel Geduld baut er einen hohen Turm.',
      'Unsere Klasse plant eine Wanderung im Wald.', 'Vor lauter Neugier öffnet sie das Paket.', 'Wir feiern am Wochenende eine große Party.',
      'Der alte Kapitän erzählt von seiner Kindheit.']
c6 = ['Ihre Freundschaft ist ihnen sehr wichtig.', 'Das Zeugnis macht meinen Eltern gute Laune.', 'Bei Nebel fährt der Zug ganz langsam.',
      'Er hat Durst und trinkt ein Glas Wasser.']
lw = '<div class="low">' + ''.join(f'<p>{low(s)}</p>' for s in s6) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Großschreib-Profi', 'Großschreib-Profi',
  'Nicht vor jedem Nomen steht ein Artikel. Manchmal steht ein Adjektiv dazwischen: ein schnelles <b class="ez">Auto</b>. Manchmal fehlt der Artikel ganz: Ich habe <b class="ez">Hunger</b>. Mach trotzdem die Probe: das Auto, der Hunger.',
  task(1, 'Hier ist fast alles kleingeschrieben! Unterstreiche alle Nomen und schreibe den großen Anfangsbuchstaben darüber.', lw) +
  task(2, 'Schreibe die Sätze richtig auf.', copy([low(s) for s in c6], 'low')))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
l1 = sol(1, 'Nomen oder kein Nomen?', '<p><b>Aufgabe 1:</b> Nomen (blau): KATZE, BALL, ANGST, BRUDER, BUCH, FREUDE, PFERD, UHR, IDEE</p>'
  '<p><b>Aufgabe 2:</b> <b>Lebewesen:</b> die Katze, der Bruder, das Pferd · <b>Dinge:</b> der Ball, das Buch, die Uhr · <b>Gefühle und Gedanken:</b> die Angst, die Freude, die Idee</p>'
  '<p><b>Aufgabe 3:</b> lacht, schläft, schwimmt (Verben) · kalt, lecker, krank (Adjektive)</p>')
l2 = sol(2, 'Groß oder klein?', '<p><b>Aufgabe 1:</b> Vogel · singt · Tasche · traurig · Oma · rennt · Fahrrad · süß · Traum · malt · Kind · hungrig · Schlüssel · trinkt · Wut</p>'
  '<p><b>Aufgabe 2:</b> der Vogel · die Tasche · die Oma · das Fahrrad · der Traum · das Kind · der Schlüssel · die Wut</p>'
  '<p><b>Aufgabe 3:</b> Eigene Beispiele, zum Beispiel: der Igel · die Schere · der Spaß</p>')
l3 = sol(3, 'Nomen-Jagd', '<p><b>Aufgabe 1:</b> Hund, Knochen · Mädchen, Zeitung · Maus, Käse · Sonne, Himmel · Bus, Schule · Apfel, Teller · Baby, Hunger · Opa, Kuchen · Frosch, Teich · Schwester, Wunsch · Küken, Nest</p>'
  '<p><b>Aufgabe 2:</b> Die Freunde spielen im Garten. · Das Auto steht vor der Garage. · Der Regen tropft auf das Dach. · Der Lehrer wünscht uns Glück.</p>')
l4 = sol(4, 'Wortarten-Körbe', '<p><b>Aufgabe 1:</b> <b>Nomen:</b> der Onkel, die Zeit, das Fenster, der Mut, die Ente, das Geheimnis, der Koffer · '
  '<b>Verben:</b> hüpft, kocht, tanzt, fliegt, weint, klettert, flüstert · <b>Adjektive:</b> leise, mutig, rund, dünn, freundlich, gesund (eine Zeile bleibt leer)</p>'
  '<p><b>Aufgabe 2:</b> Eigene Beispiele, zum Beispiel: die Tante, der Löffel · rechnet, lernt · klug, weich</p>')
l5 = sol(5, 'Wortfamilien-Detektiv', '<p><b>Aufgabe 1:</b> der Ärger · die Hilfe · der Sturm · der Zauber · der Schreck · die Farbe · das Wunder · die Furcht · der Schmerz · der Gedanke</p>'
  '<p><b>Aufgabe 2:</b> das Gefühl · der Neid · die Sprache · die Musik · die Ordnung · die Freiheit · der Sieg · das Rätsel · das Salz · die Bewegung</p>')
l6 = sol(6, 'Großschreib-Profi', '<p><b>Aufgabe 1:</b> Gewitter, Luft · Cousine, Geburtstag · Licht, Tür · Aufregung · Lehrerin, Geschichte · Geduld, Turm · Klasse, Wanderung, Wald · Neugier, Paket · Wochenende, Party · Kapitän, Kindheit</p>'
  '<p><b>Aufgabe 2:</b> Ihre Freundschaft ist ihnen sehr wichtig. · Das Zeugnis macht meinen Eltern gute Laune. · Bei Nebel fährt der Zug ganz langsam. · Er hat Durst und trinkt ein Glas Wasser.</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

write('nomen-erkennen', 'Übungsblätter: Nomen erkennen (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps], EXTRA)
