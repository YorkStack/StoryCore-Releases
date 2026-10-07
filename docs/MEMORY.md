# Kontextspeicher für lange Geschichten

Aktueller Funktionsstand: **2.0.4 Vorabversion · 7. Oktober 2026**.
[Dokumentationsübersicht](../README.md#anleitungen).

StoryCore bietet ab **65 %** geplanter Kontextbelegung die Komprimierung direkt
über dem Eingabefeld an. Ab **80 %** wird der Hinweis dringlicher. Die Anzeige
schließt die reservierten Ausgabetokens ein und ist eine Schätzung.

1. **Kontext komprimieren** starten.
2. Der ausgewählte Modellserver schreibt einen knappen Kontextspeicher.
3. Die fertige Kurzfassung wird automatisch gespeichert und aktiviert.
   **Kontextspeicher aktiv** bestätigt die Übernahme; die Kontextanzeige wird
   neu berechnet. Davor/danach zeigt die geschätzte Eingabe ohne Antwortreserve.
4. Normal weiterschreiben oder die letzte Passage fortsetzen. Bereits getippte
   Eingaben bleiben erhalten. Unter **Gespeicherte Zusammenfassung ansehen**
   kannst du die Kurzfassung prüfen oder zum vollständigen Verlauf zurückkehren.

## Was an das Modell geht

Der Kontextspeicher ersetzt ausschließlich den älteren Nachrichtenanfang.
Mindestens die letzten vier Nachrichten bleiben unverändert; wenn nötig bleibt
eine weitere Nachricht erhalten, damit ein jüngster Dialog nicht mitten in einer
Antwort beginnt. Charakterkern, Persona, aktuelle Szene und budgetierte Lore
bleiben nach ihren bisherigen Regeln aktiv. Der Prompt Inspector zeigt die
Kurzfassung im Abschnitt `STORY MEMORY` und nur den jüngsten wörtlichen Verlauf
unter `CHAT HISTORY`. Alte Ortsnamen im Gedächtnis aktivieren nicht erneut alle
historischen Lore-Einträge.

Die Kurzfassung soll Fakten, Identitäten, Beziehungen, Zusagen, Gegenstände,
Ziele, Wissensgrenzen und offene Handlungsfäden erhalten. Sie verwendet kurze
Sätze oder Semikolon-Fakten. Das Ziel liegt je nach Kontextfenster zwischen
128 und 768 geschätzten Tokens (etwa 8 % des Fensters). Metadaten und Prompt-
Anweisungen verursachen zusätzlich Tokens. Zusammenfassungen sind nicht
verlustfrei; kleinere Details können fehlen. Das Modell liest archivierte
Details nicht automatisch nach. Wichtige fehlende Details können aus dem
Original übernommen und in der nächsten Nachricht erneut genannt werden.

## Wiederholte Komprimierung und Rückweg

Bei der nächsten Komprimierung verdichtet das Modell den vorhandenen Speicher
zusammen mit den inzwischen älteren Nachrichten. Die bisherigen Originaltexte
werden nicht erneut vollständig gesendet. Bereits übergroße Verläufe werden
innerhalb des eingestellten Modellfensters in begrenzten Abschnitten verarbeitet;
auch übergroße Einzeltexte werden vollständig aufgeteilt. Keine Quellzeichen
werden dabei still abgeschnitten. Für diesen Vorgang sind mindestens 2.048
Kontexttokens erforderlich, höchstens 128 Teilabschnitte pro Vorgang.

Unter **Gespeicherte Zusammenfassung ansehen** lässt sich der vollständige
Verlauf wieder aktivieren und anschließend erneut auf den Speicher umschalten.
Bei Änderungen, Löschungen oder Neuerzeugungen im zusammengefassten Abschnitt
wird dieser Speicher automatisch ungültig. StoryCore verwendet dann den
vollständigen Verlauf und fordert zum erneuten Komprimieren auf.

## Speicherung und Fehler

Alle Nachrichten bleiben sichtbar, gespeichert und exportierbar. Der Speicher
liegt als `context.memory` im Chat-JSON und wird auch mit Projekten exportiert.
Er enthält Kurzfassung, Modell, Datum, Nachrichtengrenze und eine Prüfsumme des
zusammengefassten Textanfangs. Die Prüfsumme dient der Änderungserkennung,
nicht der Authentifizierung. Es gibt keine neue Cloudverbindung; die Funktion
nutzt die bereits konfigurierte Modell-Laufzeit.

Eine erfolgreiche Zusammenfassung wird automatisch gespeichert und aktiviert.
Währenddessen ist das Absenden einer neuen Nachricht gesperrt; du kannst aber
weiter tippen. Abbrechen, ungültiges JSON, leere/zu lange Modellantworten,
abgebrochene Ausgaben und Vorschläge ohne Tokenersparnis verändern den Kontext
nicht. Bei einem Speicherfehler bleibt die fertige Kurzfassung im geöffneten
Chat für **Speichern erneut versuchen** erhalten; bis dahin gilt der bisherige
Kontext. Wenn die nächste Anfrage trotz Ersparnis zu groß bleibt, weist
StoryCore ausdrücklich darauf hin.

## Modellwechsel und Updates

Modellwechsel ändern nicht den gespeicherten Originaltext oder die Kurzfassung. Die Tokenanzeige richtet sich nach dem aktuellen Profil; mit einem kleineren Kontextfenster kann erneut Komprimierung nötig sein. Ein Update mit dem Mac-Installer ersetzt nur Programmdateien. Kontextspeicher und Verläufe bleiben im lokalen Datenordner. Sichere diesen Ordner zusätzlich, wenn du einen unabhängigen Rückweg für deine Arbeit benötigst.

Embedding-Modelle im Katalog sind keine Voraussetzung für diese Funktion: Die Komprimierung verwendet eine Textgenerierungsanfrage an das ausgewählte Modell. Die bloße Installation eines Embedding- oder Spracherkennungsmodells macht es nicht zu einem geeigneten Chat-/Zusammenfassungsmodell.

## Komprimierung und Web-Recherche

Komprimieren führt keine neue Internetsuche aus. Antworten mit Recherche gehen als Teil des älteren Gesprächs in die Zusammenfassung ein; die Kurzfassung ist deshalb keine vollständige Quellenablage. Der Originalverlauf bleibt erhalten, gespeicherte Quellen unterliegen den Regeln des jeweiligen Anbieters. Für zeitabhängige Fakten vor der Fortsetzung erneut explizit recherchieren. Quellen-Tokenbudget und Antwortreserve müssen weiterhin in das aktuelle Kontextfenster passen.

## Projektgedächtnis und Dateien · 2.0.4

Der Kontextspeicher komprimiert den Verlauf eines Gesprächs. Das Projektgedächtnis enthält dagegen ausdrücklich bestätigte Erkenntnisse aus mehreren Aufgaben. Anhänge und Projektwissen bleiben separat erhalten und werden anhand der nächsten Frage erneut innerhalb der Budgets ausgewählt. Komprimieren löscht weder Originaldateien noch den sichtbaren Verlauf. Entfernen eines Anhangs bereinigt keine historischen Prompt-Snapshots. [Projektablauf](PROJEKTE-2.0.md).
