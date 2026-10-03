"""Übungsblätter Zeitformen der Verben."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

PR, PT, PF, FU = [(lambda c: (lambda s: f'<span class="{c}">{s}</span>'))(c) for c in ('pr', 'pt', 'pf', 'fu')]
NAMES = [('pr', 'Präsens'), ('pt', 'Präteritum'), ('pf', 'Perfekt'), ('fu', 'Futur')]
EXTRA = '''
.pr{color:#1F57C3;font-weight:700}.pt{color:#14713C;font-weight:700}.pf{color:#C22A63;font-weight:700}.fu{color:#5B34B0;font-weight:700}
.bpr{--c:#2B6BE0}.bpt{--c:#1A8C4B}.bpf{--c:#DE3A76}.bfu{--c:#7A4FD8}
.tick{width:100%;border-collapse:collapse;font-size:12.5pt;table-layout:fixed}
.tick th{font-family:'Grandstander',sans-serif;font-size:9.5pt;color:#fff;background:var(--c);padding:1mm 0;width:20mm;border-left:.6mm solid #fff}
.tick th:first-child{background:none;width:auto}
.tick td{height:10.4mm;border-bottom:.35mm solid #B8C4D6;padding:0 1mm;white-space:nowrap}
.tick td.b{text-align:center}
.cb{display:inline-block;width:5.5mm;height:5.5mm;border:.55mm solid #22304A;border-radius:1.2mm;vertical-align:middle}
.rows p{margin:0;height:11.6mm;display:flex;align-items:flex-end;gap:2mm;font-size:13.5pt;white-space:nowrap}
.rows .line{flex:1;width:auto;min-width:24mm}
.rows .fix{flex:none;width:31mm;min-width:0}
.rows .plus{color:#56657F;font-weight:700}
.rows .emo{align-self:center}
.full p{margin:0;font-size:13.5pt;line-height:1.25}
.full .to{font-size:11pt;color:#56657F}
.full .line.f{height:8.6mm;margin-bottom:2.6mm}
.vt{width:100%;border-collapse:collapse;font-size:13pt}
.vt th{font-family:'Grandstander',sans-serif;font-size:11.5pt;color:#fff;background:var(--c);padding:1mm 3mm;text-align:left;border-left:.6mm solid #fff}
.vt td{height:10.2mm;border-bottom:.4mm solid #56657F;border-left:.4mm solid #B8C4D6;padding:0 3mm;font-weight:700}
.vt td:first-child,.vt th:first-child{border-left:none}
.pick{display:inline-block;border:.5mm solid #22304A;border-radius:99px;padding:0 3mm;margin:0 1mm;font-weight:700;font-size:12pt;line-height:1.5}
.rule h3{white-space:nowrap}
.rule h3 small{font-size:8.5pt}
.picks p{margin:0;height:8.8mm;font-size:13.5pt;display:flex;align-items:center}
.rule .wr{gap:1.2mm}
.rule .wr .line{min-width:10mm}
.rule .wr .line.w2{flex:1.7}
'''
def split(s):
    """'Der Hund *hat den Ball *geholt.' -> Satz ohne Sternchen"""
    return s.replace('*', '')
def ticks(rows):
    head = '<tr><th></th>' + ''.join(f'<th class="b{k}">{n}</th>' for k, n in NAMES) + '</tr>'
    return '<table class="tick">' + head + ''.join(f'<tr><td><span class="emo">{e}</span>{s}</td>' + '<td class="b"><span class="cb"></span></td>' * 4 + '</tr>' for e, s in rows) + '</table>'

# ---------------- Blatt 1 ----------------
t1 = [('📞', 'Jetzt klingelt das Telefon.'), ('❄️', 'Gestern schneite es den ganzen Tag.'), ('⚽', 'Gestern hat Lea ein Tor geschossen.'), ('🚗', 'Morgen wird Oma uns abholen.'),
      ('🚜', 'Früher wohnte Opa auf einem Bauernhof.'), ('🐕', 'Gerade bellt der Hund laut.'), ('🎂', 'Bald wird Jonas seinen Geburtstag feiern.'), ('🏖️', 'Letzten Sommer sind wir ans Meer gereist.')]
t2 = [('🚲', 'Heute putzt Papa das Fahrrad.'), ('🐈', 'Vorhin hat die Katze eine Maus gefangen.'), ('🚌', 'Nächste Woche werden wir einen Ausflug machen.'), ('🏡', 'Letzte Woche besuchte Mia ihre Tante.'),
      ('⏰', 'Am Sonntag ist Tom früh aufgestanden.'), ('🌧️', 'Im Moment regnet es stark.'), ('🏫', 'Vor einem Jahr war Ben in der dritten Klasse.')]
r2 = '<div class="rows">' + ''.join(f'<p><span class="emo">{e}</span>{s} {L()}</p>' for e, s in t2) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Zeit-Sortierer', 'Zeit-Sortierer',
  f'Schau auf das <b>Verb</b>! Ein Teil: {PR("Präsens")} (er spielt) oder {PT("Präteritum")} (er spielte). Zwei Teile: {PF("Perfekt")} (er hat gespielt) oder {FU("Futur")} (er wird spielen).',
  task(1, 'In welcher Zeitform steht der Satz? Unterstreiche das Verb und kreuze an.', ticks(t1)) +
  task(2, 'Unterstreiche alle Teile des Verbs. Schreibe die Zeitform auf die Linie.', r2))

# ---------------- Blatt 2 ----------------
left = [('💃', 'tanzen'), ('🏊', 'schwimmen'), ('👂', 'hören'), ('🪑', 'sitzen'), ('📣', 'rufen'), ('🛁', 'baden'), ('🐎', 'reiten'), ('🤔', 'denken')]
right = ['er rief', 'er badete', 'er tanzte', 'er dachte', 'er schwamm', 'er ritt', 'er hörte', 'er saß']
connect = '<div class="connect">' + ''.join(f'<div class="row"><span class="l"><span class="emo">{e}</span><b>{w}</b></span><span class="dot"></span><span class="gap"></span><span class="dot"></span><span class="r">{PT(r)}</span></div>' for (e, w), r in zip(left, right)) + '</div>'
write2 = [('😢', 'weinen'), ('💭', 'träumen'), ('🔢', 'zählen'), ('🧍', 'stehen'), ('🛏️', 'liegen'), ('🥶', 'frieren'), ('⛏️', 'graben')]
wr2 = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="emo">{e}</span><b>{w}</b> <span class="arr">→</span> {PT("er")} {L()}</div>' for e, w in write2) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Verb-Memory', 'Verb-Memory',
  f'Das {PT("Präteritum")} erzählt, was <b>früher</b> war. Viele Verben bekommen ein <b>-te</b>: tanzen → er tanzte. Manche verändern sich stärker: schwimmen → er schwamm.',
  task(1, 'Was gehört zusammen? Verbinde Grundform und Präteritum mit einer Linie.', connect) +
  task(2, 'Schreibe das Präteritum auf.', wr2))

# ---------------- Blatt 3 ----------------
a3 = [('🐕', 'Der Hund hat den Ball geholt.'), ('🔧', 'Papa wird das Regal reparieren.'), ('🌲', 'Wir sind durch den Wald gewandert.'), ('✉️', 'Ich werde dir einen Brief schicken.'),
      ('🧹', 'Ich habe mein Zimmer aufgeräumt.'), ('🧩', 'Du wirst das Rätsel bestimmt lösen.'), ('🚆', 'Der Zug ist pünktlich angekommen.'), ('🐦', 'Die Vögel werden bald nach Süden ziehen.')]
tk3 = '<table class="tick"><tr><th></th><th class="bpf">Perfekt</th><th class="bfu">Futur</th></tr>' + ''.join(
  f'<tr><td><span class="emo">{e}</span>{s}</td>' + '<td class="b"><span class="cb"></span></td>' * 2 + '</tr>' for e, s in a3) + '</table>'
b3 = [('🏰', 'Emma hat eine Sandburg gebaut.'), ('🍰', 'Wir werden einen Kuchen backen.'), ('🎵', 'Die Kinder haben ein Lied geübt.'), ('🎭', 'Die Klasse wird ein Theaterstück proben.'),
      ('🚗', 'Mama hat das Auto geparkt.'), ('🐹', 'Nina wird ihren Hamster füttern.'), ('🏃', 'Du bist sehr schnell gerannt.')]
r3 = '<div class="rows">' + ''.join(f'<p><span class="emo">{e}</span>{s} {L("fix")}<span class="plus">+</span>{L("fix")}</p>' for e, s in b3) + '</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Zwei-Teile-Detektiv', 'Zwei-Teile-Detektiv',
  f'Im {PF("Perfekt")} und im {FU("Futur")} hat das Verb <b>zwei Teile</b>. Der zweite Teil steht am Satzende: Der Hund {PF("hat")} den Ball {PF("geholt")}. Der Hund {FU("wird")} den Ball {FU("holen")}.',
  task(1, 'Kreise die zwei Teile des Verbs ein. Kreuze an: Perfekt oder Futur?', tk3) +
  task(2, 'Schreibe die zwei Teile des Verbs auf die Linien.', r3))

# ---------------- Blatt 4 ----------------
s4 = [('Die Kinder spielen im Garten.', 'pt'), ('Mia isst einen Apfel.', 'pf'), ('Der Bus kam um acht Uhr.', 'fu'), ('Wir werden laut lachen.', 'pr'),
      ('Opa hat die Zeitung gelesen.', 'pt'), ('Jonas geht zur Schule.', 'pf')]
nm = dict(NAMES)
f4 = '<div class="full">' + ''.join(f'<p>{s} <span class="to">→ Reiseziel:</span> <span class="{k}">{nm[k]}</span></p>{L("f")}' for s, k in s4) + '</div>'
tab4 = [('er schläft', '', '', ''), ('', 'sie kochte', '', ''), ('', '', 'er ist gefallen', ''), ('', '', '', 'sie wird fahren'), ('er sieht', '', '', ''), ('', 'sie kaufte', '', '')]
cls = ['pr', 'pt', 'pf', 'fu']
v4 = '<table class="vt"><tr>' + ''.join(f'<th class="b{k}">{n}</th>' for k, n in NAMES) + '</tr>' + ''.join(
  '<tr>' + ''.join(f'<td class="{cls[i]}">{c}</td>' for i, c in enumerate(row)) + '</tr>' for row in tab4) + '</table>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Zeitmaschine', 'Zeitmaschine',
  f'Ein Satz kann in jede Zeit reisen. Dabei ändert sich nur das <b>Verb</b>: sie {PR("lacht")} – sie {PT("lachte")} – sie {PF("hat gelacht")} – sie {FU("wird lachen")}.',
  task(1, 'Schicke jeden Satz in die Zeitmaschine. Schreibe ihn in der neuen Zeitform auf.', f4) +
  task(2, 'Ergänze die fehlenden Zeitformen.', v4))

# ---------------- Blatt 5 ----------------
c5 = [('Der Vogel', 'auf das Dach geflogen.'), ('Oma', 'einen Kuchen gebracht.'), ('Die Schnecke', 'über den Weg gekrochen.'), ('Papa', 'das Brot geschnitten.'),
      ('Der Schnee', 'in der Sonne geschmolzen.'), ('Leo', 'mir einen Stift gegeben.'), ('Anna', 'über einen Stein gestolpert.'), ('Mama', 'den Koffer gepackt.'),
      ('Die Blume', 'sehr schnell gewachsen.'), ('Max', 'ein Gedicht gelernt.')]
pk = '<div class="picks">' + ''.join(f'<p>{a}&nbsp;<span class="pick">hat</span><span class="pick">ist</span>&nbsp;{b}</p>' for a, b in c5) + '</div>'
s5 = ['Der Frosch hüpft in den Teich.', 'Jana wäscht ihre Hände.', 'Das Flugzeug landet pünktlich.']
f5 = '<div class="full">' + ''.join(f'<p>{s}</p>{L("f")}' for s in s5) + '</div>'
w5 = ['er trägt', 'sie bastelt', 'er platzt', 'er verschwindet']
wr5 = '<div class="grid2">' + ''.join(f'<div class="wr">{PR(w)} <span class="arr">→</span> {L()}</div>' for w in w5) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Perfekt-Baukasten', 'Perfekt-Baukasten',
  f'Das {PF("Perfekt")} hat zwei Teile: <b>hat</b> oder <b>ist</b> und das <b>Partizip</b>. Die meisten Verben brauchen <b>hat</b>. Bei Bewegung von Ort zu Ort oder bei einer Veränderung heißt es <b>ist</b>.',
  task(1, 'hat oder ist? Kreise das richtige Hilfsverb ein.', pk) +
  task(2, 'Schreibe den Satz im Perfekt auf.', f5) +
  task(3, 'Schreibe das Perfekt auf, zum Beispiel: er lacht → er hat gelacht.', wr5))

# ---------------- Blatt 6 ----------------
rules = [('ei – ie – ie', 'schweigen – schwieg – hat geschwiegen', ['bleiben', 'schreiben', 'steigen', 'scheinen', 'leihen']),
         ('i – a – u', 'klingen – klang – hat geklungen', ['finden', 'singen', 'trinken', 'sinken', 'binden']),
         ('e – a – o', 'stehlen – stahl – hat gestohlen', ['helfen', 'nehmen', 'sprechen', 'treffen', 'werfen']),
         ('ie – o – o', 'schießen – schoss – hat geschossen', ['verlieren', 'schließen', 'gießen', 'riechen', 'schieben'])]
rb = '<div class="rules">' + ''.join(f'<div class="rule k5"><h3>{h}<small>{s}</small></h3>' + ''.join(f'<div class="wr"><b>{w}</b> – {L()} – {L("w2")}</div>' for w in ws) + '</div>' for h, s, ws in rules) + '</div>'
det = '<div class="grid2">' + ''.join(f'<div class="wr"><s>{w}</s> <span class="arr">→</span> {L()}</div>' for w in ['er bleibte', 'sie hat gesingt', 'er helfte', 'sie hat geschließt']) + '</div>'
s6 = ['Lina findet einen Schlüssel.', 'Der Hund riecht die Wurst.', 'Tom wirft den Ball.']
sn6 = '<div class="sents two">' + ''.join(f'<p>{s} <span class="arr">→</span> {L()}</p>' for s in s6) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Verb-Meister', 'Verb-Meister', '',
  task(1, f'Vier Muster für starke Verben: Schreibe das {PT("Präteritum")} und das {PF("Perfekt")} (mit hat oder ist) auf.', rb) +
  task(2, 'Fehler-Detektiv: Diese Formen sind falsch. Schreibe sie richtig auf.', det) +
  task(3, 'Setze den Satz ins Präteritum.', sn6))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
l1 = sol(1, 'Zeit-Sortierer', f'<p><b>Aufgabe 1:</b> klingelt: {PR("Präsens")} · schneite: {PT("Präteritum")} · hat … geschossen: {PF("Perfekt")} · wird … abholen: {FU("Futur")} · wohnte: {PT("Präteritum")} · bellt: {PR("Präsens")} · wird … feiern: {FU("Futur")} · sind … gereist: {PF("Perfekt")}</p>'
  f'<p><b>Aufgabe 2:</b> putzt: {PR("Präsens")} · hat … gefangen: {PF("Perfekt")} · werden … machen: {FU("Futur")} · besuchte: {PT("Präteritum")} · ist … aufgestanden: {PF("Perfekt")} · regnet: {PR("Präsens")} · war: {PT("Präteritum")}</p>')
l2 = sol(2, 'Verb-Memory', '<p><b>Aufgabe 1:</b> tanzen – er tanzte · schwimmen – er schwamm · hören – er hörte · sitzen – er saß · rufen – er rief · baden – er badete · reiten – er ritt · denken – er dachte</p>'
  '<p><b>Aufgabe 2:</b> er weinte · er träumte · er zählte · er stand · er lag · er fror · er grub</p>')
l3 = sol(3, 'Zwei-Teile-Detektiv', f'<p><b>Aufgabe 1:</b> {PF("Perfekt:")} hat … geholt · sind … gewandert · habe … aufgeräumt · ist … angekommen. {FU("Futur:")} wird … reparieren · werde … schicken · wirst … lösen · werden … ziehen.</p>'
  '<p><b>Aufgabe 2:</b> hat + gebaut · werden + backen · haben + geübt · wird + proben · hat + geparkt · wird + füttern · bist + gerannt</p>')
l4 = sol(4, 'Zeitmaschine', '<p><b>Aufgabe 1:</b> Die Kinder spielten im Garten. · Mia hat einen Apfel gegessen. · Der Bus wird um acht Uhr kommen. · Wir lachen laut. · Opa las die Zeitung. · Jonas ist zur Schule gegangen.</p>'
  '<p><b>Aufgabe 2:</b> er schläft – er schlief – er hat geschlafen – er wird schlafen · sie kocht – sie kochte – sie hat gekocht – sie wird kochen · er fällt – er fiel – er ist gefallen – er wird fallen · '
  'sie fährt – sie fuhr – sie ist gefahren – sie wird fahren · er sieht – er sah – er hat gesehen – er wird sehen · sie kauft – sie kaufte – sie hat gekauft – sie wird kaufen</p>')
l5 = sol(5, 'Perfekt-Baukasten', '<p><b>Aufgabe 1:</b> <b>ist:</b> geflogen, gekrochen, geschmolzen, gestolpert, gewachsen. <b>hat:</b> gebracht, geschnitten, gegeben, gepackt, gelernt.</p>'
  '<p><b>Aufgabe 2:</b> Der Frosch ist in den Teich gehüpft. · Jana hat ihre Hände gewaschen. · Das Flugzeug ist pünktlich gelandet.</p>'
  '<p><b>Aufgabe 3:</b> er hat getragen · sie hat gebastelt · er ist geplatzt · er ist verschwunden</p>')
l6 = sol(6, 'Verb-Meister', '<p><b>Aufgabe 1:</b> blieb – ist geblieben · schrieb – hat geschrieben · stieg – ist gestiegen · schien – hat geschienen · lieh – hat geliehen · fand – hat gefunden · sang – hat gesungen · trank – hat getrunken · sank – ist gesunken · band – hat gebunden · '
  'half – hat geholfen · nahm – hat genommen · sprach – hat gesprochen · traf – hat getroffen · warf – hat geworfen · verlor – hat verloren · schloss – hat geschlossen · goss – hat gegossen · roch – hat gerochen · schob – hat geschoben</p>'
  '<p><b>Aufgabe 2:</b> er blieb · sie hat gesungen · er half · sie hat geschlossen</p><p><b>Aufgabe 3:</b> Lina fand einen Schlüssel. · Der Hund roch die Wurst. · Tom warf den Ball.</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

write('zeitformen', 'Übungsblätter: Zeitformen der Verben (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps], extra_css=EXTRA)
