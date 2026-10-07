# Download-Statistik

Die README enthält eine automatisch erzeugte Tabelle für öffentliche Releases ab 2.0.2. Der App-Quellcode bleibt privat; in diesem Repository liegt nur das Skript zur Pflege dieser Downloadseite.

## Was gezählt wird

GitHub führt für jede Release-Datei einen kumulierten `download_count`. Die Tabelle addiert ausschließlich `StoryCore_*_Mac-Installer.zip`, `StoryCore_*.dmg` und `StoryCore.app.tar.gz`. Das Update-Paket kann auch manuell geladen werden: Diese Spalte ist kein Nachweis einer erfolgreichen In-App-Installation. Metadaten, Signaturen, PDFs, Lizenzen und Quellarchive werden ausgeschlossen. Entwürfe und Versionen vor 2.0.2 erscheinen nicht; Beta-Releases bleiben als Beta gekennzeichnet.

Downloads sind keine eindeutigen Nutzer, Installationen oder aktiven Anwender. Eigene Tests und wiederholte Downloads werden mitgezählt. Werden Assets gelöscht und neu hochgeladen, können deren Zähler zurückgesetzt sein; die Tabelle ist keine dauerhafte historische Statistik. Sie fügt der App keine Telemetrie hinzu.

## Automatische Aktualisierung

Der Workflow `.github/workflows/download-stats.yml` läuft täglich gegen 05:37 UTC, bei Release-Veröffentlichung, -Änderung oder -Löschung sowie bei Änderungen an README, Skript, Tests oder Workflow auf main. GitHub kann geplante Ausführungen verzögern und geplante Workflows in öffentlichen Repositories nach längerer Inaktivität deaktivieren. Im Tab Actions lässt sich der Status prüfen und der Workflow wieder aktivieren.

Manueller Start: **Actions → Download statistics → Run workflow → main → Run workflow**. Bei Veröffentlichungen durch einen anderen GitHub-Workflow mit dessen `GITHUB_TOKEN` wird das Release-Ereignis nicht automatisch erneut ausgeführt. Dann diesen Workflow am Ende der Veröffentlichung per `workflow_dispatch` starten oder den täglichen Lauf abwarten.

Das Skript liest alle Seiten der GitHub-Releases-API. Nur der Bereich zwischen `download-stats:start` und `download-stats:end` wird geändert. Bleiben die Zahlen und Versionen unverändert, gibt es keinen Commit und der angezeigte Datenstand bleibt erhalten. Die letzte tatsächliche Prüfung ist jederzeit bei Actions sichtbar. Bei API-Fehlern bleiben die bisherigen Zahlen stehen und der Workflow meldet einen Fehler.

Der Workflow verwendet den von GitHub bereitgestellten kurzlebigen Token mit `contents: write`, um ausschließlich die README zu committen. Kein persönlicher Schlüssel und kein zusätzliches Secret notwendig. Änderungen über diesen Token lösen keine Endlosschleife von Push-Workflows aus. Bei Branch-Schutz, der direkte Bot-Commits verbietet, muss dieser Veröffentlichungsweg angepasst werden; Schutzregeln werden nicht automatisch gelockert.

## Lokal prüfen

Python 3 genügt, keine Zusatzpakete:

```sh
python3 -m unittest discover -s tests -p 'test_download_stats.py'
python3 scripts/update-download-stats.py
```

Ohne `GH_TOKEN` verwendet das Skript die öffentliche API mit deren niedrigeren Abfragelimits. Zugangstoken nie in Dateien oder Commits speichern.

Quellen: [Release-Assets-API](https://docs.github.com/en/rest/releases/assets), [Workflow-Ereignisse](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [GitHub-Token und Auslösung weiterer Workflows](https://docs.github.com/en/actions/concepts/security/github_token).
