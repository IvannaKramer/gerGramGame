"""Übungsblätter Artikel (bestimmt und unbestimmt)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

UNB = {'der': 'ein', 'die': 'eine', 'das': 'ein'}
A = lambda k, s=None: f'<b class="a-{k}">{s or k}</b>'          # Artikel in seiner Farbe
EXTRA = '''
.a-der{color:#1F57C3}.a-die{color:#C22A63}.a-das{color:#147A40}.a-u{color:#086169}
.grid2.eq{grid-template-columns:repeat(2,minmax(0,1fr))}.grid2.eq .aw:last-child{grid-column:1/-1}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:0 6mm}
.aw{height:11.5mm;display:flex;align-items:flex-end;gap:1.5mm;font-size:14pt;white-space:nowrap}
.aw .emo{align-self:center}
.aw .line{width:17mm}.aw .line.w2{width:24mm}.aw .line.w3{width:40mm}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.cols3 .c{border:.6mm solid var(--c);border-radius:3mm;padding:0 3mm 3mm;background:#fff}
.cols3 h3{margin:0 -3mm 0;background:var(--c);color:#fff;font-size:14pt;padding:1mm 2mm;text-align:center;border-radius:2.2mm 2.2mm 0 0}
.kder{--c:#2B6BE0}.kdie{--c:#DE3A76}.kdas{--c:#1A8C4B}
.store{justify-content:space-between}
.ch{display:inline-block;border:.5mm solid #56657F;border-radius:2.5mm;padding:0 2.5mm;margin:0 .8mm;font-weight:700}
.sj{display:grid;gap:0}
.sj p{margin:0;height:9.4mm;display:flex;align-items:flex-end;gap:2mm;font-size:13.5pt;white-space:nowrap;border-bottom:.3mm dotted #B8C4D6;padding-bottom:1mm}
.sj .sp{flex:1}
.cb{display:inline-flex;align-items:center;gap:1.5mm;font-size:11.5pt;color:#22304A}
.cb i{display:inline-block;width:4.2mm;height:4.2mm;border:.5mm solid #22304A;border-radius:1mm}
.st2 p{margin:0;height:11mm;display:flex;align-items:flex-end;gap:1.5mm;font-size:13.5pt;white-space:nowrap}
.st2 .line{width:19mm}
.st3 p{margin:0;height:9.4mm;display:flex;align-items:flex-end;gap:1mm;font-size:13.5pt;white-space:nowrap}
.dic{display:inline-block;min-width:39mm;border-left:1.4mm solid #FFB627;background:#F4F7FB;padding:0 2.5mm;border-radius:1.5mm}
.dic i{font-style:italic}
.rules3{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.rules3 .rule .aw{height:9.5mm;font-size:12.5pt}
.rules3 .rule h3{font-size:12pt}
.rules3 .rule .line{width:12mm}
'''

# ---------------- Blatt 1 ----------------
w1 = [('🥄','Löffel','der'),('💡','Lampe','die'),('🐑','Schaf','das'),('🦆','Ente','die'),('🪑','Stuhl','der'),('🐴','Pferd','das'),('🌙','Mond','der'),
      ('🚢','Schiff','das'),('☁️','Wolke','die'),('🐟','Fisch','der'),('👗','Kleid','das'),('🍐','Birne','die'),('🎸','Gitarre','die'),('🔑','Schlüssel','der'),('🥚','Ei','das')]
t1 = '<div class="grid3">' + ''.join(f'<div class="aw"><span class="emo">{e}</span>{L()} {n}</div>' for e, n, k in w1) + '</div>'
c1 = '<div class="cols3">' + ''.join(f'<div class="c k{k}"><h3>{k}</h3>' + ''.join(L('f') for _ in range(5)) + '</div>' for k in ('der', 'die', 'das')) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Drei Körbe', 'Drei Körbe',
  f'Jedes Nomen hat seinen Artikel: {A("der")}, {A("die")} oder {A("das")}. Sprich das Wort leise mit allen drei Artikeln. Was klingt richtig? Lerne jedes Nomen immer zusammen mit seinem Artikel.',
  task(1, 'der, die oder das? Schreibe den Artikel vor das Nomen.', t1) +
  task(2, 'Sortiere die Nomen aus Aufgabe 1 in die drei Körbe. Schreibe sie mit Artikel auf.', c1))

# ---------------- Blatt 2 ----------------
left = [('🦔','der Igel'),('🐝','die Biene'),('⛺','das Zelt'),('⭐','der Stern'),('🚀','die Rakete'),('🐖','das Schwein'),('🧳','der Koffer'),('🍋','die Zitrone')]
right = ['eine Rakete','ein Koffer','ein Zelt','eine Zitrone','ein Igel','ein Schwein','eine Biene','ein Stern']
connect = '<div class="connect">' + ''.join(f'<div class="row"><span class="l"><span class="emo">{e}</span>{w}</span><span class="dot"></span><span class="gap"></span><span class="dot"></span><span class="r">{r}</span></div>' for (e, w), r in zip(left, right)) + '</div>'
w2 = [('🐇','der Hase'),('🕯️','die Kerze'),('✈️','das Flugzeug'),('🐅','der Tiger'),('🥁','die Trommel'),('🎁','das Geschenk'),('🐊','das Krokodil')]
t2 = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="emo">{e}</span>{w} <span class="arr">→</span> {L()}</div>' for e, w in w2) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Artikel-Zwillinge', 'Artikel-Zwillinge',
  '<b>der</b>, <b>die</b>, <b>das</b> heißen <b>bestimmte Artikel</b>. <b>ein</b> und <b>eine</b> heißen <b>unbestimmte Artikel</b>. Aus <b>der</b> wird <b>ein</b>, aus <b>die</b> wird <b>eine</b>, aus <b>das</b> wird <b>ein</b>.',
  task(1, 'Finde die Zwillinge. Verbinde den bestimmten und den unbestimmten Artikel mit einer Linie.', connect) +
  task(2, 'Schreibe den Zwilling mit <b>ein</b> oder <b>eine</b> auf.', t2))

# ---------------- Blatt 3 ----------------
w3a = [('🐧','der','Pinguin'),('🐌','die','Schnecke'),('🦓','das','Zebra'),('🦒','die','Giraffe'),('🐘','der','Elefant'),('🦉','die','Eule'),('🐫','das','Kamel'),('🍓','die','Erdbeere')]
t3a = '<div class="grid2">' + ''.join(f'<div class="aw"><span class="emo">{e}</span>{k} {n} <span class="arr">→</span> <span class="ch">ein</span><span class="ch">eine</span></div>' for e, k, n in w3a) + '</div>'
w3b = [('🍄','der','Pilz'),('🥕','die','Karotte'),('🦘','das','Känguru'),('👑','die','Krone'),('🤖','der','Roboter'),('🐜','die','Ameise'),('🐿️','das','Eichhörnchen')]
t3b = '<div class="grid2 eq">' + ''.join(f'<div class="aw"><span class="emo">{e}</span>{k} {n} <span class="arr">→</span> {L()} {n}</div>' for e, k, n in w3b) + '</div>'
t3c = f'<div class="aw">Aus <b>der</b> wird {L()}. &nbsp; Aus <b>die</b> wird {L()}. &nbsp; Aus <b>das</b> wird {L()}.</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Ein oder eine?', 'Ein oder eine?',
  'Schau auf den bestimmten Artikel: Aus <b>der</b> wird <b>ein</b>. Aus <b>die</b> wird <b>eine</b>. Aus <b>das</b> wird <b>ein</b>. Nur bei <b>die</b> hängt also ein <b>e</b> am Ende.',
  task(1, 'ein oder eine? Kreise den passenden unbestimmten Artikel ein.', t3a) +
  task(2, 'Schreibe den unbestimmten Artikel in die Lücke.', t3b) +
  task(3, 'Ergänze die Regel.', t3c))

# ---------------- Blatt 4 ----------------
s4a = ['Der Wecker klingelt sehr laut.','Dort oben kreist ein Adler.','Heute leuchtet die Laterne hell.','Hier wächst eine Tanne.','Das Küken piept ganz leise.',
       'Da vorne hüpft ein Frosch.','Die Ampel zeigt gerade Rot.','Eine Glocke läutet laut.','Endlich öffnet das Schwimmbad wieder.','Ein Kaninchen hoppelt vorbei.']
t4a = '<div class="sj">' + ''.join(f'<p>{s}<span class="sp"></span><span class="cb"><i></i>bestimmt</span><span class="cb"><i></i>unbestimmt</span></p>' for s in s4a) + '</div>'
s4b = ['Draußen bellt der Dackel.','Draußen summt eine Hummel.','Morgen beginnt das Turnier.','Dort hinten liegt ein Dorf.','Plötzlich wackelt der Turm.',
       'Gleich startet ein Rennen.','Die Treppe knarrt schon wieder.','Ein Sturm zieht auf.','Die Zwiebel riecht ziemlich scharf.','Oben flattert eine Fahne.']
t4b = '<div class="grid2">' + ''.join(f'<div class="wr" style="font-size:12.5pt">{s} {L()}</div>' for s in s4b) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Artikel-Jagd', 'Artikel-Jagd',
  'Artikel sind kleine Wörter, die ein Nomen begleiten. <b>der</b>, <b>die</b>, <b>das</b> sind <b>bestimmte Artikel</b>. <b>ein</b> und <b>eine</b> sind <b>unbestimmte Artikel</b>. Der Artikel steht vor seinem Nomen.',
  task(1, 'In jedem Satz steckt ein Artikel. Kreise ihn ein und kreuze an: bestimmt oder unbestimmt?', t4a) +
  task(2, 'Schreibe den Artikel zusammen mit seinem Nomen heraus. Beispiel: Der Hahn kräht. → <b>der Hahn</b>', t4b))

# ---------------- Blatt 5 ----------------
st = [('Kran','der','Dort steht ___ Kran.','___ Kran ist riesig.'),('Rose','die','Dort blüht ___ Rose.','___ Rose duftet herrlich.'),('Boot','das','Dort liegt ___ Boot.','___ Boot schaukelt leicht.'),
      ('Brief','der','Hier liegt ___ Brief.','___ Brief kommt von Oma.'),('Kiste','die','Hier steht ___ Kiste.','___ Kiste ist sehr schwer.'),('Glas','das','Hier steht ___ Glas.','___ Glas ist ganz voll.'),
      ('Delfin','der','Dort schwimmt ___ Delfin.','___ Delfin springt hoch.'),('Mütze','die','Hier hängt ___ Mütze.','___ Mütze gehört Emil.'),('Feuer','das','Da hinten brennt ___ Feuer.','___ Feuer wärmt schön.')]
t5a = '<div class="st2">' + ''.join(f'<p>{a.replace("___", L())} &nbsp;{b.replace("___", L())}</p>' for n, k, a, b in st) + '</div>'
st2 = [('Bus','der','Draußen wartet ___ Bus.','___ Bus fährt gleich los.'),('Spinne','die','Dort oben sitzt ___ Spinne.','___ Spinne krabbelt langsam weiter.'),('Baby','das','Dort schläft ___ Baby.','___ Baby träumt bestimmt schön.'),
       ('Kaktus','der','Da hinten wächst ___ Kaktus.','___ Kaktus hat viele Stacheln.'),('Kutsche','die','Dort fährt ___ Kutsche.','___ Kutsche hat goldene Räder.'),('Bild','das','Oben hängt ___ Bild.','___ Bild zeigt hohe Berge.'),
       ('Zug','der','Gleich kommt ___ Zug.','___ Zug hat zehn Wagen.'),('Robbe','die','Da vorne schwimmt ___ Robbe.','___ Robbe taucht plötzlich ab.')]
ch = lambda a, b: f'<span class="ch">{a}</span><span class="ch">{b}</span>'
t5b = '<div class="st3">' + ''.join(f'<p>{a.replace("___", ch(UNB[k], k))} {b.replace("___", ch(UNB[k].capitalize(), k.capitalize()))}</p>' for n, k, a, b in st2) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Neu oder bekannt?', 'Neu oder bekannt?',
  'Kommt etwas <b>zum ersten Mal</b> vor, steht der unbestimmte Artikel: <b>ein</b> oder <b>eine</b>. Ist es <b>schon bekannt</b>, steht der bestimmte Artikel: <b>der</b>, <b>die</b> oder <b>das</b>.',
  task(1, 'Setze die Artikel ein: im ersten Satz <b>ein</b> oder <b>eine</b>, im zweiten Satz <b>Der</b>, <b>Die</b> oder <b>Das</b>.', t5a) +
  task(2, 'Welcher Artikel passt? Kreise ihn ein.', t5b), )

# ---------------- Blatt 6 ----------------
w6a = [('Ärger','der'),('Angst','die'),('Abenteuer','das'),('Urlaub','der'),('Antwort','die'),('Geheimnis','das'),('Streit','der'),('Gefahr','die'),('Rätsel','das'),('Gedanke','der')]
t6a = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="dic">{n}, <i>{k}</i></span> <span class="arr">→</span> {L()}</div>' for n, k in w6a) + '</div>'
w6b = [('Hunger','der'),('Idee','die'),('Gefühl','das'),('Unterricht','der'),('Reise','die'),('Wetter','das'),('Fehler','der')]
t6b = '<div class="grid3">' + ''.join(f'<div class="aw">{L()} {n}</div>' for n, k in w6b) + '</div>'
rules = [('-ung','kdie','fast immer die',['Überraschung','Wohnung','Zeitung']),('-heit','kdie','fast immer die',['Gesundheit','Krankheit','Klugheit']),('-chen','kdas','immer das',['Märchen','Häuschen','Kätzchen'])]
t6c = '<div class="rules3">' + ''.join(f'<div class="rule {c}"><h3>{h}<small>{s}</small></h3>' + ''.join(f'<div class="aw">{L()} {w}</div>' for w in ws) + '</div>' for h, c, s, ws in rules) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Wörterbuch-Profi', 'Wörterbuch-Profi',
  'Bist du beim Artikel unsicher? Dann schlag im <b>Wörterbuch</b> nach. Dort steht der Artikel hinter dem Nomen: <b>Rätsel, das</b>. Du schreibst: <b>das Rätsel</b>.',
  task(1, 'So stehen die Nomen im Wörterbuch. Schreibe sie mit dem Artikel davor auf.', t6a) +
  task(2, 'Schreibe den Artikel davor. Schlag im Wörterbuch nach, wenn du unsicher bist.', t6b) +
  task(3, 'Manche Endungen verraten den Artikel. Schreibe ihn davor.', t6c))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
by = lambda ws, k: ', '.join(f'{k} {n}' for e, n, kk in ws if kk == k)
l1 = sol(1, 'Drei Körbe', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{k} {n}' for e, n, k in w1) + '</p>'
  f'<p><b>Aufgabe 2:</b> {A("der")}: {by(w1, "der")} · {A("die")}: {by(w1, "die")} · {A("das")}: {by(w1, "das")}</p>')
l2 = sol(2, 'Artikel-Zwillinge', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{w} – {UNB[w.split()[0]]} {w.split()[1]}' for e, w in left) + '</p>'
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{UNB[w.split()[0]]} {w.split()[1]}' for e, w in w2) + '</p>')
l3 = sol(3, 'Ein oder eine?', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{UNB[k]} {n}' for e, k, n in w3a) + '</p>'
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{UNB[k]} {n}' for e, k, n in w3b) + '</p>'
  '<p><b>Aufgabe 3:</b> Aus der wird <b>ein</b>. Aus die wird <b>eine</b>. Aus das wird <b>ein</b>.</p>')
def art(s):
    for i, w in enumerate(s.rstrip('.').split()):
        if w.lower() in ('der', 'die', 'das', 'ein', 'eine'): return w, s.rstrip('.').split()[i + 1]
l4 = sol(4, 'Artikel-Jagd', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'<b>{art(s)[0]}</b> {art(s)[1]} ({"bestimmt" if art(s)[0].lower() in ("der", "die", "das") else "unbestimmt"})' for s in s4a) + '</p>'
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{art(s)[0].lower()} {art(s)[1]}' for s in s4b) + '</p>')
fl = lambda x: ' · '.join(f'{a.replace("___", "<b>" + UNB[k] + "</b>")} {b.replace("___", "<b>" + k.capitalize() + "</b>")}' for n, k, a, b in x)
l5 = sol(5, 'Neu oder bekannt?', f'<p><b>Aufgabe 1:</b> {fl(st)}</p><p><b>Aufgabe 2:</b> {fl(st2)}</p>')
l6 = sol(6, 'Wörterbuch-Profi', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{k} {n}' for n, k in w6a) + '</p>'
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{k} {n}' for n, k in w6b) + '</p>'
  '<p><b>Aufgabe 3:</b> die Überraschung, die Wohnung, die Zeitung · die Gesundheit, die Krankheit, die Klugheit · das Märchen, das Häuschen, das Kätzchen</p>'
  '<p>Hinweis: Die Endungs-Hilfen sind Faustregeln. Bei wenigen Wörtern ist <b>-ung</b> keine Endung, sondern gehört zum Wortstamm (zum Beispiel der Sprung). Im Zweifel hilft das Wörterbuch.</p>')
ps1 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 4', '', '', l1 + l2 + l3 + l4, solution=True)
ps2 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 5 und 6', '', '', l5 + l6, solution=True)

write('artikel', 'Übungsblätter: Artikel (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps1, ps2], extra_css=EXTRA)
