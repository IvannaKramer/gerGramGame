"""Übungsblätter Verlängern (b/p, d/t, g/k). Das Wortmaterial ist dasselbe wie in den sechs Spielen."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

PAIR = dict(b='pb', p='pb', d='pd', t='pd', g='pg', k='pg')
G = '<i class="g"></i>'
gap = lambda s: s.replace('_', G)                                   # Wort mit Lücke
plain = lambda e: re.sub(r'[\[\]]', '', e)                          # Verlängerung ohne Klammern
egap = lambda e: re.sub(r'\[.\]', G, e)                             # Verlängerung mit Lücke
col = lambda e: re.sub(r'\[(.)\]', lambda m: f'<b class="{PAIR[m.group(1)]}">{m.group(1)}</b>', e)
full = lambda w, l: w.replace('_', f'<b class="{PAIR[l]}">{l}</b>')  # Lösung, Buchstabe farbig
emo = lambda e: f'<span class="emo">{e}</span>'
ARR = '<span class="arr">→</span>'
MERK = 'Am Wortende klingt <b class="pb">b</b> wie p, <b class="pd">d</b> wie t und <b class="pg">g</b> wie k. '

EXTRA = '''
.pb{color:#1F57C3}.pd{color:#C22A63}.pg{color:#157A41}
.g{display:inline-block;width:5.5mm;border-bottom:.5mm solid #22304A;margin:0 .4mm}
.wr b,.box b,.sents b{font-weight:700}
.wr .w{font-weight:700}
.grid2{grid-template-columns:repeat(2,minmax(0,1fr))}
.wr .line{min-width:12mm}
.box2{border:.7mm solid #22304A;border-radius:3.5mm;padding:1.2mm .5mm 1.6mm;text-align:center;line-height:1.2}
.box2 .w{display:block;font-size:13.5pt;font-weight:700;white-space:nowrap}
.box2 small{display:block;font-size:9pt;color:#56657F;white-space:nowrap}
.grid5{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:3mm 2mm}
.cols6{display:grid;grid-template-columns:repeat(6,1fr);gap:2.5mm}
.cols6 .c{border:.6mm solid var(--c);border-radius:3mm;padding:0 1.5mm 3mm}
.cols6 h3{margin:0 -1.5mm;background:var(--c);color:#fff;font-size:15pt;padding:.5mm 2mm;text-align:center;border-radius:2.2mm 2.2mm 0 0}
.cb{--c:#2B6BE0}.cd{--c:#DE3A76}.cg{--c:#1A8C4B}
.connect .l{width:62mm;font-weight:700}.connect .r{width:48mm;font-weight:700}
.hrow{display:grid;grid-template-columns:38mm repeat(3,1fr);align-items:center;gap:3mm;height:10.6mm;font-size:14pt}
.hrow .w{font-weight:700;white-space:nowrap}
.hrow .o{border:.6mm solid #56657F;border-radius:99px;text-align:center;padding:.6mm 1mm;white-space:nowrap;font-size:13pt}
.sents p{height:11mm;white-space:nowrap}
.tight .wr{height:10.4mm}
.sents .line{flex:1;width:auto;min-width:30mm}
.sol ul{margin:0;padding:0}
'''

# ---------------- Blatt 1: Verlängerungs-Trick ----------------
a1 = [('🐕','Hun_','d','viele Hun·[d]e'),('🧺','Kor_','b','viele Kör·[b]e'),('⛺','Zel_','t','viele Zel·[t]e'),('⛰️','Ber_','g','viele Ber·[g]e'),
      ('🍋','gel_','b','gel·[b]e Zitronen'),('💪','star_','k','stär·[k]er'),('🙋','er fra_t','g','fra·[g]en'),('🐻','plum_','p','ein plum·[p]er Bär')]
a2 = [('🌳','Wal_','d','Wälder'),('🖼️','Bil_','d','Bilder'),('🍞','Bro_','t','Brote'),('🎩','Hu_','t','Hüte'),('🚂','Zu_','g','Züge'),('🦹','Die_','b','Diebe'),('🎁','Geschen_','k','Geschenke')]
t1 = '<div class="grid2">' + ''.join(f'<div class="wr">{emo(e)}{plain(x)} {ARR} <span class="w">{gap(w)}</span></div>' for e, w, l, x in a1) + '</div>'
t2 = '<div class="grid2">' + ''.join(f'<div class="wr">{emo(e)}<span class="w">{gap(w)}</span> {ARR} viele {L()}</div>' for e, w, l, x in a2) + '</div>'
t3 = '<div class="grid2">' + ''.join(f'<div class="wr">{L("s")} {ARR} viele {L()}</div>' for _ in range(4)) + '</div>'
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Verlängerungs-Trick', 'Verlängerungs-Trick',
  MERK + 'Der Trick: <b>Verlängere</b> das Wort und sprich es in Silben. Bei „Hun·de“ hörst du das <b class="pd">d</b>. Also schreibst du auch „Hund“ mit <b class="pd">d</b>.',
  task(1, 'Sprich das verlängerte Wort laut in Silben. Setze dann den fehlenden Buchstaben ein.', t1) +
  task(2, 'Verlängere selbst: Schreibe die Mehrzahl auf. Setze dann den fehlenden Buchstaben ein.', t2) +
  task(3, 'Finde eigene Wörter, die am Ende mit b, d oder g geschrieben werden. Schreibe sie mit ihrer Mehrzahl auf.', t3))

# ---------------- Blatt 2: Buchstaben-Körbe ----------------
w2 = [('🐴','Pfer_','d','viele Pfer·[d]e'),('🔭','Telesko_','p','viele Telesko·[p]e'),('🏰','Bur_','g','viele Bur·[g]en'),('⛵','Boo_','t','viele Boo·[t]e'),('🐄','Kal_','b','viele Käl·[b]er'),
      ('🤒','kran_','k','ein kran·[k]es Kind'),('🌙','Mon_','d','viele Mon·[d]e'),('🌈','bun_','t','bun·[t]e Farben'),('✈️','Flugzeu_','g','viele Flugzeu·[g]e'),('🪄','Zaubersta_','b','viele Zauberstä·[b]e'),
      ('👗','Klei_','d','viele Klei·[d]er'),('🥤','Geträn_','k','viele Geträn·[k]e'),('🧔','Bar_','t','viele Bär·[t]e'),('🩹','es kle_t','b','kle·[b]en'),('🐦','er flie_t','g','flie·[g]en')]
bx = '<div class="grid5">' + ''.join(f'<div class="box2"><span class="w">{gap(w)}</span><small>{egap(x)}</small></div>' for e, w, l, x in w2) + '</div>'
c6 = '<div class="cols6">' + ''.join(f'<div class="c {c}"><h3>{l}</h3>' + L('f') * 3 + '</div>' for l, c in [('b','cb'),('p','cb'),('d','cd'),('t','cd'),('g','cg'),('k','cg')]) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Buchstaben-Körbe', 'Buchstaben-Körbe',
  'Unter jedem Wort steht die <b>Verlängerung</b>. Sprich sie laut in Silben: „Pfer·de“. Nach dem Punkt hörst du den Buchstaben, der fehlt.',
  task(1, 'Welcher Buchstabe fehlt: b, p, d, t, g oder k? Setze ihn im Wort und in der Verlängerung ein.', bx) +
  task(2, 'Sortiere die Wörter aus Aufgabe 1 in die Körbe. Schreibe jedes Wort in die Spalte mit seinem Buchstaben.', c6))

# ---------------- Blatt 3: Verlängerungs-Memory ----------------
left = [('🖐️','Han_'),('🧳','Urlau_'),('🌍','Wel_'),('🌿','Zwei_'),('🚲','Ra_'),('🥛','er trin_t'),('🦉','klu_'),('🐘','Elefan_')]
right = ['klü·ger','Wel·ten','Rä·der','Hän·de','Elefan·ten','Urlau·be','Zwei·ge','trin·ken']
connect = '<div class="connect">' + ''.join(f'<div class="row"><span class="l">{emo(e)}{gap(w)}</span><span class="dot"></span><span class="gap"></span><span class="dot"></span><span class="r">{r}</span></div>' for (e, w), r in zip(left, right)) + '</div>'
w3 = [('🏖️','Stran_','viele'),('📅','Ta_','viele'),('🏭','Fabri_','viele'),('🔬','Mikrosko_','viele'),('✍️','sie schrei_t',''),('🔊','lau_','noch'),('🍕','hal_','eine')]
t32 = '<div class="grid2">' + ''.join(f'<div class="wr">{emo(e)}<span class="w">{gap(w)}</span> {ARR} {h} {L("m")}</div>' for e, w, h in w3) + '</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Verlängerungs-Memory', 'Verlängerungs-Memory',
  'Nomen verlängerst du mit der <b>Mehrzahl</b> (Hand → Hän·de), Verben mit der <b>Grundform</b> (sie schreibt → schrei·ben). Adjektive kannst du <b>steigern</b> (klug → klü·ger).',
  task(1, 'Welche Verlängerung gehört zu welchem Wort? Verbinde mit einer Linie. Setze dann links den fehlenden Buchstaben ein.', connect) +
  task(2, 'Schreibe die Verlängerung auf. Setze dann den fehlenden Buchstaben ein. (Bei „halb“: eine … Pizza)', t32))

# ---------------- Blatt 4: Welches Wort hilft? ----------------
h4 = [('er gi_t',['du gi_st','ge_en','er ga_']),('der Freun_',['Freun_e','Freun_schaft','freun_lich']),('das Wer_',['Wer_zeug','Wer_statt','Wer_e']),
      ('die Zei_',['Zei_schrift','Zei_en','Mahlzei_']),('der Stau_',['stau_ig','Stau_sauger','Stau_tuch']),('sie trä_t',['du trä_st','er tru_','tra_en']),
      ('gesun_',['Gesun_heit','gesün_er','ungesun_']),('der Pie_matz',['pie_en','Pie_ton','der Pie_s']),('der Schran_',['Schran_tür','Kleiderschran_','Schrän_e']),
      ('al_',['al_modisch','äl_er','ural_'])]
t41 = ''.join(f'<div class="hrow"><span class="w">{gap(w)}</span>' + ''.join(f'<span class="o">{gap(o)}</span>' for o in os) + '</div>' for w, os in h4)
w4 = ['sie blei_t','der Rau_','das Fel_','wil_','das Wor_','der Mu_','der We_','er sa_t','sie den_t','das Vol_']
t42 = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="w">{gap(w)}</span> {ARR} {L()}</div>' for w in w4) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Welches Wort hilft?', 'Welches Wort hilft?',
  'Eine <b>Verlängerung</b> hilft nur, wenn nach der Lücke ein <b>Selbstlaut</b> kommt (a, e, i, o, u, ä, ö, ü). Dann beginnt mit dem Buchstaben eine neue Silbe und du hörst ihn: ge·<b class="pb">b</b>en. Bei „du gibst“ hörst du ihn nicht.',
  task(1, 'Nur eins der drei Wörter hilft dir. Kreise es ein. Setze dann überall in der Zeile den fehlenden Buchstaben ein.', t41) +
  task(2, 'Schreibe eine Verlängerung auf, die dir hilft. Setze dann den fehlenden Buchstaben ein.', t42, 'tight'))

# ---------------- Blatt 5: Grundform-Trick ----------------
s5 = ['Tim ü_t jeden Tag Klavier.','Der Busfahrer hu_t dreimal.','Der Hund ja_t die Katze.','Mama par_t das Auto vor dem Haus.','Papa schie_t den Kinderwagen.',
      'Oma win_t uns zum Abschied.','Emma zei_t mir ihr Zimmer.','Jonas pum_t den Ball auf.','Mama erlau_t uns ein Eis.','Der Müll stin_t.']
t51 = '<div class="sents">' + ''.join(f'<p><span>{gap(s)}</span> <span class="clue">Grundform:</span> {L()}</p>' for s in s5) + '</div>'
v5 = [('er grä_t','er'),('sie glau_t','sie'),('sie lo_t','sie'),('er pie_t','er'),('er sä_t','er'),('er fe_t','er'),('er stei_t','er'),('er lü_t','er'),('er qua_t','er'),('sie schen_t','sie')]
t52 = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="w">{gap(w)}</span> {ARR} {L()}</div>' for w, _ in v5) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Grundform-Trick', 'Grundform-Trick',
  'Auch mitten im Wort klingt <b class="pb">b</b> vor einem t wie p und <b class="pg">g</b> wie k. Bilde die <b>Grundform</b> und sprich sie in Silben: er gibt → ge·<b class="pb">b</b>en, sie fragt → fra·<b class="pg">g</b>en, er denkt → den·<b class="pg">k</b>en.',
  task(1, 'Schreibe die Grundform des Verbs auf. Setze dann im Satz b, p, g oder k ein.', t51) +
  task(2, 'Schreibe die Grundform auf. Setze dann den fehlenden Buchstaben ein.', t52))

# ---------------- Blatt 6: Fehler-Detektiv ----------------
s6 = ['Zum Abentbrot gibt es Käse und Tomaten.','Im Mäppchen liegen zwölf bunte Farpstifte.','An der Tangstelle kauft Mama ein Eis.','Der Postbote bringt ein großes Paked.',
      'Am Freitag macht die Klasse einen Ausfluk.','Im Stau gab es ein lautes Hubkonzert.','Die Schiltkröte frisst gern Salat.','Heute ist das Wetter kalt und trüp.',
      'Im Radio läuft schöne Musig.','Im Beet wächst viel Unkraud.']
t61 = '<div class="sents">' + ''.join(f'<p><span>{s}</span> {L()}</p>' for s in s6) + '</div>'
w6 = [('Lie_ling','lieben'),('Er_beeren','Erde'),('Schla_zeug','schlagen'),('Len_rad','lenken'),('Gol_fisch','golden'),('Erle_nis','erleben'),('aufgepum_t','pumpen'),('Plane_','Planeten'),('Zwer_','Zwerge'),('Tei_','Teige')]
t62 = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="w">{gap(w)}</span> <span class="clue">Beweis:</span> {L()}</div>' for w, _ in w6) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Fehler-Detektiv', 'Fehler-Detektiv',
  'Zerlege lange Wörter und verlängere den Teil mit dem schwierigen Buchstaben: <b>Abend</b>brot → die A·ben·<b class="pd">d</b>e, <b>Tank</b>stelle → tan·<b class="pg">k</b>en.',
  task(1, 'In jedem Satz ist ein Wort falsch geschrieben. Unterstreiche es und schreibe es richtig auf die Linie.', t61) +
  task(2, 'Setze den fehlenden Buchstaben ein. Schreibe als Beweis ein Wort auf, bei dem du den Buchstaben deutlich hörst.', t62, 'tight'))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
J = ' · '.join
l1 = sol(1, 'Verlängerungs-Trick', f'<p><b>Aufgabe 1:</b> {J(full(w, l) for e, w, l, x in a1)}</p><p><b>Aufgabe 2:</b> {J(f"{full(w, l)} – viele {x}" for e, w, l, x in a2)}</p><p><b>Aufgabe 3:</b> Eigene Wörter, zum Beispiel: Kind – viele Kinder · Weg – viele Wege · Stab – viele Stäbe</p>')
order = 'bpdtgk'
l2 = sol(2, 'Buchstaben-Körbe', f'<p><b>Aufgabe 1:</b> {J(f"{full(w, l)} ({col(x)})" for e, w, l, x in w2)}</p><p><b>Aufgabe 2:</b> ' +
  J(f'<b class="{PAIR[k]}">{k}:</b> ' + ', '.join(w.replace('_', l) for e, w, l, x in w2 if l == k) for k in order) + '</p>')
sol3 = [('Han_','d','Hän·de'),('Urlau_','b','Urlau·be'),('Wel_','t','Wel·ten'),('Zwei_','g','Zwei·ge'),('Ra_','d','Rä·der'),('er trin_t','k','trin·ken'),('klu_','g','klü·ger'),('Elefan_','t','Elefan·ten')]
sol3b = [('Stran_','d','viele Strände'),('Ta_','g','viele Tage'),('Fabri_','k','viele Fabriken'),('Mikrosko_','p','viele Mikroskope'),('sie schrei_t','b','schreiben'),('lau_','t','noch lauter'),('hal_','b','eine halbe Pizza')]
l3 = sol(3, 'Verlängerungs-Memory', f'<p><b>Aufgabe 1:</b> {J(f"{full(w, l)} – {x}" for w, l, x in sol3)}</p><p><b>Aufgabe 2:</b> {J(f"{full(w, l)} – {x}" for w, l, x in sol3b)}</p>')
sol4 = [('er gi_t','b','geben'),('der Freun_','d','Freunde'),('das Wer_','k','Werke'),('die Zei_','t','Zeiten'),('der Stau_','b','staubig'),('sie trä_t','g','tragen'),('gesun_','d','gesünder'),('der Pie_matz','p','piepen'),('der Schran_','k','Schränke'),('al_','t','älter')]
sol4b = [('sie blei_t','b','bleiben'),('der Rau_','b','rauben, Räuber'),('das Fel_','d','Felder'),('wil_','d','wilder, wilde Tiere'),('das Wor_','t','Wörter'),('der Mu_','t','mutig'),('der We_','g','Wege'),('er sa_t','g','sagen'),('sie den_t','k','denken'),('das Vol_','k','Völker')]
l4 = sol(4, 'Welches Wort hilft?', f'<p><b>Aufgabe 1</b> (eingekreist wird die Verlängerung): {J(f"{full(w, l)} – {x}" for w, l, x in sol4)}</p><p><b>Aufgabe 2</b> (zum Beispiel): {J(f"{full(w, l)} – {x}" for w, l, x in sol4b)}</p>')
sol5 = [('üben','ü_t','b'),('hupen','hu_t','p'),('jagen','ja_t','g'),('parken','par_t','k'),('schieben','schie_t','b'),('winken','win_t','k'),('zeigen','zei_t','g'),('pumpen','pum_t','p'),('erlauben','erlau_t','b'),('stinken','stin_t','k')]
sol5b = [('er grä_t','b','graben'),('sie glau_t','b','glauben'),('sie lo_t','b','loben'),('er pie_t','p','piepen'),('er sä_t','g','sägen'),('er fe_t','g','fegen'),('er stei_t','g','steigen'),('er lü_t','g','lügen'),('er qua_t','k','quaken'),('sie schen_t','k','schenken')]
l5 = sol(5, 'Grundform-Trick', f'<p><b>Aufgabe 1:</b> {J(f"{x} – {full(w, l)}" for x, w, l in sol5)}</p><p><b>Aufgabe 2:</b> {J(f"{full(w, l)} – {x}" for w, l, x in sol5b)}</p>')
sol6 = [('Aben_brot','d','Abende'),('Far_stifte','b','Farbe'),('Tan_stelle','k','tanken'),('Pake_','t','Pakete'),('Ausflu_','g','Ausflüge'),('Hu_konzert','p','hupen'),('Schil_kröte','d','Schilder'),('trü_','b','trübes Wetter'),('Musi_','k','Musiker'),('Unkrau_','t','Kräuter')]
sol6b = [(w, l, x) for (w, x), l in zip(w6, 'bdgkdbptgg')]
l6 = sol(6, 'Fehler-Detektiv', f'<p><b>Aufgabe 1:</b> {J(f"{full(w, l)} ({x})" for w, l, x in sol6)}</p><p><b>Aufgabe 2</b> (Beweiswörter zum Beispiel): {J(f"{full(w, l)} – {x}" for w, l, x in sol6b)}</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

write('verlaengern', 'Übungsblätter: Verlängern – b oder p, d oder t, g oder k? (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps], extra_css=EXTRA)
