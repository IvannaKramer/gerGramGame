"""Gemeinsame Bausteine für alle Übungsblätter (A4, druckfertig)."""
import pathlib, subprocess
OUT = pathlib.Path(__file__).resolve().parent.parent.parent / 'arbeitsblaetter'; OUT.mkdir(exist_ok=True)

OWL = '''<svg class="owl" viewBox="0 0 120 120" aria-hidden="true"><path d="M30 42 L32 12 L52 30 Z" fill="#8A5A3B"/><path d="M90 42 L88 12 L68 30 Z" fill="#8A5A3B"/><ellipse cx="60" cy="66" rx="40" ry="44" fill="#8A5A3B"/><ellipse cx="25" cy="76" rx="9" ry="21" fill="#6E4630" transform="rotate(14 25 76)"/><ellipse cx="95" cy="76" rx="9" ry="21" fill="#6E4630" transform="rotate(-14 95 76)"/><ellipse cx="60" cy="84" rx="25" ry="24" fill="#EBCDA5"/><circle cx="44" cy="52" r="16" fill="#fff"/><circle cx="76" cy="52" r="16" fill="#fff"/><circle cx="46" cy="54" r="7.5" fill="#22304A"/><circle cx="78" cy="54" r="7.5" fill="#22304A"/><circle cx="48.5" cy="51.5" r="2.4" fill="#fff"/><circle cx="80.5" cy="51.5" r="2.4" fill="#fff"/><path d="M54 63 L66 63 L60 73 Z" fill="#FFB627" stroke="#D98E00" stroke-width="1.5" stroke-linejoin="round"/><ellipse cx="48" cy="109" rx="7" ry="4" fill="#FFB627"/><ellipse cx="72" cy="109" rx="7" ry="4" fill="#FFB627"/></svg>'''
def face(mouth):
    return f'<svg class="face" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="17" fill="none" stroke="#22304A" stroke-width="2.4"/><circle cx="14" cy="16" r="2.2" fill="#22304A"/><circle cx="26" cy="16" r="2.2" fill="#22304A"/><path d="{mouth}" fill="none" stroke="#22304A" stroke-width="2.4" stroke-linecap="round"/></svg>'
FACES = face('M12 24 Q20 32 28 24') + face('M13 26 H27') + face('M12 28 Q20 21 28 28')
STAR = '<svg class="st" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z" fill="{f}" stroke="#D98E00" stroke-width="1.6" stroke-linejoin="round"/></svg>'
def stars(n): return ''.join(STAR.format(f='#FFB627' if i < n else '#fff') for i in range(3))
L = lambda w='': f'<span class="line {w}"></span>'

def page(nr, level, lv, title, game, merk, body, solution=False):
    foot = '' if solution else f'''<footer class="foot"><span class="how">So ging es mir: {FACES}</span>
      <span class="play">Das Spiel dazu: <b>{game}</b> · Meine Sterne im Spiel: {stars(0)}</span></footer>'''
    name = '' if solution else f'<div class="name"><span>Name: {L("m")}</span><span>Datum: {L("s")}</span></div>'
    merkbox = f'<div class="merk"><b class="tag">Merke</b><p>{merk}</p></div>' if merk else ''
    return f'''<section class="page{' sol' if solution else ''}">
  <header class="head">{OWL}<div class="ttl"><span class="lvl">{level} {stars(lv) if lv else ''}<i>{nr}</i></span><h1>{title}</h1></div>{name}</header>
  {merkbox}
  {body}
  {foot}
</section>'''
def task(n, text, inner, cls=''):
    return f'<div class="task {cls}"><h2><span class="n">{n}</span><span>{text}</span></h2>{inner}</div>'
E, M = (lambda s: f'<span class="ez">{s}</span>'), (lambda s: f'<span class="mz">{s}</span>')

CSS = '''
@page{size:A4;margin:0}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;background:#E9EEF5;color:#22304A;font-family:'Andika','Segoe UI',Arial,sans-serif;font-size:13.5pt;line-height:1.35}
.page{width:210mm;height:297mm;margin:8mm auto;padding:11mm 15mm 9mm;background:#fff;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 4px 18px rgba(34,48,74,.18);page-break-after:always;break-after:page}
.page:last-child{page-break-after:auto;break-after:auto}
@media print{body{background:#fff}.page{margin:0;box-shadow:none}}
h1,h2,h3,.lvl,.tag,.n{font-family:'Grandstander','Trebuchet MS',sans-serif}
.ez{color:#1F57C3;font-weight:700}.mz{color:#C22A63;font-weight:700}
.head{display:flex;align-items:center;gap:5mm;border-bottom:1.2mm dashed #D5E3F1;padding-bottom:3mm;margin-bottom:5mm}
.owl{width:21mm;flex:none}
.ttl{flex:1}
.lvl{display:inline-flex;align-items:center;gap:1.5mm;background:#EEE7FF;color:#5B34B0;font-weight:800;font-size:10.5pt;padding:.6mm 3.5mm;border-radius:99px}
.lvl i{font-style:normal;margin-left:2mm;padding-left:3mm;border-left:.5mm solid #B9A4EC}
.st{width:4.6mm;height:4.6mm}
h1{font-size:25pt;line-height:1.05;margin:1mm 0 0;font-weight:800}
.name{display:flex;flex-direction:column;gap:3mm;font-size:11.5pt;white-space:nowrap}
.line{display:inline-block;border-bottom:.45mm solid #56657F;width:46mm;height:1.25em;vertical-align:baseline}
.line.s{width:27mm}.line.m{width:38mm}.line.f{display:block;width:100%;height:10mm}.line.xl{display:block;width:100%;height:9mm}
.merk{position:relative;background:#FFF2CF;border:.8mm solid #FFB627;border-radius:4mm;padding:4.5mm 5mm 2.5mm;margin:1mm 0 5mm;font-size:12.5pt}
.merk p{margin:0}
.tag{position:absolute;top:-3.6mm;left:4mm;background:#FFB627;color:#2A2308;font-weight:800;font-size:11pt;padding:0 3.5mm;border-radius:99px;transform:rotate(-2deg)}
.task{margin-bottom:5mm}
.task h2{display:flex;align-items:flex-start;gap:3mm;font-family:'Andika',sans-serif;font-size:13.5pt;font-weight:700;margin:0 0 3mm;line-height:1.3}
.n{flex:none;width:8mm;height:8mm;border-radius:50%;background:#FFB627;color:#2A2308;font-weight:800;font-size:13pt;display:grid;place-items:center;margin-top:-.6mm}
.emo{display:inline-block;width:9mm;font-size:16pt;line-height:1;text-align:center;margin-right:1.5mm;vertical-align:-1mm}
.arr{color:#56657F;margin:0 1mm}
.connect{padding:0 6mm}
.connect .row{display:flex;align-items:center;height:12.5mm;font-size:15pt}
.connect .l{width:58mm}.connect .r{width:44mm;padding-left:4mm}
.connect .gap{flex:1}
.dot{width:3.4mm;height:3.4mm;border-radius:50%;background:#22304A;flex:none}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:0 8mm}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm 3.5mm}
.wr{height:11.5mm;display:flex;align-items:flex-end;gap:1.5mm;font-size:14pt;white-space:nowrap}
.wr .line{flex:1;width:auto;min-width:20mm}
.wr .emo{align-self:center}
.boxes{display:flex;flex-wrap:wrap;gap:3.5mm 4mm;justify-content:center}
.box{border:.7mm solid #22304A;border-radius:3.5mm;padding:2.2mm 5mm;font-size:15pt;font-weight:700;min-width:33mm;text-align:center}
.box:nth-child(odd){transform:rotate(-1.2deg)}.box:nth-child(3n){transform:rotate(1.4deg)}
.tab{width:100%;border-collapse:separate;border-spacing:0;font-size:14pt}
.tab th{font-family:'Grandstander',sans-serif;font-size:13pt;color:#fff;padding:1.5mm 4mm;text-align:left}
.tab .ezh{background:#2B6BE0;border-radius:3mm 0 0 0}.tab .mzh{background:#DE3A76;border-radius:0 3mm 0 0}
.tab td{height:11.2mm;border-bottom:.45mm solid #56657F;padding:0 4mm;width:46%}
.tab td.emo,.tab th:first-child{width:8%;border:none;padding:0}
.tab td + td + td{border-left:.45mm solid #56657F}
.brows{display:grid;gap:1.5mm}
.brow{display:grid;grid-template-columns:44mm repeat(3,1fr);align-items:center;gap:4mm;height:18mm}
.bw{font-size:14.5pt}
.ball{position:relative;justify-self:center;width:40mm;height:13.5mm;border:.7mm solid #22304A;border-radius:50%;display:grid;place-items:center;font-weight:700;font-size:13pt;margin-bottom:3mm}
.ball::after{content:"";position:absolute;left:50%;bottom:-3.6mm;width:.5mm;height:3mm;background:#22304A}
.store{border:.7mm dashed #56657F;border-radius:4mm;padding:2.5mm 4mm 3mm;display:flex;flex-wrap:wrap;gap:1mm 5.5mm;font-size:12.5pt;margin-bottom:4mm;align-items:baseline}
.store b{font-family:'Grandstander',sans-serif;width:100%;font-size:11pt;color:#56657F}
.cols5{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm}
.cols5 .c{border:.6mm solid var(--c);border-radius:3mm;padding:0 2mm 3mm;background:#fff}
.cols5 h3,.rule h3{margin:0 -2mm 0;background:var(--c);color:#fff;font-size:12.5pt;padding:1mm 2mm;text-align:center;border-radius:2.2mm 2.2mm 0 0}
.k1{--c:#2B6BE0}.k2{--c:#1A8C4B}.k3{--c:#DE3A76}.k4{--c:#7A4FD8}.k5{--c:#0B8791}
.sents p{margin:0;height:12.5mm;display:flex;align-items:flex-end;gap:2mm;font-size:14pt}
.sents .line{width:44mm}
.clue{color:#56657F;font-size:12pt}
.sents.two p{height:11.5mm;white-space:nowrap}
.sents.two .line{flex:1;width:auto}
.dotw{border:.6mm solid #D5E3F1;border-radius:3.5mm;padding:1.5mm 2mm 2mm;text-align:center;font-size:12pt;line-height:1.2}
.dotw .arr{display:block;font-size:9pt;line-height:1}
.dotw .big{display:block;font-size:16.5pt;font-weight:700;letter-spacing:.05em;line-height:1.55;white-space:nowrap}
.chg{display:inline-block;min-width:21mm;font-weight:700;color:#C22A63}
.rules{display:grid;grid-template-columns:1fr 1fr;gap:4mm 6mm}
.rule{border:.6mm solid var(--c);border-radius:3mm;padding:0 3mm 2.5mm}
.rule h3{margin:0 -3mm 0;display:flex;justify-content:space-between;align-items:baseline;padding:1mm 3mm;text-align:left}
.rule h3 small{font-family:'Andika',sans-serif;font-weight:400;font-size:9.5pt}
.rule .wr{height:9mm;font-size:12.5pt}
s{text-decoration-thickness:.4mm;font-weight:700}
.foot{margin-top:auto;border-top:1.2mm dashed #D5E3F1;padding-top:2.5mm;display:flex;justify-content:space-between;align-items:center;font-size:10pt;color:#56657F;flex:none}
.foot>span{white-space:nowrap}
.foot svg{vertical-align:middle;margin-left:1mm}
.face{width:8.5mm;height:8.5mm}
.foot b{color:#22304A}
.sol{font-size:10.5pt;line-height:1.3}
.solb{border:.5mm solid #D5E3F1;border-radius:3mm;padding:2mm 4mm;margin-bottom:3mm}
.solb h3{margin:0 0 1mm;font-size:12.5pt}
.solb p{margin:0 0 1.2mm}
'''

def write(slug, title, pages, extra_css=''):
    """Schreibt arbeitsblaetter/<slug>.html und druckt daraus <slug>.pdf (eine A4-Seite pro page)."""
    html = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Grandstander:wght@600;800&display=swap">
<style>{CSS}{extra_css}</style>
</head>
<body>
{chr(10).join(pages)}
</body>
</html>
'''
    f = OUT / f'{slug}.html'
    f.write_text(html, encoding='utf-8')
    subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=8000',
                    f'--print-to-pdf={OUT / (slug + ".pdf")}', f'file://{f}'], capture_output=True, timeout=120)
    print('ok', f, len(html))
