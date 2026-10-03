"""Übungsblätter Die vier Fälle. Das Satzmaterial wird direkt aus den Spieldateien g1.txt … g6.txt gelesen."""
import sys, pathlib, re, ast, random
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from ws_common import *

def data(n):
    """Liest die Liste SENTENCES aus gN.txt (Zeilen der Form   [ ... ],)."""
    src = (HERE / f'g{n}.txt').read_text(encoding='utf-8')
    block = src.split('const SENTENCES = [', 1)[1].split('\n];', 1)[0]
    return [ast.literal_eval(ln.strip().rstrip(',')) for ln in block.split('\n') if ln.strip().startswith('[')]

NAME = {'nom': 'Nominativ', 'gen': 'Genitiv', 'dat': 'Dativ', 'akk': 'Akkusativ'}
ASK = {'nom': 'Wer oder was?', 'gen': 'Wessen?', 'dat': 'Wem?', 'akk': 'Wen oder was?'}
LET = {'nom': 'N', 'gen': 'G', 'dat': 'D', 'akk': 'A'}
ART = {'der': 'nom', 'des': 'gen', 'dem': 'dat', 'den': 'akk'}
ORDER = ['nom', 'gen', 'dat', 'akk']
C = lambda k, s: f'<span class="{k}">{s}</span>'
G = '<span class="g"></span>'
GW = '<span class="g w"></span>'
MARK = re.compile(r'\[([^\]]+)\]')
def under(s): return MARK.sub(r'<u>\1</u>', s)
def plain(s): return MARK.sub(r'\1', s)
def colored(s, k): return MARK.sub(lambda m: C(k, m.group(1)), s)
def mixed(items, seed):
    out = items[:]; random.Random(seed).shuffle(out); return out
def low(s): return s[0].lower() + s[1:]

MERK = (f'Mit vier Fragen findest du den Fall: {C("nom", "Wer oder was?")} Nominativ · {C("gen", "Wessen?")} Genitiv · '
        f'{C("dat", "Wem?")} Dativ · {C("akk", "Wen oder was?")} Akkusativ.')
KEY = '<div class="key">' + ''.join(f'<span><b>{LET[k]}</b> = {NAME[k]} ({ASK[k]})</span>' for k in ORDER) + '</div>'
ABC = '<span class="abc">' + ''.join(f'<i>{LET[k]}</i>' for k in ORDER) + '</span>'

EXTRA = '''
.nom{color:#1F57C3;font-weight:700}.gen{color:#6A3FC8;font-weight:700}.dat{color:#157A41;font-weight:700}.akk{color:#C22A63;font-weight:700}
u{text-decoration-thickness:.5mm;text-underline-offset:1mm;font-weight:700}
.g{display:inline-block;border-bottom:.45mm solid #56657F;width:17mm;height:1.1em;margin:0 .8mm;vertical-align:baseline}
.g.w{width:48mm}
.list p{margin:0;height:7.9mm;display:flex;align-items:flex-end;font-size:13.5pt;white-space:nowrap}
.list.tight p{height:7.5mm;font-size:12.5pt}
.list.roomy p{height:8.2mm;font-size:13pt}
.list.t6 p{height:6.6mm;font-size:12.5pt}
.q{color:#56657F;font-size:11pt;display:inline-block;width:31mm;flex:none}
.base{color:#56657F;font-size:11pt;margin-left:2mm}
.abc{margin-left:auto;display:inline-flex;gap:2mm;align-self:center}
.abc i{font-style:normal;font-family:'Grandstander',sans-serif;font-weight:800;font-size:9.5pt;width:6mm;height:6mm;border:.45mm solid #22304A;border-radius:50%;display:grid;place-items:center}
.sq{margin-left:auto;width:7mm;height:7mm;border:.45mm solid #22304A;border-radius:1.5mm;align-self:center;flex:none}
.key{display:flex;gap:1mm 5mm;font-size:10pt;margin:-1mm 0 1.5mm;flex-wrap:wrap}
.key b{font-family:'Grandstander',sans-serif}
.qa{margin-bottom:1mm}
.qa p{margin:0;font-size:13.5pt;white-space:nowrap}
.qa .line.f{height:8mm}
.qb{height:10.3mm}
.qb p{margin:0;white-space:nowrap;font-size:12.5pt;line-height:1.25}
.qb .ask{font-size:10pt;color:#56657F}
.qw{margin-bottom:2.4mm}
.qw p{margin:0;white-space:nowrap;font-size:12.5pt;line-height:1.25}
.qw .ans{display:flex;align-items:flex-end;gap:2mm;font-size:10.5pt;line-height:1;color:#56657F;height:6.2mm}
.qw .ans .line{flex:1;width:auto}
.count{display:flex;gap:5mm;font-size:11.5pt;align-items:flex-end;height:9mm;white-space:nowrap}
.count .line{width:8mm}
.four{display:grid;grid-template-columns:1fr 1fr;gap:0 9mm}
.four p{margin:0;height:8.6mm;display:flex;align-items:flex-end;font-size:13pt;white-space:nowrap}
.four .line{flex:1;width:auto;margin-left:2mm}
.four .q{width:auto;margin-right:2mm}
.sol .solb p{margin-bottom:1mm}
'''

# ---------------- Blatt 1: Fall-Detektiv ----------------
s1 = data(1)
own = [s1[8], s1[5], s1[12]]
rest = mixed([s for s in s1 if s not in own], 1)
t1 = KEY + '<div class="list">' + ''.join(f'<p><span>{under(s[0])}</span>{ABC}</p>' for s in rest) + '</div>'
t2 = ''.join(f'<div class="qa"><p>{under(s[0])}</p>{L("f")}</div>' for s in own)
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Fall-Detektiv', 'Fall-Detektiv', MERK,
  task(1, 'Frag nach dem unterstrichenen Satzteil. In welchem Fall steht er? Male den passenden Kreis an.', t1) +
  task(2, 'Schreibe die Frage auf, mit der du nach dem unterstrichenen Satzteil fragst.', t2))

# ---------------- Blatt 2: Artikel-Dreher ----------------
s2 = mixed(data(2), 2)
def qword(s): return ASK[ART[s[1]]]
u1 = '<div class="list tight">' + ''.join(f'<p><span class="q">{qword(s)}</span><span>{s[0].replace("___", G)}</span></p>' for s in s2) + '</div>'
tiger = [('nom', '{} Tiger schläft.'), ('gen', 'das Fell {} Tigers'), ('dat', 'Ich helfe {} Tiger.'), ('akk', 'Ich sehe {} Tiger.')]
u2 = '<div class="four">' + ''.join(f'<p><span class="q">{ASK[k]}</span><span>{t.format(G)}</span></p>' for k, t in tiger) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Artikel-Dreher', 'Artikel-Dreher',
  f'Der Artikel verändert sich mit dem Fall: Wer oder was? {C("nom", "der")} Tiger · Wessen? {C("gen", "des")} Tigers · Wem? {C("dat", "dem")} Tiger · Wen oder was? {C("akk", "den")} Tiger.',
  task(1, f'Lies die Frage. Setze den passenden Artikel ein: {C("nom", "der")}, {C("gen", "des")}, {C("dat", "dem")} oder {C("akk", "den")}. Am Satzanfang schreibst du groß!', u1) +
  task(2, 'Der Tiger in allen vier Fällen: Setze den Artikel ein.', u2))

# ---------------- Blatt 3: Frage-Lupe ----------------
s3 = data(3)
def sent(s): return plain(s[0]).replace(' | ', ' ')
wr = [s3[5], s3[9], s3[13], s3[1], s3[10]]
ul = mixed([s for s in s3 if s not in wr], 3)
v1 = ''.join(f'<div class="qb"><p class="ask">{s[2]}</p><p>{sent(s)}</p></div>' for s in ul)
v2 = ''.join(f'<div class="qw"><p>{sent(s)}</p><p class="ans"><span>{s[2]}</span>{L()}</p></div>' for s in wr)
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Frage-Lupe', 'Frage-Lupe', MERK,
  task(1, 'Lies die Frage. Unterstreiche im Satz den Satzteil, der auf die Frage antwortet.', v1) +
  task(2, 'Beantworte die Frage. Schreibe den passenden Satzteil auf die Linie.', v2))

# ---------------- Blatt 4: Fall-Kästen ----------------
s4 = mixed(data(4), 4)
w1 = KEY + '<div class="list tight">' + ''.join(f'<p><span>{under(s[0])}</span>{ABC}</p>' for s in s4) + '</div>'
w2 = '<div class="count">' + ''.join(f'<span>{C(k, NAME[k])}: {L()} -mal</span>' for k in ORDER) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Fall-Kästen', 'Fall-Kästen',
  f'Auch bei <b>die</b>, <b>das</b> und in der Mehrzahl verändert sich der Artikel. Frag immer nach: {C("nom", "Wer oder was?")} · {C("gen", "Wessen?")} · {C("dat", "Wem?")} · {C("akk", "Wen oder was?")}',
  task(1, 'In welchem Fall steht der unterstrichene Satzteil? Male den passenden Kreis an.', w1) +
  task(2, 'Zähle nach: Wie oft kommt jeder Fall vor? (Gleich oft!)', w2))

# ---------------- Blatt 5: Wort-Verwandler ----------------
s5 = mixed(data(5), 5)
def row5(s, box=False): return f'<p><span>{s[0].replace("___", GW)}</span><span class="base">({s[1]})</span>{"<span class=sq></span>" if box else ""}</p>'
x1 = '<div class="list roomy">' + ''.join(row5(s) for s in s5[:10]) + '</div>'
x2 = '<div class="list roomy">' + ''.join(row5(s, True) for s in s5[10:]) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Wort-Verwandler', 'Wort-Verwandler',
  f'Frag nach der Lücke, dann weißt du den Fall. Manchmal verändert sich auch das Nomen: {C("gen", "des Zeltes")}, {C("dat", "dem Bären")}, {C("dat", "den Spielern")}.',
  task(1, 'Setze das Nomen aus der Klammer in der richtigen Form ein. Am Satzanfang schreibst du groß!', x1) +
  task(2, 'Setze das Nomen ein. Schreibe den Fall in das Kästchen: N, G, D oder A.', x2))

# ---------------- Blatt 6: Fall-Profi ----------------
s6 = data(6)
prep = [s for s in s6 if s[4].startswith('Schau')]
norm = mixed([s for s in s6 if s not in prep], 6)
def row6(s): return f'<p><span>{s[0].replace("___", GW)}</span><span class="base">({s[1]})</span></p>'
y1 = '<div class="list t6">' + ''.join(row6(s) for s in norm) + '</div>'
y2 = '<div class="list t6">' + ''.join(row6(s) for s in prep) + '</div>'
y3 = '<div class="four">' + ''.join(f'<p><span class="q">{NAME[k]}:</span>{L()}</p>' for k in ORDER) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Fall-Profi', 'Fall-Profi',
  f'Manche Nomen bekommen eine Endung: {C("gen", "des Flusses")}, {C("dat", "dem Raben")}, {C("dat", "den Zuschauern")}.',
  task(1, 'Frag nach der Lücke. Schreibe Artikel und Nomen im richtigen Fall hinein.', y1) +
  task(2, 'Nach <b>mit</b> und <b>nach</b> steht immer der Dativ, nach <b>für</b> und <b>ohne</b> immer der Akkusativ. Setze ein.', y2) +
  task(3, 'Schreibe <b>der Rabe</b> in allen vier Fällen auf.', y3))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
l1 = sol(1, 'Fall-Detektiv',
  '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{colored(s[0], s[1])} <b>({LET[s[1]]})</b>' for s in rest) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{colored(s[0], s[1])} – {s[2]}' for s in own) + '</p>')
def fill2(s):
    a = s[1].capitalize() if s[0].startswith('___') else s[1]
    return s[0].replace('___', C(ART[s[1]], a))
l2 = sol(2, 'Artikel-Dreher',
  '<p><b>Aufgabe 1:</b> ' + ' · '.join(fill2(s) for s in s2) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(t.format(C(k, a.capitalize() if t.startswith('{}') else a)) for (k, t), a in zip(tiger, ['der', 'des', 'dem', 'den'])) + '</p>')
def col3(s): return ' '.join(C(s[1], p[1:-1]) if p.startswith('[') else p for p in s[0][:-1].split(' | ')) + '.'
def ans3(s):
    parts = s[0][:-1].split(' | '); i = [p.startswith('[') for p in parts].index(True); a = parts[i][1:-1]
    return low(a) if i == 0 else a
l3 = sol(3, 'Frage-Lupe',
  '<p><b>Aufgabe 1:</b> ' + ' · '.join(col3(s) for s in ul) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{s[2]} – {C(s[1], ans3(s))}' for s in wr) + '</p>')
l4 = sol(4, 'Fall-Kästen',
  '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{colored(s[0], s[1])} <b>({LET[s[1]]})</b>' for s in s4) + '</p>' +
  '<p><b>Aufgabe 2:</b> Jeder Fall kommt 5-mal vor.</p>')
l5 = sol(5, 'Wort-Verwandler',
  '<p><b>Aufgabe 1:</b> ' + ' · '.join(s[0].replace('___', C(s[4], s[3])) for s in s5[:10]) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{s[0].replace("___", C(s[4], s[3]))} <b>({LET[s[4]]})</b>' for s in s5[10:]) + '</p>')
l6 = sol(6, 'Fall-Profi',
  '<p><b>Aufgabe 1:</b> ' + ' · '.join(s[0].replace('___', C(s[3], s[2])) for s in norm) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(s[0].replace('___', C(s[3], s[2])) for s in prep) + '</p>' +
  f'<p><b>Aufgabe 3:</b> Nominativ: {C("nom", "der Rabe")} · Genitiv: {C("gen", "des Raben")} · Dativ: {C("dat", "dem Raben")} · Akkusativ: {C("akk", "den Raben")}</p>')
farben = f'<p>Farben: {C("nom", "Nominativ (N)")} · {C("gen", "Genitiv (G)")} · {C("dat", "Dativ (D)")} · {C("akk", "Akkusativ (A)")}</p>'
psA = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 3', '', '', farben + l1 + l2 + l3, solution=True)
psB = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 4 bis 6', '', '', farben + l4 + l5 + l6, solution=True)

write('vier-faelle', 'Übungsblätter: Die vier Fälle (Klasse 4)', [p1, p2, p3, p4, p5, p6, psA, psB], extra_css=EXTRA)
