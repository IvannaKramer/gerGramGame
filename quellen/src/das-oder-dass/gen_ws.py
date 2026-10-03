"""Übungsblätter das oder dass."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

D1, D2 = (lambda s: f'<span class="d1">{s}</span>'), (lambda s: f'<span class="d2">{s}</span>')
G = '<span class="g"></span>'
def col(w): return D2(w) if w.lower() == 'dass' else D1(w)
def gap(s): return s.replace('___', G)
def solved(s, a): return s.replace('___', col(a), 1)
MERK = f'Mach die Probe: Kannst du <b>dieses</b> oder <b>welches</b> einsetzen? Dann schreibst du {D1("das")}. Passt keins von beiden? Dann schreibst du {D2("dass")}.'

EXTRA = '''
.d1{color:#157A41;font-weight:700}.d2{color:#6A3FC8;font-weight:700}
.g{display:inline-block;border-bottom:.45mm solid #56657F;width:17mm;height:1.1em;margin:0 .8mm;vertical-align:baseline}
.list p{margin:0;height:10mm;display:flex;align-items:flex-end;font-size:13.5pt;white-space:nowrap}
.list p>span.t{white-space:nowrap}
.list.tight p{height:8.6mm;font-size:12.5pt}
.list.b2 p{height:7.9mm}
.list.b1 p{height:8.6mm}
.list.komma p{height:8.5mm}
.komma .t{word-spacing:.35em}
.list.b6 p{height:7.3mm}
.pro{margin-bottom:2.2mm}
.pro p{margin:0;font-size:13.5pt;white-space:nowrap}
.pro .p{font-size:11pt;color:#56657F;display:flex;gap:3mm;align-items:center;margin-top:.6mm}
.pro .p b{color:#22304A}
.ck{margin-left:auto;display:inline-flex;gap:4mm;color:#22304A}
.o{display:inline-block;width:3.6mm;height:3.6mm;border:.45mm solid #22304A;border-radius:50%;vertical-align:-.5mm;margin-right:1.2mm}
.o.big{width:5mm;height:5mm;margin-right:2.5mm;flex:none;align-self:center}
.two{display:grid;grid-template-columns:1fr 1fr;gap:0 7mm}
.two p{font-size:12.5pt}
.abc{margin-left:auto;display:inline-flex;gap:2mm;align-self:center}
.abc i{font-style:normal;font-family:'Grandstander',sans-serif;font-weight:800;font-size:9.5pt;width:6mm;height:6mm;border:.45mm solid #22304A;border-radius:50%;display:grid;place-items:center}
.key{display:flex;gap:6mm;font-size:11pt;margin:-1mm 0 2mm;flex-wrap:wrap}
.key b{font-family:'Grandstander',sans-serif}
.story{border:.6mm solid #D5E3F1;border-radius:3.5mm;padding:1.2mm 4mm 1.6mm;margin-bottom:2mm}
.story h3{margin:0;font-size:12pt;color:#56657F}
.story p{margin:0;font-size:12.5pt;line-height:1.68}
.count{display:flex;gap:12mm;font-size:13.5pt;align-items:flex-end;height:10mm}
.count .line{width:16mm}
.err{border:.7mm dashed #56657F;border-radius:4mm;padding:2mm 5mm 3mm;font-size:13pt;line-height:2}
.own .line{margin-bottom:1mm}
.sol .d1,.sol .d2{font-weight:700}
.sol .solb p{margin-bottom:1mm}
'''

# ---------------- Blatt 1: Proben-Lupe ----------------
a1 = [('Ich lese ___ Buch über Pferde.', 'dieses'), ('Ich hoffe, ___ du bald kommst.', 'dieses'), ('Dort steht ein Fahrrad, ___ ich mir wünsche.', 'welches'),
      ('Mama sagt, ___ wir jetzt essen.', 'welches'), ('___ schmeckt mir sehr gut.', 'Dieses'), ('Schön, ___ du da bist!', 'welches')]
ck = '<span class="ck"><span><span class="o"></span>klingt richtig</span><span><span class="o"></span>klingt falsch</span></span>'
t1 = ''.join(f'<div class="pro"><p>{gap(s)}</p><p class="p"><span>Probe: {s.replace("___", "<b>" + p + "</b>")}</span>{ck}</p></div>' for s, p in a1)
a2 = ['___ Mädchen malt ein Bild.', 'Ich weiß, ___ du gut schwimmen kannst.', 'Leo füttert ___ Kaninchen.', 'Papa glaubt, ___ es heute regnet.',
      'Wir haben ein Zelt, ___ sehr groß ist.', 'Wir freuen uns, ___ bald Ferien sind.', 'Oma wünscht sich, ___ wir sie besuchen.',
      'Tom hat ein Pferd, ___ Blitz heißt.', 'Ich finde es toll, ___ ihr mitspielt.']
t2 = '<div class="list b1">' + ''.join(f'<p><span class="t">{gap(s)}</span></p>' for s in a2) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Proben-Lupe', 'Proben-Lupe', MERK,
  task(1, f'Lies den Probe-Satz leise vor. Klingt er richtig? Kreuze an. Setze dann {D1("das")} oder {D2("dass")} in die Lücke ein.', t1) +
  task(2, f'Mach die Probe im Kopf. Setze {D1("das")} oder {D2("dass")} ein. Denk an den Satzanfang!', t2))

# ---------------- Blatt 2: Zwei Körbe ----------------
b1 = ['___ Baby schläft.', 'Tim sagt, ___ er müde ist.', 'Ich mag ___ Lied.', 'Ich denke, ___ sie gewinnt.', 'Wir putzen ___ Auto.',
      'Es ist schade, ___ du gehst.', '___ Eis ist kalt.', 'Opa meint, ___ es schneit.', '___ habe ich selbst gebaut.',
      'Ich verspreche, ___ ich aufräume.', 'Hier ist ein Spiel, ___ Spaß macht.', 'Gut, ___ ihr helft!',
      'Ich habe ein Haustier, ___ gern schmust.', 'Sie hofft, ___ er anruft.', 'Lina trägt ___ Kleid von Oma.']
u1 = '<div class="list b2">' + ''.join(f'<p><span class="o big"></span><span class="t">{gap(s)}</span></p>' for s in b1) + '</div>'
u2 = f'<div class="count"><span>{D1("das")}: {L()} -mal</span><span>{D2("dass")}: {L()} -mal</span></div>'
u3 = f'<div class="own"><div class="wr"><span>{D1("das")}:</span> {L()}</div><div class="wr"><span>{D2("dass")}:</span> {L()}</div></div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Zwei Körbe', 'Zwei Körbe', MERK,
  task(1, f'Setze {D1("das")} oder {D2("dass")} ein. Male den Kreis vor dem Satz an: <b class="d1">grün</b> für das, <b class="d2">lila</b> für dass.', u1) +
  task(2, 'Zähle nach: Wie oft hast du jedes Wort eingesetzt?', u2) +
  task(3, 'Schreibe zwei eigene Sätze auf.', u3))

# ---------------- Blatt 3: Komma-Wächter ----------------
c1 = ['Ich glaube dass du gewinnst.', 'Das Kind lacht laut.', 'Lea hofft dass die Sonne scheint.', 'Wir besuchen das Museum.',
      'Der Lehrer sagt dass wir leise sein sollen.', 'Der Hund frisst das Futter.', 'Wir wissen dass Hunde gern spielen.',
      'Das Wetter ist heute schön.', 'Es ist toll dass du mitkommst.', 'Emma holt das Brot vom Bäcker.', 'Mir gefällt dass ihr teilt.', 'Im Garten steht das Zelt.']
def sig(s): return re.sub(r'\b(dass|[Dd]as)\b', lambda m: col(m.group(1)), s)
v1 = '<div class="list komma">' + ''.join(f'<p><span class="t">{sig(s)}</span></p>' for s in c1) + '</div>'
c2 = ['Jonas merkt dass sein Schuh offen ist.', 'Das macht mir Spaß.', 'Ich bin froh dass heute Freitag ist.']
v2 = ''.join(f'<div class="wr"><span>{sig(s)}</span></div>{L("f")}' for s in c2)
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Komma-Wächter', 'Komma-Wächter',
  f'Steht in einem Satz {D2("dass")} mit zwei s? Dann gehört direkt davor ein <b>Komma</b>: Ich hoffe<b>,</b> {D2("dass")} du kommst. Der Artikel {D1("das")} braucht kein Komma: Ich lese {D1("das")} Buch.',
  task(1, 'Hier fehlen Kommas. Setze sie mit einem bunten Stift. Achtung: Sechs Sätze brauchen kein Komma!', v1) +
  task(2, 'Schreibe die Sätze richtig ab. Vergiss das Komma nicht, wenn eins fehlt.', v2))

# ---------------- Blatt 4: Wort-Detektiv ----------------
d = ['___ Pferd steht auf der Wiese.', 'Ich weiß, ___ Wale keine Fische sind.', '___ gefällt mir gut.', 'Das Kind, ___ dort winkt, ist mein Bruder.',
     'Mila schneidet ___ Papier.', 'Hast du ___ gehört?', 'Die Lehrerin hofft, ___ alle pünktlich sind.', 'Ich suche das Heft, ___ ich gestern gekauft habe.',
     '___ glaube ich dir nicht.', 'Am Abend wird ___ Licht ausgemacht.', 'Im Hafen liegt ein Schiff, ___ morgen abfährt.', 'Es stimmt, ___ Igel Winterschlaf halten.',
     'Wir schmücken ___ Klassenzimmer.', 'Mein Opa hat ein Auto, ___ sehr alt ist.', '___ kann jeder lernen.', 'Ben erzählt, ___ er einen Fuchs gesehen hat.',
     'Wer hat ___ gesagt?', 'Wir essen das Gemüse, ___ im Garten wächst.', '___ kleine Küken piept.', 'Wir wünschen dir, ___ du schnell gesund wirst.']
abc = '<span class="abc"><i>A</i><i>P</i><i>R</i><i>B</i></span>'
w1 = '<div class="key"><span><b>A</b> = Artikel</span><span><b>P</b> = Pronomen</span><span><b>R</b> = Relativpronomen</span><span><b>B</b> = Bindewort</span></div>' + \
     '<div class="list tight">' + ''.join(f'<p><span class="t">{gap(s)}</span>{abc}</p>' for s in d) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Wort-Detektiv', 'Wort-Detektiv',
  f'{D1("das")} kann ein <b>Artikel</b> sein ({D1("das")} Haus), ein <b>Pronomen</b> ({D1("Das")} gefällt mir.) oder ein <b>Relativpronomen</b> (das Buch, {D1("das")} ich lese). {D2("dass")} ist ein <b>Bindewort</b>: Ich hoffe, {D2("dass")} du kommst.',
  task(1, f'Setze {D1("das")} oder {D2("dass")} ein. Welche Aufgabe hat das Wort? Male den passenden Kreis an.', w1))

# ---------------- Blatt 5: Lücken-Geschichten ----------------
texts = [('Im Zoo', 'Heute gehen wir in den Zoo. Ich hoffe, [dass] die Affen wach sind. Zuerst sehen wir [das] Zebra. Mein Bruder ruft, [dass] er Hunger hat. Also kaufen wir ein Eis, [das] nach Erdbeere schmeckt. [Das] finden wir beide lecker.'),
  ('Im Schwimmbad', 'Am Samstag fahre ich ins Schwimmbad. Mama sagt, [dass] ich die Badehose einpacken soll. Ich nehme auch [das] Handtuch mit. Im Wasser merke ich, [dass] es ziemlich kalt ist. Dann springe ich von einem Brett, [das] ganz oben ist. Ich bin stolz, [dass] ich mich getraut habe.'),
  ('Unser Kaninchen', 'Wir haben ein Kaninchen, [das] Flocke heißt. Jeden Morgen fülle ich [das] Wasser nach. Ich weiß, [dass] Flocke gern Möhren frisst. Papa meint, [dass] der Stall zu klein ist. Deshalb bauen wir ein Gehege, [das] viel Platz hat.'),
  ('Omas Geburtstag', 'Morgen hat Oma Geburtstag. Ich glaube, [dass] sie sich über Blumen freut. Meine Schwester malt [das] Bild für die Karte. Wir hoffen, [dass] Oma nichts merkt. Die Geschenke liegen in einem Zimmer, [das] Oma nie benutzt. Es ist schön, [dass] wir zusammen feiern.')]
BR = re.compile(r'\[(\w+)\]')
x1 = ''.join(f'<div class="story"><h3>{t}</h3><p>{BR.sub(G, s)}</p></div>' for t, s in texts)
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Lücken-Geschichten', 'Lücken-Geschichten', MERK + f' Vor {D2("dass")} steht ein Komma.',
  task(1, f'Setze {D1("das")} oder {D2("dass")} in die Lücken ein.', x1) +
  task(2, 'Zähle nach: Wie oft hast du jedes Wort eingesetzt? (Gleich oft!)', u2))

# ---------------- Blatt 6: Schreib-Profi ----------------
e = ['Ich weiß, [dass] [das] Kind müde ist.', 'Mama sagt, [dass] [das] Essen fertig ist.', 'Es kann sein, [dass] [das] Paket morgen kommt.',
     '[Dass] [das] nicht stimmt, weiß ich schon lange.', 'Er hofft, [dass] ihm [das] Geschenk gefällt.', '[Das] freut mich, [dass] du gewonnen hast.',
     '[Das] Gewitter war so laut, [dass] ich aufgewacht bin.', '[Das] Pferd, [das] dort grast, gehört Lena.', '[Dass] du mir hilfst, finde ich toll.',
     'Es regnet so stark, [dass] wir drinnen bleiben.', 'Er geht, ohne [dass] er sich verabschiedet.', 'Pass auf, [dass] du nicht hinfällst!',
     'Weißt du, [dass] Delfine Säugetiere sind?', 'Ich bin sicher, [dass] sie die Wahrheit sagt.', 'Weil [das] Seil zu kurz war, holten wir ein neues.',
     'Kannst du mir [das] noch einmal erklären?', 'Sie nimmt den Füller und legt [das] Mäppchen dazu.', 'Das Märchen, [das] Oma vorliest, kenne ich schon.',
     'Zeig mir bitte das Bild, [das] du gemalt hast.', '[Das] hätte ich nie gedacht!']
y1 = '<div class="list tight b6">' + ''.join(f'<p><span class="t">{BR.sub(G, s)}</span></p>' for s in e) + '</div>'
err = 'Ich glaube, das wir morgen einen Ausflug machen. Dass Wetter soll schön werden. Mama sagt, dass ich das Fernglas mitnehmen darf. Wir fahren zu einem Schloss, dass auf einem Berg steht. Ich hoffe, das es dort auch Ritter gibt.'
p6 = page('Blatt 6', 'Für Profis', 3, 'Schreib-Profi', 'Schreib-Profi', '',
  task(1, f'Schreibe {D1("das")} oder {D2("dass")} in jede Lücke. Mach bei jeder Lücke die Probe. Am Satzanfang schreibst du groß!', y1) +
  task(2, 'Fehler-Detektiv: In diesem Text sind vier Wörter falsch geschrieben. Streiche sie durch und schreibe sie richtig darüber.', f'<div class="err">{err}</div>'))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def fills(sents, answers): return ' · '.join(solved(s, a) for s, a in zip(sents, answers))
def br(s): return BR.sub(lambda m: col(m.group(1)), s)
l1 = sol(1, 'Proben-Lupe',
  '<p><b>Aufgabe 1:</b> ' + fills([s for s, _ in a1], ['das', 'dass', 'das', 'dass', 'Das', 'dass']) + ' – Die Probe klingt bei Satz 1, 3 und 5 richtig, bei Satz 2, 4 und 6 falsch.</p>' +
  '<p><b>Aufgabe 2:</b> ' + fills(a2, ['Das', 'dass', 'das', 'dass', 'das', 'dass', 'dass', 'das', 'dass']) + '</p>')
l2 = sol(2, 'Zwei Körbe',
  '<p><b>Aufgabe 1:</b> ' + fills(b1, ['Das', 'dass', 'das', 'dass', 'das', 'dass', 'Das', 'dass', 'Das', 'dass', 'das', 'dass', 'das', 'dass', 'das']) + '</p>' +
  f'<p><b>Aufgabe 2:</b> {D1("das")}: 8-mal · {D2("dass")}: 7-mal</p><p><b>Aufgabe 3:</b> Eigene Sätze, zum Beispiel: Ich füttere {D1("das")} Pferd. · Ich hoffe, {D2("dass")} es morgen schneit.</p>')
full3 = ['Ich glaube, dass du gewinnst.', 'Lea hofft, dass die Sonne scheint.', 'Der Lehrer sagt, dass wir leise sein sollen.', 'Wir wissen, dass Hunde gern spielen.', 'Es ist toll, dass du mitkommst.', 'Mir gefällt, dass ihr teilt.']
l3 = sol(3, 'Komma-Wächter',
  '<p><b>Aufgabe 1:</b> <b>Mit Komma:</b> ' + ' · '.join(sig(s) for s in full3) + '</p><p><b>Ohne Komma:</b> ' + ' · '.join(sig(s) for s in c1 if 'dass' not in s) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(sig(s) for s in ['Jonas merkt, dass sein Schuh offen ist.', 'Das macht mir Spaß.', 'Ich bin froh, dass heute Freitag ist.']) + '</p>')
ans4 = [('Das', 'A'), ('dass', 'B'), ('Das', 'P'), ('das', 'R'), ('das', 'A'), ('das', 'P'), ('dass', 'B'), ('das', 'R'), ('Das', 'P'), ('das', 'A'),
        ('das', 'R'), ('dass', 'B'), ('das', 'A'), ('das', 'R'), ('Das', 'P'), ('dass', 'B'), ('das', 'P'), ('das', 'R'), ('Das', 'A'), ('dass', 'B')]
l4 = sol(4, 'Wort-Detektiv', '<p>' + ' · '.join(f'{solved(s, a)} <b>({j})</b>' for s, (a, j) in zip(d, ans4)) + '</p>')
l5 = sol(5, 'Lücken-Geschichten', ''.join(f'<p><b>{t}:</b> {br(s)}</p>' for t, s in texts) + f'<p><b>Aufgabe 2:</b> {D1("das")}: 10-mal · {D2("dass")}: 10-mal</p>')
fixed = f'Ich glaube, {D2("dass")} wir morgen einen Ausflug machen. {D1("Das")} Wetter soll schön werden. Mama sagt, dass ich das Fernglas mitnehmen darf. Wir fahren zu einem Schloss, {D1("das")} auf einem Berg steht. Ich hoffe, {D2("dass")} es dort auch Ritter gibt.'
l6 = sol(6, 'Schreib-Profi', '<p><b>Aufgabe 1:</b> ' + ' · '.join(br(s) for s in e) + '</p><p><b>Aufgabe 2:</b> ' + fixed + '</p>')
psA = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 4', '', '', l1 + l2 + l3 + l4, solution=True)
psB = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 5 und 6', '', '', l5 + l6, solution=True)

write('das-oder-dass', 'Übungsblätter: das oder dass? (Klasse 4)', [p1, p2, p3, p4, p5, p6, psA, psB], extra_css=EXTRA)
