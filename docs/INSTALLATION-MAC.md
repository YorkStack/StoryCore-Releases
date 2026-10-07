# StoryCore auf dem Mac installieren

Stand: **2.0.7 Beta / 2.0.4 stabil · 7. Oktober 2026**. Für Anwender ist der fertige Download vorgesehen; ein eigener Build ist optional.

**Bebilderte Kurzfassungen als PDF:** [Download und Installation (2 Seiten)](https://github.com/YorkStack/StoryCore-Releases/releases/download/v2.0.7/StoryCore-Installation-Mac.pdf) · [Erste Schritte (10 Seiten)](https://github.com/YorkStack/StoryCore-Releases/releases/download/v2.0.7/StoryCore-Erste-Schritte.pdf). Beide PDFs liegen auch direkt im Installer-ZIP/DMG und als einzelne Release-Downloads. Die App-Abbildungen verwenden eine separate neutrale Demo-Bibliothek; simulierte Vergleichsantworten sind kein Benchmark. Diese Beispiele werden nicht in die App eingebaut.

## Fertiges Installationspaket von GitHub

1. Öffne [den neuesten StoryCore-Release](https://github.com/YorkStack/StoryCore-Releases/releases/tag/v2.0.4). Die Downloads sind öffentlich und benötigen keinen GitHub-Zugang. Optional: [2.0.7 Beta](https://github.com/YorkStack/StoryCore-Releases/releases/tag/v2.0.7) ergänzt Updates unter /Applications mit macOS-Freigabe. 2.0.4 bleibt die stabile Standardversion.
2. Lade unter **Assets** das zur Version passende `StoryCore_<Version>_Mac-Installer.zip` herunter. Verwende für die Installation **nicht** GitHubs automatisch angebotene „Source code“-Archive.
3. Entpacke das ZIP und doppelklicke auf **Install-StoryCore.command**. Es öffnet sich ein Terminalfenster mit der geführten Prüfung und Installation. Die Datei `StoryCore.app` muss daneben liegen.
4. Lies die Prüfung. Falls Ollama fehlt oder noch nicht läuft, wähle einen der angebotenen Wege. Installiere anschließend StoryCore und öffne die App auf Wunsch direkt aus der Routine.
5. Unter **Modelle** ein kompatibles Modell herunterladen; dann **Verwenden**, **In Speicher laden** oder die erste Nachricht senden. Die App startet mit leerer Bibliothek und vier neutralen Generierungsprofilen.

Alternativ: `StoryCore_<Version>_aarch64.dmg` öffnen. Darin liegt dieselbe Installationsroutine. Die App lässt sich auch manuell in Programme ziehen; dabei findet keine Voraussetzungenprüfung statt. Verwende genau einen Installationsweg. Das ZIP/DMG enthält keine Modelle oder persönlichen Storys.

## Was die Routine prüft

| Prüfung | Verhalten |
| --- | --- |
| Betriebssystem | macOS 14 oder neuer für diese Installationsroutine und aktuelles Ollama. |
| Prozessor | Apple Silicon, also M-Serie; kein Intel-/Universal-Paket. Auch unter Rosetta wird die Hardware geprüft. |
| Arbeitsspeicher | Chip und eingebauter RAM werden angezeigt. Die spätere Modellauswahl berücksichtigt grobe RAM-Schätzungen. |
| Ollama installiert | Sucht im PATH, in `/Applications`, `~/Applications` sowie üblichen Homebrew-/CLI-Pfaden. |
| Ollama erreichbar | Prüft ausschließlich `http://127.0.0.1:11434/api/version`, mit Zeitlimit und ohne Proxy/Weiterleitungen. |
| App-Paket | Erwartete Bundle-ID, ARM64-Binärdatei und Integrität der Codesign-Signatur werden geprüft. Eine Ad-hoc-Signatur bestätigt keine Entwickleridentität. |
| Bestehende App | Eine laufende StoryCore-App muss mit ⌘Q beendet werden; sie wird nicht zwangsweise geschlossen. |
| Installationsziel | Neue Installation unter `~/Applications/StoryCore.app`; eine bestehende Installation unter `/Applications` wird dort aktualisiert, bei Bedarf mit macOS-Administratorfreigabe. Bei zwei Kopien stoppt die Routine mit einem Hinweis. |
| Update | Alte App wird als ZIP gesichert und geprüft. Die neue App wird zuerst separat kopiert und geprüft, dann umbenannt. Bei fehlgeschlagenem Austausch wird die vorherige App zurückgestellt. |

**Bei geschütztem /Applications:** Der interaktive Installer zeigt die macOS-Abfrage für Administrator-Zugangsdaten. `--yes` öffnet keinen versteckten Passwortdialog, sondern meldet den nötigen interaktiven Aufruf. Die Datei `install-macos.sh` muss neben der Routine bleiben. [Einmalige Reparatur bisher blockierter Updates](UPDATES.md#updates-unter-applications-ab-206-beta).

Node.js, npm, Rust, Xcode und Homebrew sind für die fertige App **nicht erforderlich**. Ollama und die Modellgewichte bleiben separate Komponenten. Die Hardwareprüfung und lokalen Daten werden nicht an einen Server übertragen.

## Wenn Ollama fehlt

Die Routine bietet an:

- **Offiziellen Download öffnen:** [Ollama für macOS](https://ollama.com/download/mac) installieren und Ollama öffnen; danach die StoryCore-Routine erneut starten.
- **Homebrew-Anleitung anzeigen:** Falls Homebrew bereits installiert ist, kannst du selbst `brew install --cask ollama` ausführen. Die Routine installiert weder Homebrew noch zusätzliche Software ungefragt.
- **Vorhandene Ollama-App starten** und anschließend die Verbindung erneut prüfen.
- **Ohne Ollama fortfahren:** StoryCore lässt sich schon installieren. Später Ollama starten oder unter **Einstellungen → Modellserver** eine lokale OpenAI-kompatible Laufzeit konfigurieren. Ohne erreichbaren Modellserver funktionieren Bibliotheken und Exporte, aber keine LLM-Ausgaben.

Ein anderer Ollama-Port oder ein eigener Installationspfad kann vom Standardcheck unentdeckt bleiben. Das ist kein Grund, Ollama ein zweites Mal zu installieren: Wähle „ohne Ollama fortfahren“ und konfiguriere die vorhandene lokale Adresse in StoryCore. Die Routine ändert keine bestehenden Server-Einstellungen und lädt keine Modellgewichte.

Ollama verlangt aktuell macOS 14 oder neuer, siehe [Herstelleranforderungen](https://docs.ollama.com/macos). Tauri deklariert im Projekt zwar ein Mindestziel von macOS 11, dies ist **keine Zusage**, dass das vollständige aktuelle Paket auf älteren Systemen läuft. Der verifizierte Rechner und Testumfang stehen im [Prüfprotokoll](VERIFICATION.md).

## Internetrecherche optional einrichten

Ollama und die Textgenerierung bleiben lokal. Für Websuche unter **Einstellungen → Web-Recherche** Tavily, Serper oder Brave wählen, dort der Kontoanleitung folgen und den eigenen API-Schlüssel eintragen. **Web-Recherche erlauben** aktivieren und speichern. Es wird weder ein Browser noch ein Container zusätzlich installiert; der Installer legt keine Suchkonten an und bringt keine Zugangsdaten mit.

Anschließend vor einer Anfrage im Chat, in Stories, Projektgesprächen oder im Modellvergleich die Recherche einschalten, Suchbegriffe eingeben, **Im Web suchen**, Quellen prüfen und senden. Nur die Suchbegriffe gehen an den Suchdienst. Anbieter können Kontingente und Kosten vorgeben. Einrichtung, Schlüsseltrennung und Fehlersuche: [Internetrecherche](WEB-RECHERCHE.md); vollständiger Einstieg: [Nutzung](NUTZUNG.md).

## macOS fragt nach einer Freigabe

Die aktuellen Builds sind **ad-hoc signiert und nicht Apple-notarisiert**. Eine vollständig warnungsfreie öffentliche Installation ist damit nicht zugesichert. Lade das Paket nur aus diesem Repository bzw. von einer dir bekannten Weitergabe.

Wenn macOS den Start blockiert, lies die Meldung und die [Apple-Anleitung zum Öffnen vertrauenswürdiger Apps](https://support.apple.com/de-de/102445). Die Freigabe erfolgt bei Bedarf manuell unter **Systemeinstellungen → Datenschutz & Sicherheit**. Weder der Installer noch die Dokumentation verlangen das globale Abschalten von Gatekeeper, SIP oder das Entfernen von Quarantäneattributen.

Wenn nur die `.command`-Datei nicht startet, kannst du nach Prüfung ihres Inhalts im Terminal `bash ` eingeben, die Datei hineinziehen und Enter drücken. Das umgeht keine macOS-Freigabe für die eigentliche App.

## Update, Sicherung und Entfernen

- StoryCore mit **⌘Q** beenden, neues Paket laden und denselben Installer starten.
- Sicherungen vorheriger Apps: `~/Library/Application Support/StoryCore Installer/Backups/`. Zur Wiederherstellung ein ZIP separat entpacken, StoryCore schließen und dessen App-Paket installieren. Der Installer führt keine Datenmigration oder Versionsbereinigung aus.
- Nutzerdaten bleiben unter `~/Library/Application Support/Still Workbench/` oder den selbst konfigurierten Speicherorten. Die App-Sicherung enthält **nur die Anwendung**, keine Chats; den Datenordner gesondert sichern.
- Ollama speichert seine Modelle separat, üblicherweise unter `~/.ollama`. Entladen gibt RAM frei; Löschen über die Modellverwaltung entfernt die Modelldateien.
- Nach erfolgreicher Installation das DMG auswerfen bzw. den entpackten Installationsordner entfernen. Bewahre bei Bedarf das ZIP auf. Lose zusätzliche `.app`-Pakete können in der macOS-Suche als weitere Installationen auftauchen.
- Zum Entfernen nur die gewünschte `StoryCore.app` im Finder in den Papierkorb bewegen. Persönliche Daten und Ollama bleiben erhalten.

## Terminaloptionen und Diagnose

```sh
# Ohne Installation oder Rückfragen prüfen; funktioniert auch im Quellcode-Checkout:
bash Install-StoryCore.command --check

# Ein bereits vorhandenes Paket installieren; keine Programme öffnen:
bash Install-StoryCore.command --yes --app /absoluter/Pfad/StoryCore.app
```

`--yes` bestätigt nur den StoryCore-Austausch. Ollama wird weder installiert noch gestartet. Exitcodes: **0** erfolgreich; **1** Fehler/inkompatibles System; **2** Check unvollständig (Ollama nicht erreichbar), Abbruch oder Übergabe an den Ollama-Download. `--check` prüft den Standardserver, nicht die individuelle StoryCore-Konfiguration.

## Selbst aus dem Repository bauen

Nur für Entwicklung: Apple Silicon, Node.js **22.12 oder neuer**, npm, Rust/Cargo und Xcode Command Line Tools. Tauri-Voraussetzungen: [offizielle Anleitung](https://v2.tauri.app/start/prerequisites/). Installationsquellen: [Node.js](https://nodejs.org/en/download), [Rust](https://www.rust-lang.org/tools/install). Die Apple-Werkzeuge werden bei Bedarf über `xcode-select --install` angefordert.

```sh
git clone https://github.com/YorkStack/OLLAMA-GUI.git
cd OLLAMA-GUI
npm ci
npm run check
npm run test:installer
npm run desktop:build
```

Ergebnisse liegen unter `src-tauri/target/release/bundle/`: App in `macos/`, DMG und fertiges Installer-ZIP in `dmg/`. Im Checkout enthält `Install-StoryCore.command` selbst **keine eingebettete App** und lädt auch keinen privaten GitHub-Release automatisch herunter.

Bestehende Release-Version aus dem Build installieren, ohne die Version zu erhöhen:

```sh
bash Install-StoryCore.command --app "$PWD/src-tauri/target/release/bundle/macos/StoryCore.app"
```

Die entwicklerseitigen Befehle `npm run desktop:install` und `npm run release:minor` erhöhen hingegen die Versionsnummer, bauen und nutzen den bisherigen Node-Installer mit ZIP-Sicherungen unter `../StoryCore-Mac/archived-apps/`. Details zur Veröffentlichung: [Release-Anleitung](RELEASING.md).
