"""Erzeugt die Startseite index.html im Repo-Wurzelordner: alle Themen mit Links zu Spielen und Übungsblättern.
Aufruf: python3 quellen/src/landing.py"""
import json, pathlib

SRC = pathlib.Path(__file__).resolve().parent
REPO = SRC.parent.parent

# Reihenfolge und Nummern wie in Interaktive_Spiele_Deutsch_Klasse4.md: (Nr., Ordner, Titel, Bild, kurzer Satz)
GRAMMATIK = [
    (1, 'nomen-erkennen', 'Nomen erkennen', '🔎', 'Nomen von Verben und Adjektiven unterscheiden.'),
    (2, 'artikel', 'Artikel', '🧺', 'der, die oder das? Finde den richtigen Begleiter.'),
    (3, 'einzahl-mehrzahl', 'Einzahl und Mehrzahl', '🐕', 'Eins oder viele: die Mehrzahl richtig bilden.'),
    (4, 'zusammengesetzte-nomen', 'Zusammengesetzte Nomen', '🧩', 'Aus zwei Wörtern wird ein neues Nomen.'),
    (5, 'wortbausteine', 'Wortbausteine', '🧱', 'Wörter aus Vorsilbe, Wortstamm und Nachsilbe bauen.'),
    (6, 'vier-faelle', 'Die vier Fälle', '🕵️', 'Wer? Wessen? Wem? Wen? Den Fall bestimmen.'),
    (7, 'pronomen', 'Pronomen', '🔁', 'Nomen durch er, sie, es und Co. ersetzen.'),
    (8, 'adjektive-steigern', 'Adjektive steigern', '🏆', 'groß, größer, am größten.'),
    (9, 'zeitformen', 'Zeitformen der Verben', '⏰', 'Präsens, Präteritum, Perfekt und Futur.'),
    (10, 'satzglieder', 'Satzglieder', '🚂', 'Mit der Umstellprobe Satzglieder finden.'),
    (11, 'subjekt-praedikat-objekt', 'Subjekt, Prädikat, Objekte', '🖍️', 'Satzglieder mit Fragen bestimmen.'),
    (12, 'woertliche-rede', 'Wörtliche Rede', '💬', 'Anführungszeichen, Doppelpunkt und Komma setzen.'),
]
RECHTSCHREIBUNG = [
    (13, 'verlaengern', 'Verlängern', '↔️', 'b oder p, d oder t, g oder k? Verlängere das Wort.'),
    (14, 'ableiten', 'Ableiten', '🌳', 'ä oder e, äu oder eu? Suche ein verwandtes Wort.'),
    (15, 'kurze-lange-vokale', 'Kurze und lange Vokale', '👂', 'Kurz oder lang? Genau hinhören und richtig schreiben.'),
    (16, 's-ss-eszett', 's, ss oder ß?', '🐍', 'Summt oder zischt das s? Ist der Vokal kurz oder lang?'),
    (17, 'das-oder-dass', 'das oder dass?', '🔍', 'Mit der Ersatzprobe richtig entscheiden.'),
    (18, 'nominalisierungen', 'Nomen aus Verben und Adjektiven', '🔠', 'Wann schreibt man Verben und Adjektive groß?'),
    (19, 'komma', 'Das Komma', '✏️', 'Kommas bei Aufzählungen und Nebensätzen.'),
    (20, 'alphabet-ordnen', 'Alphabet und Wörterbuch', '📖', 'Wörter ordnen und im Wörterbuch finden.'),
]

def meta(path):
    out = {}
    for ln in path.read_text(encoding='utf-8').split('\n')[1:]:
        if ln.startswith('@@'):
            break
        if ': ' in ln:
            k, v = ln.split(': ', 1); out[k] = v
    return out

def topic(nr, slug, title, emoji, desc):
    if slug == 'artikel':   # älteres Einzelspiel mit 5 Phasen, ohne Übungsblatt
        return {'nr': nr, 'title': title, 'emoji': emoji, 'desc': desc, 'href': 'games/artikel-match.html', 'count': '1 Spiel',
                'keys': ['artikel-match-v1'], 'max': 15, 'sheet': ''}
    d = SRC / slug
    if not (d / 'topic.txt').exists() or not (REPO / 'games' / slug / 'index.html').exists():
        return None
    sheet = f'arbeitsblaetter/{slug}.pdf'
    return {'nr': nr, 'title': title, 'emoji': emoji, 'desc': desc, 'href': f'games/{slug}/index.html', 'count': '6 Spiele',
            'keys': [f"{slug}-{meta(d / f'g{n}.txt')['id']}-v1" for n in range(1, 7)], 'max': 18,
            'sheet': sheet if (REPO / sheet).exists() else ''}

parts = [('Grammatik', [t for t in (topic(*x) for x in GRAMMATIK) if t]),
         ('Rechtschreibung', [t for t in (topic(*x) for x in RECHTSCHREIBUNG) if t])]

ref = (REPO / 'games' / 'artikel-match.html').read_text(encoding='utf-8').split('\n')
css = '\n'.join('\n'.join(ref[a - 1:b]) for a, b in [(11, 98), (99, 103), (140, 143), (354, 356)]) + '\n' + (SRC / 'extra.css').read_text(encoding='utf-8')

html = '''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Deutsch-Lernspiele Klasse 4</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Grandstander:wght@600;800&display=swap">
<style>
{{CSS}}
/* ---------- Startseite ---------- */
.hero{margin-bottom:18px}
.total{display:inline-flex;align-items:center;gap:8px;background:var(--card);border:3px solid var(--card-edge);border-radius:999px;padding:4px 16px;font-weight:700;margin:0 0 6px}
.total svg{width:26px;height:26px}
.part{font-family:var(--f-display);font-weight:800;font-size:1.8rem;margin:34px 0 4px;line-height:1.15}
.part-lead{margin:0 0 14px;color:var(--ink-soft)}
.topics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
@media (max-width:900px){.topics{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:600px){.topics{grid-template-columns:1fr}.hero{align-items:flex-start}}
.topic{background:var(--card);border:3px solid var(--card-edge);border-radius:22px;padding:16px 18px;box-shadow:0 5px 0 var(--card-edge);display:flex;flex-direction:column;gap:4px}
.topic.started{border-color:var(--sun);box-shadow:0 5px 0 var(--sun-deep)}
.topic .top{display:flex;align-items:center;gap:10px}
.topic .emo{font-size:2.2rem;line-height:1}
.topic .num{font-weight:700;color:var(--ink-soft);font-size:1rem}
.topic h3{font-family:var(--f-display);font-weight:800;font-size:1.45rem;line-height:1.12;margin:2px 0 2px;overflow-wrap:anywhere}
.topic p{margin:0;color:var(--ink-soft);font-size:1.05rem}
.topic .got{display:flex;align-items:center;gap:6px;font-weight:700;font-size:1rem;margin-top:6px}
.topic .got svg{width:22px;height:22px}
.topic .links{display:flex;flex-wrap:wrap;gap:8px;margin-top:auto;padding-top:12px}
.topic a{font-weight:700;font-size:1rem;text-decoration:none;border-radius:999px;padding:8px 14px;min-height:48px;display:inline-flex;align-items:center;white-space:nowrap}
.topic a.play{background:var(--sun);color:var(--on-sun);box-shadow:0 3px 0 var(--sun-deep)}
.topic a.sheet{background:var(--card);color:var(--ink);border:3px solid var(--card-edge)}
.topic a:hover{transform:translateY(-2px)}
.note{margin:36px 0 0;color:var(--ink-soft);font-size:1rem;max-width:70ch}
</style>
</head>
<body>
<main class="wrap">
  <div class="hero">
    <span id="owl"></span>
    <div>
      <h1 class="title">Deutsch-Lernspiele</h1>
      <p class="subtitle">Grammatik und Rechtschreibung für die 4. Klasse. Such dir ein Thema aus!</p>
    </div>
  </div>
  <p class="total" id="total" hidden></p>
{{PARTS}}
  <p class="note">Für Lehrkräfte und Eltern: Zu jedem Thema gibt es sechs Spiele in drei Stufen (Anfänger, Fortgeschrittene, Profis) und Übungsblätter mit Lösungen zum Ausdrucken. Sterne und Punkte werden nur auf diesem Gerät gespeichert.</p>
</main>
<script>
(() => {
'use strict';
const TOPICS = {{TOPICS}};
const STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path class="star-on" d="M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z" stroke-width="1.6" stroke-linejoin="round"/></svg>';
function stars(key) {
  try {
    const p = JSON.parse(localStorage.getItem(key)) || {};
    const list = Array.isArray(p.stars) ? p.stars : [p.stars];
    return list.reduce((a, n) => a + Math.max(0, Math.min(3, n | 0)), 0);
  } catch (e) { return 0; }
}
let sum = 0, max = 0;
TOPICS.forEach(t => {
  const got = t.keys.reduce((a, k) => a + stars(k), 0);
  sum += got; max += t.max;
  const el = document.querySelector(`[data-nr="${t.nr}"]`);
  el.querySelector('.got').innerHTML = `${STAR}<span>${got} von ${t.max} Sternen</span>`;
  el.classList.toggle('started', got > 0);
  if (got > 0) el.querySelector('.play').textContent = 'Weiterspielen';
});
if (sum > 0) { const tot = document.getElementById('total'); tot.hidden = false; tot.innerHTML = `${STAR}<span>Du hast schon ${sum} von ${max} Sternen gesammelt!</span>`; }
document.getElementById('owl').outerHTML = `<svg class="owl" viewBox="0 0 120 120" aria-hidden="true">
  <path d="M30 42 L32 12 L52 30 Z" fill="var(--owl)"/><path d="M90 42 L88 12 L68 30 Z" fill="var(--owl)"/>
  <ellipse cx="60" cy="66" rx="40" ry="44" fill="var(--owl)"/>
  <ellipse cx="25" cy="76" rx="9" ry="21" fill="var(--owl-wing)" transform="rotate(14 25 76)"/>
  <ellipse cx="95" cy="76" rx="9" ry="21" fill="var(--owl-wing)" transform="rotate(-14 95 76)"/>
  <ellipse cx="60" cy="84" rx="25" ry="24" fill="var(--owl-belly)"/>
  <circle cx="44" cy="52" r="16" fill="#fff"/><circle cx="76" cy="52" r="16" fill="#fff"/>
  <circle cx="46" cy="54" r="7.5" fill="#22304A"/><circle cx="78" cy="54" r="7.5" fill="#22304A"/>
  <circle cx="48.5" cy="51.5" r="2.4" fill="#fff"/><circle cx="80.5" cy="51.5" r="2.4" fill="#fff"/>
  <path d="M54 63 L66 63 L60 73 Z" fill="#FFB627" stroke="#D98E00" stroke-width="1.5" stroke-linejoin="round"/>
  <ellipse cx="48" cy="109" rx="7" ry="4" fill="#FFB627"/><ellipse cx="72" cy="109" rx="7" ry="4" fill="#FFB627"/>
</svg>`;
})();
</script>
</body>
</html>
'''

def card(t):
    sheet = f'<a class="sheet" href="{t["sheet"]}">Übungsblätter</a>' if t['sheet'] else ''
    return f'''    <article class="topic" data-nr="{t['nr']}">
      <div class="top"><span class="emo" aria-hidden="true">{t['emoji']}</span><span class="num">Thema {t['nr']} · {t['count']}</span></div>
      <h3>{t['title']}</h3>
      <p>{t['desc']}</p>
      <div class="got"></div>
      <div class="links"><a class="play" href="{t['href']}">Spielen</a>{sheet}</div>
    </article>'''

LEADS = {'Grammatik': 'Wortarten, Zeitformen und Satzbau.', 'Rechtschreibung': 'Tricks und Regeln für das richtige Schreiben.'}
body = '\n'.join(f'  <h2 class="part">{name}</h2>\n  <p class="part-lead">{LEADS[name]}</p>\n  <div class="topics">\n' + '\n'.join(card(t) for t in ts) + '\n  </div>'
                 for name, ts in parts if ts)
all_topics = [{'nr': t['nr'], 'keys': t['keys'], 'max': t['max']} for _, ts in parts for t in ts]
html = html.replace('{{CSS}}', css).replace('{{PARTS}}', body).replace('{{TOPICS}}', json.dumps(all_topics, ensure_ascii=False))
(REPO / 'index.html').write_text(html, encoding='utf-8')
print('ok index.html mit', len(all_topics), 'Themen')
