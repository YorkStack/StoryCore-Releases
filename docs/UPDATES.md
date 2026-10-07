# StoryCore aktualisieren

Stand: 2.0.6 Beta, 7. Oktober 2026. Der öffentliche Update-Kanal ist ab 2.0.2 enthalten. Ältere Apps benötigen einmal den normalen Installer aus dem öffentlichen Download-Repository.

## Updates unter /Applications ab 2.0.6 Beta

`/Applications` ist ein unterstützter normaler Installationsort. StoryCore aktualisiert die App dort, ohne sie in den Benutzerordner zu verschieben. Sind Administratorrechte erforderlich, erscheint der macOS-Systemdialog. Zugangsdaten werden ausschließlich dort eingegeben; StoryCore speichert sie nicht. Der Download und die Datensicherung laufen ohne erhöhte Rechte. Nur der abschließende App-Austausch verwendet die Freigabe. Kein dauerhaft installierter privilegierter Dienst.

Das signierte Paket wird vor dem Austausch in einem separaten Verzeichnis geprüft. Die bisherige App bleibt bis zur Kontrolle der neuen Installation erhalten. Bei Fehlern wird sie mit denselben Rechten zurückgestellt; bei abgebrochener Freigabe bleibt sie unverändert. Ein echtes schreibgeschütztes DMG wird separat erkannt und kann auch mit Administratorrechten nicht aktualisiert werden.

**Einmaliger Übergang:** 2.0.2 bis 2.0.5 brechen bei bestimmten Installationsrechten schon vor dem Download ab. Dieser alte Programmcode lässt sich nicht durch neue Release-Metadaten reparieren. Betroffene Nutzer müssen einmal den [reparierten Installer 2.0.6 Beta](https://github.com/YorkStack/StoryCore-Releases/releases/tag/v2.0.6) ausführen. Er aktualisiert eine vorhandene App unter `/Applications` mit macOS-Freigabe. Danach ist dieser Weg direkt in der App eingebaut. Chats und Einstellungen werden nicht gelöscht; der separate Installer sichert die App, Nutzerdaten bitte zusätzlich sichern. Ohne verfügbaren Administrator kann eine geschützte Installation weiterhin nur durch die IT geändert werden.

**Release-Status:** 2.0.6 ist Beta und nur im freiwilligen Beta-Kanal sichtbar. 2.0.4 bleibt stabil. Der native Administrator-Dialog ist implementiert; ein kompletter Test mit interaktiver Administratorfreigabe steht noch aus. Unprivilegierter Austausch, Fehler-Rücksetzung, Archiv-Prüfung und Dialogskript-Kompilierung sind automatisiert geprüft.

## Für Benutzer

Links unten **Updates** öffnen. Die App fragt beim Start nach der neuesten stabilen GitHub-Veröffentlichung und speichert den Zeitpunkt. Auch nach einem Neustart wird innerhalb von 24 Stunden nicht erneut automatisch angefragt. Bei dauerhaft geöffneter App erfolgt die nächste Prüfung nach 24 Stunden. Das gilt auch nach Netzwerkfehlern. **Jetzt prüfen** startet eine ausdrückliche zusätzliche Prüfung. Die Automatik lässt sich abschalten.

Die Prüfung lädt nur Release-Metadaten. Weder Chattexte noch Dokumente, Profil oder Modellnamen werden übertragen. GitHub erhält die üblichen Verbindungsdaten und gegebenenfalls deinen Zugangstoken. Unveröffentlichte Commits und Entwicklungszweige werden nicht installiert. Vorabversionen werden nur nach bewusster Freigabe angeboten.

### Öffentliche Downloads und Vorabversionen

[YorkStack/StoryCore-Releases](https://github.com/YorkStack/StoryCore-Releases) ist öffentlich. Nutzer brauchen keinen GitHub-Account oder Zugangstoken. Der Quellcode bleibt im getrennten privaten Entwicklungsrepository.

Standardmäßig werden **nur stabile Versionen** angeboten. Unter **Updates → Versionen anbieten → Auch Vorabversionen** lassen sich Vorabversionen ausdrücklich einschalten. Danach **Jetzt prüfen** wählen. Vorabversionen können Fehler enthalten. Zurückschalten auf stabile Versionen ändert nur künftige Angebote und führt keinen Downgrade aus.

Ein optionaler Token kann bei GitHub-API-Limits helfen. Ein ungültiger alter Token sollte unter **Optionaler GitHub-Zugang → Token entfernen** gelöscht werden. Tokens werden lokal mit eingeschränkten Dateirechten, aber nicht verschlüsselt gespeichert und sind in Datensicherungen enthalten. Backups niemals öffentlich weitergeben.

### Grafische Fortschrittsanzeige ab 2.0.5

Die Installation zeigt sechs Schritte, einen Downloadbalken mit echten Prozent- und MB-Werten, die vergangene Zeit und die nächste Aktion. Prüfung, Sicherung und Installation verwenden eine Aktivitätsanzeige ohne erfundene Prozentwerte oder Restzeit. Bei Fehlern bleibt die Meldung sichtbar; es gibt keinen automatischen Neustart. „Zurück zu Updates“ schließt die Meldung, „Erneut versuchen“ startet nach erneuter Bestätigung. Nach einem Fehler während der Wiederherstellung zuerst die genannte Sicherung prüfen.

Beim ersten Update auf 2.0.5 verwendet die ältere App noch ihren bisherigen Bildschirm. Die neue Anzeige gilt für nachfolgende Updates. 2.0.5 ist Beta; 2.0.4 bleibt stabil und Latest.

![Update-Anzeige mit simuliertem Downloadstand](guide-assets/205-update-progress.png)

### Installieren

Bei einem verfügbaren Update zeigt die App einen Hinweis. **Update ansehen → Sichern und Update installieren** zeigt Versionshinweise und die angekündigten Datenänderungen. Nach Bestätigung:

1. Laufende Aufgaben und ungespeicherte Eingaben müssen abgeschlossen sein.
2. Das vollständige App-Paket wird heruntergeladen. SHA-256 und Tauri-Updatesignatur einschließlich der signierten Versionsnummer werden geprüft.
3. Schreibzugriffe werden gesperrt. Alle konfigurierten Datenverzeichnisse werden unverändert kopiert und mit Prüfsummen überprüft. Eigene Speicherorte werden berücksichtigt.
4. Die bisherige App wird als geprüftes ZIP gesichert. Erst danach wird das App-Paket ersetzt und StoryCore neu gestartet.

Ollama und dessen heruntergeladene Modelle werden dabei nicht verändert. Aktuell gibt es vollständige App-Updates, keine binären Delta-Patches. Es ist kein Apple-Entwicklerabo für die separate Updatesignatur erforderlich. Diese Signatur ersetzt keine Apple-Notarisierung und hebt Gatekeeper nicht auf.

Die App muss in einem beschreibbaren Anwendungsordner liegen, beispielsweise `~/Applications/StoryCore.app`. Ein schreibgeschütztes DMG kann nicht aktualisiert werden.

## Daten und Wiederherstellung

Gesichert werden der gesamte Hauptdatenordner und alle zusätzlichen konfigurierten Speicherorte: Chats, Stories, Charaktere, Personas, Lorebooks, Presets, Projekte, Vergleiche, Wissensdateien samt Originalen, Ergebnisversionen und persönliches Profil. Bestätigte Projekterinnerungen befinden sich in den Projektdateien. Unbekannte Felder und zusätzliche Dateien werden bytegetreu erhalten.

Standardpfad der Sicherungen:

```text
~/Library/Application Support/Still Workbench.backups/before-<Version>-<Zeitpunkt>-<ID>/
```

Bei einem anderen Hauptdatenordner wird `.backups` an dessen Pfad angehängt. Jeder Sicherungsordner enthält:

- `source-N/`: Originaldateien aus den gesicherten Verzeichnissen.
- `backup.json`: Zuordnung zu den ursprünglichen Dateipfaden, Dateigrößen und SHA-256-Prüfsummen.
- `WIEDERHERSTELLUNG.txt`: Vorgehen zum Wiederherstellen.
- `previous-app.zip`: bisherige App, sobald auch deren Archivierung abgeschlossen ist.

Backups werden nicht automatisch gelöscht. Zum Aufräumen können ältere Sicherungen nach erfolgreicher Kontrolle der neuen App manuell entfernt werden. Für eine Wiederherstellung StoryCore beenden, zunächst den aktuellen Datenstand separat sichern und die Dateien anhand von `backup.json` an ihre ursprünglichen Orte zurückkopieren. Die vorherige App kann aus dem ZIP wiederhergestellt werden. Bei einem erkannten Installationsfehler versucht der Updater dies automatisch; bei einem späteren Startfehler bleibt das ZIP für eine manuelle Wiederherstellung erhalten.

Bei Platzmangel, fehlenden Speicherorten, symbolischen Links innerhalb der Datenverzeichnisse oder einer fehlgeschlagenen Sicherung wird nicht installiert. Quellverzeichnisse mit symbolischen Pfadangaben werden auf ihren tatsächlichen Ort aufgelöst. Backups dürfen keine Datenverzeichnisse überlappen.

### Formatänderungen

`release-data-policy.json` beschreibt die unterstützte Datenformat-Version und Änderungen pro Release. 2.0.2 schreibt bestehende Datensätze nicht um. Es ergänzt nur `.data-format.json` und Update-Einstellungen. Alte Daten ohne Kennung gelten als bestehendes Format 1.

Der Updater akzeptiert derzeit nur Releases, die Format 1 lesen und weiter schreiben und keine Datenlöschung ankündigen. **Andere Formatänderungen werden mit Erklärung blockiert.** Eine zukünftige Migration muss gezielt implementiert und mit bestehenden Daten getestet werden. Eine alte App mit dieser Schutzfunktion verweigert das Öffnen eines unbekannten Datenformats, bevor sie Daten anlegt oder verändert. Ältere Versionen vor 2.0.1 kennen diese Prüfung noch nicht und sollten nicht auf neuere Datenbestände angesetzt werden.

Eine Sicherung schützt nicht vor jedem möglichen Fehler eines neuen Programms. Deshalb bleiben Originaldateien, frühere App und Prüfmanifest erhalten. Es gibt keine automatische Löschung von Nutzerdaten im Updateablauf.

## Datenänderungen in 2.0.4

Optionale Anhänge werden in Chat und Vergleich gespeichert; Projektwissen unterstützt zusätzlich Tabellen. Das Datenformat bleibt 1. Bestehende Daten werden weder migriert noch gelöscht. Originaldateien sind Bestandteil der Datensicherung. Die reguläre Version 2.0.4 enthält Installer, beide neuen PDF-Anleitungen und signierte Update-Artefakte.

## Reguläre Freigabe von 2.0.4

2.0.4 wird im Standardkanal **Nur stabile Versionen** angeboten. **Jetzt prüfen** umgeht die tägliche Wartefrist. Ein Vorabversions-Opt-in ist nicht erforderlich. GitHubs Latest zeigt ebenfalls auf 2.0.4; 1.7.1 ist nur noch im Archiv. App-Paket und Datenformat bleiben bei dieser Freigabe unverändert.

## Freigaberegel und stabile Vorgängerversion

Neue Releases sind grundsätzlich **Beta** (GitHub: Pre-release). Nur die ausdrückliche Freigabe durch YorkStack macht eine Version stabil; abgeschlossene Tests allein reichen nicht. Beta-Releases setzen GitHubs Latest nicht um. Der Standardkanal bleibt **Nur stabile Versionen**; Betas erfordern **Auch Vorabversionen** im Update-Menü.

Aktuell stabil: **2.0.4**. Stabile Vorgängerversion: **2.0.2**, die erste öffentliche Ausgabe mit dem öffentlichen Updater. Intern war die Update-Funktion bereits in 2.0.1 enthalten, damals noch mit privater Repository-Adresse. Der Vorgänger bleibt ein historischer Download und wird nicht als Downgrade angeboten.
