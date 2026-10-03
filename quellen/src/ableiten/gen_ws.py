"""Übungsblätter Ableiten (ä/e, äu/eu). Das Wortmaterial ist dasselbe wie in den sechs Spielen."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

CLS = {'ä': 'ka', 'e': 'ke', 'äu': 'kau', 'eu': 'keu'}
def gap(s, l=''):                      # Wort mit Lücke; bei äu/eu ist die Lücke breiter
    return s.replace('_', '<i class="g w2"></i>' if len(l) == 2 else '<i class="g"></i>')
def full(s, l):                        # Lösung, Laut farbig
    return s.replace('_', f'<b class="{CLS[l]}">{l}</b>')
emo = lambda e: f'<span class="emo">{e}</span>'
ARR = '<span class="arr">→</span>'
K = lambda l: f'<b class="{CLS[l]}">{l}</b>'
J = ' · '.join

EXTRA = '''
.ka{color:#1F57C3}.ke{color:#C22A63}.kau{color:#157A41}.keu{color:#5B34B0}
.g{display:inline-block;width:5.5mm;border-bottom:.5mm solid #22304A;margin:0 .4mm}
.g.w2{width:9mm}
.wr .w,.box2 .w{font-weight:700}
.grid2{grid-template-columns:repeat(2,minmax(0,1fr))}
.wr .line{min-width:12mm}
.box2{border:.7mm solid #22304A;border-radius:3.5mm;padding:2mm .5mm 2.4mm;text-align:center;line-height:1.2}
.box2 .w{display:block;font-size:14pt;white-space:nowrap}
.grid5{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:3mm 2mm}
.cols4{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}
.cols4 .c{border:.6mm solid var(--c);border-radius:3mm;padding:0 2mm 3mm}
.cols4 h3{margin:0 -2mm;background:var(--c);color:#fff;font-size:15pt;padding:.5mm 2mm;text-align:center;border-radius:2.2mm 2.2mm 0 0}
.ca{--c:#2B6BE0}.ce{--c:#DE3A76}.cau{--c:#1A8C4B}.ceu{--c:#7A4FD8}.cab{--c:#0B8791}.cmw{--c:#D98E00}
.hrow{display:grid;grid-template-columns:44mm repeat(3,1fr);align-items:center;gap:3mm;height:11mm;font-size:14pt}
.hrow .w{font-weight:700;white-space:nowrap}
.hrow .o{border:.6mm solid #56657F;border-radius:99px;text-align:center;padding:.6mm 1mm;white-space:nowrap;font-size:13pt}
.hrow .o.no{border-style:dashed;color:#56657F;font-size:11.5pt}
.sents p{height:10.6mm;white-space:nowrap}
.sents .line{flex:1;width:auto;min-width:30mm}
.tight .wr{height:10.4mm}
.fam{display:grid;grid-template-columns:30mm repeat(3,1fr);gap:1.6mm 3mm;align-items:center;border:.6mm solid #D5E3F1;border-radius:3.5mm;padding:2mm 3mm;margin-bottom:2.6mm;font-size:13.5pt}
.fam .h{grid-row:span 2;font-weight:700;font-size:15pt;line-height:1.15}
.fam .h small{display:block;font-size:9.5pt;font-weight:400;color:#56657F}
.fam .o{border:.6mm solid #56657F;border-radius:99px;text-align:center;padding:.5mm 1mm;white-space:nowrap;font-weight:700}
.rule .wr{height:9.6mm;font-size:13pt}
.sol ul{margin:0;padding:0}
'''

# ---------------- Blatt 1: Umlaut-Zauber ----------------
a1 = [('⚽','der Ball','viele B_lle','ä'),('🌳','der Baum','viele B_me','äu'),('🛏️','das Bett','viele B_tten','e'),('👫','der Freund','zwei Fr_nde','eu'),
      ('✋','die Hand','zwei H_nde','ä'),('🐭','die Maus','viele M_se','äu'),('⭐','der Stern','viele St_rne','e'),('🔥','das Feuer','viele F_er','eu')]
a2 = [('🦷','der Zahn','viele','Zähne'),('🏠','das Haus','viele','Häuser'),('⛺','das Zelt','viele','Zelte'),('✈️','das Flugzeug','viele','Flugzeuge'),
      ('🍁','das Blatt','viele','Blätter'),('✊','die Faust','zwei','Fäuste'),('⛰️','der Berg','viele','Berge')]
t1 = '<div class="grid2">' + ''.join(f'<div class="wr">{emo(e)}{b} {ARR} <span class="w">{gap(g, l)}</span></div>' for e, b, g, l in a1) + '</div>'
t2 = '<div class="grid2">' + ''.join(f'<div class="wr">{emo(e)}<span class="w">{b}</span> {ARR} {h} {L()}</div>' for e, b, h, s in a2) + '</div>'
t3 = '<div class="grid2">' + ''.join(f'<div class="wr">{L("s")} {ARR} viele {L()}</div>' for _ in range(4)) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Umlaut-Zauber', 'Umlaut-Zauber',
  f'In der Mehrzahl wird aus <b>a</b> oft {K("ä")} und aus <b>au</b> oft {K("äu")}: der Ball → viele B{K("ä")}lle, der Baum → viele B{K("äu")}me. '
  f'Steht im Wort schon {K("e")} oder {K("eu")}, dann bleibt es so: das Bett → viele B{K("e")}tten.',
  task(1, 'Schau auf die Einzahl. Setze dann in der Mehrzahl ä, e, äu oder eu ein.', t1) +
  task(2, 'Schreibe die Mehrzahl auf.', t2) +
  task(3, 'Finde eigene Wörter mit a oder au, die in der Mehrzahl ä oder äu bekommen.', t3))

# ---------------- Blatt 2: Wortfamilien-Suche ----------------
h2 = [('🥨','B_cker','ä',['baden','backen']),('🪟','F_nster','e',['Fahne','fangen']),('🦹','R_ber','äu',['rauben','Raupe']),('👥','L_te','eu',['Laus','Laune']),
      ('🥶','k_lter','ä',['Kanne','kalt']),('🕯️','K_rze','e',['Karte','Karton']),('💭','tr_men','äu',['Traube','Traum']),('💎','t_er','eu',['Tau','tauchen'])]
t21 = ''.join(f'<div class="hrow"><span class="w">{emo(e)}{gap(w, l)}</span>' + ''.join(f'<span class="o">{o}</span>' for o in os) + '<span class="o no">keins passt</span></div>' for e, w, l, os in h2)
w2 = [('🌷','G_rtner','ä','Garten'),('🐌','Schn_cke','e',''),('🌿','Str_cher','äu','Strauch'),('📜','Z_gnis','eu',''),('😴','er schl_ft','ä','schlafen'),('🎁','Gesch_nk','e',''),('🏃','L_fer','äu','laufen')]
t22 = '<div class="grid2">' + ''.join(f'<div class="wr">{emo(e)}<span class="w">{gap(w, l)}</span> <span class="clue">verwandt:</span> {L()}</div>' for e, w, l, r in w2) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Wortfamilien-Suche', 'Wortfamilien-Suche',
  f'Verwandte Wörter haben etwas miteinander zu tun: Der B{K("ä")}cker kann b<b>a</b>cken. Gibt es ein verwandtes Wort mit <b>a</b>, schreibst du {K("ä")}. '
  f'Gibt es eins mit <b>au</b>, schreibst du {K("äu")}. Findest du keins, schreibst du {K("e")} oder {K("eu")}.',
  task(1, 'Welches Wort ist verwandt? Kreise es ein. Passt keins, kreise „keins passt“ ein. Setze dann ä, e, äu oder eu ein.', t21) +
  task(2, 'Schreibe ein verwandtes Wort mit a oder au auf. Findest du keins, mache einen Strich. Setze dann den Laut ein.', t22))

# ---------------- Blatt 3: Merkwort-Körbe ----------------
w3 = ['die Äpfel','der Käse','die Kräuter','der Bär','die Gläser','das Mädchen','die Räder','der März','das Kätzchen','die Säge','die Hähne','der Käfer','die Bräute','die Säule','die Bänder']
bx3 = '<div class="boxes">' + ''.join(f'<span class="box">{w}</span>' for w in w3) + '</div>'
c3 = ('<div class="rules"><div class="rule cab"><h3>Ableiten <small>Wort ← verwandtes Wort</small></h3>' + ''.join(f'<div class="wr">{L()} ← {L()}</div>' for _ in range(8)) + '</div>'
      '<div class="rule cmw"><h3>Merkwörter <small>kein Wort mit a oder au</small></h3>' + ''.join(f'<div class="wr">{L()}</div>' for _ in range(7)) + '</div></div>')
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Merkwort-Körbe', 'Merkwort-Körbe',
  f'Bei den meisten Wörtern mit {K("ä")} oder {K("äu")} findest du ein verwandtes Wort mit a oder au: die Äpfel ← der Apfel. '
  'Bei einigen Wörtern gibt es keins, zum Beispiel bei Käse, Bär und Mädchen. Das sind <b>Merkwörter</b>. Du musst sie dir einprägen.',
  task(1, 'Lies die Wörter. Findest du ein verwandtes Wort mit a oder au? Male alle Merkwörter gelb an.', bx3) +
  task(2, 'Sortiere die Wörter aus Aufgabe 1. Schreibe bei „Ableiten“ auch das verwandte Wort dazu.', c3))

# ---------------- Blatt 4: Lücken-Blitz ----------------
w4 = [('W_lder','ä','Wald'),('F_ld','e',''),('Schl_che','äu','Schlauch'),('n_n','eu',''),('St_dte','ä','Stadt'),
      ('Fr_de','eu',''),('Z_ne','äu','Zaun'),('W_lt','e',''),('w_rmer','ä','warm'),('s_bern','äu','sauber'),
      ('H_ft','e',''),('B_le','eu',''),('er f_hrt','ä','fahren'),('Ger_sch','äu','rauschen'),('g_lb','e',''),
      ('l_chten','eu',''),('z_hlen','ä','Zahl'),('N_st','e',''),('h_fig','äu','Haufen'),('f_cht','eu','')]
bx4 = '<div class="grid5">' + ''.join(f'<div class="box2"><span class="w">{gap(w, l)}</span></div>' for w, l, r in w4) + '</div>'
c4 = '<div class="cols4">' + ''.join(f'<div class="c {c}"><h3>{l}</h3>' + L('f') * 5 + '</div>' for l, c in [('ä','ca'),('e','ce'),('äu','cau'),('eu','ceu')]) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Lücken-Blitz', 'Lücken-Blitz',
  f'Suche im Kopf ein <b>verwandtes Wort</b>: W{K("ä")}lder ← Wald, er f{K("ä")}hrt ← fahren, h{K("äu")}fig ← Haufen. '
  f'Findest du ein Wort mit a oder au, schreibst du {K("ä")} oder {K("äu")}. Sonst schreibst du {K("e")} oder {K("eu")}.',
  task(1, 'Setze ä, e, äu oder eu ein. Suche dazu im Kopf ein verwandtes Wort.', bx4) +
  task(2, 'Sortiere die Wörter aus Aufgabe 1. Schreibe jedes Wort in die Spalte mit seinem Laut.', c4))

# ---------------- Blatt 5: Familien-Treffen ----------------
f5 = [('fangen','ä',[('er f_ngt',1),('F_rien',0),('Anf_nger',1),('Gef_ngnis',1),('F_ll',0),('Empf_nger',1)],'e'),
      ('kaufen','äu',[('K_le',0),('K_fer',1),('Verk_fer',1),('B_tel',0),('K_ferin',1),('verk_flich',1)],'eu'),
      ('Land','ä',[('L_nder',1),('Gel_nde',1),('Kal_nder',0),('l_ndlich',1),('L_nker',0),('Ausl_nder',1)],'e'),
      ('Raum','äu',[('R_me',1),('n_gierig',0),('aufr_men',1),('ger_mig',1),('Zwischenr_me',1),('Abent_er',0)],'eu'),
      ('lang','ä',[('l_cker',0),('l_nger',1),('L_nge',1),('L_hrer',0),('verl_ngern',1),('l_nglich',1)],'e')]
t51 = ''.join(f'<div class="fam"><span class="h"><small>Familie</small>{h}</span>' + ''.join(f'<span class="o">{gap(w, l)}</span>' for w, m in ws) + '</div>' for h, l, ws, o in f5)
t52 = L('xl') * 2
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Familien-Treffen', 'Familien-Treffen',
  f'Wörter einer <b>Wortfamilie</b> haben denselben Wortstamm und etwas miteinander zu tun: Land – L{K("ä")}nder, Gel{K("ä")}nde. '
  f'Zu einer Familie mit a gehört {K("ä")}, zu einer Familie mit au gehört {K("äu")}. Kal{K("e")}nder klingt ähnlich, hat aber mit Land nichts zu tun.',
  task(1, 'In jeder Reihe gehören vier Wörter zur Familie. Kreise sie ein und setze ä oder äu ein. Zwei Wörter gehören nicht dazu: Dort fehlt e oder eu.', t51) +
  task(2, 'Wähle eine Familie aus. Schreibe einen Satz mit zwei Wörtern dieser Familie.', t52))

# ---------------- Blatt 6: Schreib-Profi ----------------
s6 = [('Der Bauer hat zwei St_lle für seine Kühe.','ä','Ställe','Stall'),('An dieser St_lle überqueren wir die Straße.','e','Stelle',''),
      ('Unsere Schule ist ein großes Geb_de.','äu','Gebäude','bauen'),('An der Kr_zung biegen wir links ab.','eu','Kreuzung',''),
      ('Das Eis auf dem See ist dünn und gef_hrlich.','ä','gefährlich','Gefahr'),('Opa repariert das Rad mit seinem W_rkzeug.','e','Werkzeug',''),
      ('Wale sind keine Fische, sondern S_getiere.','äu','Säugetiere','saugen'),('Im Märchen bewacht ein Ungeh_er den Schatz.','eu','Ungeheuer',''),
      ('Auf der Baustelle ist viel L_rm.','ä','Lärm','Merkwort'),('Die Katze spielt mit einem Kn_el Wolle.','äu','Knäuel','Merkwort')]
t61 = '<div class="sents">' + ''.join(f'<p><span>{gap(s, l)}</span> {L()}</p>' for s, l, w, r in s6) + '</div>'
w6 = [('Gem_lde','ä','malen'),('Gr_nze','e',''),('l_ten','äu','laut'),('Sch_ne','eu',''),('R_tsel','ä','raten'),
      ('Schm_tterling','e',''),('es sch_mt','äu','Schaum'),('d_tlich','eu',''),('K_tte','e',''),('St_er','eu','')]
t62 = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="w">{gap(w, l)}</span> <span class="clue">verwandt:</span> {L()}</div>' for w, l, r in w6) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Schreib-Profi', 'Schreib-Profi',
  f'Manchmal ist das verwandte Wort gut versteckt: Geb{K("äu")}de ← bauen, gef{K("ä")}hrlich ← Gefahr. Achte auch auf den Satz: '
  f'die St{K("ä")}lle ← Stall, aber die St{K("e")}lle hat kein verwandtes Wort mit a. Und denk an die Merkwörter!',
  task(1, 'Setze ä, e, äu oder eu ein. Schreibe das ganze Wort noch einmal auf die Linie.', t61) +
  task(2, 'Setze den Laut ein. Schreibe ein verwandtes Wort mit a oder au auf. Findest du keins, mache einen Strich.', t62, 'tight'))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
l1 = sol(1, 'Umlaut-Zauber', f'<p><b>Aufgabe 1:</b> {J(full(g, l) for e, b, g, l in a1)}</p><p><b>Aufgabe 2:</b> {J(f"{b} – {h} {s}" for e, b, h, s in a2)}</p>'
  '<p><b>Aufgabe 3:</b> Eigene Wörter, zum Beispiel: Gast – viele Gäste · Schrank – viele Schränke · Traum – viele Träume</p>')
REL2 = {'B_cker': 'backen', 'R_ber': 'rauben', 'k_lter': 'kalt', 'tr_men': 'Traum'}
no = lambda l: 'kein verwandtes Wort mit ' + ('au' if len(l) == 2 else 'a')
l2 = sol(2, 'Wortfamilien-Suche', '<p><b>Aufgabe 1:</b> ' + J(f"{full(w, l)} ({REL2.get(w, 'keins passt')})" for e, w, l, os in h2) + '</p>'
  '<p><b>Aufgabe 2:</b> ' + J(f"{full(w, l)} ({r or '–'})" for e, w, l, r in w2) + '</p>')
ab3 = [('die Äpfel','der Apfel'),('die Kräuter','das Kraut'),('die Gläser','das Glas'),('die Räder','das Rad'),('das Kätzchen','die Katze'),('die Hähne','der Hahn'),('die Bräute','die Braut'),('die Bänder','das Band')]
mw3 = ['der Käse','der Bär','das Mädchen','der März','die Säge','der Käfer','die Säule']
l3 = sol(3, 'Merkwort-Körbe', f'<p><b>Aufgabe 1</b> (gelb): {J(mw3)}</p><p><b>Aufgabe 2:</b> Ableiten: {J(f"{w} ← {r}" for w, r in ab3)}. Merkwörter: siehe Aufgabe 1.</p>')
l4 = sol(4, 'Lücken-Blitz', '<p><b>Aufgabe 1:</b> ' + J(full(w, l) + (f' ({r})' if r else '') for w, l, r in w4) + '</p><p><b>Aufgabe 2:</b> ' +
  J(f'{K(k)}: ' + ', '.join(w.replace('_', l) for w, l, r in w4 if l == k) for k in CLS) + '</p>')
l5 = sol(5, 'Familien-Treffen', '<p><b>Aufgabe 1:</b> ' + J(f'<b>{h}:</b> ' + ', '.join(full(w, l) for w, m in ws if m) + ' (nicht verwandt: ' +
  ', '.join(full(w, o) for w, m in ws if not m) + ')' for h, l, ws, o in f5) + '</p><p><b>Aufgabe 2:</b> Eigener Satz, zum Beispiel: Der Verkäufer gibt der Käuferin das Brot.</p>')
l6 = sol(6, 'Schreib-Profi', '<p><b>Aufgabe 1:</b> ' + J(f"{full(next(t for t in s.split() if '_' in t).strip('.,!'), l)} ({r or '–'})" for s, l, w, r in s6) + '</p>'
  '<p><b>Aufgabe 2</b> (– bedeutet: kein verwandtes Wort mit a oder au): ' + J(f"{full(w, l)} ({r or '–'})" for w, l, r in w6) + '</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

write('ableiten', 'Übungsblätter: Ableiten – ä oder e, äu oder eu? (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps], extra_css=EXTRA)
