# Master-Prompt: Lernspiel Deutsch, Klasse 4

## Rolle und Ziel
Du bist Lernspiel-Entwickler und erfahrene Grundschullehrkraft für Deutsch.
Erstelle ein interaktives Lernspiel für Kinder der 4. Klasse zum Thema **[THEMA]**
(Rechtschreibung und Grammatik, aktueller Lehrplan). Das Spiel gehört zu einer Reihe
und soll genauso aufgebaut sein und aussehen wie das fertige Spiel „Artikel-Match“.
Leitidee: viel üben, schnelle Erfolgserlebnisse, kein Frust.

## Eingaben
- Thema: [z. B. „Einzahl und Mehrzahl“]
- Referenz: [Link zum Artikel-Match-Artefakt] – übernimm Aufbau, Farben, Schriften und Code-Struktur
- Lernziel: [Was kann das Kind am Ende?]
- Merksatz: [z. B. „In der Mehrzahl heißt der Artikel immer die.“] – falls leer: formuliere einen kindgerechten
- Spielidee: [Mechanik für Phase 1–3 und Phase 4–5] – falls leer: siehe „Ablauf“
- Wortmaterial: [eigene Wörter oder Sätze] – falls leer: erstelle es selbst
- Kategorien und Farben: [z. B. Präsens = blau] – falls leer: lege 2–4 Kategorien mit gut unterscheidbaren Farben fest

## Ablauf
Ist keine Spielidee angegeben, schlage zuerst 3 Ideen vor (je 2–3 Sätze: Mechanik,
warum sie das Lernen fördert, wie Phase 4 und 5 auf Zeit aussehen). Nutze die Ideenbank
unten als Ausgangspunkt und warte auf meine Auswahl. Sonst baue direkt.

## Spielaufbau

### Startseite
- Titel, ein Satz Erklärung, Merksatz in einer „Tipp“-Box wie im Arbeitsheft
- 3 Beispiele, farbig nach Kategorie
- „So geht’s“ in 3 Schritten
- Phasenwahl mit Sternen; gesperrte Phasen zeigen, was vorher zu schaffen ist
- Punktestand (Sterne, Punkte, Extrapunkte) und „Fortschritt löschen“ (Bestätigung durch zweites Tippen)

### Phase 1–3 (Pflicht, je 10 Aufgaben)
- Phase 1 Einsteiger: mit Hilfe (Emoji-Bild, Beispiel oder Teillösung)
- Phase 2 Fortgeschritten: ohne Hilfe
- Phase 3 Profi: schwierigere, abstraktere oder seltenere Beispiele
- Freischaltung der Reihe nach, Fortschrittsanzeige („6 von 10 geschafft“)
- Punkte: 10 beim ersten Versuch, 5 danach
- Sterne: 0–1 Fehlversuche = 3, 2–4 = 2, mehr = 1
- Erfolgsbildschirm: Konfetti, Sterne nacheinander, alle Lösungen nach Kategorien als
  Übersicht, Buttons „Nächste Phase“, „Nochmal spielen“, „Zur Startseite“
- Nach Phase 3: „Spiel geschafft!“, Hinweis auf die Bonus-Phasen, „Alles neu starten“

### Phase 4 und 5 (freiwillige Bonus-Spiele auf Zeit, Extrapunkte)
- Zwei verschiedene, spannende Mechaniken (z. B. fallende Karten, Wörter bauen, Sortier-Rennen)
- Phase 4: 60 Sekunden, öffnet nach Phase 3; Phase 5: 90 Sekunden, öffnet nach dem ersten Spiel in Phase 4
- Vorher Anleitungskarte mit Beispiel, dann Countdown 3-2-1-Los
- Die Uhr läuft nur, während das Kind überlegt; beim Lesen der Lösung steht sie
- Serie: ab 3 richtigen +5 Bonus, ab 6 richtigen +10
- Falsche Aufgaben kommen 3–4 Aufgaben später wieder
- Steigende Schwierigkeit (schneller oder „Profi-Modus“ ohne Hilfe nach 6 richtigen)
- Pause-Knopf und Leertaste, automatische Pause beim Verlassen des Tabs
- Auswertung: Sterne nach Anzahl richtiger, „Neuer Rekord!“, beste Serie,
  Liste „Diese Wörter merkst du dir am besten“ mit richtiger Lösung

## Feedback (sehr wichtig)
- Richtig: kleine Erfolgsanimation, kurzer Ton, die vollständige richtige Form wird
  farbig gezeigt (z. B. „die Häuser“), damit sie sich einprägt
- Falsch: kein Fehler-Ton, kein rotes Kreuz; Karte wackelt kurz, freundlicher Satz
  („Fast! Probier es noch einmal.“), die Auswahl bleibt bestehen
- Nach 2 Fehlversuchen beim selben Item: Tipp mit Regel, die richtige Antwort leuchtet
- Eine Eulen-Figur (eigenes SVG) spricht in einer Sprechblase; Du-Form, kurze Sätze

## Bedienung
- Tippen (erst Karte, dann Ziel, oder umgekehrt) UND Drag & Drop mit Pointer Events
  (Maus, Finger, Stift)
- Tastatur: Tab/Enter; in Bonus-Phasen Zifferntasten für die Antworten
- Große Tippflächen (mind. 48 px); Antwortknöpfe auf dem Tablet immer erreichbar (sticky)

## Gestaltung
- Kindgerecht, bunt, freundlich; Hintergrund wie liniertes Heftpapier
- Schriften: „Andika“ (Leselernschrift) für Texte, „Grandstander“ für Überschriften,
  jeweils mit Ersatzschriften
- Wörter auf Karten mind. 24 px, Fließtext mind. 18–20 px
- Jede Kategorie hat eine feste Farbe im ganzen Spiel; Aufgabenkarten bleiben neutral weiß,
  damit die Farbe keine Lösung verrät
- Abgerundete Karten, sanfte Schatten, leichte Schräglage wie echte Papierkarten
- Heller und dunkler Modus; „prefers-reduced-motion“ beachten

## Technik
- Eine einzige HTML-Datei (HTML, CSS, JavaScript); keine externen Bilder, nur Emojis und eigene SVGs
- Responsive für Tablet (Hauptgerät), Desktop und Handy
- Kein Login, kein Server; Fortschritt, Rekorde und Ton-Einstellung im localStorage
  (mit try/catch, das Spiel muss auch ohne Speicher laufen)
- Töne mit der Web Audio API erzeugen, mit Ton-Schalter
- Alle Inhalte (Wortlisten, Lösungen, Tipps) als übersichtliche Datenliste am Anfang
  des Skripts, damit eine Lehrkraft sie leicht ändern kann

## Inhaltliche Qualität
- Jedes Beispiel eindeutig und nach Duden richtig; keine Wörter mit zwei möglichen
  Lösungen (z. B. der/das Keks), keine regionalen Varianten
- Wortschatz aus der Welt von 9- bis 10-Jährigen (Schule, Familie, Tiere, Freizeit)
- Lösungen gleichmäßig verteilt, nicht 8-mal dieselbe Antwort
- Prüfe am Ende jede Aufgabe und jede Lösung einzeln

## Abgabe
1. Veröffentliche das Spiel als Artefakt
2. Kurze Zusammenfassung: Mechanik jeder Phase, warum sie das Lernen fördert, Punkte- und Sterneregeln
3. Vollständige Wortliste mit Lösungen zur Kontrolle

## Ideenbank zur Themenliste
- Nomen erkennen: Nomen-Jagd (im Satz alle Nomen antippen); Bonus: Großschreib-Blitz
- Einzahl und Mehrzahl: Einzahl-Mehrzahl-Memory; Bonus: Plural-Falle (Mehrzahl = immer „die“)
- Bestimmte und unbestimmte Artikel: der/die/das zu ein/eine zuordnen; Bonus: Artikel-Tausch auf Zeit
- Nomen und ihre Wortbausteine: Wort-Werkstatt (frei + -heit = die Freiheit; -ung, -keit, -nis, -schaft)
- Zusammengesetzte Nomen: Wort-Baumeister (das letzte Wort bestimmt den Artikel)
- Die vier Fälle: Fall-Detektiv (mit Wer? Wessen? Wem? Wen? das Satzglied in den richtigen Fall-Kasten ziehen)
- Pronomen: Stellvertreter-Spiel (Nomen durch er, sie, es, ihm, ihn ersetzen)
- Adjektive: Gegenteil-Memory; Bonus: Adjektive im Text antippen
- Adjektive steigern: Siegertreppchen (groß, größer, am größten auf die Stufen ziehen)
- Verben: Grundform finden (er läuft → laufen); Bonus: Verben-Regen
- Zeitformen der Verben: Zeitmaschine (Sätze nach Präsens, Präteritum, Perfekt, Futur sortieren oder umwandeln)
- Satzglieder: Satz-Zug (Waggons mit der Umstellprobe verschieben)
- Subjekt und Prädikat: „Wer oder was?“ und „Was tut?“ – Satzteile farbig markieren
- Die Objekte: „Wem?“ oder „Wen oder was?“ – Dativ- und Akkusativobjekt sortieren
- Wörtliche Rede: Satzzeichen-Puzzle (Anführungszeichen, Doppelpunkt, Komma an die richtige Stelle ziehen)
