# StoryCore nutzen

**Vorabversion 2.0.2:** Die neue Navigation sowie Projekte, Profil und Dokumentwissen sind in [Projektarbeitsbereiche 2.0](PROJEKTE-2.0.md) beschrieben. Die gemeinsamen Funktionen unten gelten auch für 1.7.1. Die PDF-Anleitung für 2.0.2 ergänzt Projekte und Updates.

Stand: **1.7.1 · 6. Oktober 2026**. [Bebilderte PDF-Anleitung](https://github.com/YorkStack/StoryCore-Releases/releases/download/v2.0.2/StoryCore-Erste-Schritte.pdf) · [Installation](INSTALLATION-MAC.md).

## Modell auswählen und starten

1. Ollama öffnen, dann StoryCore. Oben sollte **Ollama verbunden** stehen.
2. Unter **Modelle** einen Modellnamen oder kopierten Ollama-Befehl einfügen und **Herunterladen** starten. Über die Ollama-Bibliothek oder den Hugging-Face-GGUF-Katalog passende Textmodelle suchen.
3. Chip und RAM sowie die grobe Speicherprognose beachten. GGUF-Format allein garantiert keine Ollama-Kompatibilität. Embeddings/Spracherkennung sind Katalogfilter; ihre Inferenz ist in StoryCore noch nicht implementiert.
4. Beim installierten Modell **Verwenden** wählen, dann **Zurück zum Schreiben**. **In Speicher laden** ist optional: beim ersten Senden lädt Ollama das Modell bei Bedarf.

**Herunterladen** belegt Festplatte; **Aus Speicher entladen** gibt RAM frei und behält die Modelldateien. **Von Festplatte löschen** entfernt das Modell aus Ollama und der Liste und betrifft auch andere Apps mit derselben Ollama-Installation.

## Chat oder Geschichte

Auf der Startseite **Chat beginnen**, **Story erstellen** oder **Modelle vergleichen** wählen. Nachricht eingeben, mit Enter oder Pfeil senden; Shift+Enter erzeugt eine neue Zeile. Im Chat spricht die gewählte Figur, ohne Charakter ein Assistent. Story erzeugt Prosa mit Handlung und Figurendialog.

Während der Ausgabe kannst du nach oben scrollen. **Zur neuesten Ausgabe** aktiviert das Mitlaufen wieder. **STOP** beendet die Ausgabe und erhält den bisher erzeugten Teil. Chats über den Titel oder das sichtbare **…**-Menü umbenennen, archivieren oder nach Bestätigung löschen. Ein neuer Entwurf erscheint erst nach der ersten Nachricht in der Liste.

## Einstellungen und Profile

| Regler | Bedeutung |
| --- | --- |
| Temperatur | Mehr oder weniger Zufall bei der Tokenauswahl; niedriger garantiert keine richtigen Fakten. |
| Top P | Beschränkt Kandidaten auf eine kumulierte Wahrscheinlichkeit, z. B. 0,9. |
| Top K | Beschränkt die Anzahl der Kandidaten, z. B. 40. |
| Wiederholungsstrafe | 1 ist neutral; etwas höher bremst Wiederholungen, zu hoch kann Sprache verfälschen. |
| Kontextfenster | Gesamtplatz für Anweisungen, Karten, Lore, Quellen, Verlauf und Antwortreserve. Größer benötigt mehr RAM. |
| Max. Ausgabetokens | Obergrenze je Antwort. Eine größere Reserve lässt weniger Platz für Eingaben. |

Zunächst Standardwerte verwenden und nur einen Regler ändern. **Preset speichern unter** sichert die Kombination, **Preset laden** stellt sie wieder her. Diese Regler ändern keine trainierten Modellgewichte. Lokale OpenAI-kompatible Server unterstützen nicht alle Ollama-Optionen; siehe [Kontext und Verwaltung](CONTEXT.md).

## Charakter, Persona, Orte und Lore

Ein **Charakter** beschreibt die Modellrolle, eine **Persona** deine Rolle. Unter **Charaktere → Neu** Name, Eigenschaften, Hintergrund und optional Aussehen ausfüllen. Der kurze Charakterkern bündelt die wichtigsten Fakten und ersetzt, sofern ausgefüllt, die langen Beschreibungsfelder im Prompt. Die **LLM-Schreibhilfe** erzeugt mit dem ausgewählten Modell einen Vorschlag: prüfen, übernehmen und die Karte speichern. **Details** öffnet die Bearbeitung später erneut.

Ein **Lorebook** ist eine Sammlung: beispielsweise ein Buch für eine Welt und darin je ein Eintrag für Ort, Firma, Gegenstand oder Nebenfigur. Ein Buch mit nur einem Ort ist ebenfalls möglich. **Lorebooks → Neu → Eintrag hinzufügen**: Titel, Typ, Schlüsselwörter, Kurzfassung und Details ergänzen, aktivieren und speichern. Rechts im Chat das Buch auswählen und unter **Aktuelle Szene** den aktuellen Ort setzen. Beim Ortswechsel aktualisieren.

Charaktere und Lore über **Verknüpfungen** verbinden. **App verwalten → Kontext & Budgets** begrenzt geladenes Wissen und Nachladeebenen. Ein Buch wird nicht pauschal vollständig geladen. Markierte Begriffe öffnen den Eintrag; **Verwenden**, **Weglassen** und **Automatisch** steuern dessen Verwendung pro Chat. Geheimnisse benötigen eine zusätzliche Freigabe. Der **Prompt Inspector** zeigt geladenes Wissen mit Gründen und Token-Schätzung.

## Internetrecherche einrichten und verwenden

1. **App verwalten → Web-Recherche** öffnen. Tavily, Serper oder Brave wählen.
2. Beim Anbieter ein Konto erstellen, API-Schlüssel kopieren und im zugehörigen Feld eintragen. Die Registrierungslinks und kurzen Kontoanleitungen stehen direkt in der App; ausführlich unter [Web-Recherche](WEB-RECHERCHE.md).
3. **Web-Recherche erlauben** aktivieren und **Einstellungen speichern**. Jeder Anbieter behält einen getrennten Schlüssel.
4. In Schreiben oder Modellvergleich **Web-Recherche an** einschalten. Eigene Suchbegriffe eingeben und **Im Web suchen** klicken.
5. Treffer aufklappen und prüfen. Erst danach die eigentliche Frage senden oder den Vergleich starten.

Beispiel: Suchbegriffe `Forward Proxy Reverse Proxy Unterschied`; Frage `Erkläre beide anhand der Quellen, belege Aussagen mit [W1], [W2] und benenne fehlende Belege.` Für zeitabhängige Aktienkurse müssen Börse, Währung und Kurszeitpunkt aus den Quellen hervorgehen; Suchauszüge sind kein Echtzeit-Kursfeed.

Nur die Suchbegriffe gehen an den Suchdienst, nicht automatisch private Karten oder Chatverläufe. Die zurückgegebenen Auszüge gehen mit der Frage an das gewählte lokale Modell. Standardmäßig maximal vier Quellen und 1.200 geschätzte Tokens. Kein Container, keine Browser-Engine, kein automatischer Anbieterwechsel und keine selbstständigen Folgeabrufe.

Nach Sendebeginn ist die Recherche wieder ausgeschaltet. Ohne Recherche arbeitet das Modell mit vorhandenem Wissen und lokalem Kontext. Bei fehlendem Schlüssel, ausgeschöpftem Kontingent oder Netzwerkfehlern erscheint eine Fehlermeldung. Schlüssel und Verbrauch im Anbieter-Dashboard prüfen. Nach 30 Minuten oder geänderten App-Einstellungen erneut suchen.

Tavily-/Serper-Auszüge bleiben mit der Antwort gespeichert. Bei Brave werden Quellen und vollständige Promptkopien ohne bestätigte vertragliche Speicherrechte nicht gespeichert; die Modellantwort bleibt. Schlüssel befinden sich nur lokal in `settings.json` (0600), nicht im macOS-Schlüsselbund und nicht in Projekt-Exporten. Kontingente und mögliche Kosten gelten je Anbieter. Ein erfolgreicher Live-Test mit produktiven Tavily-/Serper-Schlüsseln steht noch aus; die automatisierten Anbindungstests verwenden simulierte Antworten.

## Zwei Modelle vergleichen

Beide Textmodelle installieren, **Modellvergleich** öffnen und unterschiedliche Modelle A/B wählen. Gemeinsamen Test-Prompt eingeben, **Prompt prüfen**, dann **Vergleich starten**. StoryCore führt die Modelle nacheinander mit denselben vorbereiteten Nachrichten, Einstellungen, Karten, Lore und gegebenenfalls Recherchequellen aus. Quellen vor dem Vergleich einmal suchen; keine getrennten Suchläufe je Modell.

Bewerte zuerst Vorgabentreue, Faktentreue, Vollständigkeit und Verständlichkeit. Prüfe Quellenverweise auf Übereinstimmung mit den Auszügen. Danach Laufzeit, Ausgabetokens und Tokens/s vergleichen. Eine schnelle Antwort ist nicht automatisch besser. Unterschiedliche Tokenizer, Vorlagen und Antwortlängen begrenzen direkte Leistungsvergleiche. Mehrfach mit verschiedenen Aufgaben wiederholen. **Export** sichert Ergebnisse; **Übernehmen** macht daraus einen Chat.

## Kontext komprimieren und sichern

Der Tacho schätzt den nächsten Request einschließlich Antwortreserve. Ab 65 % wird **Kontext komprimieren** angeboten, ab 80 % dringlicher. Das ausgewählte Modell verdichtet ältere Nachrichten; die fertige Kurzfassung wird automatisch gespeichert und aktiviert. **Kontextspeicher aktiv** bestätigt den Erfolg. Originaltext und mindestens vier jüngste Nachrichten bleiben erhalten.

Unter **Gespeicherte Zusammenfassung ansehen** Namen, Beziehungen und offene Handlungen prüfen. Zusammenfassungen können Details verlieren. Bei Änderungen an schon verdichteten Nachrichten wird der Speicher ungültig; erneut komprimieren. Komprimierung führt keine neue Internetsuche aus. Für aktuelle Fakten gezielt erneut recherchieren. [Details zum Kontextspeicher](MEMORY.md).

Chats, Karten und Projekte exportieren oder den gesamten lokalen Datenordner separat sichern. Die Installer-Sicherung betrifft nur die App. Standard auf dem Mac: `~/Library/Application Support/Still Workbench/`; eigene Speicherorte stehen unter App verwalten. Modelle liegen getrennt bei Ollama. Das Installationspaket enthält keine persönlichen Geschichten, Schlüssel oder Modellgewichte.
