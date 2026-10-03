#!/bin/bash
# Aufruf: shot.sh <thema> <datei.html> <modus> <breite,höhe> <ausgabe.png>
#   modus: start | game (stoppt nach 3 gelösten Aufgaben) | play (bis zum Erfolgsbildschirm). Immer hell + ohne Animationen.
cd "$(dirname "$0")/.."
B=60000; [ "$3" = play ] && B=1500000; [ "$3" = start ] && B=3000
timeout 120 google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --virtual-time-budget=$B --window-size=$4 --screenshot="$PWD/test/$1/$5" "file://$PWD/test/$1/$2#$3-still-light" >/dev/null 2>&1; ls -la "test/$1/$5" | awk '{print $5,$9}'
