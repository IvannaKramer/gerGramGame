"""Übungsblätter Kurze und lange Vokale."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

EXTRA = '''
.ku{color:#C22A63;font-weight:700}.la{color:#1F57C3;font-weight:700}.gn{color:#1A8C4B;font-weight:700}
.vk,.vl{position:relative;display:inline-block;line-height:1}
.vk{color:#C22A63}.vl{color:#1F57C3}
.vk::after,.vl::after{content:"";position:absolute;bottom:-.04em;background:currentColor}
.vk::after{left:50%;width:.2em;height:.2em;margin-left:-.1em;border-radius:50%}
.vl::after{left:.04em;right:.04em;height:.1em;border-radius:.05em}
.gp{display:inline-block;width:9mm;height:1.05em;border-bottom:.45mm solid #56657F;margin:0 .6mm;vertical-align:baseline}
.gp.w{width:12mm}
.tk{display:inline-block;width:4.4mm;height:4.4mm;border:.5mm solid #22304A;border-radius:50%;margin:0 1.2mm 0 3mm;vertical-align:-.7mm}
.it{height:10.6mm;display:flex;align-items:flex-end;font-size:14.5pt;white-space:nowrap}
.it .emo{align-self:center}
.it .w{min-width:31mm;font-weight:700}
.it .ch{font-size:11.5pt;color:#22304A}
.it .op{font-size:11.5pt;color:#56657F;margin-left:2mm}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:0 5mm}
.grid3 .it{height:10.2mm}.grid3 .it .w{min-width:0}
.box{min-width:26mm;padding:1.6mm 4mm;font-size:14.5pt}
.rule .wr{height:9.4mm;font-size:13pt}
.rule .wr .line{min-width:16mm}
.rule .wr small{font-size:9.5pt;color:#56657F}
.cols5.c4{grid-template-columns:repeat(4,1fr)}
.cols5.c2{grid-template-columns:repeat(2,1fr);gap:6mm}
.k1{--c:#C22A63}.k2{--c:#1F57C3}.k3{--c:#1A8C4B}.k4{--c:#0B8791}
.zw{border:.6mm solid #D5E3F1;border-radius:3.5mm;padding:1.5mm 2mm 1mm;text-align:center}
.zw b{display:block;font-size:16pt;letter-spacing:.04em;line-height:1.3}
.zw .line{display:block;width:100%;height:8.5mm}
.sents p{white-space:nowrap}
.nw{white-space:nowrap}
.h1s{font-size:18pt;white-space:nowrap}
.r4 .rule .wr{height:8.5mm}
.spruch{font-size:14pt;margin:0;height:11mm;display:flex;align-items:flex-end}
'''
GP = '<span class="gp"></span>'
def gapw(w):  # runde Klammer -> Lücke, eckige Klammer weg
    return re.sub(r'\(.+?\)', GP, w).replace('[', '').replace(']', '')
def vgap(w):  # eckige Klammer -> Lücke
    return re.sub(r'\[.+?\]', GP, w)
def plain(w): return re.sub(r'[\[\]()]', '', w)
def mark(w, k): return '<span class="nw">' + re.sub(r'\[(.+?)\]', lambda m: f'<span class="{"vk" if k == "k" else "vl"}">{m.group(1)}</span>', w).replace('(', '').replace(')', '') + '</span>'
TICKS = '<span class="ch"><span class="tk"></span>kurz<span class="tk"></span>lang</span>'

# ---------------- Blatt 1 ----------------
W1 = [('S[o](nn)e','k','☀️'),('N[a](s)e','l','👃'),('B[a](ll)','k','⚽'),('H[o](s)e','l','👖'),('B[e](tt)','k','🛏️'),('H[u](t)','l','🎩'),('[A](ff)e','k','🐒'),
      ('M[o](nd)','l','🌙'),('F[i](sch)','k','🐟'),('Br[o](t)','l','🍞'),('H[a](mm)er','k','🔨'),('L[ö](w)e','l','🦁'),('L[ö](ff)el','k','🥄'),('K[ä](s)e','l','🧀'),('T[e](ll)er','k','🍽️')]
a1 = '<div class="grid2">' + ''.join(f'<div class="it"><span class="emo">{e}</span><span class="w">{gapw(w)}</span>{TICKS}</div>' for w, k, e in W1) + '</div>'
order1 = [8, 1, 12, 5, 0, 13, 2, 9, 14, 3, 6, 11, 4, 7, 10]
b1 = '<div class="boxes">' + ''.join(f'<span class="box">{plain(W1[i][0])}</span>' for i in order1) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Punkt oder Strich?', 'Punkt oder Strich?',
  'Vokale sind a, e, i, o, u und ä, ö, ü. Ein <b class="ku">kurzer</b> Vokal klingt kurz und knapp: S<span class="vk">o</span>nne. Er bekommt einen <b class="ku">Punkt</b>. Einen <b class="la">langen</b> Vokal kannst du ziehen: N<span class="vl">a</span>se. Er bekommt einen <b class="la">Strich</b>.',
  task(1, 'Sprich das Wort zum Bild laut. Ist der Vokal vor der Lücke kurz oder lang? Kreuze an.', a1) +
  task(2, 'Hier stehen die Wörter ganz. Setze unter den Vokal, den du in Aufgabe 1 geprüft hast, einen <b class="ku">Punkt</b> (kurz) oder einen <b class="la">Strich</b> (lang).', b1))

# ---------------- Blatt 2 ----------------
W2 = [('T[a](nn)e','k','🌲'),('G[a](b)el','l','🍴'),('K[o](ff)er','k','🧳'),('V[o](g)el','l','🐦'),('B[u](tt)er','k','🧈'),('Tom[a](t)e','l','🍅'),('Tr[o](mm)el','k','🥁'),
      ('Ban[a](n)e','l','🍌'),('S[u](pp)e','k','🍲'),('L[u](p)e','l','🔍'),('W[e](ll)e','k','🌊'),('Kam[e](l)','l','🐫'),('Kr[a](bb)e','k','🦀'),('N[u](d)eln','l','🍝'),('Fl[a](gg)e','k','🚩')]
def opt2(w):
    c = re.search(r'\((.)', w).group(1); return f'<span class="op">{c} oder {c}{c}?</span>'
a2 = '<div class="grid2">' + ''.join(f'<div class="it"><span class="emo">{e}</span><span class="w">{gapw(w)}</span>{opt2(w)}</div>' for w, k, e in W2) + '</div>'
b2 = '<div class="cols5 c2">' + ''.join(f'<div class="c {c}"><h3>{h}</h3>' + ''.join(L('f') for _ in range(3)) + '</div>' for h, c in [('kurzer Vokal: Mitlaut doppelt', 'k1'), ('langer Vokal: Mitlaut einfach', 'k2')]) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Doppel-Werkstatt', 'Doppel-Werkstatt',
  'Nach einem <b class="ku">kurzen</b> Vokal wird der Mitlaut <b class="ku">verdoppelt</b>: K<span class="vk">a</span>nne. Nach einem <b class="la">langen</b> Vokal steht <b class="la">nur ein</b> Mitlaut: Sal<span class="vl">a</span>t.',
  task(1, 'Sprich das Wort laut. Ist der Vokal kurz oder lang? Schreibe einen oder zwei Mitlaute in die Lücke.', a2) +
  task(2, 'Suche dir aus Aufgabe 1 je drei Wörter aus und schreibe sie ganz auf.', b2))

# ---------------- Blatt 3 ----------------
W3 = [('B[ie]ne','🐝'),('K[i]nd','🧒'),('Z[ie]ge','🐐'),('R[i]ng','💍'),('F[i]lm','🎬'),('Fl[ie]ge','🪰'),('St[i]ft','✏️'),('Br[ie]f','✉️'),('M[i]lch','🥛'),('Sp[ie]gel','🪞'),
      ('P[i]nsel','🖌️'),('Zw[ie]bel','🧅'),('[I]nsel','🏝️'),('W[i]nd','💨'),('St[ie]fel','👢'),('v[ie]r','4️⃣'),('B[i]rne','🍐'),('s[ie]ben','7️⃣'),('Sch[i]rm','☂️'),('Sp[ie]l','🎲'),
      ('H[i]rsch','🦌'),('Pap[ie]r','📄'),('F[i]nger','☝️'),('Klav[ie]r','🎹'),('F[ie]ber','🤒'),('B[i]ld','🖼️'),('K[i]rche','⛪'),('L[ie]be','❤️'),('K[i]ste','📦'),('Z[ie]l','🏁')]
a3 = '<div class="grid3">' + ''.join(f'<div class="it"><span class="emo">{e}</span><span class="w">{vgap(w)}</span></div>' for w, e in W3) + '</div>'
b3 = ''.join(L('f') for _ in range(3))
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Langes i gesucht', 'Langes i gesucht',
  'Ein <b class="la">langes i</b> schreibst du meist <b class="la">ie</b>: B<span class="vl">ie</span>ne. Ein <b class="ku">kurzes i</b> schreibst du nur <b class="ku">i</b>: K<span class="vk">i</span>nd. Sprich das Wort laut, dann hörst du es.',
  task(1, 'Sprich jedes Wort laut. Setze <b class="ku">i</b> oder <b class="la">ie</b> in die Lücke. Am Wortanfang schreibst du groß.', a3) +
  task(2, 'Schreibe zehn Wörter mit <b class="la">ie</b> ab.', b3))

# ---------------- Blatt 4 ----------------
G4 = [('ck oder k?', 'k4', [('Z[u](ck)er',''),('qu[a](k)en',''),('B[ä](ck)er',''),('H[a](k)en','für die Jacke'),('Br[ü](ck)e','')]),
      ('tz oder z?', 'k4', [('M[ü](tz)e','für den Kopf'),('Kap[u](z)e',''),('Pf[ü](tz)e',''),('[O](z)ean',''),('Sch[a](tz)','')]),
      ('i oder ie?', 'k4', [('W[ie]se',''),('W[i]nter',''),('R[ie]se',''),('H[i]mmel',''),('D[ie]nstag','')]),
      ('ein Mitlaut oder zwei?', 'k4', [('schw[i](mm)en','m'),('N[a](d)el','d'),('kl[e](tt)ern','t'),('F[e](d)er','d'),('schl[a](f)en','f')])]
def row4(w, note, vg):
    n = f' <small>({note})</small>' if note else ''
    return f'<div class="wr"><b>{vgap(w) if vg else gapw(w)}</b>{n} <span class="arr">→</span> {L()}</div>'
a4 = '<div class="rules r4">' + ''.join(f'<div class="rule {c}"><h3>{h}</h3>' + ''.join(row4(w, n, i == 2) for w, n in ws) + '</div>' for i, (h, c, ws) in enumerate(G4)) + '</div>'
s4 = [f'Der Bä{GP}er streut Zu{GP}er auf den Kuchen.', f'Der R{GP}se schläft auf der W{GP}se.', f'Die Frösche qua{GP}en an der Pfü{GP}e.']
b4 = '<div class="sents">' + ''.join(f'<p><span>{s}</span></p>' for s in s4) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, '<span class="h1s">Kurz-oder-lang-Entscheider</span>', 'Entscheider (Spiel 4)',
  'Nach einem <b class="ku">kurzen</b> Vokal schreibst du <b class="ku">ck</b>, <b class="ku">tz</b> oder einen <b class="ku">doppelten Mitlaut</b>. Nach einem <b class="la">langen</b> Vokal schreibst du <b class="la">k</b>, <b class="la">z</b> oder nur <b class="la">einen Mitlaut</b>. Ein langes i schreibst du meist <b class="la">ie</b>.',
  task(1, 'Sprich das Wort laut. Entscheide: kurz oder lang? Schreibe dann das ganze Wort auf. Im letzten Kasten steht in Klammern, welcher Mitlaut fehlt.', a4) +
  task(2, 'Fülle die Lücken.', b4))

# ---------------- Blatt 5 ----------------
W5 = [('Zan','Zahn'),('Schule',''),('faren','fahren'),('Blume',''),('Stul','Stuhl'),('Tür',''),('Son','Sohn'),('Krone',''),('Mel','Mehl'),('schön',''),
      ('Tal',''),('wonen','wohnen'),('Dame',''),('Jar','Jahr'),('Schere',''),('Bone','Bohne'),('Träne',''),('nemen','nehmen'),('hören',''),('Kole','Kohle')]
a5 = '<div class="grid4">' + ''.join(f'<div class="zw"><b>{a}</b>{L()}</div>' for a, b in W5) + '</div>'
b5 = '<div class="cols5 c4">' + ''.join(f'<div class="c k2"><h3>h vor {x}</h3>' + ''.join(L('f') for _ in range(n)) + '</div>' for x, n in [('l', 4), ('m', 4), ('n', 4), ('r', 4)]) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Das verschwundene h', 'Das verschwundene h',
  'Das <b class="la">Dehnungs-h</b> hörst du nicht. Es steht nach einem langen Vokal und nur vor <b>l, m, n</b> oder <b>r</b>: <span class="vl">U</span>hr, z<span class="vl">ä</span>hlen. Viele Wörter mit langem Vokal haben aber kein h: Pl<span class="vl">a</span>n. Wörter mit Dehnungs-h sind Merkwörter.',
  task(1, 'Ein Zauberer hat bei zehn Wörtern das Dehnungs-h versteckt. Schreibe alle Wörter richtig auf. Zehn Wörter stimmen schon!', a5) +
  task(2, 'Sortiere die zehn Wörter mit Dehnungs-h: Vor welchem Buchstaben steht das h? Nicht alle Zeilen werden voll.', b5))

# ---------------- Blatt 6 ----------------
W6 = ['Ba[n](k)','Schn[e](ck)e','He[r](z)','Sch[au](k)el','Wo[l](k)e','Bl[i](tz)','Pi[l](z)','P[au](k)e','Gu[r](k)e','W[e](ck)er',
      'Ke[r](z)e','Kr[eu](z)','Gesche[n](k)','gl[ü](ck)lich','ta[n](z)en','h[ei](z)en','du[n](k)el','pl[ö](tz)lich','Sa[l](z)','Schn[au](z)e']
a6 = '<div class="grid4">' + ''.join(f'<div class="it"><span class="w">{gapw(w)}</span></div>' for w in W6) + '</div>'
s6 = ['Im Park sitzt Opa auf einer', 'Auf dem Geburtstagskuchen brennt eine', 'Jeden Morgen klingelt mein', 'Der Hund hat eine feuchte']
b6 = '<div class="sents">' + ''.join(f'<p>{s} {L("m")}.</p>' for s in s6) + '</div>'
c6 = f'<p class="spruch">Nach l, n, r, das merke ja, steht nie&nbsp; {L("s")} &nbsp;und nie&nbsp; {L("s")}.</p>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Regel-Meister', 'Regel-Meister',
  '<b class="ku">ck</b> und <b class="ku">tz</b> stehen nur direkt nach einem <b class="ku">kurzen Vokal</b>: J<span class="vk">a</span>cke, K<span class="vk">a</span>tze. Nach <b class="gn">l, n, r</b> und nach den Zwielauten <b class="la">au, ei, eu</b> schreibst du nur <b>k</b> oder <b>z</b>: Onkel, Holz, W<span class="vl">ei</span>zen.',
  task(1, 'Setze ein: <b>k</b>, <b>ck</b>, <b>z</b> oder <b>tz</b>. Schau genau auf den Buchstaben vor der Lücke. (Bli… gehört zum Gewitter.)', a6) +
  task(2, 'Welches Wort aus Aufgabe 1 passt? Schreibe es ganz auf.', b6) +
  task(3, 'Ergänze den Merkspruch.', c6))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
j = ' · '.join
l1 = sol(1, 'Punkt oder Strich?', f'<p><b>Aufgabe 1 und 2:</b> <span class="ku">kurz (Punkt):</span> {j(mark(w, k) for w, k, e in W1 if k == "k")}</p><p><span class="la">lang (Strich):</span> {j(mark(w, k) for w, k, e in W1 if k == "l")}</p>')
l2 = sol(2, 'Doppel-Werkstatt', f'<p><b>Aufgabe 1:</b> <span class="ku">kurzer Vokal, Mitlaut doppelt:</span> {j(mark(w, k) for w, k, e in W2 if k == "k")}</p><p><span class="la">langer Vokal, Mitlaut einfach:</span> {j(mark(w, k) for w, k, e in W2 if k == "l")}</p><p><b>Aufgabe 2:</b> je drei dieser Wörter.</p>')
l3 = sol(3, 'Langes i gesucht', f'<p><b>Aufgabe 1:</b> <span class="la">langes i (ie):</span> {j(mark(w, "l") for w, e in W3 if "[ie]" in w)}</p><p><span class="ku">kurzes i (i):</span> {j(mark(w, "k") for w, e in W3 if "[ie]" not in w)}</p><p><b>Aufgabe 2:</b> zehn der Wörter mit ie.</p>')
K4 = {'Z[u](ck)er':'k','B[ä](ck)er':'k','Br[ü](ck)e':'k','M[ü](tz)e':'k','Pf[ü](tz)e':'k','Sch[a](tz)':'k','W[i]nter':'k','H[i]mmel':'k','schw[i](mm)en':'k','kl[e](tt)ern':'k'}
l4 = sol(4, 'Kurz-oder-lang-Entscheider', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'<b>{h}</b> ' + ', '.join(mark(w, K4.get(w, 'l')) for w, n in ws) for h, c, ws in G4) + '</p><p><b>Aufgabe 2:</b> Bäcker, Zucker · Riese, Wiese · quaken, Pfütze</p>')
l5 = sol(5, 'Das verschwundene h', f'<p><b>Aufgabe 1:</b> <span class="la">mit Dehnungs-h:</span> {j(b for a, b in W5 if b)}</p><p><b>ohne h (stimmen schon):</b> {j(a for a, b in W5 if not b)}</p><p><b>Aufgabe 2:</b> <b>h vor l:</b> Stuhl, Mehl, Kohle · <b>h vor m:</b> nehmen · <b>h vor n:</b> Zahn, Sohn, wohnen, Bohne · <b>h vor r:</b> fahren, Jahr</p>')
def m6(w):
    if re.search(r'\[[lnr]\]', w): return '<span class="nw">' + re.sub(r'\[(.)\]', r'<span class="gn">\1</span>', w).replace('(', '').replace(')', '') + '</span>'
    return mark(w, 'l' if re.search(r'\[(au|ei|eu)\]', w) else 'k')
l6 = sol(6, 'Regel-Meister', f'<p><b>Aufgabe 1:</b> <span class="gn">nach l, n, r:</span> {j(m6(w) for w in W6 if re.search(r"\[[lnr]\]", w))}</p><p><span class="ku">kurzer Vokal:</span> {j(m6(w) for w in W6 if re.search(r"\[[eiüö]\]", w))}</p><p><span class="la">Zwielaut:</span> {j(m6(w) for w in W6 if re.search(r"\[(au|ei|eu)\]", w))}</p><p><b>Aufgabe 2:</b> Bank · Kerze · Wecker · Schnauze</p><p><b>Aufgabe 3:</b> Nach l, n, r, das merke ja, steht nie tz und nie ck.</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

write('kurze-lange-vokale', 'Übungsblätter: Kurze und lange Vokale (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps], extra_css=EXTRA)
