"""Übungsblätter Pronomen."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

PRON = {'er': 'er', 'sie': 'sie', 'es': 'es', 'pl': 'sie'}
def C(k, s): return f'<span class="{k}">{s}</span>'
def cap(s): return s[0].upper() + s[1:]
G = '<span class="g"></span>'
def gap(s): return s.replace('___', G)
RULE = f'{C("er", "der → er")} · {C("sie", "die → sie")} · {C("es", "das → es")} · {C("pl", "viele → sie")}'
MERK = f'Ein <b>Pronomen</b> steht für ein Nomen. Der Artikel hilft dir: {C("er", "der")} Hund → {C("er", "er")}, {C("sie", "die")} Katze → {C("sie", "sie")}, {C("es", "das")} Pferd → {C("es", "es")}. Sind es viele, heißt es immer {C("pl", "sie")}: die Kinder → {C("pl", "sie")}.'

EXTRA = '''
.er{color:#1F57C3;font-weight:700}.sie{color:#C22A63;font-weight:700}.es{color:#157A41;font-weight:700}.pl{color:#6A3FC8;font-weight:700}.sp{color:#086169;font-weight:700}
.g{display:inline-block;border-bottom:.45mm solid #56657F;width:17mm;height:1.1em;margin:0 .8mm;vertical-align:baseline}
.list p{margin:0;height:9.4mm;display:flex;align-items:flex-end;font-size:13.5pt;white-space:nowrap}
.list .emo{align-self:flex-end;margin-bottom:.5mm;width:13mm;font-size:13pt;white-space:nowrap}
.list.t4 p{height:8.3mm;font-size:12pt}
.list.t6 p{height:7.5mm;font-size:12.5pt}
.nr{flex:none;width:7mm;color:#56657F;font-size:10.5pt}
.pick{margin-left:auto;font-size:10.5pt;color:#22304A;word-spacing:.1em}
.pick i{font-style:normal;color:#A9B4C6;margin:0 1.2mm}
.cols4{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}
.cols4 .c{border:.6mm solid var(--c);border-radius:3mm;padding:0 2mm 3mm}
.cols4 h3{margin:0 -2mm 0;background:var(--c);color:#fff;font-size:12.5pt;padding:1mm 2mm;text-align:center;border-radius:2.2mm 2.2mm 0 0}
.cols4 h3 small{font-family:'Andika',sans-serif;font-weight:400;font-size:9.5pt}
.cols4 .line{display:block;width:100%;height:10mm}
.q1{--c:#2B6BE0}.q2{--c:#DE3A76}.q3{--c:#1A8C4B}.q4{--c:#7A4FD8}
.bank{border:.7mm dashed #56657F;border-radius:4mm;padding:1.5mm 5mm;display:flex;gap:8mm;font-size:13pt;font-weight:700;margin-bottom:1mm;align-items:baseline}
.bank b{font-family:'Grandstander',sans-serif;font-size:11pt;color:#56657F;font-weight:800}
.vblock{margin-bottom:2.5mm}
.vblock h3{margin:0;font-size:12pt;color:#56657F}
.story{border:.6mm solid #D5E3F1;border-radius:3.5mm;padding:1mm 4mm 1.2mm;margin-bottom:1.5mm}
.story h3{margin:0;font-size:12pt;color:#56657F}
.story p{margin:0;font-size:12.5pt;line-height:1.9}
.count span{white-space:nowrap}
.count{display:flex;gap:6mm;font-size:13pt;align-items:flex-end;height:9mm}
.count .line{width:12mm}
.sol .solb p{margin-bottom:1mm}
'''

# ---------------- Blatt 1: Pronomen-Körbe ----------------
w1 = [('der Hund', 'er', '🐕'), ('die Katze', 'sie', '🐈'), ('das Pferd', 'es', '🐎'), ('die Kinder', 'pl', '🧒🧒'), ('der Ball', 'er', '⚽'),
      ('das Buch', 'es', '📖'), ('die Blume', 'sie', '🌸'), ('die Schuhe', 'pl', '👟👟'), ('das Auto', 'es', '🚗'), ('der Opa', 'er', '👴'),
      ('die Oma', 'sie', '👵'), ('die Vögel', 'pl', '🐦🐦'), ('das Baby', 'es', '👶'), ('der Apfel', 'er', '🍎'), ('die Uhr', 'sie', '⏰')]
t1 = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="emo" style="width:13mm;font-size:13pt;white-space:nowrap">{e}</span><span>{n} <span class="arr">→</span></span>{L()}</div>' for n, k, e in w1) + '</div>'
heads = [('q1', 'er', 'der'), ('q2', 'sie', 'die (eine)'), ('q3', 'es', 'das'), ('q4', 'sie', 'die (viele)')]
t1b = '<div class="cols4">' + ''.join(f'<div class="c {q}"><h3>{p} <small>{s}</small></h3>{L()}{L()}</div>' for q, p, s in heads) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Pronomen-Körbe', 'Pronomen-Körbe', MERK,
  task(1, 'Welches Pronomen steht für das Nomen? Schreibe <b>er</b>, <b>sie</b> oder <b>es</b> auf die Linie.', t1) +
  task(2, 'Finde selbst Nomen. Schreibe in jeden Korb zwei Nomen mit Artikel.', t1b))

# ---------------- Blatt 2: Pronomen-Lücke ----------------
s2 = [('Der Igel ist müde.', '___ rollt sich ein.', 'er', '🦔'), ('Die Maus ist klein.', '___ frisst Käse.', 'sie', '🐭'),
      ('Das Schaf steht auf der Wiese.', '___ frisst Gras.', 'es', '🐑'), ('Die Bienen sind fleißig.', '___ fliegen von Blüte zu Blüte.', 'pl', '🐝🐝'),
      ('Der Bus ist voll.', '___ fährt zur Schule.', 'er', '🚌'), ('Das Fahrrad ist neu.', '___ hat eine Klingel.', 'es', '🚲'),
      ('Die Sonne scheint.', '___ ist heute sehr warm.', 'sie', '☀️'), ('Die Birnen sind reif.', '___ fallen vom Baum.', 'pl', '🍐🍐'),
      ('Der Kuchen ist fertig.', '___ duftet lecker.', 'er', '🍰'), ('Die Lehrerin kommt.', '___ trägt eine Tasche.', 'sie', '👩‍🏫'),
      ('Das Eis ist kalt.', '___ schmeckt nach Erdbeere.', 'es', '🍦'), ('Die Fische sind bunt.', '___ schwimmen im Teich.', 'pl', '🐟🐟'),
      ('Der Papagei ist bunt.', '___ kann sprechen.', 'er', '🦜'), ('Die Rakete startet.', '___ fliegt zum Mond.', 'sie', '🚀'),
      ('Das Schiff ist groß.', '___ fährt über das Meer.', 'es', '🚢')]
t2 = '<div class="list">' + ''.join(f'<p><span class="emo">{e}</span><span>{a} {gap(b)}</span></p>' for a, b, k, e in s2) + '</div>'
t2b = f'<div class="count"><span>{C("er", "Er")}: {L()} -mal</span><span>{C("sie", "Sie")} (eine): {L()} -mal</span><span>{C("es", "Es")}: {L()} -mal</span><span>{C("pl", "Sie")} (viele): {L()} -mal</span></div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Pronomen-Lücke', 'Pronomen-Lücke',
  f'Das Pronomen steht für das Nomen aus dem ersten Satz. Schau auf den Artikel: {RULE}. Am Satzanfang schreibst du das Pronomen groß.',
  task(1, 'Unterstreiche im ersten Satz das Nomen mit seinem Artikel. Schreibe dann das passende Pronomen in die Lücke.', t2) +
  task(2, 'Zähle nach: Wie oft hast du jedes Pronomen eingesetzt?', t2b))

# ---------------- Blatt 3: Pronomen-Memory ----------------
verbs = [('sein', [('ich', 'bin müde.'), ('du', 'bist mutig.'), ('er', 'ist stark.'), ('wir', 'sind Freunde.'), ('ihr', 'seid schnell.')]),
         ('haben', [('ich', 'habe Durst.'), ('du', 'hast Zeit.'), ('er', 'hat Hunger.'), ('wir', 'haben Ferien.'), ('ihr', 'habt Glück.')]),
         ('sehen', [('ich', 'sehe einen Vogel.'), ('du', 'siehst müde aus.'), ('er', 'sieht einen Film.'), ('wir', 'sehen das Meer.'), ('ihr', 'seht alles.')])]
left = ['wir', 'du', 'ihr', 'ich', 'er']
right = ['… ist stark.', '… bin müde.', '… sind Freunde.', '… bist mutig.', '… seid schnell.']
t3 = '<div class="connect">' + ''.join(f'<div class="row"><span class="l sp" style="width:30mm">{a}</span><span class="dot"></span><span class="gap"></span><span class="dot"></span><span class="r" style="width:60mm">{b}</span></div>' for a, b in zip(left, right)) + '</div>'
order = {'haben': [2, 0, 4, 1, 3], 'sehen': [3, 1, 0, 4, 2]}
bank = '<div class="bank"><b>Wörter:</b><span>ich</span><span>du</span><span>er</span><span>wir</span><span>ihr</span></div>'
def block(v, pairs):
    return f'<div class="vblock"><h3>Das Verb „{v}“</h3><div class="grid2">' + ''.join(f'<div class="wr">{L("s")}<span>{pairs[i][1]}</span></div>' for i in order[v]) + '</div></div>'
t3b = bank + block(*verbs[1]) + block(*verbs[2])
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Pronomen-Memory', 'Pronomen-Memory',
  f'Zu jedem Pronomen gehört eine eigene Form des Verbs: {C("sp", "ich")} bin, {C("sp", "du")} bist, {C("sp", "er")} ist, {C("sp", "wir")} sind, {C("sp", "ihr")} seid. Sprich den Satz leise: Klingt er richtig?',
  task(1, 'Was gehört zusammen? Verbinde jedes Pronomen mit dem passenden Satz.', t3) +
  task(2, 'Setze die Pronomen ein. Bei jedem Verb passt jedes Pronomen genau einmal. Denk an den Satzanfang!', t3b))

# ---------------- Blatt 4: Wer ist gemeint? ----------------
sets = [['der Frosch', 'die Ente', 'das Boot', 'die Enten'], ['der Bäcker', 'die Ärztin', 'das Kind', 'die Nachbarn'],
        ['der Mond', 'die Wolke', 'das Flugzeug', 'die Sterne'], ['der Löffel', 'die Gabel', 'das Messer', 'die Teller'],
        ['der Tiger', 'die Giraffe', 'das Zebra', 'die Affen'], ['der Rucksack', 'die Jacke', 'das Heft', 'die Stifte'],
        ['der Zug', 'die Fähre', 'das Motorrad', 'die Traktoren'], ['der Hahn', 'die Kuh', 'das Schwein', 'die Hühner'],
        ['der Baum', 'die Rose', 'das Blatt', 'die Tulpen'], ['der Pullover', 'die Mütze', 'das Kleid', 'die Handschuhe']]
KI = ['er', 'sie', 'es', 'pl']
s4 = [(0, 'Sie schwimmen auf dem See.', 'pl'), (0, 'Es schaukelt auf dem Wasser.', 'es'), (1, 'Er backt jeden Morgen Brot.', 'er'), (1, 'Sie hilft kranken Menschen.', 'sie'),
      (2, 'Sie leuchten in der Nacht.', 'pl'), (2, 'Er ist heute rund und hell.', 'er'), (3, 'Es schneidet gut.', 'es'), (3, 'Sie stehen schon auf dem Tisch.', 'pl'),
      (4, 'Sie hat einen langen Hals.', 'sie'), (4, 'Es hat schwarze und weiße Streifen.', 'es'), (5, 'Er ist heute sehr schwer.', 'er'), (5, 'Sie liegen im Mäppchen.', 'pl'),
      (6, 'Sie fährt über den Fluss.', 'sie'), (6, 'Er hält am Bahnhof.', 'er'), (7, 'Er kräht am Morgen.', 'er'), (7, 'Sie legen Eier.', 'pl'),
      (8, 'Es fällt im Herbst vom Ast.', 'es'), (8, 'Sie hat Dornen.', 'sie'), (9, 'Sie wärmt den Kopf.', 'sie'), (9, 'Es hat bunte Punkte.', 'es')]
ROT = [[1, 3, 0, 2], [2, 0, 3, 1], [3, 1, 2, 0], [0, 2, 1, 3]]
def opts(i, si): return '<i>|</i>'.join(sets[si][j] for j in ROT[i % 4])
t4 = '<div class="list t4">' + ''.join(f'<p><span class="nr">{i + 1}.</span><span><b>{s}</b></span><span class="pick">{opts(i, si)}</span></p>' for i, (si, s, k) in enumerate(s4)) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Wer ist gemeint?', 'Wer ist gemeint?',
  f'{C("er", "er")} steht für ein Nomen mit <b>der</b>, {C("es", "es")} für ein Nomen mit <b>das</b>. Bei <b>sie</b> hilft dir das Verb: {C("sie", "Sie schwimmt")} ist nur eine. {C("pl", "Sie schwimmen")} sind viele.',
  task(1, 'Für welches Nomen steht das Pronomen? Kreise das passende Nomen ein. Unterstreiche bei <b>sie</b> zuerst das Verb.', t4))

# ---------------- Blatt 5: Ersetz-Spiel ----------------
texts = [('Der Kater', 'Lina hat einen Kater. [Der Kater|er] heißt Felix. Am Morgen hat [der Kater|er] großen Hunger. [Lina|sie] füllt den Napf. Dann geht [Lina|sie] in die Schule.'),
  ('Das Zelt', 'Jonas bekommt ein Zelt. [Das Zelt|es] ist grün. Im Garten steht [das Zelt|es] unter dem Baum. [Jonas|er] holt eine Lampe. Am Abend schläft [Jonas|er] draußen.'),
  ('Die Zwillinge', 'Die Zwillinge haben ein Kaninchen. [Das Kaninchen|es] hat weiches Fell. Jeden Tag bekommt [das Kaninchen|es] frisches Heu. [Die Zwillinge|pl] putzen den Stall. Danach spielen [die Zwillinge|pl] im Hof.'),
  ('Die Eule', 'Im Wald wohnt eine Eule. Am Tag schläft [die Eule|sie] in einem Baum. In der Nacht jagt [die Eule|sie]. Im Gras sitzen zwei Hasen. [Die Hasen|pl] hören jedes Geräusch. Schnell hoppeln [die Hasen|pl] davon.'),
  ('Auf dem Bauernhof', 'Auf dem Hof stehen ein Esel, eine Ziege und ein Lamm. [Der Esel|er] ruft laut. [Die Ziege|sie] klettert auf einen Stein. [Das Lamm|es] trinkt Milch. Hinter dem Stall laufen viele Küken. [Die Küken|pl] piepen leise.')]
BR = re.compile(r'\[([^|\]]+)\|(\w+)\]')
def with_pron(s):
    def r(m):
        start = m.start() == 0 or s[:m.start()].rstrip()[-1] in '.!?'
        p = PRON[m.group(2)]
        return C(m.group(2), cap(p) if start else p)
    return BR.sub(r, s)
t5 = ''.join(f'<div class="story"><h3>{t}</h3><p>{BR.sub(lambda m: m.group(1), s)}</p></div>' for t, s in texts)
t5b = f'<div class="count"><span>{C("er", "er")}: {L()} -mal</span><span>{C("sie", "sie")} (eine): {L()} -mal</span><span>{C("es", "es")}: {L()} -mal</span><span>{C("pl", "sie")} (viele): {L()} -mal</span></div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Ersetz-Spiel', 'Ersetz-Spiel',
  'Beim <b>ersten Mal</b> brauchst du das Nomen. Kommt dasselbe Nomen <b>noch einmal</b>, nimmst du ein Pronomen. So klingt der Text viel besser.',
  task(1, 'In jedem Text wiederholen sich Nomen. Streiche jede Wiederholung durch und schreibe das Pronomen darüber. In jedem Text sind es vier.', t5) +
  task(2, 'Zähle nach: Wie oft hast du jedes Pronomen geschrieben? (Gleich oft!)', t5b))

# ---------------- Blatt 6: Pronomen-Profi ----------------
s6a = [('Das Mädchen lacht. [Es] hat einen Witz gehört.', 'es'), ('Der Tisch wackelt. [Er] hat ein kurzes Bein.', 'er'), ('Die Tür klemmt. [Sie] geht nicht auf.', 'sie'),
       ('Die Eltern warten am Tor. [Sie] winken fröhlich.', 'pl'), ('Das Kätzchen ist erst vier Wochen alt. [Es] trinkt noch Milch.', 'es'),
       ('Der Schmetterling ist gelb. [Er] fliegt über die Wiese.', 'er'), ('Die Schnecke ist langsam. [Sie] kriecht über den Weg.', 'sie'),
       ('Die Geschwister streiten selten. [Sie] spielen oft zusammen.', 'pl'), ('Das Eichhörnchen sammelt Nüsse. [Es] klettert flink auf den Baum.', 'es'),
       ('Der Regen hört auf. [Er] hat alle Pfützen gefüllt.', 'er'), ('Die Pause beginnt. [Sie] dauert zwanzig Minuten.', 'sie'),
       ('Die Ferien fangen an. [Sie] dauern sechs Wochen.', 'pl')]
s6b = [('Papa sucht den Schlüssel. Er findet [ihn] in der Jacke.', 'er'), ('Der Hamster hat Durst. Emma gibt [ihm] frisches Wasser.', 'er'),
       ('Tante Eva hat Geburtstag. Wir schenken [ihr] einen Strauß.', 'sie'), ('Die Gäste haben Hunger. Der Koch bringt [ihnen] die Suppe.', 'pl'),
       ('Der Drachen hängt in der Tanne. Onkel Max holt [ihn] herunter.', 'er'), ('Das Fohlen friert. Die Bäuerin legt [ihm] eine Decke um.', 'es'),
       ('Frau Kaya trägt schwere Taschen. Ben hilft [ihr] gern.', 'sie'), ('Die Freunde kommen zu Besuch. Lea zeigt [ihnen] den Garten.', 'pl')]
B6 = re.compile(r'\[(\w+)\]')
def rows6(items, n0=0): return '<div class="list t6">' + ''.join(f'<p><span class="nr">{n0 + i + 1}.</span><span>{B6.sub(G, s)}</span></p>' for i, (s, k) in enumerate(items)) + '</div>'
bank6 = '<div class="bank"><b>Wörter:</b><span>ihn</span><span>ihm</span><span>ihr</span><span>ihnen</span><span style="font-weight:400;font-size:11pt">(jedes passt zweimal)</span></div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Pronomen-Profi', 'Pronomen-Profi',
  f'Es zählt immer der <b>Artikel</b>: {C("es", "das")} Mädchen → {C("es", "es")}, {C("er", "der")} Tisch → {C("er", "er")}. Manchmal ändert sich das Pronomen. Frage <b>Wen?</b> → ihn. Frage <b>Wem?</b> → ihm, ihr oder (bei vielen) ihnen.',
  task(1, 'Schreibe <b>er</b>, <b>sie</b> oder <b>es</b> in die Lücke. Am Satzanfang schreibst du groß!', rows6(s6a)) +
  task(2, 'Frage zuerst: Wen? oder Wem? Schreibe dann das passende Pronomen in die Lücke.', bank6 + rows6(s6b, 12)))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def f6(s, k): return B6.sub(lambda m: C(k, m.group(1)), s)
l1 = sol(1, 'Pronomen-Körbe', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{n} → {C(k, PRON[k])}' for n, k, e in w1) + '</p>' +
  f'<p><b>Aufgabe 2:</b> Eigene Nomen, zum Beispiel: {C("er", "er")}: der Tisch, der Vater · {C("sie", "sie")} (eine): die Lampe, die Tante · {C("es", "es")}: das Haus, das Kind · {C("pl", "sie")} (viele): die Bücher, die Hunde</p>')
cnt = lambda items: {k: sum(1 for it in items if it[2] == k) for k in KI}
c2 = cnt(s2)
l2 = sol(2, 'Pronomen-Lücke', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{a} {b.replace("___", C(k, cap(PRON[k])))}' for a, b, k, e in s2) + '</p>' +
  f'<p><b>Aufgabe 2:</b> {C("er", "Er")}: {c2["er"]}-mal · {C("sie", "Sie")} (eine): {c2["sie"]}-mal · {C("es", "Es")}: {c2["es"]}-mal · {C("pl", "Sie")} (viele): {c2["pl"]}-mal</p>')
l3 = sol(3, 'Pronomen-Memory', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{C("sp", cap(p))} {r}' for p, r in verbs[0][1]) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{C("sp", cap(verbs[n][1][i][0]))} {verbs[n][1][i][1]}' for n, v in ((1, 'haben'), (2, 'sehen')) for i in order[v]) + '</p>')
l4 = sol(4, 'Wer ist gemeint?', '<p>' + ' · '.join(f'{i + 1}. {C(k, s.split(" ")[0])} {s.split(" ", 1)[1]} → {C(k, sets[si][KI.index(k)])}' for i, (si, s, k) in enumerate(s4)) + '</p>')
n5 = {k: sum(len(re.findall(r'\|' + k + r'\]', s)) for t, s in texts) for k in KI}
l5 = sol(5, 'Ersetz-Spiel', ''.join(f'<p><b>{t}:</b> {with_pron(s)}</p>' for t, s in texts) +
  f'<p><b>Aufgabe 2:</b> {C("er", "er")}: {n5["er"]}-mal · {C("sie", "sie")} (eine): {n5["sie"]}-mal · {C("es", "es")}: {n5["es"]}-mal · {C("pl", "sie")} (viele): {n5["pl"]}-mal</p>')
l6 = sol(6, 'Pronomen-Profi', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{i + 1}. {f6(s, k)}' for i, (s, k) in enumerate(s6a)) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{i + 13}. {f6(s, k)}' for i, (s, k) in enumerate(s6b)) + '</p>' +
  '<p><b>Hinweis:</b> In der Schule gilt bei „das Mädchen“ das Pronomen „es“, weil der Artikel zählt. Im Alltag hört man oft auch „sie“.</p>')
psA = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 4', '', '', l1 + l2 + l3 + l4, solution=True)
psB = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 5 und 6', '', '', l5 + l6, solution=True)

write('pronomen', 'Übungsblätter: Pronomen (Klasse 4)', [p1, p2, p3, p4, p5, p6, psA, psB], extra_css=EXTRA)
