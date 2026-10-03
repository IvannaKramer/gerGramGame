"""Übungsblätter Subjekt, Prädikat und Objekte."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

NAME = {'P': 'Prädikat', 'S': 'Subjekt', 'D': 'Dativobjekt', 'A': 'Akkusativobjekt', 'Z': 'Zeit', 'O': 'Ort'}
ASK = {'S': 'Wer oder was', 'D': 'Wem', 'A': 'Wen oder was', 'Z': 'Wann', 'O': 'Wo'}
PRON = ['ihm', 'ihn', 'ihr', 'mir', 'mich', 'dir', 'dich']
cap = lambda s: s[0].upper() + s[1:]
R = lambda r, s: f'<b class="r{r}">{s}</b>'

def S(*chunks):
    """Ein Satz: Satzglieder wie im Spiel als 'Text|Art' (dritte Angabe = falsch angezeigte Art auf Blatt 6)."""
    out = []
    for i, c in enumerate(chunks):
        t, r, *shown = c.split('|')
        out.append({'t': t, 'r': r, 'shown': shown[0] if shown else None, 'text': cap(t) if i == 0 else t})
    return out
plain = lambda s: ' '.join(p['text'] for p in s) + '.'
colored = lambda s, roles='PSDAZO': ' '.join(R(p['r'], p['text']) if p['r'] in roles else p['text'] for p in s) + '.'
answer = lambda s, r: ' … '.join(p['t'] for p in s if p['r'] == r)
def ask(s, r):
    P = [p['t'] for p in s if p['r'] == 'P']
    rest = [p for p in s if p['r'] not in ('P', r)]
    rest.sort(key=lambda p: 0 if p['r'] == 'S' else 1 if p['t'] in PRON else 2 + 'ZDO-A'.index(p['r']))
    return ' '.join([ASK[r], P[0]] + [p['t'] for p in rest] + P[1:]) + '?'
abc = lambda i: f'<span class="num">{chr(97 + i)})</span>'

EXTRA = '''
.rP{color:#C22A63}.rS{color:#1F57C3}.rD{color:#147A40}.rA{color:#6A3FC8}.rZ{color:#0B7780}.rO{color:#A66A00}
.num{display:inline-block;width:8mm;font-family:'Grandstander',sans-serif;font-weight:800;color:#56657F;flex:none}
.cb{display:inline-block;width:5mm;height:5mm;border:.6mm solid #22304A;border-radius:1mm;flex:none;vertical-align:-1mm;margin:0 1.5mm 0 4mm}
.row{display:flex;align-items:center;justify-content:space-between;height:9.6mm;font-size:14pt;border-bottom:.3mm dashed #D5E3F1}
.row .ch{font-size:12pt;white-space:nowrap}
.wide{word-spacing:2.6mm}
u{text-decoration-thickness:.5mm;text-underline-offset:1.2mm}
.grid2 .row{justify-content:flex-start}
.item{margin-bottom:2mm}
.item .s{font-size:14pt;margin:0;font-weight:700}
.qa{display:flex;align-items:flex-end;gap:2mm;height:9.5mm;font-size:13.5pt;white-space:nowrap}
.qa .line{flex:1;width:auto;min-width:20mm}
.qa .line.q{flex:2}
.sq{display:inline-block;width:11mm;height:8mm;border:.6mm solid #22304A;border-radius:2mm;flex:none}
.tb{width:100%;border-collapse:collapse;font-size:13pt}
.tb th{font-family:'Grandstander',sans-serif;font-size:11.5pt;color:#fff;padding:1mm 2mm;border:.4mm solid #fff}
.tb td{border:.45mm solid #56657F;height:10.5mm;width:25%}
.tb td.full{border:none;height:7.5mm;font-weight:700;padding-top:1.5mm;vertical-align:bottom}
.bP{background:#DE3A76}.bS{background:#2B6BE0}.bD{background:#1A8C4B}.bA{background:#7A4FD8}.bZ{background:#0B8791}.bO{background:#E9A200}
.plan{display:flex;gap:2.5mm;align-items:flex-end;margin:1mm 0 3.6mm 8mm}
.pl{flex:1;border:.6mm solid var(--c);border-radius:2.5mm;overflow:hidden;height:14.5mm;max-width:46mm}
.pl i{display:block;font-style:normal;background:var(--c);color:#fff;font-size:9.5pt;font-weight:700;text-align:center;line-height:1.35}
.cP{--c:#DE3A76}.cS{--c:#2B6BE0}.cD{--c:#1A8C4B}.cA{--c:#7A4FD8}
.bank{margin:0;font-size:13.5pt}
.bank span.w{display:inline-block;border:.5mm dashed #56657F;border-radius:2mm;padding:0 3mm;margin-right:2mm}
.det{display:flex;align-items:flex-start;gap:2.5mm;margin-bottom:3.2mm}
.det .num{margin-top:1.5mm}
.dc{display:flex;flex-direction:column;align-items:center;font-size:13.5pt;font-weight:700;border:.5mm solid #D5E3F1;border-radius:2mm;padding:.3mm 2.5mm .8mm;line-height:1.25;white-space:nowrap}
.dc small{font-size:9.5pt;font-weight:700}
.legend{margin:0 0 2.5mm;font-size:12pt}
.sol{font-size:11pt;line-height:1.4}
.sol .solb{padding:2.5mm 5mm;margin-bottom:3.5mm}
.sol .solb p{margin-bottom:1.6mm}
'''
LEG2 = f'Prädikat = {R("P", "pink")}, Subjekt = {R("S", "blau")}'
LEG4 = LEG2 + f', Dativobjekt = {R("D", "grün")}, Akkusativobjekt = {R("A", "lila")}'

# ---------------- Blatt 1: Subjekt oder Prädikat? ----------------
g1 = [(S('der Hund|S', 'vergräbt|P', 'einen Knochen|-'), 'S'), (S('der Kater|S', 'fängt|P', 'eine Maus|-'), 'P'), (S('Oma|S', 'kocht|P', 'eine Suppe|-'), 'S'),
      (S('den Ball|-', 'schießt|P', 'Tim|S'), 'S'), (S('Lena|S', 'liest|P', 'ein Buch|-'), 'P'), (S('der Vogel|S', 'sucht|P', 'einen Wurm|-'), 'P'),
      (S('Papa|S', 'hat|P', 'das Auto|-', 'gewaschen|P'), 'P'), (S('einen Apfel|-', 'isst|P', 'das Mädchen|S'), 'S'), (S('das Pferd|S', 'frisst|P', 'Heu|-'), 'S'),
      (S('Mia|S', 'hat|P', 'ein Bild|-', 'gemalt|P'), 'P'), (S('der Bauer|S', 'melkt|P', 'die Kuh|-'), 'P'), (S('den Brief|-', 'öffnet|P', 'Jonas|S'), 'S'),
      (S('der Junge|S', 'hat|P', 'einen Schneemann|-', 'gebaut|P'), 'P'), (S('das Eichhörnchen|S', 'sammelt|P', 'Nüsse|-'), 'S'), (S('die Lehrerin|S', 'singt|P', 'ein Lied|-'), 'P')]
under = lambda s, k: ' '.join(f'<u>{p["text"]}</u>' if p['r'] == k else p['text'] for p in s) + '.'
a1 = ''.join(f'<div class="row"><span>{abc(i)}{under(s, k)}</span><span class="ch"><span class="cb"></span>Subjekt<span class="cb"></span>Prädikat</span></div>' for i, (s, k) in enumerate(g1[:9]))
a2 = ''.join(f'<div class="row"><span class="wide">{plain(s)}</span></div>' for s, _ in g1[9:])
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Subjekt oder Prädikat?', 'Subjekt oder Prädikat?',
  f'Das {R("P", "Prädikat")} ist das Verb im Satz. Es sagt, was jemand tut: Oma {R("P", "kocht")}. Das {R("S", "Subjekt")} sagt, wer es tut. Du findest es mit der Frage <b>Wer oder was?</b> Wer oder was kocht? → {R("S", "Oma")}.',
  task(1, 'Ist das unterstrichene Satzglied das Subjekt oder das Prädikat? Kreuze an.', a1) +
  task(2, f'Unterstreiche mit Farbe: {LEG2}. Achtung: Manche Prädikate haben zwei Teile!', a2))

# ---------------- Blatt 2: Farb-Markierer ----------------
g2 = [S('der Dackel|S', 'jagt|P', 'den Ball|-'), S('die Katze|S', 'trinkt|P', 'Milch|-'), S('den Reifen|-', 'flickt|P', 'Papa|S'), S('Oma|S', 'backt|P', 'einen Kuchen|-'),
      S('den Salat|-', 'frisst|P', 'der Hase|S'), S('Paul|S', 'schreibt|P', 'einen Brief|-'), S('der Fuchs|S', 'hat|P', 'eine Gans|-', 'gestohlen|P'), S('Mama|S', 'fegt|P', 'den Hof|-'),
      S('die Blumen|-', 'gießt|P', 'der Gärtner|S'), S('Emma|S', 'hat|P', 'ein Lied|-', 'gespielt|P'), S('der Bär|S', 'angelt|P', 'einen Fisch|-'), S('Opa|S', 'hat|P', 'seine Socken|-', 'gefunden|P'),
      S('das Küken|S', 'pickt|P', 'Körner|-'), S('den Zaun|-', 'hat|P', 'der Maler|S', 'gestrichen|P'), S('der Koch|S', 'belegt|P', 'die Pizza|-')]
b1 = '<div class="grid2">' + ''.join(f'<div class="row">{plain(s)}</div>' for s in g2[:10]) + '</div>'
b2 = ''.join(f'<div class="item"><p class="s">{abc(i)}{plain(s)}</p><div class="qa"><span class="num"></span>Wer oder was {L("q")} ? → {L()}</div></div>' for i, s in enumerate(g2[10:]))
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Farb-Markierer', 'Farb-Markierer',
  f'Such immer zuerst das {R("P", "Prädikat")}: Was tut jemand? Frag dann mit dem Prädikat nach dem {R("S", "Subjekt")}: Wer oder was {R("P", "frisst")} den Salat? → {R("S", "der Hase")}. Das Subjekt steht nicht immer am Satzanfang!',
  task(1, f'Unterstreiche zuerst das Prädikat, dann das Subjekt: {LEG2}.', b1) +
  task(2, 'Schreibe die Frage nach dem Subjekt auf. Schreibe dahinter die Antwort.', b2))

# ---------------- Blatt 3: Frag die Eule ----------------
g3 = [(S('Oma|S', 'schenkt|P', 'dem Enkel|D', 'einen Roller|A'), 'D'), (S('Lena|S', 'gibt|P', 'dem Hund|D', 'einen Knochen|A'), 'A'), (S('der Vater|S', 'zeigt|P', 'den Kindern|D', 'ein Foto|A'), 'S'),
      (S('dem Schüler|D', 'leiht|P', 'die Lehrerin|S', 'ein Buch|A'), 'D'), (S('Papa|S', 'kauft|P', 'seiner Tochter|D', 'ein Eis|A'), 'A'), (S('die Postbotin|S', 'übergibt|P', 'dem Nachbarn|D', 'ein Paket|A'), 'S'),
      (S('Tom|S', 'pflückt|P', 'seiner Mutter|D', 'einen Blumenstrauß|A'), 'D'), (S('die Tante|S', 'strickt|P', 'dem Baby|D', 'eine Mütze|A'), 'A'), (S('ein Märchen|A', 'erzählt|P', 'der Opa|S', 'den Enkeln|D'), 'S')]
conn = [('Wer oder was?', 'Akkusativobjekt'), ('Wem?', 'Subjekt'), ('Wen oder was?', 'Dativobjekt')]
c1 = '<div class="connect">' + ''.join(f'<div class="row2"><span class="l"><b>{a}</b></span><span class="dot"></span><span class="gap"></span><span class="dot"></span><span class="r">{b}</span></div>' for a, b in conn) + '</div>'
c2 = ''.join(f'<div class="item"><p class="s">{abc(i)}{plain(s)}</p><div class="qa"><span class="num"></span>{ask(s, k)} {L()}<span class="sq"></span></div></div>' for i, (s, k) in enumerate(g3[:7]))
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Frag die Eule', 'Frag die Eule',
  f'Jedes Satzglied hat seine Frage: <b>Wer oder was?</b> → {R("S", "Subjekt")} (S). <b>Wem?</b> → {R("D", "Dativobjekt")} (D). <b>Wen oder was?</b> → {R("A", "Akkusativobjekt")} (A). In die Frage gehört immer das Prädikat.',
  task(1, 'Welche Frage gehört zu welchem Satzglied? Verbinde.', c1) +
  task(2, 'Beantworte die Frage mit dem passenden Satzglied. Schreibe in das Kästchen S, D oder A.', c2))

# ---------------- Blatt 4: Vier Farben ----------------
g4 = [S('der Clown|S', 'schenkt|P', 'dem Kind|D', 'einen Luftballon|A'), S('den Schlüssel|A', 'sucht|P', 'die Hausmeisterin|S'), S('der Hund|S', 'folgt|P', 'dem Jungen|D'),
      S('dem Sieger|D', 'überreicht|P', 'der Bürgermeister|S', 'einen Pokal|A'), S('die Ärztin|S', 'untersucht|P', 'den Patienten|A'), S('der Schüler|S', 'hat|P', 'dem Lehrer|D', 'geantwortet|P'),
      S('dem Bäcker|D', 'dankt|P', 'die Kundin|S'), S('Felix|S', 'hat|P', 'seiner Schwester|D', 'einen Witz|A', 'erzählt|P'), S('einen Tunnel|A', 'gräbt|P', 'der Maulwurf|S'),
      S('Ben|S', 'hört|P', 'seiner Oma|D', 'zu|P'),
      S('der Zauberer|S', 'zeigt|P', 'den Zuschauern|D', 'einen Trick|A'), S('die Klasse|S', 'gratuliert|P', 'der Lehrerin|D'), S('der Ritter|S', 'hat|P', 'den Drachen|A', 'besiegt|P'),
      S('die Mutter|S', 'liest|P', 'dem Sohn|D', 'eine Geschichte|A', 'vor|P')]
d1 = ''.join(f'<div class="row"><span class="wide">{abc(i)}{plain(s)}</span></div>' for i, s in enumerate(g4[:9]))
d2 = '<table class="tb"><tr>' + ''.join(f'<th class="b{r}">{NAME[r]}</th>' for r in 'SPDA') + '</tr>' + \
     ''.join(f'<tr><td class="full" colspan="4">{plain(s)}</td></tr><tr><td></td><td></td><td></td><td></td></tr>' for s in g4[10:13]) + '</table>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Vier Farben', 'Vier Farben',
  f'Geh immer so vor: zuerst das {R("P", "Prädikat")} (Was tut jemand?), dann das {R("S", "Subjekt")} (Wer oder was?), dann das {R("D", "Dativobjekt")} (Wem?) und das {R("A", "Akkusativobjekt")} (Wen oder was?). Nicht jeder Satz hat beide Objekte.',
  task(1, f'Unterstreiche alle Satzglieder mit Farbe: {LEG4}.', d1) +
  task(2, 'Schreibe die Satzglieder in die Tabelle. Bleibt ein Feld leer, mach einen Strich.', d2))

# ---------------- Blatt 5: Satz-Bauplan ----------------
g5 = [(S('der Pirat|S', 'zeigt|P', 'dem Papagei|D', 'die Schatzkarte|A'), [2, 1, 3, 0]), (S('dem Igel|D', 'bringt|P', 'das Mädchen|S', 'einen Apfel|A'), [3, 2, 0, 1]),
      (S('einen Brief|A', 'schreibt|P', 'der König|S', 'der Prinzessin|D'), [2, 3, 1, 0]), (S('dem Verkäufer|D', 'gibt|P', 'Nina|S', 'das Geld|A'), [1, 3, 2, 0]),
      (S('ein Geheimnis|A', 'verrät|P', 'Lukas|S', 'seinem Freund|D'), [3, 2, 0, 1]), (S('dem Wanderer|D', 'winkt|P', 'die Bäuerin|S'), [2, 0, 1]),
      (S('den Dieb|A', 'verfolgt|P', 'der Polizist|S'), [1, 2, 0])]
G5 = [g5[i] for i in (0, 1, 2, 4, 5)]
def plan(s, fill=False): return '<div class="plan">' + ''.join(f'<div class="pl c{p["r"]}"><i>{NAME[p["r"]]}</i></div>' for p in s) + '</div>'
e1 = ''.join(f'<p class="bank">{abc(i)}' + ''.join(f'<span class="w">{s[j]["t"]}</span>' for j in o) + f'</p>{plan(s)}' for i, (s, o) in enumerate(G5))
own = S('x|S', 'x|P', 'x|D', 'x|A')
e2 = plan(own) + f'<div class="qa" style="margin-left:8mm">{L()}</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Satz-Bauplan', 'Satz-Bauplan',
  f'Frag bei jeder Karte: Ist es ein Verb? Dann ist es das {R("P", "Prädikat")}. <b>Wer oder was?</b> → {R("S", "Subjekt")}. <b>Wem?</b> → {R("D", "Dativobjekt")}. <b>Wen oder was?</b> → {R("A", "Akkusativobjekt")}. Achte auf die kleinen Wörter: <b>der</b> Igel, <b>dem</b> Igel, <b>den</b> Igel.',
  task(1, 'Schreibe jede Karte in das richtige Feld im Bauplan. Lies dann den Satz. Denke an den großen Satzanfang!', e1) +
  task(2, 'Erfinde einen eigenen Satz zu diesem Bauplan. Schreibe ihn auf die Linie.', e2))

# ---------------- Blatt 6: Fehler-Detektiv ----------------
g6 = [S('am Montag|Z', 'schickt|P', 'Onkel Max|S', 'dem Neffen|D|A', 'ein Päckchen|A'), S('der Trainer|S', 'hat|P', 'ihn|A|D', 'nach dem Spiel|Z', 'gelobt|P'),
      S('im Garten|O|Z', 'pflückt|P', 'der Opa|S', 'reife Kirschen|A'), S('heute|Z', 'hilft|P', 'mir|D', 'mein Bruder|S|A'),
      S('den Schatz|A|S', 'hat|P', 'der Pirat|S', 'auf der Insel|O', 'vergraben|P'), S('der Hausmeister|S', 'öffnet|P', 'am Morgen|Z|O', 'das Schultor|A'),
      S('morgen|Z', 'zeigt|P', 'die Försterin|S', 'der Klasse|D|S', 'einen Ameisenhaufen|A'), S('am Wochenende|Z', 'besucht|P', 'Familie Klein|S', 'den Tierpark|A|O'),
      S('das Kind|S', 'baut|P', 'am Strand|O', 'eine Sandburg|A'), S('in der Pause|Z', 'leiht|P', 'Nele|S', 'ihrer Freundin|D', 'einen Stift|A'),
      S('auf dem Schulhof|O', 'hat|P', 'mich|A', 'ein Ball|S', 'getroffen|P'), S('vor dem Frühstück|Z', 'hat|P', 'Jan|S', 'dem Kaninchen|D', 'frisches Heu|A', 'gegeben|P')]
def det(i, s):
    return f'<div class="det">{abc(i)}' + ''.join(f'<span class="dc">{p["text"]}<small class="r{p["shown"] or p["r"]}">{NAME[p["shown"] or p["r"]]}</small></span>' for p in s) + '</div>'
f1 = ''.join(det(i, s) for i, s in enumerate(g6[:8]))
f2 = ''.join(f'<div class="row"><span style="word-spacing:1.2mm">{abc(i)}{plain(s)}</span></div>' for i, s in enumerate(g6[8:]))
p6 = page('Blatt 6', 'Für Profis', 3, 'Fehler-Detektiv', 'Fehler-Detektiv',
  f'Prüfe jedes Satzglied mit seiner Frage. Neu für Profis: <b>Wann?</b> → {R("Z", "Bestimmung der Zeit")}. <b>Wo?</b> → {R("O", "Bestimmung des Ortes")}. Passt die Frage nicht zu dem Namen unter dem Satzglied, hast du den Fehler gefunden.',
  task(1, 'In jedem Satz steht unter genau einem Satzglied der falsche Name. Streiche ihn durch und schreibe den richtigen Namen darunter.', f1) +
  task(2, f'Unterstreiche nur die Bestimmung der Zeit {R("Z", "türkis")} und die Bestimmung des Ortes {R("O", "gelb")}.', f2))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
key = '<p>Farben: ' + ' · '.join(R(r, n) for r, n in [('P', 'Prädikat'), ('S', 'Subjekt'), ('D', 'Dativobjekt'), ('A', 'Akkusativobjekt'), ('Z', 'Bestimmung der Zeit'), ('O', 'Bestimmung des Ortes')]) + '</p>'
letters = lambda items: ' · '.join(f'{chr(97 + i)}) {x}' for i, x in enumerate(items))
l1 = sol(1, 'Subjekt oder Prädikat?', f'<p><b>Aufgabe 1:</b> {letters(NAME[k] for _, k in g1[:9])}</p><p><b>Aufgabe 2:</b> ' + ' · '.join(colored(s, 'PS') for s, _ in g1[9:]) + '</p>')
l2 = sol(2, 'Farb-Markierer', '<p><b>Aufgabe 1:</b> ' + ' · '.join(colored(s, 'PS') for s in g2[:10]) + '</p><p><b>Aufgabe 2:</b> ' + letters(f'{ask(s, "S")} → {R("S", answer(s, "S"))}' for s in g2[10:]) + '</p>')
l3 = sol(3, 'Frag die Eule', '<p><b>Aufgabe 1:</b> Wer oder was? – Subjekt · Wem? – Dativobjekt · Wen oder was? – Akkusativobjekt</p><p><b>Aufgabe 2:</b> ' + letters(f'{R(k, answer(s, k))} ({k})' for s, k in g3[:7]) + '</p>')
row = lambda s: ' | '.join(R(r, answer(s, r)) if answer(s, r) else '–' for r in 'SPDA')
l4 = sol(4, 'Vier Farben', '<p><b>Aufgabe 1:</b> ' + letters(colored(s) for s in g4[:9]) + '</p><p><b>Aufgabe 2</b> (Subjekt | Prädikat | Dativobjekt | Akkusativobjekt): ' + ' · '.join(row(s) for s in g4[10:13]) + '</p>')
l5 = sol(5, 'Satz-Bauplan', '<p><b>Aufgabe 1:</b> ' + letters(colored(s) for s, _ in G5) + f'</p><p><b>Aufgabe 2:</b> Eigener Satz, zum Beispiel: {colored(S("der Pirat|S", "zeigt|P", "dem Papagei|D", "die Schatzkarte|A"))}</p>')
bad = lambda s: next(p for p in s if p['shown'])
l6 = sol(6, 'Fehler-Detektiv', '<p><b>Aufgabe 1:</b> ' + letters(f'{bad(s)["t"]}: nicht {NAME[bad(s)["shown"]]}, sondern {R(bad(s)["r"], NAME[bad(s)["r"]])} ({ask(s, bad(s)["r"])})' for s in g6[:8]) +
  '</p><p><b>Aufgabe 2:</b> ' + letters(colored(s, 'ZO') for s in g6[8:]) + '</p>')
ps1 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 3', '', '', key + l1 + l2 + l3, solution=True)
ps2 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 4 bis 6', '', '', key + l4 + l5 + l6, solution=True)

EXTRA += '.connect .row2{display:flex;align-items:center;height:10.5mm;font-size:14pt}.connect .l{width:52mm}.connect .r{width:52mm;padding-left:4mm}'
write('subjekt-praedikat-objekt', 'Übungsblätter: Subjekt, Prädikat und Objekte (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps1, ps2], extra_css=EXTRA)
