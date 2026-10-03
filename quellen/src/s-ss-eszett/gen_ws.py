"""Übungsblätter s, ss oder ß. Das Wortmaterial ist dasselbe wie in den sechs Spielen."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

K = {'s': 'ks', 'ss': 'kss', 'ß': 'ksz'}
G = '<i class="g"></i>'
gap = lambda s: s.replace('_', G)                                    # Wort mit Lücke
full = lambda w, l: w.replace('_', f'<b class="{K[l]}">{l}</b>')      # Lösung, Buchstabe farbig
plain = lambda w, l: w.replace('_', l)
emo = lambda e: f'<span class="emo">{e}</span>'
ARR = '<span class="arr">→</span>'
RX = re.compile(r'\[(ss|s|ß)\]')
J = ' · '.join

EXTRA = '''
.ks{color:#1F57C3}.kss{color:#C22A63}.ksz{color:#157A41}
.g{display:inline-block;width:6.5mm;border-bottom:.5mm solid #22304A;margin:0 .4mm}
.wr .w,.sents .w{font-weight:700}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 6mm}
.grid5{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:3mm 2mm}
.box2{border:.7mm solid #22304A;border-radius:3.5mm;padding:1.2mm .5mm 1.6mm;text-align:center;line-height:1.25}
.box2 .w{display:block;font-size:14pt;font-weight:700;white-space:nowrap}
.box2 small{display:block;font-size:9pt;color:#56657F;white-space:nowrap}
.cols{display:grid;gap:4mm}
.cols.c2{grid-template-columns:repeat(2,1fr)}.cols.c3{grid-template-columns:repeat(3,1fr)}
.cols .c{border:.6mm solid var(--c);border-radius:3mm;padding:0 3mm 3mm}
.cols h3{margin:0 -3mm;background:var(--c);color:#fff;font-size:13pt;padding:.8mm 2mm;text-align:center;border-radius:2.2mm 2.2mm 0 0}
.cs{--c:#2B6BE0}.css{--c:#DE3A76}.csz{--c:#1A8C4B}
.cols .line.f{height:9.5mm}
.story{margin:0 0 2.5mm;font-size:14pt;line-height:2}
.story b.t{font-family:'Grandstander',sans-serif;color:#56657F;font-size:12pt;margin-right:2mm}
.story .w{font-weight:700;white-space:nowrap}
.fam{width:100%;border-collapse:collapse;font-size:14pt}
.fam th{font-family:'Grandstander',sans-serif;font-size:11.5pt;color:#56657F;text-align:left;padding:0 3mm 1mm}
.fam td{height:10.5mm;padding:0 3mm;border-top:.4mm solid #D5E3F1;white-space:nowrap;font-weight:700}
.fam td:first-child{color:#56657F}
.fam small{font-weight:400;font-size:9.5pt}
.sents p{height:11mm;white-space:nowrap}
.sents .line{flex:1;width:auto;min-width:30mm}
.sol ul{margin:0;padding:0}
'''
MERK3 = ('Vokal <b>kurz</b> → <b class="kss">ss</b>. Vokal <b>lang</b> (oder au, ei, eu) und der s-Laut <b>zischt</b> scharf → <b class="ksz">ß</b>. '
         'Vokal lang und das s <b>summt</b> weich wie eine Biene → <b class="ks">s</b>.')

# ---------------- Blatt 1: Kurz oder lang? ----------------
w1 = [('🏞️','Flu_','ss'),('🦶','Fu_','ß'),('☕','Ta_e','ss'),('🛣️','Stra_e','ß'),('🔥','hei_','ß'),('💋','Ku_','ss'),('🔪','Me_er','ss'),('🍬','sü_','ß'),
      ('🔑','Schlü_el','ss'),('💐','Strau_','ß'),('🌰','Nu_','ss'),('💧','Wa_er','ss'),('🏕️','drau_en','ß'),('🏰','Schlo_','ss'),('🍝','So_e','ß')]
t1 = '<div class="grid3">' + ''.join(f'<div class="wr">{emo(e)}<span class="w">{gap(w)}</span></div>' for e, w, l in w1) + '</div>'
t2 = ('<div class="cols c2"><div class="c css"><h3>kurzer Vokal → ss</h3>' + L('f') * 8 + '</div>'
      '<div class="c csz"><h3>langer Vokal oder au, ei, eu → ß</h3>' + L('f') * 8 + '</div></div>')
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Kurz oder lang?', 'Kurz oder lang?',
  'Sprich das Wort laut. Klingt der Vokal <b>kurz</b> und knapp? Dann schreibst du <b class="kss">ss</b>: Fluss. Kannst du den Vokal <b>lang</b> ziehen? '
  'Dann schreibst du <b class="ksz">ß</b>: Fuuuß. Auch nach <b>au, ei, eu</b> steht ß und nie ss: heiß, Strauß.',
  task(1, 'Sprich jedes Wort laut. Setze ss oder ß ein.', t1) +
  task(2, 'Sortiere die Wörter aus Aufgabe 1. Schreibe jedes Wort in die passende Spalte.', t2))

# ---------------- Blatt 2: Drei Körbe ----------------
w2 = [('Na_e','s','a lang · s summt'),('Schü_el','ss','ü kurz'),('drei_ig','ß','ei · s zischt'),('Ho_e','s','o lang · s summt'),('Kompa_','ss','a kurz'),
      ('flei_ig','ß','ei · s zischt'),('Prinze_in','ss','e kurz'),('Ro_e','s','o lang · s summt'),('Klö_e','ß','ö lang · s zischt'),('kü_en','ss','ü kurz'),
      ('grü_en','ß','ü lang · s zischt'),('Kä_e','s','ä lang · s summt'),('Kla_e','ss','a kurz'),('bei_en','ß','ei · s zischt'),('Be_en','s','e lang · s summt')]
bx = '<div class="grid5">' + ''.join(f'<div class="box2"><span class="w">{gap(w)}</span><small>{h}</small></div>' for w, l, h in w2) + '</div>'
c3 = '<div class="cols c3">' + ''.join(f'<div class="c {c}"><h3>{h}</h3>' + L('f') * 5 + '</div>' for h, c in [('s · summt','cs'),('ss · kurz','css'),('ß · zischt','csz')]) + '</div>'
own = '<div class="grid3">' + ''.join(f'<div class="wr">{L()}</div>' for _ in range(3)) + '</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Drei Körbe', 'Drei Körbe', MERK3,
  task(1, 'Sprich jedes Wort laut. Die kleine Hilfe steht darunter. Setze s, ss oder ß ein.', bx) +
  task(2, 'Sortiere die Wörter aus Aufgabe 1 in die drei Körbe.', c3) +
  task(3, 'Finde zu jedem Korb ein eigenes Wort. Schreibe es auf.', own))

# ---------------- Blatt 3: Verlängerungs-Zauber ----------------
a1 = [('🏠','viele Häu_er','Hau_','s'),('🛢️','viele Fä_er','Fa_','ss'),('🛶','viele Flö_e','Flo_','ß'),('🏷️','viele Prei_e','Prei_','s'),
      ('💦','na_e Haare','na_','ss'),('🍢','viele Spie_e','Spie_','ß'),('🥅','viele Schü_e','Schu_','ss'),('🚿','gie_en','er gie_t','ß')]
a2 = [('🐭','Mau_','viele','s','Mäuse'),('🛂','Pa_','viele','ss','Pässe'),('🦒','gro_','noch','ß','größer'),('🥛','Gla_','viele','s','Gläser'),
      ('🦷','Bi_','viele','ss','Bisse'),('🏺','Gefä_','viele','ß','Gefäße'),('🌿','Gra_','viele','s','Gräser')]
t31 = '<div class="grid2">' + ''.join(f'<div class="wr">{emo(e)}<span>{gap(x)}</span> {ARR} <span class="w">{gap(w)}</span></div>' for e, x, w, l in a1) + '</div>'
t32 = '<div class="grid2">' + ''.join(f'<div class="wr">{emo(e)}<span class="w">{gap(w)}</span> {ARR} {h} {L()}</div>' for e, w, h, l, x in a2) + '</div>'
t33 = '<div class="grid2">' + ''.join(f'<div class="wr">{L("s")} {ARR} {L()}</div>' for _ in range(4)) + '</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Verlängerungs-Zauber', 'Verlängerungs-Zauber',
  'Am Wortende klingen s, ss und ß gleich. <b>Verlängere</b> das Wort und sprich es laut! <b>Summt</b> das s → <b class="ks">s</b>: Gras – Gräser. '
  '<b>Zischt</b> es nach kurzem Vokal → <b class="kss">ss</b>: Fass – Fässer. Zischt es nach langem Vokal → <b class="ksz">ß</b>: Floß – Flöße.',
  task(1, 'Sprich das lange Wort laut. Setze dann in beiden Wörtern s, ss oder ß ein.', t31) +
  task(2, 'Verlängere selbst: Schreibe das lange Wort auf die Linie. Setze dann links s, ss oder ß ein.', t32) +
  task(3, 'Finde eigene Wörter, die am Ende mit s, ss oder ß geschrieben werden. Schreibe sie mit dem langen Wort auf.', t33))

# ---------------- Blatt 4: Lücken-Geschichte ----------------
stories = [
  ('Im Zoo', 'Ein grauer E[s]el steht auf der Wie[s]e. Der Elefant hebt seinen langen Rü[ss]el. Das Zebra ist schwarz und wei[ß]. Vor dem Käfig mü[ss]en wir still sein.'),
  ('Bei Oma und Opa', 'Oma sitzt im Se[ss]el auf einem weichen Ki[ss]en. Auf dem Tisch steht eine Va[s]e mit Blumen. Opa mäht im Garten den Ra[s]en. Später kocht Oma für alle Grie[ß]brei.'),
  ('In der Schule', 'In der Pau[s]e spielen wir Fangen. Mir läuft der Schwei[ß] von der Stirn. Der Hausmeister kann das Tor aufschlie[ß]en. Ich schreibe meine Adre[ss]e auf einen Zettel. Morgen will ich noch be[ss]er rechnen.'),
  ('Im Märchen', 'Ein Rie[s]e wohnt in einer Höhle. Er ist gar nicht bö[s]e. In seinem Ke[ss]el kocht er Suppe. Die genie[ß]t er jeden Abend. Au[ß]erdem singt er gern.')]
def story_html(text):
    return ' '.join(f'<span class="w">{RX.sub(G, t)}</span>' if RX.search(t) else t for t in text.split(' '))
def story_words(text):
    return [(RX.sub('_', t.strip('.,!?')), RX.search(t).group(1)) for t in text.split(' ') if RX.search(t)]
t41 = ''.join(f'<p class="story"><b class="t">{ti}</b>{story_html(tx)}</p>' for ti, tx in stories)
t42 = '<div class="grid3">' + ''.join(f'<div class="wr">{L()}</div>' for _ in range(6)) + '</div>'
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Lücken-Geschichte', 'Lücken-Geschichte', MERK3,
  task(1, 'Lies die vier Geschichten. Sprich jedes Wort mit Lücke leise vor und setze s, ss oder ß ein.', t41) +
  task(2, 'In sechs Wörtern hast du ß eingesetzt. Schreibe diese Wörter noch einmal auf.', t42))

# ---------------- Blatt 5: Wortfamilien-Werkstatt ----------------
fams = [('lesen','',[('er lie_t','s'),('er la_','s'),('er hat gele_en','s')]),
        ('essen','',[('er i_t','ss'),('er a_','ß'),('er hat gege_en','ss')]),
        ('fließen','',[('es flie_t','ß'),('es flo_','ss'),('es ist geflo_en','ss')]),
        ('heißen','',[('er hei_t','ß'),('er hie_','ß'),('er hat gehei_en','ß')]),
        ('reisen','eine Reise machen',[('sie rei_t','s'),('sie rei_te','s'),('sie ist gerei_t','s')]),
        ('reißen','kaputtgehen',[('es rei_t','ß'),('es ri_','ss'),('es ist geri_en','ss')]),
        ('vergessen','',[('sie vergi_t','ss'),('sie verga_','ß')])]
t51 = ('<table class="fam"><tr><th>Grundform</th><th>heute</th><th>früher</th><th>schon vorbei</th></tr>' +
       ''.join(f'<tr><td>{h}{f" <small>({n})</small>" if n else ""}</td>' + ''.join(f'<td>{gap(f)}</td>' for f, l in fs) + ('<td></td>' * (3 - len(fs))) + '</tr>' for h, n, fs in fams) + '</table>')
s5 = [('Gestern a_ Tim drei Brötchen.','ß'),('Der Bach flo_ früher durch unser Dorf.','ss'),('Meine Freundin hei_t Lena.','ß'),
      ('Oma ist nach Italien gerei_t.','s'),('Plötzlich ri_ das Seil in der Mitte.','ss'),('Papa lie_t jeden Morgen die Zeitung.','s')]
t52 = '<div class="sents">' + ''.join(f'<p><span>{gap(s)}</span> {L()}</p>' for s, l in s5) + '</div>'
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Wortfamilien-Werkstatt', 'Wortfamilien-Werkstatt',
  'In einer Wortfamilie kann der s-Laut wechseln. Hör auf den Vokal: <b>e</b>ssen und er <b>i</b>sst klingen kurz → <b class="kss">ss</b>. '
  'Aber er <b>a</b>ß klingt lang → <b class="ksz">ß</b>. Bei einfachem <b class="ks">s</b> hilft die Grundform: er liest → le·sen. Dort summt das s.',
  task(1, 'Sprich jede Form laut. Setze s, ss oder ß ein.', t51) +
  task(2, 'Setze auch in diesen Sätzen s, ss oder ß ein. Schreibe das Wort mit der Lücke dann noch einmal auf die Linie.', t52))

# ---------------- Blatt 6: Schreib-Meister ----------------
s6 = [('Der Detektiv sucht einen {Bewei_}.','s'),('Die Hexe im Märchen ist alt und {hä_lich}.','ss'),('Die Tür geht nur nach {au_en} auf.','ß'),
      ('Papa {nie_t} laut, weil er Schnupfen hat.','s'),('Ich habe heute leider den Bus {verpa_t}.','ss'),('Gestern {sa_} ich lange am Schreibtisch.','ß'),
      ('Die bunte {Seifenbla_e} platzt in der Luft.','s'),('Ich möchte noch ein {bi_chen} spielen.','ss'),('Der kalte Tee schmeckt {scheu_lich}.','ß'),
      ('Um acht Uhr ist {Schlu_} mit Fernsehen.','ss')]
w6 = [('Krei_','s'),('Terra_e','ss'),('blo_','ß'),('Lo_','s'),('Flo_e','ss'),('gesto_en','ß'),('Gemü_e','s'),('Ka_e','ss'),('regelmä_ig','ß'),('Amei_e','s')]
sent = lambda s: re.sub(r'\{(.+?)\}', lambda m: f'<span class="w">{gap(m.group(1))}</span>', s)
word6 = lambda s: re.search(r'\{(.+?)\}', s).group(1)
t61 = '<div class="sents">' + ''.join(f'<p><span>{sent(s)}</span> {L()}</p>' for s, l in s6) + '</div>'
t62 = '<div class="grid2">' + ''.join(f'<div class="wr"><span class="w">{gap(w)}</span> {ARR} {L()}</div>' for w, l in w6) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Schreib-Meister', 'Schreib-Meister',
  'Prüfe in zwei Schritten. Vokal <b>kurz</b>? → <b class="kss">ss</b>: hässlich. Vokal <b>lang</b> oder au, ei, eu? Dann sprich das Wort oder seine Verlängerung laut. '
  '<b>Zischt</b> es → <b class="ksz">ß</b>: außen. <b>Summt</b> es → <b class="ks">s</b>: Beweis – Beweise.',
  task(1, 'In jedem Satz hat ein Wort eine Lücke. Schreibe das ganze Wort richtig auf die Linie.', t61) +
  task(2, 'Schreibe auch diese Wörter vollständig auf.', t62))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def by(ws):  # nach s, ss, ß sortiert
    return J(f'<b class="{K[k]}">{k}:</b> ' + ', '.join(plain(w, l) for w, l in ws if l == k) for k in ('s', 'ss', 'ß') if any(l == k for w, l in ws))
l1 = sol(1, 'Kurz oder lang?', f'<p><b>Aufgabe 1:</b> {J(full(w, l) for e, w, l in w1)}</p><p><b>Aufgabe 2:</b> {by([(w, l) for e, w, l in w1])}</p>')
l2 = sol(2, 'Drei Körbe', f'<p><b>Aufgabe 1:</b> {J(full(w, l) for w, l, h in w2)}</p><p><b>Aufgabe 2:</b> {by([(w, l) for w, l, h in w2])}</p>'
  '<p><b>Aufgabe 3:</b> Eigene Wörter, zum Beispiel: Dose (s) · Tasse (ss) · Straße (ß)</p>')
l3 = sol(3, 'Verlängerungs-Zauber', f'<p><b>Aufgabe 1:</b> {J(f"{full(x, l)} – {full(w, l)}" for e, x, w, l in a1)}</p>'
  f'<p><b>Aufgabe 2:</b> {J(f"{full(w, l)} – {h} {x}" for e, w, h, l, x in a2)}</p>'
  '<p><b>Aufgabe 3:</b> Eigene Wörter, zum Beispiel: Kreis – viele Kreise · Kuss – viele Küsse · Fuß – viele Füße</p>')
allw = [w for ti, tx in stories for w in story_words(tx)]
l4 = sol(4, 'Lücken-Geschichte', ''.join(f'<p><b>{ti}:</b> {J(full(w, l) for w, l in story_words(tx))}</p>' for ti, tx in stories) +
  f'<p><b>Aufgabe 2:</b> {", ".join(plain(w, l) for w, l in allw if l == "ß")}</p>')
l5 = sol(5, 'Wortfamilien-Werkstatt', '<p><b>Aufgabe 1:</b> ' + J(f'{h}: ' + ', '.join(full(f, l) for f, l in fs) for h, n, fs in fams) + '</p>' +
  f'<p><b>Aufgabe 2:</b> {J(full(s, l) for s, l in s5)}</p>')
l6 = sol(6, 'Schreib-Meister', f'<p><b>Aufgabe 1:</b> {J(full(word6(s), l) for s, l in s6)}</p><p><b>Aufgabe 2:</b> {J(full(w, l) for w, l in w6)}</p>')
ps = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 6', '', '', l1 + l2 + l3 + l4 + l5 + l6, solution=True)

assert len(allw) == 20 and sum(len(fs) for h, n, fs in fams) == 20
write('s-ss-eszett', 'Übungsblätter: s, ss oder ß? (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps], extra_css=EXTRA)
