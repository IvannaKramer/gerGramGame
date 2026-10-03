"""Übungsblätter Satzglieder (Umstellprobe)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

V = lambda s: f'<span class="vb">{s}</span>'
cap = lambda s: s[0].upper() + s[1:]
sent = lambda parts: cap(' '.join(parts)) + '.'
bars = lambda parts: ' | '.join(V(p) if i == 1 else (cap(p) if i == 0 else p) for i, p in enumerate(parts)) + '.'
def blocks(parts, verb): return ''.join(f'<span class="blk{" v" if p == verb else ""}">{p}</span>' for p in parts)
def start_line(start): return f'<div class="wr"><b>{start}</b> {L()}</div>'

EXTRA = '''
.vb{color:#C22A63;font-weight:700}
.blk{display:inline-block;border:.6mm solid #2B6BE0;border-radius:2.5mm;padding:.6mm 3.5mm;margin-right:2.5mm;font-size:14pt;font-weight:700;background:#fff}
.blk.v{border-color:#DE3A76;background:#FFE4EE}
.item{margin-bottom:2.2mm}
.item .s{font-size:14pt;margin:0}
.item .line.f{height:8.6mm}
.item .u{color:#56657F;font-size:12.5pt;margin:0}
.wr b{font-size:14pt}
.opt{display:flex;align-items:center;gap:3mm;font-size:13.5pt;height:7mm}
.cb{display:inline-block;width:5mm;height:5mm;border:.6mm solid #22304A;border-radius:1mm;flex:none}
.q{margin:0 0 .5mm;font-size:13.5pt}
.q b{font-weight:700}
.num{display:inline-block;width:8mm;font-family:'Grandstander',sans-serif;font-weight:800;color:#56657F}
.cnt{display:flex;align-items:center;justify-content:space-between;gap:4mm;height:11.4mm;font-size:14pt;border-bottom:.3mm dashed #D5E3F1}
.cnt .wide{word-spacing:3.2mm}
.sq{display:inline-block;width:9mm;height:9mm;border:.6mm solid #22304A;border-radius:2mm;flex:none}
.two{margin-bottom:1.6mm;padding-bottom:1.2mm;border-bottom:.3mm dashed #D5E3F1;display:flex;align-items:center;justify-content:space-between;gap:4mm}
.two p{margin:0;font-size:13.5pt}
.two .u{color:#56657F;font-size:12pt}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1mm 4mm;margin:1mm 0 3.2mm 8mm}
.cards .opt{font-size:12pt;height:6mm;white-space:nowrap}
.solb ol{margin:0;padding-left:5.5mm}
.solb li{margin:0}
.sol .vb{color:#C22A63}
.sol{font-size:12pt;line-height:1.4}
.sol .solb{padding:3mm 5mm;margin-bottom:5mm}
.sol .solb p{margin-bottom:2.5mm}
'''

# ---------------- Blatt 1: Satz-Zug ----------------
t1 = [(['laut', 'bellt', 'der Hund'], 'bellt'), (['im Teich', 'der Fisch', 'schwimmt'], 'schwimmt'),
      (['die Zeitung', 'Opa', 'am Abend', 'liest'], 'liest'), (['ins Tor', 'schießt', 'Tim', 'den Ball'], 'schießt'),
      (['Milch', 'die Katze', 'in der Küche', 'trinkt'], 'trinkt')]
a1 = ''.join(f'<div class="item"><span class="num">{chr(97 + i)})</span>{blocks(p, v)}{L("f")}</div>' for i, (p, v) in enumerate(t1))
t2 = [('Der Bus hält am Morgen vor der Schule.', 'Am Morgen'), ('Lena malt nach der Schule ein Bild.', 'Nach der Schule'),
      ('Papa repariert in der Garage das Fahrrad.', 'Das Fahrrad')]
a2 = ''.join(f'<div class="item"><p class="s">{s}</p>{start_line(st)}</div>' for s, st in t2)
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Satz-Zug', 'Satz-Zug',
  'Im Aussagesatz steht das <b class="vb">Verb</b> immer an <b>zweiter Stelle</b>. Die anderen Satzglieder dürfen ihre Plätze tauschen: <b>Der Hund bellt laut.</b> oder <b>Laut bellt der Hund.</b>',
  task(1, 'Die Wagen sind durcheinander. Schreibe den Satz richtig auf. Das <b class="vb">Verb</b> steht im pinken Wagen. Denke an den großen Satzanfang und den Punkt!', a1) +
  task(2, 'Stelle den Satz um. Der neue Anfang steht schon da.', a2))

# ---------------- Blatt 2: Welcher Satz stimmt? ----------------
q2 = [('Die Kinder spielen in der Pause Fußball.', ['In der Pause die Kinder spielen Fußball.', 'In der Pause spielen die Kinder Fußball.', 'Die spielen Kinder in der Pause Fußball.']),
      ('Mama kauft auf dem Markt frisches Obst.', ['Auf dem Markt kauft Mama frisches Obst.', 'Auf dem kauft Mama Markt frisches Obst.', 'Frisches Obst Mama kauft auf dem Markt.']),
      ('Paul füttert jeden Tag seinen Hamster.', ['Jeden füttert Paul Tag seinen Hamster.', 'Jeden Tag Paul füttert seinen Hamster.', 'Seinen Hamster füttert Paul jeden Tag.']),
      ('Der Schnee fällt leise auf die Dächer.', ['Leise fällt der Schnee auf die Dächer.', 'Auf die Dächer der Schnee fällt leise.', 'Auf fällt der Schnee leise die Dächer.'])]
b1 = ''.join(f'<div class="item"><p class="q"><span class="num">{chr(97 + i)})</span><b>{s}</b></p>' + ''.join(f'<div class="opt"><span class="num"></span><span class="cb"></span>{o}</div>' for o in opts) + '</div>' for i, (s, opts) in enumerate(q2))
t22 = [('Der Zug fährt um acht Uhr nach Berlin.', 'Um acht Uhr'), ('Anna schreibt ihrer Freundin einen Brief.', 'Einen Brief'), ('Wir fahren in den Ferien ans Meer.', 'In den Ferien')]
b2 = ''.join(f'<div class="item"><p class="s">{s}</p>{start_line(st)}</div>' for s, st in t22)
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Welcher Satz stimmt?', 'Welcher Satz stimmt?',
  'Beim Umstellen gelten zwei Regeln: Das <b class="vb">Verb</b> bleibt an <b>zweiter Stelle</b>. Und die Wörter eines <b>Satzglieds</b> bleiben immer zusammen, zum Beispiel <b>in der Pause</b>.',
  task(1, 'Nur ein Satz ist richtig umgestellt. Kreuze ihn an.', b1) +
  task(2, 'Stelle den Satz um. Der neue Anfang steht schon da.', b2))

# ---------------- Blatt 3: Satzglieder zählen ----------------
t3 = [(['Mia', 'tanzt', 'gern'], 'Gern tanzt Mia.'), (['der Frosch', 'hüpft', 'ins Wasser'], 'Ins Wasser hüpft der Frosch.'),
      (['das kleine Küken', 'piept'], 'Hier kann man nichts umstellen.'),
      (['Felix', 'holt', 'am Morgen', 'die Post'], 'Am Morgen holt Felix die Post.'),
      (['die Kuh', 'kaut', 'den ganzen Tag', 'frisches Gras'], 'Den ganzen Tag kaut die Kuh frisches Gras.'),
      (['mein Bruder', 'hört', 'in seinem Zimmer', 'Musik'], 'In seinem Zimmer hört mein Bruder Musik.'),
      (['Emma', 'bringt', 'ihrem Opa', 'am Sonntag', 'einen Kuchen'], 'Am Sonntag bringt Emma ihrem Opa einen Kuchen.'),
      (['der Bauer', 'fährt', 'im Sommer', 'mit dem Traktor', 'auf das Feld'], 'Mit dem Traktor fährt der Bauer im Sommer auf das Feld.'),
      (['Ben', 'zeigt', 'seiner Mutter', 'stolz', 'sein Zeugnis'], 'Stolz zeigt Ben seiner Mutter sein Zeugnis.')]
c1 = ''.join(f'<div class="two"><div><p>{sent(p)}</p><p class="u">{u}</p></div><span class="sq"></span></div>' for p, u in t3)
own = [('3', ''), ('4', ''), ('5', '')]
c2 = ''.join(f'<div class="wr">{n} Satzglieder: {L()}</div>' for n, _ in own)
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Satzglieder zählen', 'Satzglieder zählen',
  'Wörter, die beim Umstellen <b>zusammenbleiben</b>, sind zusammen <b>ein</b> Satzglied. Auch das <b class="vb">Verb</b> ist ein Satzglied. <b>Mia | tanzt | gern.</b> hat also 3 Satzglieder.',
  task(1, 'Unter jedem Satz steht derselbe Satz umgestellt. Trenne die Satzglieder im oberen Satz mit Strichen. Schreibe in das Kästchen, wie viele es sind.', c1) +
  task(2, 'Schreibe eigene Sätze auf.', c2))

# ---------------- Blatt 4: Satz-Schere ----------------
t4 = [['meine Oma', 'strickt', 'warme Socken'], ['der Briefträger', 'bringt', 'heute', 'eine Postkarte'], ['die Ärztin', 'hilft', 'dem kranken Kind'],
      ['unsere Katze', 'schläft', 'oft', 'auf dem Sofa'], ['der Koch', 'schneidet', 'das Gemüse', 'in kleine Stücke'],
      ['die Vögel', 'fliegen', 'im Herbst', 'gemeinsam', 'in den Süden'], ['der Hausmeister', 'öffnet', 'um sieben Uhr', 'das Tor'],
      ['Leon', 'putzt', 'jeden Abend', 'gründlich', 'seine Zähne'], ['viele Leute', 'warten', 'an der Haltestelle', 'auf den Bus'],
      ['die Lehrerin', 'diktiert', 'der Klasse', 'deutlich', 'einen Satz']]
d1 = ''.join(f'<div class="cnt"><span class="wide">{sent(p)}</span><span class="sq"></span></div>' for p in t4)
t42 = [['der Mond', 'leuchtet', 'in der Nacht', 'hell'], ['der Pirat', 'vergräbt', 'auf der Insel', 'einen Schatz'], ['zwei Affen', 'klettern', 'flink', 'auf den Baum']]
d2 = ''.join(f'<div class="item"><p class="s">{sent(p)}</p>{L("f")}</div>' for p in t42)
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Satz-Schere', 'Satz-Schere',
  'Mach im Kopf die <b>Umstellprobe</b>: Welche Wörter wandern nur gemeinsam nach vorn? Sie sind zusammen ein Satzglied. Das <b class="vb">Verb</b> ist immer ein eigenes Satzglied.',
  task(1, 'Trenne die Satzglieder mit Strichen. Kreise das Verb ein. Schreibe in das Kästchen, wie viele Satzglieder der Satz hat.', d1) +
  task(2, 'Mach die Umstellprobe: Schreibe jeden Satz mit einem anderen Satzanfang auf.', d2))

# ---------------- Blatt 5: Neuer Satzanfang ----------------
t5 = [('Marie besucht am Freitag ihre Tante.', 'Am Freitag'), ('Der Fuchs schleicht leise um den Hühnerstall.', 'Leise'),
      ('Die Mannschaft gewinnt heute das letzte Spiel.', 'Das letzte Spiel'), ('Herr Becker trinkt nach dem Essen einen Kaffee.', 'Nach dem Essen'),
      ('Der Torwart fängt den Ball mit beiden Händen.', 'Mit beiden Händen'), ('Unser Nachbar mäht jeden Samstag den Rasen.', 'Den Rasen')]
e1 = ''.join(f'<div class="item"><p class="s"><span class="num">{chr(97 + i)})</span>{s}</p>{start_line(st)}</div>' for i, (s, st) in enumerate(t5))
e2 = '<p class="s" style="font-size:14pt;margin:0 0 1mm"><b>Die Familie fährt in den Osterferien mit dem Zug zu den Großeltern.</b></p>' + ''.join(start_line(st) for st in ['In den Osterferien', 'Mit dem Zug', 'Zu den Großeltern'])
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Neuer Satzanfang', 'Neuer Satzanfang',
  'Mit der Umstellprobe machst du deine Sätze abwechslungsreich. Ein anderes Satzglied wandert nach vorn. Danach kommt sofort das <b class="vb">Verb</b>, denn es bleibt an <b>zweiter Stelle</b>.',
  task(1, 'Stelle den Satz um. Der neue Anfang steht schon da.', e1) +
  task(2, 'Ein Satz, drei neue Anfänge: Schreibe den Satz dreimal auf.', e2), )

# ---------------- Blatt 6: Satzanfang-Profi ----------------
t6 = [(['der kleine Dackel', 'vergräbt', 'am frühen Morgen', 'einen dicken Knochen'], ['am frühen', 'einen dicken Knochen', 'der kleine', 'am frühen Morgen', 'Morgen einen', 'der kleine Dackel']),
      (['Finn', 'spielt', 'am späten Nachmittag', 'mit seinem besten Freund', 'Tischtennis'], ['mit seinem', 'am späten Nachmittag', 'besten Freund', 'mit seinem besten Freund', 'am späten', 'Nachmittag mit seinem']),
      (['der alte Fischer', 'repariert', 'vor dem Sturm', 'sein kaputtes Netz'], ['vor dem Sturm', 'der alte', 'kaputtes Netz', 'vor dem', 'sein kaputtes Netz', 'Sturm sein kaputtes']),
      (['der dicke Kater', 'liegt', 'seit zwei Stunden', 'faul', 'auf der warmen Heizung'], ['seit zwei', 'faul', 'auf der warmen Heizung', 'Stunden faul', 'seit zwei Stunden', 'auf der warmen']),
      (['die müden Wanderer', 'erreichen', 'nach einem langen Tag', 'endlich', 'die kleine Hütte'], ['die müden Wanderer', 'einem langen Tag', 'endlich', 'die kleine', 'nach einem langen Tag', 'die kleine Hütte'])]
f1 = ''.join(f'<p class="q"><span class="num">{chr(97 + i)})</span><b>{sent(p)}</b></p><div class="cards">' + ''.join(f'<div class="opt"><span class="cb"></span>{c}</div>' for c in cs) + '</div>' for i, (p, cs) in enumerate(t6))
f2 = '<p class="s" style="font-size:14pt;margin:0 0 1mm"><b>Unser Trainer erklärt der ganzen Mannschaft vor dem Spiel die neuen Regeln.</b></p>' + ''.join(L('f') for _ in range(3))
p6 = page('Blatt 6', 'Für Profis', 3, 'Satzanfang-Profi', 'Satzanfang-Profi',
  'Ein <b>ganzes Satzglied</b> kann allein vor dem <b class="vb">Verb</b> stehen, und der Satz klingt immer noch richtig. Fehlt ein Wort oder ist eines zu viel, klingt der Satz falsch.',
  task(1, 'Welche Wortgruppen sind ganze Satzglieder? Mach die Umstellprobe und kreuze alle richtigen an.', f1) +
  task(2, 'Schreibe den Satz mit drei verschiedenen neuen Satzanfängen auf.', f2))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
alt = '<i>Auch andere Reihenfolgen sind richtig, wenn das Verb an zweiter Stelle steht.</i>'
l1 = sol(1, 'Satz-Zug', '<p><b>Aufgabe 1</b> (zum Beispiel): a) Der Hund bellt laut. · b) Der Fisch schwimmt im Teich. · c) Opa liest am Abend die Zeitung. · d) Tim schießt den Ball ins Tor. · e) Die Katze trinkt in der Küche Milch. ' + alt + '</p>'
  '<p><b>Aufgabe 2:</b> Am Morgen hält der Bus vor der Schule. · Nach der Schule malt Lena ein Bild. · Das Fahrrad repariert Papa in der Garage.</p>')
l2 = sol(2, 'Welcher Satz stimmt?', '<p><b>Aufgabe 1:</b> a) In der Pause spielen die Kinder Fußball. · b) Auf dem Markt kauft Mama frisches Obst. · c) Seinen Hamster füttert Paul jeden Tag. · d) Leise fällt der Schnee auf die Dächer.</p>'
  '<p><b>Aufgabe 2:</b> Um acht Uhr fährt der Zug nach Berlin. · Einen Brief schreibt Anna ihrer Freundin. · In den Ferien fahren wir ans Meer.</p>')
l3 = sol(3, 'Satzglieder zählen', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{bars(p)} <b>({len(p)})</b>' for p, _ in t3) + '</p><p><b>Aufgabe 2:</b> Eigene Sätze, zum Beispiel: Der Hund | bellt | laut. (3) · Opa | liest | am Abend | die Zeitung. (4)</p>')
l4 = sol(4, 'Satz-Schere', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{bars(p)} <b>({len(p)})</b>' for p in t4) + '</p>'
  '<p><b>Aufgabe 2</b> (zum Beispiel): In der Nacht leuchtet der Mond hell. · Auf der Insel vergräbt der Pirat einen Schatz. · Flink klettern zwei Affen auf den Baum. ' + alt + '</p>')
l5 = sol(5, 'Neuer Satzanfang', '<p><b>Aufgabe 1:</b> a) Am Freitag besucht Marie ihre Tante. · b) Leise schleicht der Fuchs um den Hühnerstall. · c) Das letzte Spiel gewinnt die Mannschaft heute. · d) Nach dem Essen trinkt Herr Becker einen Kaffee. · e) Mit beiden Händen fängt der Torwart den Ball. · f) Den Rasen mäht unser Nachbar jeden Samstag.</p>'
  '<p><b>Aufgabe 2:</b> In den Osterferien fährt die Familie mit dem Zug zu den Großeltern. · Mit dem Zug fährt die Familie in den Osterferien zu den Großeltern. · Zu den Großeltern fährt die Familie in den Osterferien mit dem Zug.</p>')
l6 = sol(6, 'Satzanfang-Profi', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{chr(97 + i)}) ' + ', '.join(c for c in cs if c in p) for i, (p, cs) in enumerate(t6)) + '</p>'
  '<p><b>Aufgabe 2</b> (zum Beispiel): Der ganzen Mannschaft erklärt unser Trainer vor dem Spiel die neuen Regeln. · Vor dem Spiel erklärt unser Trainer der ganzen Mannschaft die neuen Regeln. · Die neuen Regeln erklärt unser Trainer der ganzen Mannschaft vor dem Spiel.</p>')
ps1 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 3', '', '', l1 + l2 + l3, solution=True)
ps2 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 4 bis 6', '', '', l4 + l5 + l6, solution=True)

write('satzglieder', 'Übungsblätter: Satzglieder (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps1, ps2], extra_css=EXTRA)
