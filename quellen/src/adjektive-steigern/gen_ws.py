"""Übungsblätter Adjektive steigern."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ws_common import *

# Feste Farben der drei Stufen: Grundstufe blau, Vergleichsstufe grün, Höchststufe pink
G, V, H = (lambda s: f'<span class="g">{s}</span>'), (lambda s: f'<span class="v">{s}</span>'), (lambda s: f'<span class="h">{s}</span>')
EXTRA = '''
.g{color:#1F57C3;font-weight:700}.v{color:#14713C;font-weight:700}.h{color:#C22A63;font-weight:700}
.t3{width:100%;border-collapse:separate;border-spacing:0;font-size:14pt}
.t3 th{font-family:'Grandstander',sans-serif;font-size:12.5pt;color:#fff;padding:1.2mm 4mm;text-align:left;width:33.3%}
.t3 th small{font-family:'Andika',sans-serif;font-weight:400;font-size:10pt;margin-left:2mm}
.t3 .gh{background:#2B6BE0;border-radius:3mm 0 0 0}.t3 .vh{background:#1A8C4B}.t3 .hh{background:#DE3A76;border-radius:0 3mm 0 0}
.t3 td{height:10mm;border-bottom:.45mm solid #56657F;padding:0 4mm 1mm;vertical-align:bottom;font-weight:700}
.t3 td + td{border-left:.45mm solid #56657F}
.trps{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm 9mm}
.trp .mix{font-size:13.5pt;font-weight:700;white-space:nowrap}
.trp .mix i{font-style:normal;font-weight:400;color:#56657F;margin:0 1.5mm}
.trp .stp{display:flex;align-items:flex-end;gap:1.5mm;height:18mm}
.trp .stp span{flex:1;height:8mm;border-bottom:.9mm solid var(--c);position:relative}
.trp .stp span b{position:absolute;left:0;bottom:1mm;font-family:'Grandstander',sans-serif;font-size:9pt;color:#fff;background:var(--c);width:4.6mm;height:4.6mm;border-radius:50%;display:grid;place-items:center}
.trp .stp .l1{--c:#2B6BE0}.trp .stp .l2{--c:#1A8C4B;margin-bottom:5mm}.trp .stp .l3{--c:#DE3A76;margin-bottom:10mm}
.gs p{margin:0;font-size:14pt;line-height:10mm}
.gs.c p{line-height:9.2mm}
.gs .line{width:40mm;height:1.1em;vertical-align:baseline}
.gs .line.k{width:17mm}
.gs u{text-decoration-thickness:.35mm;text-underline-offset:1.2mm}
.gs .ch{display:inline-block;border:.5mm solid #56657F;border-radius:99px;padding:0 3mm;margin:0 1mm;line-height:7mm;font-weight:700}
.brow{height:13.6mm;grid-template-columns:38mm repeat(3,1fr);gap:3mm}
.ball{width:44mm;height:10.4mm;font-size:12.5pt;margin-bottom:2.4mm}
.ball::after{bottom:-2.6mm;height:2mm}
.dotw .big{font-size:16pt}
.sol{font-size:12pt}
.own .line{display:block;width:100%;height:10mm}
'''
def table(rows, hint=True):
    th = ('<tr><th class="gh">Grundstufe</th><th class="vh">Vergleichsstufe<small>-er</small></th><th class="hh">Höchststufe<small>am … -sten</small></th></tr>'
          if hint else '<tr><th class="gh">Grundstufe</th><th class="vh">Vergleichsstufe</th><th class="hh">Höchststufe</th></tr>')
    return '<table class="t3">' + th + ''.join(f'<tr><td>{G(a) if a else ""}</td><td>{V(b) if b else ""}</td><td>{H(c) if c else ""}</td></tr>' for a, b, c in rows) + '</table>'
def gaps(sents, cls=''):
    return f'<div class="gs {cls}">' + ''.join(f'<p>{s}</p>' for s in sents) + '</div>'
LN, LK = L(), L('k')

# ---------------- Blatt 1 ----------------
trp = [('🐭', ['am kleinsten', 'klein', 'kleiner']), ('🐘', ['größer', 'am größten', 'groß']), ('🚀', ['schnell', 'am schnellsten', 'schneller']),
       ('📢', ['am lautesten', 'lauter', 'laut']), ('🌸', ['schöner', 'schön', 'am schönsten']), ('🏰', ['am ältesten', 'alt', 'älter'])]
t1 = '<div class="trps">' + ''.join(f'<div class="trp"><div class="mix"><span class="emo">{e}</span>{"<i>·</i>".join(ws)}</div>'
     '<div class="stp"><span class="l1"><b>1</b></span><span class="l2"><b>2</b></span><span class="l3"><b>3</b></span></div></div>' for e, ws in trp) + '</div>'
tab1 = table([('lang', '', ''), ('', 'schwerer', ''), ('', '', 'am leichtesten'), ('hell', '', ''), ('', 'dicker', ''), ('', '', 'am lustigsten'), ('leise', '', '')])
p1 = page('Blatt 1', 'Für Anfänger', 1, 'Siegertreppchen', 'Siegertreppchen',
  f'Adjektive kann man steigern. Es gibt drei Stufen: die <b>Grundstufe</b> ({G("groß")}), die <b>Vergleichsstufe</b> mit -er ({V("größer")}) und die <b>Höchststufe</b> mit am und -sten ({H("am größten")}).',
  task(1, 'Stelle die Wörter auf die Treppe: Grundstufe auf Stufe 1, Vergleichsstufe auf Stufe 2, Höchststufe auf Stufe 3.', t1) +
  task(2, 'Ergänze die fehlenden Stufen.', tab1))

# ---------------- Blatt 2 ----------------
s2a = [f'🦁 Ein Löwe ist <u>gefährlicher</u> {LK} eine Katze.', f'😀 Lena ist <u>so fröhlich</u> {LK} Paul.', f'🚲 Das Fahrrad ist <u>billiger</u> {LK} das Auto.',
       f'💨 Heute ist es <u>so windig</u> {LK} gestern.', f'🎬 Der Film war <u>trauriger</u> {LK} das Buch.', f'🐕 Mein Hund ist <u>genauso hungrig</u> {LK} ich.',
       f'🐑 Ein Schaf ist <u>weicher</u> {LK} ein Igel.', f'🍎 Der Apfel ist <u>so saftig</u> {LK} die Birne.']
ch = '<span class="ch">wie</span><span class="ch">als</span>'
s2b = [f'Ein Bär ist kräftiger {ch} ein Fuchs.', f'Opa steht früher auf {ch} Oma.', f'Die Hose ist so schmutzig {ch} die Jacke.', f'Der Affe klettert geschickter {ch} der Hund.',
       f'Ich bin genauso durstig {ch} du.', f'Die Tasche ist so voll {ch} der Koffer.', f'Der Sonntag war sonniger {ch} der Samstag.']
own2 = f'<div class="own">{L()}{L()}</div>'
p2 = page('Blatt 2', 'Für Anfänger', 1, 'Wie oder als?', 'Wie oder als?',
  f'Sind zwei Dinge <b>gleich</b>? Dann sagst du <b>so … wie</b>: {G("so groß wie")}. Sind sie <b>verschieden</b>? Dann steht die Vergleichsstufe mit <b>als</b>: {V("größer als")}.',
  task(1, 'Setze <b>wie</b> oder <b>als</b> ein. Die unterstrichenen Wörter helfen dir.', gaps(s2a, 'c')) +
  task(2, 'Welches Wort ist richtig? Kreise es ein.', gaps(s2b, 'c')) +
  task(3, 'Vergleiche selbst: Schreibe einen Satz mit <b>so … wie</b> und einen Satz mit <b>als</b>.', own2))

# ---------------- Blatt 3 ----------------
bal = [('😴', 'müde', 'Vergleichsstufe', ['mehr müde', 'müder', 'müderer']), ('🧊', 'kühl', 'Höchststufe', ['am kühlsten', 'am kühlesten', 'am kühlersten']),
       ('😜', 'frech', 'Vergleichsstufe', ['frecherer', 'mehr frech', 'frecher']), ('🎀', 'hübsch', 'Höchststufe', ['am hübschsten', 'am hübschesten', 'am hübschersten']),
       ('🌙', 'still', 'Vergleichsstufe', ['stiller', 'stillerer', 'mehr still']), ('⛰️', 'steil', 'Vergleichsstufe', ['mehr steil', 'steilerer', 'steiler'])]
bl = '<div class="brows">' + ''.join(f'<div class="brow"><span class="bw"><span class="emo">{e}</span>{G(w)}</span>' + ''.join(f'<span class="ball">{o}</span>' for o in opts) + '</div>' for e, w, lv, opts in bal) + '</div>'
p3 = page('Blatt 3', 'Für Anfänger', 1, 'Stufe gesucht', 'Stufe gesucht',
  f'Die <b>Vergleichsstufe</b> endet auf <b>-er</b>: {V("wärmer")}. Die <b>Höchststufe</b> heißt <b>am … -sten</b>: {H("am wärmsten")}. Aus a, o, u wird manchmal ä, ö, ü.',
  task(1, 'Auf jeder Treppe fehlt eine Stufe. Schreibe das fehlende Wort auf.', table([(a, b, c) for a, b, c in [
      ('warm', '', 'am wärmsten'), ('jung', 'jünger', ''), ('stark', '', 'am stärksten'), ('tief', 'tiefer', ''), ('weit', 'weiter', ''),
      ('dünn', '', 'am dünnsten'), ('reich', '', 'am reichsten'), ('nett', 'netter', '')]])) +
  task(2, 'Nur ein Ballon zeigt die richtige Steigerungsform. Male ihn an.', bl))

# ---------------- Blatt 4 ----------------
dots = [('hart', 'harter'), ('klar', 'klarer'), ('scharf', 'scharfer'), ('toll', 'toller'), ('arm', 'armer'), ('faul', 'fauler'),
        ('dumm', 'dummer'), ('satt', 'satter'), ('grob', 'grober'), ('ruhig', 'ruhiger'), ('klug', 'kluger'), ('flach', 'flacher')]
dt = '<div class="grid4">' + ''.join(f'<div class="dotw">{G(a)}<span class="arr">↓</span><span class="big">{b}</span></div>' for a, b in dots) + '</div>'
w4 = ['kalt', 'schwach', 'kurz', 'krank', 'bunt', 'mutig', 'stolz', 'sanft']
wr4 = '<div class="grid2">' + ''.join(f'<div class="wr">{G(w)} <span class="arr">→</span> {H("am")} {L()}</div>' for w in w4) + '</div>'
tab4 = table([('lang', '', ''), ('laut', '', '')], hint=False)
p4 = page('Blatt 4', 'Für Fortgeschrittene', 2, 'Stufen-Werkstatt', 'Stufen-Werkstatt',
  f'Viele kurze Adjektive bekommen beim Steigern Pünktchen: kalt – {V("kälter")}. Aber nicht alle: klar – {V("klarer")}. Die Höchststufe endet auf <b>-sten</b>. Nach <b>t</b> und <b>z</b> heißt es meistens <b>-esten</b>: {H("am kältesten")}.',
  task(1, 'Hier fehlen bei der Vergleichsstufe alle Pünktchen. Setze sie, wo sie hingehören. Achtung: Sechs Wörter brauchen keine!', dt) +
  task(2, '<b>-sten</b> oder <b>-esten</b>? Schreibe die Höchststufe auf. Denk auch an die Pünktchen!', wr4) +
  task(3, 'Baue die ganze Treppe.', tab4))

# ---------------- Blatt 5 ----------------
c = lambda w: f'<span class="clue">({w})</span>'
s5a = [f'Die zweite Aufgabe ist so {LN} wie die erste. {c("schwierig")}', f'Das neue Buch ist {LN} als das alte. {c("spannend")}',
       f'Von allen Fächern finde ich Sport am {LN}. {c("interessant")}', f'Heute ist Finn so {LN} wie immer. {c("pünktlich")}',
       f'In unserer Klasse ist Fußball am {LN}. {c("beliebt")}', f'Auf dem Sofa ist es {LN} als auf dem Stuhl. {c("gemütlich")}',
       f'Der Film war genauso {LN} wie die Werbung. {c("langweilig")}', f'An meinem Geburtstag bin ich am {LN}. {c("glücklich")}',
       f'Die Hausaufgabe ist heute {LN} als gestern. {c("einfach")}']
s5b = [f'Die Bananen sind reifer {LK} die Birnen.', f'Der zweite Witz war genauso witzig {LK} der erste.', f'Diese Sängerin ist in unserem Land {LK} bekanntesten.',
       f'Ein Ring aus Gold ist wertvoller {LK} ein Ring aus Blech.', f'Die Suppe ist so salzig {LK} Meerwasser.', f'Bei Glatteis fährt Mama {LK} vorsichtigsten.',
       f'Der Bus kommt heute später {LK} sonst.', f'Der neue Lehrer ist so freundlich {LK} Frau Berg.', f'Vor einem Wettkampf ist guter Schlaf {LK} wichtigsten.']
p5 = page('Blatt 5', 'Für Fortgeschrittene', 2, 'Treppauf, treppab', 'Treppauf, treppab',
  f'Die kleinen Wörter verraten die Stufe: {G("so schnell wie")} (Grundstufe), {V("schneller als")} (Vergleichsstufe), {H("am schnellsten")} (Höchststufe).',
  task(1, 'Setze das Adjektiv in der richtigen Stufe ein.', gaps(s5a)) +
  task(2, 'Welches kleine Wort fehlt? Setze <b>wie</b>, <b>als</b> oder <b>am</b> ein.', gaps(s5b)))

# ---------------- Blatt 6 ----------------
tab6 = table([(w, '', '') for w in ['gut', 'viel', 'gern', 'hoch', 'nah', 'teuer', 'dunkel', 'sauer']], hint=False)
s6 = [f'Erdbeereis schmeckt mir {LN} als Zitroneneis. {c("gut")}', f'Wer am {LN} Punkte hat, gewinnt das Spiel. {c("viel")}',
      f'Ich spiele {LN} draußen als drinnen. {c("gern")}', f'Von allen Kindern springt Mia am {LN}. {c("hoch")}',
      f'Welche Bushaltestelle liegt am {LN}? {c("nah")}', f'Im Juli ist es bei uns am {LN}. {c("heiß")}',
      f'Reife Kirschen schmecken am {LN}. {c("süß")}']
det = '<div class="grid2">' + ''.join(f'<div class="wr"><s>{w}</s> <span class="arr">→</span> {L()}</div>' for w in ['am gutesten', 'höcher', 'teuerer', 'am spitzsten']) + '</div>'
p6 = page('Blatt 6', 'Für Profis', 3, 'Steigerungs-Meister', 'Steigerungs-Meister', '',
  task(1, 'Diese Adjektive haben beim Steigern eine Besonderheit. Schreibe die Vergleichsstufe und die Höchststufe auf.', tab6) +
  task(2, 'Setze das Adjektiv in der richtigen Stufe ein.', gaps(s6)) +
  task(3, 'Fehler-Detektiv: Diese Formen sind falsch. Schreibe sie richtig auf.', det))

# ---------------- Lösungen ----------------
def sol(n, title, items): return f'<div class="solb"><h3>Blatt {n}: {title}</h3>{items}</div>'
def tri(a, b, c): return f'{G(a)} – {V(b)} – {H(c)}'
def tris(rows): return ' · '.join(tri(*r) for r in rows)
l1 = sol(1, 'Siegertreppchen', '<p><b>Aufgabe 1:</b> ' + tris([('klein', 'kleiner', 'am kleinsten'), ('groß', 'größer', 'am größten'), ('schnell', 'schneller', 'am schnellsten'), ('laut', 'lauter', 'am lautesten'), ('schön', 'schöner', 'am schönsten'), ('alt', 'älter', 'am ältesten')]) + '</p>'
  '<p><b>Aufgabe 2:</b> ' + tris([('lang', 'länger', 'am längsten'), ('schwer', 'schwerer', 'am schwersten'), ('leicht', 'leichter', 'am leichtesten'), ('hell', 'heller', 'am hellsten'), ('dick', 'dicker', 'am dicksten'), ('lustig', 'lustiger', 'am lustigsten'), ('leise', 'leiser', 'am leisesten')]) + '</p>')
l2 = sol(2, 'Wie oder als?', f'<p><b>Aufgabe 1:</b> gefährlicher {V("als")} · so fröhlich {G("wie")} · billiger {V("als")} · so windig {G("wie")} · trauriger {V("als")} · genauso hungrig {G("wie")} · weicher {V("als")} · so saftig {G("wie")}</p>'
  f'<p><b>Aufgabe 2:</b> kräftiger {V("als")} · früher auf {V("als")} · so schmutzig {G("wie")} · geschickter {V("als")} · genauso durstig {G("wie")} · so voll {G("wie")} · sonniger {V("als")}</p>'
  '<p><b>Aufgabe 3:</b> Eigene Sätze, zum Beispiel: Mein Bruder ist so groß wie ich. · Ein Pferd ist schneller als ein Esel.</p>')
l3 = sol(3, 'Stufe gesucht', f'<p><b>Aufgabe 1:</b> {V("wärmer")} · {H("am jüngsten")} · {V("stärker")} · {H("am tiefsten")} · {H("am weitesten")} · {V("dünner")} · {V("reicher")} · {H("am nettesten")}</p>'
  f'<p><b>Aufgabe 2:</b> {V("müder")} · {H("am kühlsten")} · {V("frecher")} · {H("am hübschesten")} · {V("stiller")} · {V("steiler")}</p>')
l4 = sol(4, 'Stufen-Werkstatt', f'<p><b>Aufgabe 1:</b> <b>Mit Pünktchen:</b> {V("härter")}, {V("schärfer")}, {V("ärmer")}, {V("dümmer")}, {V("gröber")}, {V("klüger")}. <b>Ohne Pünktchen:</b> {V("klarer")}, {V("toller")}, {V("fauler")}, {V("satter")}, {V("ruhiger")}, {V("flacher")}.</p>'
  f'<p><b>Aufgabe 2:</b> {H("am kältesten")} · {H("am schwächsten")} · {H("am kürzesten")} · {H("am kränksten")} · {H("am buntesten")} · {H("am mutigsten")} · {H("am stolzesten")} · {H("am sanftesten")}</p>'
  '<p><b>Aufgabe 3:</b> ' + tris([('lang', 'länger', 'am längsten'), ('laut', 'lauter', 'am lautesten')]) + '</p>')
l5 = sol(5, 'Treppauf, treppab', f'<p><b>Aufgabe 1:</b> so {G("schwierig")} wie · {V("spannender")} als · am {H("interessantesten")} · so {G("pünktlich")} wie · am {H("beliebtesten")} · {V("gemütlicher")} als · genauso {G("langweilig")} wie · am {H("glücklichsten")} · {V("einfacher")} als</p>'
  '<p><b>Aufgabe 2:</b> reifer <b>als</b> · genauso witzig <b>wie</b> · <b>am</b> bekanntesten · wertvoller <b>als</b> · so salzig <b>wie</b> · <b>am</b> vorsichtigsten · später <b>als</b> · so freundlich <b>wie</b> · <b>am</b> wichtigsten</p>')
l6 = sol(6, 'Steigerungs-Meister', '<p><b>Aufgabe 1:</b> ' + tris([('gut', 'besser', 'am besten'), ('viel', 'mehr', 'am meisten'), ('gern', 'lieber', 'am liebsten'), ('hoch', 'höher', 'am höchsten'), ('nah', 'näher', 'am nächsten'), ('teuer', 'teurer', 'am teuersten'), ('dunkel', 'dunkler', 'am dunkelsten'), ('sauer', 'saurer', 'am sauersten')]) + '</p>'
  f'<p><b>Aufgabe 2:</b> {V("besser")} · am {H("meisten")} · {V("lieber")} · am {H("höchsten")} · am {H("nächsten")} · am {H("heißesten")} · am {H("süßesten")}</p>'
  f'<p><b>Aufgabe 3:</b> {H("am besten")} · {V("höher")} · {V("teurer")} · {H("am spitzesten")}</p>'
  '<p><b>Profi-Wissen:</b> Manche Adjektive kann man nicht steigern, weil es kein „mehr“ davon gibt, zum Beispiel <b>tot</b>, <b>leer</b> oder <b>fertig</b>.</p>')
ps1 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 1 bis 3', '', '', l1 + l2 + l3, solution=True)
ps2 = page('Für Lehrkräfte und Eltern', 'Lösungen', 0, 'Lösungen zu Blatt 4 bis 6', '', '', l4 + l5 + l6, solution=True)

write('adjektive-steigern', 'Übungsblätter: Adjektive steigern (Klasse 4)', [p1, p2, p3, p4, p5, p6, ps1, ps2], extra_css=EXTRA)
