"""Übungsblätter Alphabet und Wörterbuch."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def key(s): return s.lower().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ß', 'ss')
def abc(ws): return sorted(ws, key=key)
STRIP = '<span class="strip">' + ''.join(f'<i>{c}</i>' for c in ABC) + '</span>'

EXTRA = '''
.strip{display:flex;justify-content:space-between;margin-top:1.5mm;font-weight:700;font-size:13pt}
.strip i{font-style:normal;width:6mm;text-align:center;background:#fff;border:.4mm solid #FFB627;border-radius:1.5mm}
.hl{color:#C22A63;font-weight:700}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm 8mm}
.tri{display:flex;gap:1.5mm;justify-content:center}
.bx{width:11mm;height:11mm;border:.6mm solid #22304A;border-radius:2mm;display:grid;place-items:center;font-weight:700;font-size:17pt;line-height:1}
.bx.e{border:.6mm dashed #56657F;background:#FFF9E8}
.fill{display:grid;grid-template-columns:repeat(13,10mm);gap:3mm 2.5mm;justify-content:center}
.fill .bx{width:10mm;height:10.5mm;font-size:15pt}
.one .wr{height:10mm}
.one .pre{display:inline-block;width:34mm}
.srow{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;align-items:center;height:11.6mm;border-bottom:.3mm solid #D5E3F1}
.srow span{display:flex;align-items:center;gap:1mm;font-size:14pt;white-space:nowrap}
.circ{flex:none;width:7.5mm;height:7.5mm;border:.6mm solid #22304A;border-radius:50%;margin-right:1mm}
.wl{margin-bottom:1.5mm}
.wl p{margin:0;font-size:13.5pt}
.wl .emo{width:7mm;font-size:13pt;margin-right:.5mm}
.pairs{display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm 7mm}
.pair{display:flex;gap:2.5mm;justify-content:center}
.pair span{flex:1;border:.6mm solid #22304A;border-radius:3mm;text-align:center;font-size:15pt;font-weight:700;padding:1.6mm 0;letter-spacing:.03em}
.lists{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm 6mm}
.lst{border:.6mm solid #2B6BE0;border-left-width:2.4mm;border-radius:1.5mm 3.5mm 3.5mm 1.5mm;padding:1.5mm 3mm 2.5mm}
.lst .new{display:block;border-bottom:.5mm dashed #56657F;padding-bottom:1.2mm;margin-bottom:.5mm;font-size:11.5pt;line-height:1.3;color:#C22A63;font-weight:700}
.lst .new small{display:block;color:#56657F;font-weight:400;font-size:9.5pt}
.lst p{margin:0;height:8.1mm;display:flex;align-items:flex-end;font-size:14pt;font-weight:700}
.lst p .line{flex:1;width:auto;height:6.5mm}
.lst.note{border-color:#FFB627;background:#FFF2CF;font-size:12pt;padding-top:2.5mm}
.lst.note b.t{font-family:'Grandstander',sans-serif;display:block;margin-bottom:1mm}
.pgs{display:grid;grid-template-columns:1fr 1fr;gap:4mm 7mm}
.pg{border:.6mm solid #0B8791;border-left-width:2.4mm;border-radius:1.5mm 3.5mm 3.5mm 1.5mm;padding:1.2mm 3mm 2mm}
.pg h3{margin:0;display:flex;justify-content:space-between;align-items:baseline;font-size:14.5pt;color:#0B8791;border-bottom:.5mm solid #0B8791;padding-bottom:.6mm}
.pg h3 small{font-family:'Andika',sans-serif;font-weight:400;font-size:9pt;color:#56657F}
.pg table{width:100%;border-collapse:collapse;font-size:13.5pt}
.pg th{font-size:8.5pt;font-weight:700;color:#56657F;width:19mm;padding:1mm 0 0;line-height:1.1}
.pg th:first-child{width:auto}
.pg td{height:8mm;text-align:center;font-weight:700}
.pg td:first-child{text-align:left}
.cb{display:inline-block;width:5.4mm;height:5.4mm;border:.55mm solid #22304A;border-radius:1.2mm;vertical-align:middle}
.pg.own{border-color:#FFB627;font-size:12pt}
.pg.own p{margin:1.5mm 0 0;display:flex;align-items:flex-end;gap:2mm;height:8.4mm;white-space:nowrap}
.pg.own p .line{flex:1;width:auto}
.pg.own p.t{height:auto;white-space:normal;display:block;line-height:1.3}
.gf .wr{height:10.4mm;font-size:13.5pt}
.num{display:grid;grid-template-columns:repeat(4,1fr);gap:0 6mm}
.num .wr{height:10.4mm}
.num b{font-family:'Grandstander',sans-serif;color:#56657F}
.sol .solb p{margin-bottom:1mm}
'''

# ---------------- Blatt 1 ----------------
rows1 = ['BC_', 'FG_', 'KL_', 'QR_', 'VW_', '_FG', '_JK', '_OP', '_UV', '_XY', 'B_D', 'F_H', 'K_M', 'P_R', 'T_V']
def trio(r, show=False):
    pos = r.index('_'); anchor = 1 if pos == 0 else 0
    start = ABC.index(r[anchor]) - anchor
    full = ABC[start:start + 3]
    if show: return ' '.join(f'<b>{c}</b>' if i == pos else c for i, c in enumerate(full))
    return '<div class="tri">' + ''.join(f'<span class="bx e"></span>' if i == pos else f'<span class="bx">{c}</span>' for i, c in enumerate(full)) + '</div>'
order1 = [10, 0, 5, 11, 1, 6, 12, 2, 7, 13, 3, 8, 14, 4, 9]
t11 = '<div class="g3">' + ''.join(trio(rows1[i]) for i in order1) + '</div>'
mids = 'HNSEKQVC'
t12 = '<div class="g3" style="grid-template-columns:repeat(4,1fr)">' + ''.join(f'<div class="tri"><span class="bx e"></span><span class="bx">{c}</span><span class="bx e"></span></div>' for c in mids) + '</div>'
missing = 'CFJNRUX'
t13 = '<div class="fill">' + ''.join(f'<span class="bx{" e" if c in missing else ""}">{"" if c in missing else c}</span>' for c in ABC) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'ABC-Nachbarn', 'ABC-Nachbarn',
  'Das <b>ABC</b> hat 26 Buchstaben. Wer es gut kennt, findet Wörter im Wörterbuch schnell.' + STRIP,
  task(1, 'Welcher Buchstabe fehlt? Schreibe ihn in das leere Kästchen.', t11) +
  task(2, 'Schreibe die Nachbarn auf: den Buchstaben davor und den Buchstaben danach.', t12) +
  task(3, 'Im ABC fehlen sieben Buchstaben. Trage sie ein.', t13))

# ---------------- Blatt 2 ----------------
rows2 = [
  [('🍎', 'Apfel'), ('🍐', 'Birne'), ('🍒', 'Kirsche'), ('🍋', 'Zitrone')],
  [('🐕', 'Hund'), ('🐈', 'Katze'), ('🐭', 'Maus'), ('🐦', 'Vogel')],
  [('🚗', 'Auto'), ('🚌', 'Bus'), ('🚲', 'Fahrrad'), ('🚆', 'Zug')],
  [('🌙', 'Mond'), ('🌧️', 'Regen'), ('☀️', 'Sonne'), ('☁️', 'Wolke')],
  [('🐘', 'Elefant'), ('🦒', 'Giraffe'), ('🦁', 'Löwe'), ('🐅', 'Tiger')],
  [('🍞', 'Brot'), ('🥚', 'Ei'), ('🧀', 'Käse'), ('🍕', 'Pizza')],
  [('⚽', 'Ball'), ('🪁', 'Drachen'), ('🛴', 'Roller'), ('🧸', 'Teddy')],
  [('👖', 'Hose'), ('🧥', 'Jacke'), ('🧢', 'Mütze'), ('👟', 'Schuh')],
  [('🐬', 'Delfin'), ('🐟', 'Fisch'), ('🐙', 'Krake'), ('🐋', 'Wal')],
  [('🎸', 'Gitarre'), ('🎹', 'Klavier'), ('🎤', 'Mikrofon'), ('🥁', 'Trommel')],
  [('🦉', 'Eule'), ('🦊', 'Fuchs'), ('🦔', 'Igel'), ('🦌', 'Reh')],
  [('🛏️', 'Bett'), ('💡', 'Lampe'), ('🪑', 'Stuhl'), ('⏰', 'Uhr')],
  [('✋', 'Hand'), ('👃', 'Nase'), ('👂', 'Ohr'), ('🦷', 'Zahn')],
  [('🐜', 'Ameise'), ('🐝', 'Biene'), ('🐞', 'Käfer'), ('🐌', 'Schnecke')],
  [('📓', 'Heft'), ('📏', 'Lineal'), ('🖌️', 'Pinsel'), ('✂️', 'Schere')],
]
MIX = [[2, 0, 3, 1], [1, 3, 0, 2], [3, 1, 2, 0], [2, 3, 1, 0], [1, 0, 3, 2], [3, 2, 0, 1], [0, 2, 1, 3], [2, 0, 1, 3], [1, 3, 2, 0]]
def mixed(i): return [rows2[i][j] for j in MIX[i % len(MIX)]]
t21 = ''.join('<div class="srow">' + ''.join(f'<span><i class="circ"></i><span class="emo">{e}</span>{w}</span>' for e, w in mixed(i)) + '</div>' for i in range(9))
t22 = ''.join(f'<div class="wl"><p>' + ' · '.join(f'<span class="emo">{e}</span>{w}' for e, w in mixed(i)) + f'</p>{L("xl")}</div>' for i in range(9, 13))
p2 = page('Blatt 2', 'Für Anfänger', 1, 'ABC-Raupe', 'ABC-Raupe',
  'Im Wörterbuch sind die Wörter nach dem <b>ABC</b> geordnet. Schau zuerst auf den <b>ersten Buchstaben</b>: <b class="ez">A</b>pfel steht vor <b class="ez">B</b>irne, <b class="ez">B</b>irne steht vor <b class="ez">K</b>irsche.',
  task(1, 'In welcher Reihenfolge stehen die Wörter im Wörterbuch? Schreibe die Zahlen 1 bis 4 in die Kreise.', t21) +
  task(2, 'Schreibe die Wörter nach dem ABC geordnet auf.', t22))

# ---------------- Blatt 3 ----------------
pairs3 = [('Baum', 'Brief'), ('Teller', 'Topf'), ('Hemd', 'Hut'), ('Kind', 'Kuh'), ('Sand', 'See'), ('Milch', 'Mund'), ('Feder', 'Fluss'), ('Gras', 'Gurke'),
          ('Nest', 'Nuss'), ('Wald', 'Wiese'), ('Dieb', 'Dorf'), ('Pferd', 'Pilz'), ('Rad', 'Ring'), ('Lied', 'Luft'), ('Ente', 'Esel')]
FLIP = [1, 0, 1, 1, 0, 0, 1, 0, 1]
t31 = '<div class="pairs">' + ''.join('<div class="pair">' + ''.join(f'<span>{w}</span>' for w in (p[::-1] if FLIP[i] else p)) + '</div>' for i, p in enumerate(pairs3[:9])) + '</div>'
t32 = '<div class="one">' + ''.join(f'<div class="wr"><span class="pre">{b}, {a}:</span> {L()} steht vor {L()}</div>' for a, b in pairs3[9:]) + '</div>'
mix3 = [['Kuh', 'Hut', 'Kind', 'Hemd'], ['Mund', 'Brief', 'Milch', 'Baum']]
t33 = ''.join(f'<div class="wl"><p>{" · ".join(m)}</p>{L("xl")}</div>' for m in mix3)
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Was steht zuerst?', 'Was steht zuerst?',
  'Fangen zwei Wörter mit <b>demselben Buchstaben</b> an, schaust du auf den <b>zweiten Buchstaben</b>: B<span class="hl">a</span>um steht vor B<span class="hl">r</span>ief, weil a im ABC vor r kommt.' + STRIP,
  task(1, 'Male in jedem Wort den zweiten Buchstaben an. Kreise dann das Wort ein, das im Wörterbuch zuerst steht.', t31) +
  task(2, 'Welches Wort steht zuerst? Schreibe die beiden Wörter in der richtigen Reihenfolge auf.', t32) +
  task(3, 'Jetzt mit vier Wörtern: Schau erst auf den ersten, dann auf den zweiten Buchstaben. Schreibe die Wörter nach dem ABC geordnet auf.', t33))

# ---------------- Blatt 4 ----------------
rounds4 = [(['Affe', 'Angel', 'Arm', 'Auge'], ['Abend', 'Ampel', 'Ast', 'Axt'], 'Der 2. Buchstabe entscheidet.'),
           (['Paket', 'Pfanne', 'Plan', 'Puppe'], ['Pech', 'Pirat', 'Post', 'Pyramide'], 'Der 2. Buchstabe entscheidet.'),
           (['Bach', 'Bagger', 'Band', 'Bart'], ['Baby', 'Bad', 'Bahn', 'Bauch'], 'Der 3. Buchstabe entscheidet.'),
           (['Hafen', 'Haken', 'Hammer', 'Hase'], ['Haar', 'Hals', 'Harfe', 'Haus'], 'Der 3. Buchstabe entscheidet.'),
           (['Mantel', 'Messer', 'Motor', 'Musik'], ['Mädchen', 'Märchen', 'Möbel', 'Mücke'], 'ä, ö, ü zählen wie a, o, u.')]
NEWMIX = [[2, 0, 3, 1], [3, 1, 0, 2], [1, 3, 2, 0], [2, 3, 0, 1], [1, 2, 0, 3]]
def lst(i):
    base, new, note = rounds4[i]
    rows = ''.join(f'<p>{w}</p>' if w in base else f'<p>{L()}</p>' for w in abc(base + new))
    return f'<div class="lst"><span class="new">{" · ".join(new[j] for j in NEWMIX[i])}<small>{note}</small></span>{rows}</div>'
note4 = '<div class="lst note"><b class="t">So gehst du vor</b>Vergleiche Buchstabe für Buchstabe. Der erste Unterschied entscheidet.<br><br>Streiche jedes Wort durch, das du schon eingetragen hast.</div>'
t41 = '<div class="lists">' + ''.join(lst(i) for i in range(5)) + note4 + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Wo ist mein Platz?', 'Wo ist mein Platz?',
  'Ist der erste Buchstabe gleich, entscheidet der <b>zweite</b>. Ist auch der gleich, entscheidet der <b>dritte</b>: Ba<span class="hl">c</span>h → Ba<span class="hl">d</span> → Ba<span class="hl">g</span>ger. Die Umlaute <b>ä, ö, ü</b> werden wie <b>a, o, u</b> einsortiert.',
  task(1, 'Jede Liste ist nach dem ABC geordnet. Sortiere die vier <span class="hl">pinken</span> Wörter ein: Schreibe sie auf die richtigen Linien.', t41))

# ---------------- Blatt 5 ----------------
pages5 = [('Garten', 'Gold', ['Geld', 'Gruppe', 'Gabel', 'Glück']), ('Laden', 'Licht', ['Liste', 'Labor', 'Löffel', 'Leiter']),
          ('Rakete', 'Rose', ['Räuber', 'Rücken', 'Rabe', 'Riese']), ('Wagen', 'Wetter', ['Wind', 'Wärme', 'Waffel', 'Wurst']),
          ('Tanz', 'Tinte', ['Tal', 'Tür', 'Tasche', 'Tabelle'])]
def where(w, a, b): return 'davor' if key(w) < key(a) else 'dahinter' if key(w) > key(b) else 'auf der Seite'
def pg(a, b, ws):
    rows = ''.join(f'<tr><td>{w}</td>' + '<td><i class="cb"></i></td>' * 3 + '</tr>' for w in ws)
    return f'<div class="pg"><h3><span>{a}</span><small>Leitwörter</small><span>{b}</span></h3><table><tr><th></th><th>weiter vorne</th><th>auf dieser Seite</th><th>weiter hinten</th></tr>{rows}</table></div>'
own5 = f'''<div class="pg own"><p class="t"><b>Dein Wörterbuch:</b> Schlage das Wort <b>Schule</b> nach. Welche Leitwörter stehen oben auf der Seite?</p>
  <p>erstes Leitwort: {L()}</p><p>letztes Leitwort: {L()}</p><p>Seite: {L()}</p></div>'''
t51 = '<div class="pgs">' + ''.join(pg(*p) for p in pages5) + own5 + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Leitwort-Detektiv', 'Leitwort-Detektiv',
  'Oben auf jeder Seite im Wörterbuch stehen zwei <b>Leitwörter</b>: das <b>erste</b> und das <b>letzte</b> Wort der Seite. Alle Wörter, die nach dem ABC dazwischen stehen, findest du auf dieser Seite.',
  task(1, 'Wo steht das Wort? Vergleiche es mit den beiden Leitwörtern und kreuze an.', t51))

# ---------------- Blatt 6 ----------------
words6 = [('die Städte', 'Stadt'), ('er lief', 'laufen'), ('größer', 'groß'), ('die Gänse', 'Gans'), ('sie hat gesungen', 'singen'), ('am höchsten', 'hoch'),
          ('die Kräuter', 'Kraut'), ('sie aß', 'essen'), ('älter', 'alt'), ('die Türme', 'Turm'), ('du liest', 'lesen'), ('kürzer', 'kurz'),
          ('die Wölfe', 'Wolf'), ('er hat gewusst', 'wissen'), ('am klügsten', 'klug'), ('die Dächer', 'Dach'), ('er fährt', 'fahren'), ('wärmer', 'warm'),
          ('die Bücher', 'Buch'), ('sie nahm', 'nehmen')]
t61 = '<div class="grid2 gf">' + ''.join(f'<div class="wr">{f} <span class="arr">→</span> {L()}</div>' for f, g in words6) + '</div>'
verbs6 = abc([g for f, g in words6 if g.endswith('en')])
t62 = '<div class="num">' + ''.join(f'<div class="wr"><b>{i}.</b> {L()}</div>' for i in range(1, 8)) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Grundform-Profi', 'Grundform-Profi',
  'Im Wörterbuch stehen die Wörter in der <b>Grundform</b>. Nomen stehen in der <b>Einzahl</b>: Bäume → Baum. Verben stehen in der Grundform mit <b>-en</b>: sie hat gespielt → spielen. Adjektive stehen <b>ungesteigert</b>: schneller → schnell.',
  task(1, 'Unter welchem Wort schlägst du im Wörterbuch nach? Schreibe die Grundform auf. Nur ein Wort, ohne Artikel!', t61) +
  task(2, 'In Aufgabe 1 hast du sieben Verben gefunden. Schreibe sie nach dem ABC geordnet auf.', t62) +
  task(3, 'Ordne auch die sieben Nomen aus Aufgabe 1 nach dem ABC.', t62))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
l1 = sol(1, 'ABC-Nachbarn', '<p><b>Aufgabe 1:</b> ' + ' · '.join(trio(rows1[i], True) for i in order1) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'<b>{ABC[ABC.index(c) - 1]}</b> {c} <b>{ABC[ABC.index(c) + 1]}</b>' for c in mids) + '</p>' +
  '<p><b>Aufgabe 3:</b> Es fehlen ' + ', '.join(missing) + '.</p>')
l2 = sol(2, 'ABC-Raupe', '<p><b>Aufgabe 1:</b> ' + ' · '.join(' '.join(f'{w} ({abc([x for _, x in rows2[i]]).index(w) + 1})' for _, w in mixed(i)) for i in range(9)) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(', '.join(abc([w for _, w in rows2[i]])) for i in range(9, 13)) + '</p>')
l3 = sol(3, 'Was steht zuerst?', '<p><b>Aufgabe 1:</b> Eingekreist ist: ' + ' · '.join(f'{abc(p)[0]} (vor {abc(p)[1]})' for p in pairs3[:9]) + '</p>' +
  '<p><b>Aufgabe 2:</b> ' + ' · '.join(f'{abc(p)[0]} steht vor {abc(p)[1]}' for p in pairs3[9:]) + '</p><p><b>Aufgabe 3:</b> ' + ' · '.join(', '.join(abc(m)) for m in mix3) + '</p>')
l4 = sol(4, 'Wo ist mein Platz?', ''.join(f'<p><b>Liste {i + 1}:</b> ' + ', '.join(f'<b class="mz">{w}</b>' if w in new else w for w in abc(base + new)) + '</p>' for i, (base, new, _) in enumerate(rounds4)))
l5 = sol(5, 'Leitwort-Detektiv', ''.join(f'<p><b>{a} – {b}:</b> ' + ' · '.join(f'{w}: {where(w, a, b).replace("davor", "weiter vorne").replace("dahinter", "weiter hinten").replace("auf der Seite", "auf dieser Seite")}' for w in ws) + '</p>' for a, b, ws in pages5) +
  '<p><b>Dein Wörterbuch:</b> Die Lösung hängt von deinem Wörterbuch ab. Das Wort Schule steht nach dem ABC zwischen den beiden Leitwörtern.</p>')
l6 = sol(6, 'Grundform-Profi', '<p><b>Aufgabe 1:</b> ' + ' · '.join(f'{f} → <b>{g}</b>' for f, g in words6) + '</p><p><b>Aufgabe 2:</b> ' + ', '.join(verbs6) + '</p><p><b>Aufgabe 3:</b> ' + ', '.join(abc([g for f, g in words6 if f.startswith('die ')])) + '</p>')
ps1 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 3', '', '', l1 + l2 + l3, solution=True)
ps2 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 4 bis 6', '', '', l4 + l5 + l6, solution=True)

write('alphabet-ordnen', 'Übungsblätter: Alphabet und Wörterbuch (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps1, ps2], extra_css=EXTRA)
