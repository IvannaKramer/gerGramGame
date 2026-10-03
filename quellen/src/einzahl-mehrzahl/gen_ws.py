"""Übungsblätter Einzahl und Mehrzahl."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

# ---------------- Blatt 1 ----------------
left = [('🐕','der Hund'),('🐈','die Katze'),('🚗','das Auto'),('⚽','der Ball'),('📖','das Buch'),('🌸','die Blume'),('🏠','das Haus'),('🐟','der Fisch')]
right = ['die Bücher','die Fische','die Hunde','die Häuser','die Autos','die Katzen','die Bälle','die Blumen']
connect = '<div class="connect">' + ''.join(f'<div class="row"><span class="l"><span class="emo">{e}</span>{E(w)}</span><span class="dot"></span><span class="gap"></span><span class="dot"></span><span class="r">{M(r)}</span></div>' for (e, w), r in zip(left, right)) + '</div>'
write1 = [('🌳','der Baum'),('🐭','die Maus'),('🍎','der Apfel'),('🥚','das Ei'),('⭐','der Stern'),('🍌','die Banane'),('👟','der Schuh')]
wr = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="emo">{e}</span>{E(w)} <span class="arr">→</span> {M("die")} {L()}</div>' for e, w in write1) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Mehrzahl-Memory', 'Mehrzahl-Memory',
  '<b>Einzahl</b> heißt: nur eins. <b>Mehrzahl</b> heißt: zwei oder mehr. In der Mehrzahl heißt der Artikel immer <b class="mz">die</b>.',
  task(1, 'Was gehört zusammen? Verbinde Einzahl und Mehrzahl mit einer Linie.', connect) +
  task(2, 'Schreibe die Mehrzahl auf.', wr))

# ---------------- Blatt 2 ----------------
boxes = ['der Stuhl','die Lampen','die Kinder','das Bett','die Vögel','die Tasche','das Bild','die Stifte','die Hefte','die Uhr','die Kühe','der Koffer','die Türen','die Brille','die Schweine']
bx = '<div class="boxes">' + ''.join(f'<span class="box">{b}</span>' for b in boxes) + '</div>'
tab = [('🪑','der Stuhl',''),('💡','','die Lampen'),('🧒','','die Kinder'),('🛏️','das Bett',''),('🐦','','die Vögel'),('👜','die Tasche',''),('⏰','die Uhr',''),('🚪','','die Türen')]
tb = '<table class="tab"><tr><th></th><th class="ezh">Einzahl (eins)</th><th class="mzh">Mehrzahl (viele)</th></tr>' + ''.join(
  f'<tr><td class="emo">{e}</td><td>{E(a) if a else ""}</td><td>{M(b) if b else ""}</td></tr>' for e, a, b in tab) + '</table>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Eins oder viele?', 'Eins oder viele?',
  '<b>der</b> und <b>das</b> stehen nur bei der Einzahl. Bei <b>die</b> musst du genau lesen: <b>die Lampe</b> ist eine, <b>die Lampen</b> sind viele.',
  task(1, 'Einzahl oder Mehrzahl? Male die Einzahl-Kästchen <b class="ez">blau</b> und die Mehrzahl-Kästchen <b class="mz">rot</b> an.', bx) +
  task(2, 'Ergänze die Tabelle. Schreibe das fehlende Wort mit Artikel auf.', tb))

# ---------------- Blatt 3 ----------------
bal = [('🦷','der Zahn',['die Zahne','die Zähne','die Zahns']),('✋','die Hand',['die Hände','die Handen','die Hands']),
       ('🐸','der Frosch',['die Froschen','die Frosche','die Frösche']),('🦆','die Ente',['die Entes','die Enten','die Enter']),
       ('🥛','das Glas',['die Gläser','die Glase','die Glasen']),('🦊','der Fuchs',['die Fuchsen','die Füchse','die Fuchse'])]
bl = '<div class="brows">' + ''.join(f'<div class="brow"><span class="bw"><span class="emo">{e}</span>{E(w)}</span>' + ''.join(f'<span class="ball">{o}</span>' for o in opts) + '</div>' for e, w, opts in bal) + '</div>'
many = [('🐑','ein Schaf'),('🐴','ein Pferd'),('🐇','ein Hase'),('🍐','eine Birne'),('🚢','ein Schiff'),('🔑','ein Schlüssel'),('☁️','eine Wolke'),('🥄','ein Löffel'),('👗','ein Kleid')]
mn = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="emo">{e}</span>{E(w)} – {M("viele")} {L()}</div>' for e, w in many) + '</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Ballon-Mehrzahl', 'Ballon-Mehrzahl',
  'Sprich leise vor: „<b>ein</b> Zahn, <b>viele</b> …“. Manche Wörter bekommen in der Mehrzahl Pünktchen: a → ä, o → ö, u → ü.',
  task(1, 'Nur ein Ballon zeigt die richtige Mehrzahl. Male ihn an.', bl) +
  task(2, 'Eins und viele: Schreibe die Mehrzahl auf.', mn))

# ---------------- Blatt 4 ----------------
store = ['der Tag','das Kino','die Schule','das Lied','der Lehrer','der Brief','das Sofa','das Feld','die Zahl','das Zimmer','der Berg','das Nest','die Straße','der Opa','der Teller','das Licht','das Foto','der Tisch','die Frau','das Mädchen']
st = '<div class="store"><b>Wortspeicher</b>' + ''.join(f'<span>{w}</span>' for w in store) + '</div>'
cols = [('-e','k1'),('-er','k2'),('-n / -en','k3'),('-s','k4'),('keine Endung','k5')]
ct = '<div class="cols5">' + ''.join(f'<div class="c {k}"><h3>{h}</h3>' + ''.join(L('f') for _ in range(4)) + '</div>' for h, k in cols) + '</div>'
sent = [('Im Briefkasten liegen zwei', 'der Brief', '.'), ('Im Baum sind drei', 'das Nest', '.'), ('In unserer Stadt gibt es zwei', 'das Kino', '.'),
        ('Wir singen heute viele', 'das Lied', '.'), ('Auf dem Tisch stehen vier', 'der Teller', '.')]
sn = '<div class="sents">' + ''.join(f'<p>{a} {L("m")}{c} <span class="clue">({w})</span></p>' for a, w, c in sent) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Endungs-Werkstatt', 'Endungs-Werkstatt',
  'Für die Mehrzahl gibt es verschiedene Endungen: <b>-e</b>, <b>-er</b>, <b>-n</b> oder <b>-en</b> und <b>-s</b>. Manche Wörter bleiben gleich. Dann ändert sich nur der Artikel.',
  task(1, 'Bilde die Mehrzahl. Schreibe jedes Wort mit <b class="mz">die</b> in die richtige Spalte.', st + ct) +
  task(2, 'Setze die Mehrzahl ein.', sn))

# ---------------- Blatt 5 ----------------
dots = [('der Traum','Traume'),('der Arm','Arme'),('der Kopf','Kopfe'),('der Monat','Monate'),('der Turm','Turme'),('das Jahr','Jahre'),
        ('der Garten','Garten'),('die Burg','Burgen'),('die Tochter','Tochter'),('das Boot','Boote'),('die Wand','Wande'),('der Punkt','Punkte')]
dt = '<div class="grid4">' + ''.join(f'<div class="dotw">{E(a)}<span class="arr">↓</span><span class="big">die {b}</span></div>' for a, b in dots) + '</div>'
w5 = ['die Nacht','das Blatt','der Bruder','das Dorf','der Zug','der Rock','der Kuchen','die Tasse']
wr5 = '<div class="grid2">' + ''.join(f'<div class="wr">{E(w)} <span class="arr">→</span> {M("die")} {L()}</div>' for w in w5) + '</div>'
own = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="chg">{c}</span> {L("s")} <span class="arr">→</span> {L("s")}</div>' for c in ['a → ä','o → ö','u → ü','au → äu']) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Umlaut-Zauber', 'Umlaut-Zauber',
  'Viele Nomen bekommen in der Mehrzahl einen <b>Umlaut</b>: a → ä, o → ö, u → ü, au → äu. Aber nicht alle! Sprich das Wort laut, dann hörst du es.',
  task(1, 'Hier hat jemand alle Pünktchen weggezaubert. Setze sie wieder auf die Buchstaben. Achtung: Sechs Wörter brauchen keine!', dt) +
  task(2, 'Schreibe die Mehrzahl auf.', wr5) +
  task(3, 'Finde zu jedem Umlaut ein eigenes Beispiel: Einzahl → Mehrzahl.', own))

# ---------------- Blatt 6 ----------------
rules = [('-y → -ys','k1','Das y bleibt stehen.',['das Baby','das Hobby','das Pony','die Party','der Teddy']),
         ('-in → -innen','k3','Achtung: zwei n!',['die Freundin','die Lehrerin','die Ärztin','die Königin','die Schülerin']),
         ('-nis, -is, -us → -sse','k2','Das s wird verdoppelt.',['das Zeugnis','das Geheimnis','das Ergebnis','der Bus','der Kürbis']),
         ('-um → -en','k4','Das -um fällt weg.',['das Museum','das Aquarium','das Zentrum','das Datum','das Album'])]
rb = '<div class="rules">' + ''.join(f'<div class="rule {k}"><h3>{h}<small>{s}</small></h3>' + ''.join(f'<div class="wr">{E(w)} <span class="arr">→</span> {M("die")} {L()}</div>' for w in ws) + '</div>' for h, k, s, ws in rules) + '</div>'
det = '<div class="grid2">' + ''.join(f'<div class="wr"><s>{w}</s> <span class="arr">→</span> {L()}</div>' for w in ['die Hobbies','die Lehrerinen','die Kürbise','die Albums']) + '</div>'
s6 = ['Das Baby schläft.','Die Freundin lacht.','Der Bus hält an der Schule.']
sn6 = '<div class="sents two">' + ''.join(f'<p>{s} <span class="arr">→</span> {L()}</p>' for s in s6) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Mehrzahl-Meister', 'Mehrzahl-Meister', '',
  task(1, 'Vier Profi-Regeln: Schreibe die Mehrzahl auf.', rb) +
  task(2, 'Fehler-Detektiv: Diese Wörter sind falsch geschrieben. Schreibe sie richtig auf.', det) +
  task(3, 'Setze den ganzen Satz in die Mehrzahl. Achtung: Auch das Verb ändert sich!', sn6))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def ul(pairs): return '<ul>' + ''.join(f'<li>{p}</li>' for p in pairs) + '</ul>'
l1 = sol(1, 'Mehrzahl-Memory', '<p><b>Aufgabe 1:</b> der Hund – die Hunde · die Katze – die Katzen · das Auto – die Autos · der Ball – die Bälle · das Buch – die Bücher · die Blume – die Blumen · das Haus – die Häuser · der Fisch – die Fische</p><p><b>Aufgabe 2:</b> die Bäume · die Mäuse · die Äpfel · die Eier · die Sterne · die Bananen · die Schuhe</p>')
l2 = sol(2, 'Eins oder viele?', '<p><b>Aufgabe 1:</b> <span class="ez">Einzahl (blau):</span> der Stuhl, das Bett, die Tasche, das Bild, die Uhr, der Koffer, die Brille. <span class="mz">Mehrzahl (rot):</span> die Lampen, die Kinder, die Vögel, die Stifte, die Hefte, die Kühe, die Türen, die Schweine.</p><p><b>Aufgabe 2:</b> der Stuhl – die Stühle · die Lampe – die Lampen · das Kind – die Kinder · das Bett – die Betten · der Vogel – die Vögel · die Tasche – die Taschen · die Uhr – die Uhren · die Tür – die Türen</p>')
l3 = sol(3, 'Ballon-Mehrzahl', '<p><b>Aufgabe 1:</b> die Zähne · die Hände · die Frösche · die Enten · die Gläser · die Füchse</p><p><b>Aufgabe 2:</b> viele Schafe · viele Pferde · viele Hasen · viele Birnen · viele Schiffe · viele Schlüssel · viele Wolken · viele Löffel · viele Kleider</p>')
l4 = sol(4, 'Endungs-Werkstatt', '<p><b>Aufgabe 1:</b> <b>-e:</b> die Tage, die Briefe, die Berge, die Tische · <b>-er:</b> die Lieder, die Felder, die Nester, die Lichter · <b>-n / -en:</b> die Schulen, die Zahlen, die Straßen, die Frauen · <b>-s:</b> die Kinos, die Sofas, die Opas, die Fotos · <b>keine Endung:</b> die Lehrer, die Zimmer, die Teller, die Mädchen</p><p><b>Aufgabe 2:</b> Briefe · Nester · Kinos · Lieder · Teller</p>')
l5 = sol(5, 'Umlaut-Zauber', '<p><b>Aufgabe 1:</b> <b>Mit Pünktchen:</b> die Träume, die Köpfe, die Türme, die Gärten, die Töchter, die Wände. <b>Ohne Pünktchen:</b> die Arme, die Monate, die Jahre, die Burgen, die Boote, die Punkte.</p><p><b>Aufgabe 2:</b> die Nächte · die Blätter · die Brüder · die Dörfer · die Züge · die Röcke · die Kuchen · die Tassen</p><p><b>Aufgabe 3:</b> Eigene Beispiele, zum Beispiel: der Ball – die Bälle · der Sohn – die Söhne · der Hut – die Hüte · das Haus – die Häuser</p>')
l6 = sol(6, 'Mehrzahl-Meister', '<p><b>Aufgabe 1:</b> die Babys, die Hobbys, die Ponys, die Partys, die Teddys · die Freundinnen, die Lehrerinnen, die Ärztinnen, die Königinnen, die Schülerinnen · die Zeugnisse, die Geheimnisse, die Ergebnisse, die Busse, die Kürbisse · die Museen, die Aquarien, die Zentren, die Daten, die Alben</p><p><b>Aufgabe 2:</b> die Hobbys · die Lehrerinnen · die Kürbisse · die Alben</p><p><b>Aufgabe 3:</b> Die Babys schlafen. · Die Freundinnen lachen. · Die Busse halten an der Schule.</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

write('einzahl-mehrzahl', 'Übungsblätter: Einzahl und Mehrzahl (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps])
