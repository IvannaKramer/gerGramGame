"""Übungsblätter Das Komma."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

A, N = (lambda s: f'<span class="ka">{s}</span>'), (lambda s: f'<span class="kn">{s}</span>')
CM = '<b class="cm">,</b>'
BINDS = 'weil dass wenn als ob'.split()
def bare(s): return re.sub(r'[,{}]', '', s)                       # Satz ohne Kommas und ohne Markierung
def blue(s, commas=False): return re.sub(r'\{([^}]+)\}', lambda m: A(m.group(1)), s if commas else s.replace(',', ''))
def sol(s, verb=False):                                             # Lösung: Kommas gelb, einleitende Bindewörter lila, auf Wunsch Verb des Nebensatzes unterstrichen
    out, prev = [], True
    has = ',' in s
    w = re.sub(r'[{}]', '', s).split(' ')
    v = -1 if not verb else next(i for i, x in enumerate(w) if x.endswith(',')) if w[0].lower() in BINDS else len(w) - 1
    for i, x in enumerate(w):
        t = x.rstrip(',')
        if i == v: t = re.sub(r'^([^.!?]+)', r'<u>\1</u>', t)
        out.append((N(t) if has and prev and t.lower() in BINDS else t) + (CM if x.endswith(',') else ''))
        prev = x.endswith(',')
    return ' '.join(out)
def lst(items, cls=''): return f'<div class="list {cls}">' + ''.join(f'<p><span class="t">{i}</span></p>' for i in items) + '</div>'
def copy(items): return ''.join(f'<div class="wr"><span class="sp">{i}</span></div>{L("f")}' for i in items)

MERK_A = f'Bei einer {A("Aufzählung")} steht zwischen den Teilen ein <b>Komma</b>: Äpfel{CM} Birnen und Kiwis. Vor <b>und</b> oder <b>oder</b> steht kein Komma.'
MERK_N = f'Ein {N("Nebensatz")} beginnt mit einem {N("Bindewort")}: weil, dass, wenn, als, ob. Sein <b>Verb</b> steht am Ende. Zwischen Hauptsatz und Nebensatz steht ein <b>Komma</b>: Ich friere{CM} {N("weil")} es kalt <u>ist</u>.'

EXTRA = '''
.ka{color:#1F57C3;font-weight:700}.kn{color:#6A3FC8;font-weight:700}
.cm{color:#C77700;font-weight:700;font-size:1.25em;line-height:.8}
u{text-decoration-thickness:.5mm;text-underline-offset:1mm}
.list p{margin:0;height:8.5mm;display:flex;align-items:flex-end;font-size:13.5pt;white-space:nowrap}
.list .t,.sp{word-spacing:.35em}
.list.h9 p{height:9mm}
.list.h8 p{height:8mm}
.list.h76 p{height:7.4mm;font-size:12.5pt}
.list.wrap p{height:auto;min-height:7.5mm;white-space:normal;font-size:12pt;line-height:1.25;padding-top:1.5mm;align-items:flex-end}
.list.wrap .t{word-spacing:.25em}
.wr .sp{white-space:nowrap}
.binds{display:flex;gap:3mm;align-items:center;font-size:11.5pt;margin:-1mm 0 2mm;color:#56657F}
.binds b{background:#EEE7FF;color:#22304A;border-radius:99px;padding:0 3mm}
.bx{display:inline-block;width:5mm;height:6mm;border:.45mm solid #22304A;border-radius:1.2mm;vertical-align:-1.2mm;margin:0 1.2mm}
.count{display:flex;gap:12mm;font-size:13.5pt;align-items:flex-end;height:10mm}
.count .line{width:16mm}
.bau p{margin:0;height:10.4mm;display:flex;align-items:flex-end;gap:2mm;font-size:13pt;white-space:nowrap}
.bau .line{flex:1;width:auto;min-width:30mm}
.bau .j{color:#56657F;font-size:11.5pt}
.abc{margin-left:auto;display:inline-flex;gap:2mm;align-self:center}
.abc i{font-style:normal;font-family:'Grandstander',sans-serif;font-weight:800;font-size:9.5pt;width:6mm;height:6mm;border:.45mm solid #22304A;border-radius:50%;display:grid;place-items:center}
.key{display:flex;gap:6mm;font-size:11pt;margin:-1mm 0 2mm;flex-wrap:wrap}
.key b{font-family:'Grandstander',sans-serif}
.num{margin-left:auto;flex:none;width:8mm;height:6.4mm;border:.45mm solid #22304A;border-radius:1.5mm;align-self:flex-end}
.sol .solb p{margin-bottom:1mm}
'''

# ---------------- Blatt 1: Komma-Klick ----------------
a1 = ['Im Zoo sehen wir {Affen}, {Löwen} und {Zebras}.', '{Lena} und {Paul} gehen ins Kino.', 'Ich kaufe {Äpfel}, {Birnen} und {Bananen}.',
      '{Mia}, {Tom} und {Ali} spielen Fußball.', 'Der Hund ist {klein}, {braun} und {frech}.', 'Ich trinke gern {Milch} oder {Kakao}.',
      'Wir {singen}, {tanzen} und {lachen}.', 'Heute ist es {kalt}, {nass} und {windig}.', 'Zum Frühstück gibt es {Brot}, {Käse}, {Eier} und {Saft}.',
      'Der Ball ist {rund} und {bunt}.', 'Magst du lieber {Eis}, {Pudding} oder {Kuchen}?', 'Oma backt {Kuchen}, {Kekse} und {Brötchen}.']
a2 = ['Im Mäppchen sind {ein Füller}, {ein Lineal} und {ein Spitzer}.', 'Fahren wir mit {dem Bus}, {dem Zug} oder {dem Auto}?',
      'Im Blumenladen gibt es {Rosen}, {Tulpen}, {Nelken} und {Lilien}.']
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Komma-Klick', 'Komma-Klick', MERK_A,
  task(1, f'Die Teile der Aufzählung sind {A("blau")}. Setze die fehlenden Kommas mit einem bunten Stift. Achtung: Drei Sätze brauchen kein Komma!', lst([blue(s) for s in a1])) +
  task(2, 'Schreibe die Sätze ab. Setze dabei alle Kommas.', copy([bare(s) for s in a2])))

# ---------------- Blatt 2: Bindewort-Jagd ----------------
b1 = ['Ich ziehe eine Jacke an, weil es draußen kalt ist.', 'Ich hoffe, dass du morgen kommst.', 'Wir fahren ans Meer, wenn die Ferien beginnen.',
      'Ich war müde, als der Wecker klingelte.', 'Ich frage Mama, ob ich ins Kino darf.', 'Mia lacht, weil der Clown lustig ist.',
      'Papa sagt, dass wir bald essen.', 'Der Hund bellt, wenn jemand klingelt.', 'Alle klatschten, als der Zauberer kam.',
      'Tom weiß nicht, ob der Bus pünktlich kommt.', 'Wir bleiben zu Hause, weil es stark regnet.', 'Lena weiß, dass Igel Stacheln haben.']
b2 = ['Ich helfe dir, wenn du Hilfe brauchst.', 'Es war schon dunkel, als wir nach Hause gingen.', 'Wir schauen nach, ob die Katze schläft.']
bar = '<div class="binds"><span>Bindewörter:</span>' + ''.join(f'<b>{b}</b>' for b in BINDS) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Bindewort-Jagd', 'Bindewort-Jagd', MERK_N,
  task(1, 'Kreise in jedem Satz das Bindewort ein. Setze das Komma davor. Unterstreiche das Verb am Ende.', bar + lst([bare(s) for s in b1])) +
  task(2, 'Schreibe die Sätze ab. Vergiss das Komma nicht.', copy([bare(s) for s in b2])))

# ---------------- Blatt 3: Komma-Ampel ----------------
BX = '<span class="bx"></span>'
c = ['Ich mag {Hunde} [,] {Katzen} und {Pferde}.', 'Im Stall stehen {Kühe}, {Schafe} [] und {Ziegen}.', 'Ich bin froh [,] <dass> heute Samstag ist.',
     'Am Abend [] liest Papa eine Geschichte vor.', 'Das Wasser ist {klar} [,] {kalt} und {tief}.', 'Nimmst du {den Roller} [] oder {das Fahrrad}?',
     'Wir gehen rodeln [,] <wenn> genug Schnee liegt.', 'Meine Schwester [] spielt gern Klavier.', 'Wir {malen} [,] {basteln} und {kleben}.',
     'Die Suppe ist {heiß} [] und {lecker}.', 'Leo weint [,] <weil> sein Knie blutet.', 'Wir brauchen {Mehl}, {Zucker} [] und {Butter}.',
     'Auf dem Tisch stehen {Teller}, {Tassen} [,] {Gläser} und {Schüsseln}.', 'Nach dem Essen [] putzen wir die Zähne.', 'Opa fragt [,] <ob> wir Hunger haben.']
def paint(s, spot):
    s = re.sub(r'<([a-zäöüß]+)>', lambda m: N(m.group(1)), s)
    s = re.sub(r'\{([^}]+)\}', lambda m: A(m.group(1)), s)
    return re.sub(r' ?\[(,?)\] ?', spot, s)
c1 = lst([paint(s, f' {BX} ') for s in c])
c2 = f'<div class="count"><span>Komma: {L()} -mal</span><span>kein Komma: {L()} -mal</span></div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Komma-Ampel', 'Komma-Ampel',
  f'Ein <b>Komma</b> steht zwischen den Teilen einer {A("Aufzählung")} und vor einem {N("Bindewort")} wie weil, dass, wenn, als, ob. <b>Kein Komma</b> steht vor <b>und</b> oder <b>oder</b> in einer Aufzählung.',
  task(1, 'Gehört in das Kästchen ein Komma? Dann schreibe es hinein. Wenn nicht, streiche das Kästchen durch.', c1) +
  task(2, 'Zähle nach: Wie oft hast du ein Komma gesetzt? Wie oft keins?', c2) +
  task(3, 'Schreibe einen eigenen Satz mit einer Aufzählung auf.', L('f')))

# ---------------- Blatt 4: Satz-Baumeister ----------------
d1 = [('Ich gehe früh ins Bett', 'bin · weil · müde · ich', 0), ('Mama freut sich', 'wir · decken · dass · den Tisch', 0),
      ('Wir grillen im Garten', 'warm · es · bleibt · wenn', 0), ('Oma lachte laut', 'sah · sie · als · das Foto', 0),
      ('Jonas fragt', 'mitspielen · ob · darf · er', 0), ('Ich glaube', 'sagt · dass · die Wahrheit · er', 0),
      ('spielen wir im Zimmer.', 'stürmt · weil · draußen · es', 1), ('werde ich Tierärztin.', 'ich · bin · wenn · groß', 1)]
t41 = '<div class="bau">' + ''.join(
    (f'<p>{L()} <span>{h}</span> <span class="j">({j})</span></p>' if front else f'<p><span>{h}</span> {L()} <span class="j">({j})</span></p>') for h, j, front in d1) + '</div>'
d2 = ['Lisa bekommt ein Pflaster, weil sie hingefallen ist.', 'Der Trainer sagt, dass wir gut spielen.', 'Es ist schade, dass du schon gehst.',
      'Ruf mich bitte an, wenn du zu Hause bist.', 'Ich habe mich gefreut, als ich das Paket bekam.', 'Ich weiß nicht, ob sie Pizza mag.',
      'Die Lehrerin prüft, ob wir die Wörter können.', 'Sag mir bitte, ob du morgen kommst.', 'Weil ich Geburtstag habe, backt Papa einen Kuchen.',
      'Wenn du leise bist, hörst du die Vögel.', 'Als wir am See waren, sahen wir einen Frosch.', 'Als ich klein war, hatte ich ein Dreirad.']
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Satz-Baumeister', 'Satz-Baumeister',
  f'Zwischen Hauptsatz und {N("Nebensatz")} steht ein <b>Komma</b>. Der Nebensatz beginnt mit dem {N("Bindewort")}, sein <b>Verb</b> steht am Ende. Er kann auch vorn stehen: {N("Weil")} ich müde <u>bin</u>{CM} schlafe ich.',
  task(1, 'Baue den Nebensatz aus den Wörtern in der Klammer. Schreibe ihn auf die Linie. Vergiss das Komma nicht!', t41) +
  task(2, 'Setze in jedem Satz das Komma. Unterstreiche das Verb im Nebensatz.', lst([bare(s) for s in d2], 'h76')))

# ---------------- Blatt 5: Regel-Sortierer ----------------
e = [('Im Rucksack sind ein Buch, eine Flasche und ein Apfel.', 'A'), ('Ich nehme den Schirm mit, weil es gleich regnet.', 'N'),
     ('Mein Bruder und ich bauen ein Baumhaus.', 'K'), ('Wenn der Wecker klingelt, stehe ich auf.', 'N'),
     ('Der Zauberer trägt einen Hut, einen Mantel und einen Stab.', 'A'), ('Heute Nachmittag gehen wir ins Schwimmbad.', 'K'),
     ('Die Kinder rennen, hüpfen und klettern.', 'A'), ('Finn erzählt, dass er ein Reh gesehen hat.', 'N'),
     ('Willst du Saft oder Wasser trinken?', 'K'), ('Mein Zimmer ist hell, groß und gemütlich.', 'A'),
     ('Als das Licht ausging, wurde es ganz still.', 'N'), ('Der kleine Igel sucht im Laub nach Futter.', 'K'),
     ('Am Montag, Mittwoch und Freitag habe ich Sport.', 'A'), ('Niemand weiß, ob der Schatz noch dort liegt.', 'N'),
     ('Nach dem Regen scheint wieder die Sonne.', 'K'), ('Möchtest du Nudeln, Reis oder Kartoffeln?', 'A'),
     ('Die Katze schnurrt, wenn man sie streichelt.', 'N'), ('Die Lehrerin liest eine spannende Geschichte vor.', 'K'),
     ('Wir besuchen Oma, Opa, Tante Eva und Onkel Jan.', 'A'), ('Weil der See zugefroren ist, laufen wir Schlittschuh.', 'N')]
abc = '<span class="abc"><i>A</i><i>N</i><i>K</i></span>'
t5 = '<div class="key"><span><b>A</b> = Aufzählung</span><span><b>N</b> = Nebensatz</span><span><b>K</b> = kein Komma</span></div>' + \
     '<div class="list h8">' + ''.join(f'<p><span class="t">{bare(s)}</span>{abc}</p>' for s, _ in e) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Regel-Sortierer', 'Regel-Sortierer',
  f'Werden <b>drei oder mehr Teile</b> aufgezählt? Dann stehen Kommas in der {A("Aufzählung")}. Gibt es ein {N("Bindewort")} und ein Verb am Ende? Dann trennt ein Komma Haupt- und {N("Nebensatz")}. Sonst braucht der Satz kein Komma.',
  task(1, 'Setze die fehlenden Kommas. Welche Regel passt? Male den passenden Kreis an.', t5))

# ---------------- Blatt 6: Komma-Meister ----------------
f = ['Die Nachricht, dass der Zirkus kommt, freut alle Kinder.', 'Mein Bruder ist größer als ich.',
     'Ich packe Badehose, Handtuch und Sonnencreme ein, weil wir ins Freibad gehen.', 'Ob das Wetter schön wird, wissen wir erst morgen.',
     'Die Frage, ob wir gewinnen, ist noch offen.', 'Lina schwimmt so schnell wie ein Fisch.',
     'Wenn die Sonne scheint, spielen Mia, Ben, Ole und Ida draußen.', 'Ich glaube, dass er sich freut, wenn wir ihn besuchen.',
     'Im Sommer fahren Oma und Opa mit dem Zug ans Meer.', 'An dem Tag, als ich Geburtstag hatte, schneite es.',
     'Mama sagt, dass wir Milch, Eier und Mehl brauchen.', 'Als Torwart trägt Ben dicke Handschuhe.',
     'Im Herbst sammeln wir bunte Blätter, glatte Kastanien, kleine Eicheln und dicke Nüsse.', 'Dass du mir geholfen hast, finde ich sehr nett.',
     'Mein Hund bellt, wenn es klingelt, immer sehr laut.', 'Als wir im Zoo waren, sahen wir Giraffen, Elefanten und Pinguine.',
     'Heute spielen wir zuerst Fangen und dann Verstecken.', 'Weil es so heiß war, fragte ich, ob wir ein Eis bekommen.',
     'Der Clown stolpert, wackelt, fällt hin und steht lachend wieder auf.', 'Ich weiß nicht, ob ich Geige, Flöte oder Klavier lernen soll.']
t6 = '<div class="list wrap">' + ''.join(f'<p><span class="t">{bare(s)}</span><span class="num"></span></p>' for s in f) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Komma-Meister', 'Komma-Meister',
  f'Steht ein {N("Nebensatz")} mitten im Satz, braucht er zwei Kommas: Der Tag{CM} {N("als")} es schneite{CM} war schön. Vorsicht bei <b>als</b> und <b>wie</b>: Ohne Nebensatz steht kein Komma: Ich bin größer als du.',
  task(1, 'Setze alle fehlenden Kommas. Schreibe in das Kästchen, wie viele Kommas der Satz hat. Achtung: Fünf Sätze brauchen keins!', t6) +
  task(2, 'Schreibe einen eigenen Satz mit zwei Kommas.', L('f')))

# ---------------- Lösungen ----------------
def box(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def under(raw): return sol(raw, verb=True)
def solblue(s): return re.sub(r'\{([^}]+)\}', lambda m: A(m.group(1)), s).replace(',', CM)
l1 = box(1, 'Komma-Klick', '<p><b>Aufgabe 1:</b> ' + ' · '.join(solblue(s) for s in a1) + '</p><p><b>Aufgabe 2:</b> ' + ' · '.join(solblue(s) for s in a2) + '</p>')
l2 = box(2, 'Bindewort-Jagd', '<p><b>Aufgabe 1:</b> ' + ' · '.join(under(s) for s in b1) + '</p><p><b>Aufgabe 2:</b> ' + ' · '.join(under(s) for s in b2) + '</p>')
nk = sum('[,]' in s for s in c)
l3 = box(3, 'Komma-Ampel', '<p><b>Aufgabe 1:</b> ' + ' · '.join(paint(s, CM + ' ' if '[,]' in s else ' ') for s in c) + '</p>' +
         f'<p><b>Aufgabe 2:</b> Komma: {nk}-mal · kein Komma: {len(c) - nk}-mal</p><p><b>Aufgabe 3:</b> Eigener Satz, zum Beispiel: Ich spiele gern Fußball' + CM + ' Tischtennis und Federball.</p>')
full4 = ['Ich gehe früh ins Bett, weil ich müde bin.', 'Mama freut sich, dass wir den Tisch decken.', 'Wir grillen im Garten, wenn es warm bleibt.',
         'Oma lachte laut, als sie das Foto sah.', 'Jonas fragt, ob er mitspielen darf.', 'Ich glaube, dass er die Wahrheit sagt.',
         'Weil es draußen stürmt, spielen wir im Zimmer.', 'Wenn ich groß bin, werde ich Tierärztin.']
l4 = box(4, 'Satz-Baumeister', '<p><b>Aufgabe 1:</b> ' + ' · '.join(under(s) for s in full4) + '</p><p><b>Aufgabe 2:</b> ' + ' · '.join(under(s) for s in d2) + '</p>')
l5 = box(5, 'Regel-Sortierer', '<p>' + ' · '.join(f'{sol(s)} <b>({k})</b>' for s, k in e) + '</p>')
l6 = box(6, 'Komma-Meister', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{sol(s)} <b>({s.count(",")})</b>' for s in f) + '</p>' +
         f'<p><b>Aufgabe 2:</b> Eigener Satz, zum Beispiel: Die Hoffnung{CM} {N("dass")} es schneit{CM} ist groß. · Ich kaufe Brot{CM} Käse und Obst{CM} {N("weil")} wir picknicken.</p>')
psA = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 4', '', '', l1 + l2 + l3 + l4, solution=True)
psB = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 5 und 6', '', '', l5 + l6, solution=True)

write('komma', 'Übungsblätter: Das Komma (Klasse 4)', [p1, p2, p3, p4, p5, p6, psA, psB], extra_css=EXTRA)
