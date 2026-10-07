# Zu einer älteren Version zurückkehren

Ein kontrollierter Rückweg ist sinnvoll. Eine Deinstallation entfernt normalerweise nur die App, nicht ihre Daten. Eine ältere App kann neuere Formate oder Funktionen nicht verstehen.

**Derzeit gibt es keinen Downgrade-Knopf.** Der Updater bietet nur höhere Versionen an. Bei einem Fehler während der Installation versucht er die gesicherte bisherige App wiederherzustellen. Für einen später bemerkten Fehler bleibt eine manuelle Wiederherstellung möglich.

1. StoryCore beenden. Den aktuellen Hauptdatenordner und alle eigenen Speicherorte zusätzlich sichern, damit neue Arbeiten nicht verloren gehen. Standard: `~/Library/Application Support/Still Workbench/`.
2. Die Sicherung vor dem betreffenden Update unter `Still Workbench.backups/before-…/` suchen. `backup.json` ordnet die gesicherten Dateien ihren ursprünglichen Speicherorten zu; `WIEDERHERSTELLUNG.txt` beschreibt die Wiederherstellung.
3. Die frühere App aus `previous-app.zip` wiederherstellen. Alternativ das konkrete ältere Installationspaket aus den offiziellen Releases wählen; nicht den neuesten Installer verwenden.
4. Bei geänderten Datenformaten den **passenden alten Datenstand** wiederherstellen. Nicht ungeprüft alte und neue Dateien mischen. Später entstandene Arbeiten bleiben in der zusätzlichen Sicherung aus Schritt 1; die alte App kann sie möglicherweise nicht öffnen.
5. Erst danach die ältere App starten und die Inhalte kontrollieren. Ollama-Modelle bleiben separat erhalten.

Besonders beim Rückwechsel von 2.x auf 1.7.1: 1.7.1 besitzt weder den neuen Projektarbeitsbereich noch die neue Datenformat-Sperre. Diese Version nicht versuchsweise auf den einzigen aktuellen Datenbestand loslassen.

Ein zukünftiger Downgrade-Assistent sollte App und Datensicherung zusammen auswählen, Kompatibilität prüfen und vor der Wiederherstellung den aktuellen Stand sichern. Ein Formatwechsel muss vorab erklären, welche neueren Arbeiten in der alten Version nicht verfügbar sind.
