#!/bin/bash
# Aufruf: test/run.sh <thema> [play]
# Baut games/<thema>/ aus src/<thema>/ und legt Testkopien in test/<thema>/ an.
# Mit "play" spielt Chrome jedes Spiel automatisch durch. Übungsblätter: python3 src/<thema>/gen_ws.py
cd "$(dirname "$0")/.."
T="$1"; python3 src/build.py "$T" >/dev/null || exit 1
SLUG=$(grep '^slug: ' "src/$T/topic.txt" | cut -d' ' -f2); mkdir -p "test/$T"
for f in "$PWD"/../games/$SLUG/[1-6]*.html; do b=$(basename $f); python3 - "$f" "test/$T/$b" "src/$T/steps.js" <<'PY'
import sys,pathlib
s=pathlib.Path(sys.argv[1]).read_text()
h=pathlib.Path('test/harness.js').read_text().replace('/*STEPS*/', pathlib.Path(sys.argv[3]).read_text())
pre="<script>if(location.hash){window.matchMedia=q=>({matches:/reduced-motion/.test(q)&&location.hash.includes('still'),addEventListener(){}});if(location.hash.includes('still'))document.write('<style>*,*::before,*::after{transition:none!important;animation:none!important}</style>');if(location.hash.includes('light'))document.documentElement.dataset.theme='light';}</script>"
s=s.replace('<style>',pre+'<style>',1).replace('</body>','<script>'+h+'</script></body>')
pathlib.Path(sys.argv[2]).write_text(s)
PY
[ "$2" = play ] && timeout 120 google-chrome --headless=new --no-sandbox --disable-gpu --virtual-time-budget=1500000 --dump-dom "file://$PWD/test/$T/$b" 2>/dev/null | grep -o '<title>.*</title>' | cut -c1-260
done
