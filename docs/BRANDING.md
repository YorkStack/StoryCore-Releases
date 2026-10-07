# Logos und Farbschemata

Aktueller Funktionsstand: **2.0.4 Vorabversion · 7. Oktober 2026**.
[Dokumentationsübersicht](../README.md#anleitungen).

Die Original-Assets stammen aus den mitgelieferten Marken-Assets und bleiben unverändert in `src/components/`:

- `OLLAMA-GUI-Logo-Light.png`: helles Prisma auf kühlem Weiß.
- `OLLAMA-GGUI-Logo-Dark.png`: leuchtendes Prisma auf dunklem Blau/Schwarz. Der originale Dateiname enthält tatsächlich „GGUI“.
- `OLLAMA-GUI-Icon-light.png`: separates helles App-Icon als Originaldatei.
- `OLLAMA-GUI-Logo-iconset.zip`: zehn Auflösungsvarianten eines App-Icons, keine Sammlung von Bedien-Icons.

`BrandLogo.tsx` verwendet beide Original-Logos. Die aktive Darstellung folgt dem `data-theme`-Attribut am Dokument. Lucide bleibt für funktionale Bedien-Icons zuständig.

## Farblogik

Die OKLCH-Variablen in `src/styles.css` definieren beide Varianten:

- Blau: Hauptaktionen und Fokusmarkierungen.
- Violett: aktive Navigation und ausgewählte Charakterkarte.
- Cyan: ergänzende Markenakzente und nicht ausgewählte Monogramme.
- Hell: kühles Weiß mit leichten Cyan-/Lavendelflächen.
- Dunkel: tiefe Blautöne, helle Schrift und leuchtende Akzente.

Erfolg, Fehler und Warnungen behalten eigene semantische Farben. Textflächen sind weitgehend einfarbig; die Lichtreflexe der Logos tauchen vor allem in Navigation und Kopfzeile auf. Aktionsbeschriftungen haben eine eigene Farbe, damit sie im dunklen Modus nicht versehentlich dunkel werden.

## Auswahl und Persistenz

In der Kopfzeile stehen **System**, **Hell** und **Dunkel** zur Auswahl. Standard ist System. `ThemePicker.tsx` speichert die Auswahl unter `still-appearance` im lokalen Browser-Speicher und reagiert auf Änderungen von `prefers-color-scheme`. Bei gesperrtem Browser-Speicher funktioniert die Auswahl für die aktuelle Sitzung weiter.

`public/theme-init.js` setzt das Farbschema vor dem Rendern der App. Das Skript bleibt extern, damit die bestehende Content Security Policy keine Inline-Skripte erlauben muss. Die Theme-Farben für die Browser-Kopfzeile werden beim Wechsel mitgeführt.

## Icons erneut vorbereiten

```sh
npm run icons:prepare
```

Das Skript übernimmt die vorhandenen PNG-Größen aus dem ZIP nach `public/icons/`. Die 16-/32-Pixel-Dateien dienen als Favicon; größere Varianten stehen für Web-App-Metadaten und Apple-Touch-Icon bereit. Auf macOS bündelt `iconutil` zusätzlich `assets/macos/AppIcon.icns`.

Die ICNS-Datei wird vom Tauri-Build als natives macOS-App-Icon verwendet. `npm run desktop:build` erzeugt App und DMG. Das Web-Manifest fügt ebenfalls keinen Service Worker oder Offline-Backend-Betrieb hinzu.

## App-Name

Der vom Nutzer gewählte Name ist **StoryCore**. Die bereitgestellten Prisma-Logos bleiben erhalten. Oberfläche, Fenstertitel, Dialogtitel, Web-Manifest und Mac-App verwenden den neuen Namen. Technische Formatkennungen und Datenpfade mit dem früheren Arbeitsnamen bleiben kompatibel.

## Native Fenster und Installation

Die Mac-App verwendet die nativen roten, gelben und grünen Fenstertasten. macOS-Overlays, etwa die Bildschirmfreigabe, können diesen Bereich zeitweise überlagern. ⌘W schließt das Fenster, ⌘M minimiert; die Vollbildfunktion steht im Fenstermenü zur Verfügung. Das Farbschema wird auch an Tauri für die native Fensterdarstellung weitergegeben.

Der neue Installer verwendet ein Terminalfenster mit beschrifteten Auswahlmöglichkeiten. Er ist keine zweite StoryCore-App und führt keine eigene Bibliothek. Für die Weitergabe bleiben die Original-Prisma-Assets in der App; Installationspakete und Dokumentation enthalten nur neutrale Beispiele. Details: [Mac-Installation](INSTALLATION-MAC.md).

## Abbildungen in den Anleitungen

Die beiden PDFs werden mit `scripts/build-guides.py` aus neutralen Demonstrationsaufnahmen unter `docs/guide-assets/` erzeugt. Die Suchansicht zeigt die echte Oberfläche; Demo-Antworten im Chat und Modellvergleich sind ausdrücklich als simuliert gekennzeichnet. Screenshots sind keine ausgelieferten Bibliothekseinträge oder Benchmark-Ergebnisse. Keine persönlichen Geschichten, Schlüssel oder Nutzerdaten in Dokumentationsbilder aufnehmen.

## Navigation und aktuelle Aufnahmen · 2.0.4

Startreihenfolge: Chat beginnen, Projekt erarbeiten, Story erstellen, Modelle vergleichen. Projekte und letzte Gespräche stehen links, Modelle/Mein Profil/Einstellungen/Updates unten. Storytelling bündelt Charaktere, Personas und Lorebooks. Dateiablagen übernehmen dieselben Flächen, Textgrößen und Aktionen in Chat, Story und Vergleich; projektweite Dateien liegen unter Wissen. `guide-assets/204-*.png` zeigt diese Oberfläche mit isolierten synthetischen Daten. Ältere Aufnahmen dokumentieren frühere Versionen und werden in aktuellen Anleitungen nicht mehr als aktuelle GUI verwendet.
