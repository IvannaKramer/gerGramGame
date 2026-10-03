"""Übungsblätter Wörtliche Rede. Die Sätze werden aus den Spieldateien g1.txt … g6.txt gelesen,
damit Spiel und Blatt immer dasselbe Material haben."""
import sys, pathlib, re, random
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from ws_common import *

def data(n):
    return (HERE / f'g{n}.txt').read_text(encoding='utf-8').split('@@data')[1].split('@@js')[0]
def lines(n):
    return re.findall(r"^  '(.*)',?$", data(n), re.M)

# ---------------- Satz zerlegen (wie im Spiel) ----------------
def model(s):
    """words = [(Wort, gehört zur Rede)], sig[i] = Zeichen „ “ : , vor Wort i"""
    words, sig, in_r, w = [], [''], False, ''
    def flush():
        nonlocal w
        if w: words.append((w, in_r)); w = ''; sig.append('')
    for ch in s:
        if ch == '„': flush(); sig[len(words)] += ch; in_r = True
        elif ch == '“': flush(); sig[len(words)] += ch; in_r = False
        elif not in_r and ch in ':,': flush(); sig[len(words)] += ch
        elif ch == ' ': flush()
        else: w += ch
    flush()
    return words, sig
def kind(s):
    return 'vorn' if not s.startswith('„') else 'mitte' if s.count('„') > 1 else 'hinten'
def build(s, zf, wf):
    words, sig = model(s)
    out = []
    for i, (w, r) in enumerate(words):
        o = zf('„') if '„' in sig[i] else ''
        c = ''.join(zf(ch) for ch in sig[i + 1].replace('„', ''))
        out.append(f'<span class="nb">{o}{wf(w, r)}{c}</span>')
    return ' '.join(out)
def col(s):      # Lösung: Rede pink, Begleitsatz blau, Zeichen gelb unterlegt
    return build(s, lambda ch: f'<b class="z">{ch}</b>', lambda w, r: f'<span class="{"rd" if r else "bg"}">{w}</span>')
def boxes(s):    # Kästchen an jeder Stelle, an der ein Zeichen fehlt
    return build(s, lambda ch: '<span class="bx"></span>', lambda w, r: w)
def bare(s):     # ganz ohne „ “ : und Begleitsatz-Kommas
    return ' '.join(w for w, r in model(s)[0])
def pieces(s):
    words, sig = model(s)
    out, buf = [], []
    for i, (w, r) in enumerate(words):
        if sig[i]:
            if buf: out.append(' '.join(buf)); buf = []
            out += list(sig[i])
        buf.append(w)
    out.append(' '.join(buf)); out += list(sig[len(words)])
    return out

RD, BG = (lambda s: f'<span class="rd">{s}</span>'), (lambda s: f'<span class="bg">{s}</span>')
EX_V, EX_H, EX_M = col('Tom sagt: „Ich komme gleich.“'), col('„Ich komme gleich“, sagt Tom.'), col('„Ich komme“, sagt Tom, „gleich nach.“')

EXTRA = '''
.rd{color:#C22A63;font-weight:700}.bg{color:#1F57C3;font-weight:700}
.z{font-weight:700;background:#FFD877;border-radius:1mm;padding:0 .4mm}
.nb{white-space:nowrap}
.bx{display:inline-block;width:5.2mm;height:6.4mm;border:.45mm solid #56657F;border-radius:1.2mm;vertical-align:-1.6mm;margin:0 .7mm}
.list p{margin:0;display:flex;align-items:center;font-size:13.5pt;white-space:nowrap}
.list .t{white-space:nowrap}
.ul p{height:10.2mm;font-size:14.5pt}
.talk{display:grid;grid-template-columns:minmax(0,1fr) 78mm;gap:5mm;align-items:center;height:12.6mm;font-size:13pt}
.talk .t{white-space:nowrap}
.talk .bub{position:relative;border:.6mm solid #C22A63;border-radius:4mm;height:10.6mm}
.talk .bub::before{content:"";position:absolute;left:-2.4mm;top:50%;width:3.6mm;height:3.6mm;background:#fff;border-left:.6mm solid #C22A63;border-bottom:.6mm solid #C22A63;transform:translateY(-50%) rotate(45deg)}
.b2 p{height:9mm;font-size:14pt}
.part{font-family:'Grandstander',sans-serif;font-weight:800;font-size:11.5pt;color:#56657F;margin:1mm 0 .5mm}
.pz{margin-bottom:2.2mm}
.pz .ps{display:flex;gap:3mm;align-items:center;margin-bottom:.5mm}
.pz .pc{border:.6mm solid #22304A;border-radius:2.4mm;padding:.6mm 3.2mm;font-size:13pt;font-weight:700;white-space:nowrap}
.pz .pc.s{min-width:9mm;text-align:center;background:#FFF2CF;border-color:#D98E00}
.pz .line.f{height:8.6mm}
.b3 p{height:7.8mm;word-spacing:.5em}
.b4 p{height:7.8mm;font-size:13pt}
.count{display:flex;gap:4mm;font-size:13pt;align-items:flex-end;height:9mm;flex-wrap:nowrap;white-space:nowrap}
.count .line{width:9mm}
.pair{margin-bottom:1.2mm}
.pair p{height:6.3mm;font-size:12.5pt}
.o{display:inline-block;width:4.2mm;height:4.2mm;border:.45mm solid #22304A;border-radius:50%;margin-right:2.5mm;flex:none}
.b5 p{height:6.8mm;font-size:12.5pt}
.b6 p{height:7.1mm;font-size:12pt;word-spacing:.4em}
.turn{margin-bottom:1.5mm}
.turn p{margin:0;font-size:13pt}
.turn .line.f{height:7.8mm}
.sol{font-size:10pt}
.sol .solb p{margin-bottom:1mm;line-height:1.32}
.sol .rd,.sol .bg{font-weight:400}
.sol .z{padding:0 .2mm}
'''
def lst(items, cls, f=lambda s: s): return f'<div class="list {cls}">' + ''.join(f'<p><span class="t">{f(s)}</span></p>' for s in items) + '</div>'

# ---------------- Blatt 1: Rede-Finder ----------------
s1 = re.findall(r"^  \['(.*?)',\s", data(1), re.M)
assert len(s1) == 15
a1 = [s1[i] for i in (0, 1, 2, 4, 6, 8, 9, 10, 11, 12)]
a2 = [s1[i] for i in (3, 5, 7, 13, 14)]
t2 = ''.join(f'<div class="talk"><span class="t">{s}</span><span class="bub"></span></div>' for s in a2)
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Rede-Finder', 'Rede-Finder',
  f'Was jemand sagt, heißt {RD("wörtliche Rede")}. Sie steht in Anführungszeichen: am Anfang unten „ und am Ende oben “. Der {BG("Begleitsatz")} sagt, wer spricht: {EX_V}',
  task(1, f'Unterstreiche die {RD("wörtliche Rede")} rot und den {BG("Begleitsatz")} blau.', lst(a1, 'ul')) +
  task(2, 'Was wird gesagt? Schreibe nur die wörtliche Rede in die Sprechblase.', t2))

# ---------------- Blatt 2: Zeichen-Helfer ----------------
s2 = lines(2); assert len(s2) == 15
v2, h2 = [s for s in s2 if kind(s) == 'vorn'], [s for s in s2 if kind(s) == 'hinten']
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Zeichen-Helfer', 'Zeichen-Helfer',
  f'Begleitsatz <b>vorn</b>: Doppelpunkt, dann die Rede in Anführungszeichen: {EX_V} Begleitsatz <b>hinten</b>: Komma nach den Anführungszeichen oben: {EX_H}',
  task(1, 'Der Begleitsatz steht vorn. Setze in jedes Kästchen das richtige Zeichen: <b>: „ “</b>', lst(v2, 'b2', boxes)) +
  task(2, 'Der Begleitsatz steht hinten. Setze in jedes Kästchen das richtige Zeichen: <b>„ “ ,</b>', lst(h2, 'b2', boxes)) +
  task(3, 'Schreibe einen Satz von oben ab. Vergiss kein Zeichen!', L('f')))

# ---------------- Blatt 3: Satz-Puzzle ----------------
s3 = lines(3); assert len(s3) == 15
z1 = [s3[0], s3[7], s3[1], s3[9]]
z2 = [s for s in s3 if s not in z1]
rnd = random.Random(12)
def puzzle(s):
    ps = pieces(s); mix = ps[:]
    while mix == ps or mix[0] == ps[0]: rnd.shuffle(mix)
    return '<div class="pz"><div class="ps">' + ''.join(f'<span class="pc{" s" if len(p) == 1 else ""}">{p}</span>' for p in mix) + f'</div>{L("f")}</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Satz-Puzzle', 'Satz-Puzzle',
  f'Gibt es einen <b>Doppelpunkt</b>? Dann steht der Begleitsatz vorn: {EX_V} Gibt es ein <b>Komma</b>? Dann steht er hinten und ist kleingeschrieben: {EX_H}',
  task(1, 'Die Teile sind durcheinander. Schreibe den Satz richtig auf die Linie.', ''.join(puzzle(s) for s in z1)) +
  task(2, 'Hier fehlen alle Anführungszeichen, Doppelpunkte und Kommas. Setze sie mit einem bunten Stift ein.', lst(z2, 'b3', bare)))

# ---------------- Blatt 4: Zeichen-Körbe ----------------
s4 = lines(4); assert len(s4) == 20
order4 = [0, 15, 5, 10, 18, 6, 1, 11, 16, 3, 8, 12, 19, 2, 7, 13, 17, 9, 4, 14]
def gap4(raw):
    return re.sub(r'(\S+)\|“(,?)', lambda m: f'<span class="nb">{m.group(1).rstrip(".?!") if m.group(1)[-1] in ".?!" else m.group(1)}<span class="bx"></span>“{m.group(2)}</span>', raw)
def ans4(raw):
    c = raw[raw.index('|') - 1]
    return c if c in '.?!' else '–'
q4 = [s4[i] for i in order4]
cnt = '<div class="count">' + ''.join(f'<span>{n}: {L()} -mal</span>' for n in ['Punkt', '?', '!', 'Strich']) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Zeichen-Körbe', 'Zeichen-Körbe',
  f'<b>?</b> und <b>!</b> bleiben in der wörtlichen Rede immer stehen. Der <b>Punkt</b> bleibt nur, wenn der Satz mit der Rede zu Ende ist: {EX_V} Geht der Satz danach weiter, fällt der Punkt weg: {EX_H}',
  task(1, 'Was gehört in das Kästchen: <b>.</b> <b>?</b> oder <b>!</b> Wenn dort kein Zeichen steht, mach einen Strich (–).', lst(q4, 'b4', gap4)) +
  task(2, 'Zähle nach: Wie oft hast du jedes Zeichen gesetzt?', cnt))

# ---------------- Blatt 5: Satz-Detektiv ----------------
d5 = data(5)
ok5 = re.findall(r"^  \['(.*)',$", d5, re.M)
bad5 = re.findall(r"^    \['(.*?)', '", d5, re.M)
assert len(ok5) == 20 and len(bad5) == 40
pick5 = [0, 8, 14, 3, 10, 16]                      # Aufgabe 1: richtig oder falsch?
rest5 = [1, 2, 4, 5, 7, 9, 11, 12, 13, 15, 17, 18]    # 6 und 19 bleiben dem Spiel vorbehalten
def pair(n, i):
    two = [ok5[i], bad5[2 * i + 1]]
    if n % 2: two.reverse()
    return '<div class="list pair">' + ''.join(f'<p><span class="o"></span><span class="t">{s}</span></p>' for s in two) + '</div>'
t51 = ''.join(pair(n, i) for n, i in enumerate(pick5))
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Satz-Detektiv', 'Satz-Detektiv',
  f'Der Begleitsatz kann auch <b>in der Mitte</b> stehen. Dann steht er zwischen zwei Kommas, und die Rede geht klein weiter: {EX_M}',
  task(1, 'Immer nur ein Satz ist richtig geschrieben. Kreuze ihn an.', t51) +
  task(2, 'Fehler-Detektiv: In jedem Satz steckt ein Fehler. Verbessere ihn mit einem bunten Stift.', lst([bad5[2 * i] for i in rest5], 'b5')))

# ---------------- Blatt 6: Satzzeichen-Setzer ----------------
s6 = lines(6); assert len(s6) == 20
order6 = [0, 6, 13, 1, 7, 14, 2, 8, 15, 3, 9, 16, 4, 10, 17, 5, 11, 18, 12, 19]
q6 = [s6[i] for i in order6]
turn = [s6[5], s6[1]]
turned = ['„Fang mich doch!“, schreit Ole auf dem Schulhof.', '„Wer hat das letzte Tor geschossen?“, fragt der Trainer nach dem Spiel.']
t62 = ''.join(f'<div class="turn"><p>{s}</p>{L("f")}</div>' for s in turn)
p6 = page('Blatt 6', 'Für Profis', 3, 'Satzzeichen-Setzer', 'Satzzeichen-Setzer',
  f'Suche zuerst den Begleitsatz: Wer spricht? Er kann vorn, hinten oder in der Mitte stehen: {EX_M}',
  task(1, 'Setze alle fehlenden Zeichen mit einem bunten Stift ein: <b>„ “ : ,</b>', lst(q6, 'b6', bare)) +
  task(2, 'Stelle um: Schreibe den Satz so auf, dass der Begleitsatz hinten steht.', t62))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def cols(items): return ' · '.join(col(s) for s in items)
def fix5(i):
    return col(ok5[i])
l1 = sol(1, 'Rede-Finder', f'<p><b>Aufgabe 1</b> ({RD("wörtliche Rede")}, {BG("Begleitsatz")}): {cols(a1)}</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(' '.join(w for w, r in model(s)[0] if r) for s in a2) + '</p>')
l2 = sol(2, 'Zeichen-Helfer', f'<p><b>Aufgabe 1:</b> {cols(v2)}</p><p><b>Aufgabe 2:</b> {cols(h2)}</p><p><b>Aufgabe 3:</b> ein Satz von oben mit allen Zeichen</p>')
l3 = sol(3, 'Satz-Puzzle', f'<p><b>Aufgabe 1:</b> {cols(z1)}</p><p><b>Aufgabe 2:</b> {cols(z2)}</p>')
n4 = [sum(1 for s in s4 if ans4(s) == c) for c in '.?!–']
l4 = sol(4, 'Zeichen-Körbe', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{col(s.replace("|", ""))} <b>({ans4(s)})</b>' for s in q4) + '</p>' +
  f'<p><b>Aufgabe 2:</b> Punkt: {n4[0]}-mal · ?: {n4[1]}-mal · !: {n4[2]}-mal · Strich: {n4[3]}-mal</p>')
l5 = sol(5, 'Satz-Detektiv', f'<p><b>Aufgabe 1</b> (richtig ist): {cols(ok5[i] for i in pick5)}</p><p><b>Aufgabe 2</b> (so ist es richtig): {cols(ok5[i] for i in rest5)}</p>')
l6 = sol(6, 'Satzzeichen-Setzer', f'<p><b>Aufgabe 1:</b> {cols(q6)}</p><p><b>Aufgabe 2:</b> {cols(turned)}</p>')
psA = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 3', '', '', l1 + l2 + l3, solution=True)
psB = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 4 bis 6', '', '', l4 + l5 + l6, solution=True)

write('woertliche-rede', 'Übungsblätter: Wörtliche Rede (Klasse 4)', [p1, p2, p3, p4, p5, p6, psA, psB], extra_css=EXTRA)
