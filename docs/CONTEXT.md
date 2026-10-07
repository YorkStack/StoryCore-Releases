# Kontext, Verknüpfungen und Verwaltung

Aktueller Funktionsstand: **2.0.4 Vorabversion · 7. Oktober 2026**.
[Dokumentationsübersicht](../README.md#anleitungen).

## Einstellungen

Die globale Verwaltung ist links in der Navigation erreichbar. Konfiguration liegt in `settings.json` im bisherigen Datenstamm. Sie wird nicht in Projekt-ZIPs exportiert.

- **Kontext & Budgets:** Hauptcharakter standardmäßig 500 geschätzte Tokens; zusätzliche Lore insgesamt 800; je Eintrag 240; höchstens fünf Einträge; eine Verknüpfungsebene; vier letzte Nachrichten. 0 Ebenen schaltet Nachladen ab. Stichwort-Rekursion ist standardmäßig aus; explizite Links bleiben möglich.
- **Modellserver:** Ollama-URL und Keep-alive in Sekunden. Alternativ lokale OpenAI-kompatible APIs, zum Beispiel LM Studio (`http://127.0.0.1:1234/v1`) oder llama.cpp (`http://127.0.0.1:8080/v1`). Verbindungstest liest die Modellliste. Die Laufzeitumgebung muss separat laufen; ausführbare Programme und Modellverzeichnisse werden dort verwaltet. Nur lokale HTTP-Adressen, keine Redirects oder URL-Zugangsdaten.
- **Web-Recherche:** Tavily, Serper oder Brave mit getrennten API-Schlüsseln; standardmäßig aus. Quellenbudget unabhängig vom Lore-Budget: vier Quellen und 1.200 geschätzte Tokens. Suche nur nach ausdrücklichem Klick. [Einrichtung und Nutzung](WEB-RECHERCHE.md).
- **Speicherorte:** separate absolute Ordner für Charakterkarten, Personas, Lorebooks, Profile, Chats, Projekte und Vergleiche. Leer bedeutet Standard. Ein Wechsel kopiert vorhandene JSON-Daten ohne Überschreiben und behält die Originale. Abweichende gleichnamige Zieldateien verhindern den Wechsel. Speicherung der Konfiguration ist atomisch; neue Schreibzugriffe sind während der Umstellung gesperrt.

OpenAI-kompatible Server erhalten `temperature`, `top_p`, `max_tokens` und Chat-Nachrichten. Kontextfenster, Top-k, Wiederholungsstrafe und Modell-Lebenszyklus sind dort zu konfigurieren. Laden/Entladen in StoryCore ist für diese Anbindung deaktiviert. Die Ollama-spezifische Cloud-Modellprüfung kann auf generische Server nicht übertragen werden; ob ein lokaler kompatibler Server selbst Daten weiterleitet, liegt in dessen Konfiguration.

## Charakter, Persona und Lorebook

Ein **Charakter** ist die Figur, als die das Modell im Chat antwortet. Eine **Persona** beschreibt die Nutzerrolle. Im Story-Modus kann das Modell über mehrere Figuren erzählen. Sichtbare **Details**-Schaltflächen öffnen die Editorbereiche; im Charaktereditor stehen unter anderem Persönlichkeit, Hintergrund, Aussehen, Start-Szene, Dialog, Erweiterungen und JSON zur Verfügung.

Ein **Lorebook** ist eine Sammlung unabhängiger Wissenseinträge. Ein Buch kann viele Orte, Firmen, Gegenstände oder Nebenfiguren enthalten; auch ein Buch mit nur einem Ort ist zulässig. Für mehrere Orte derselben Welt ist meist ein Buch mit einem Eintrag pro Ort übersichtlicher. Die Aktivierung erfolgt je Eintrag nach Schlüsselwörtern, Szene, manueller Auswahl und Verknüpfungen; ein aktiviertes Buch wird nicht pauschal vollständig in den Prompt kopiert.

## Charakterkern und aktuelle Szene

Im Charaktereditor unter **Übersicht** ersetzt ein ausgefüllter kurzer Kern die ausführlichen Felder Beschreibung, Persönlichkeit, Hintergrund und Aussehen im Modellkontext. Die Felder bleiben als Arbeitsmaterial und für CCv3-Exporte erhalten. Ohne Kern wird aus den bestehenden Feldern ein Fallback erzeugt; identische Sätze und vollständig redundantes Aussehen werden vermieden. Zu lange Kerne werden auf das globale Budget gekürzt, mit einer Warnung im Kontextbereich.

Das Start-Szenario gilt nur beim Einstieg, solange der an die Generierung übergebene Verlauf noch keinen Nutzerbeitrag enthält. Ein gesetzter Szenenzustand ersetzt es vollständig. **Aktuelle Szene** im Chat enthält Ort, aktuelle Fakten/Ziel und anwesende Figuren. Beim Ortswechsel aktualisieren oder einen Vorschlag aus den letzten zwölf Nachrichten durch die LLM ableiten lassen und prüfen. Es gibt keine heimliche automatische Ortsbestimmung nach jeder Antwort.

Der bisherige Chat bleibt unverändert gespeichert. Ohne aktiven Kontextspeicher wird der volle Verlauf übertragen; mit aktivem Speicher nur Kurzfassung und jüngere Nachrichten. Alte Fakten in Nachrichten verschwinden nicht durch einen Szenenwechsel. Der Kontextspeicher kann ältere Nachrichten komprimieren; Details stehen in MEMORY.md.

## Kurzfassung, Details, Geheimnisse

Lore enthält eine kurze Kontextfassung und ausführliche Details. Standardmäßig wird die Kurzfassung benutzt; ohne Kurzfassung der bisherige Inhalt. Details werden bei einem passenden Detail-Auslösewort in der neuesten Nachricht verwendet. Der Eintrag muss dabei selbst aktiviert sein. Passen die Details nicht in die Budgets, wird die Kurzfassung versucht. Passt auch sie nicht, wird der Eintrag ausgelassen und im Kontextbereich erklärt.

Geheimnisse benötigen zusätzlich eine ausdrückliche Freigabe **pro Chat** unter **Begriffe & Freigaben**. Auch „Immer aktiv“, manuelle Verwendung und Verknüpfungen umgehen diese Sperre nicht. Freigabe allein lädt den Eintrag noch nicht: anschließend braucht es einen Treffer oder „Verwenden“. Erneutes Sperren verhindert künftige Lore-Injektion; bereits im Verlauf ausgeschriebene Geheimnisse bleiben dort stehen. Freigaben steuern die Übertragung, nicht den Wissensstand einzelner Figuren nach der Übertragung.

## Verknüpfungen und Begriffe

Im Editor können Charaktere und Lore über **Verknüpfungen** verbunden werden. Beispiel: Testfigur → Testwerk → Teststadt. Die Hauptkarte gilt als Ausgangspunkt auf Ebene 0; eine eingestellte Nachladetiefe von 1 erlaubt nur ihre direkten Ziele. Ein direkt durch die Szene aktivierter Ort startet ebenfalls auf Ebene 0. Zyklen werden dedupliziert, und neue Einträge wirken erst auf der nächsten Ebene.

Direkte Auswahlreihenfolge: manuell verwendet, aktuelle Szene, neueste Nachricht, ältere gescannte Nachrichten, Konstanten; innerhalb gleicher Stufe entscheidet die Priorität. Weitere Ebenen folgen danach. Alle Einträge teilen sich das Lore-Budget, zusätzlich zu Buch- und Eintragsgrenzen. Der freie Platz nach Grundkontext und Ausgabetokens ist eine weitere Obergrenze. Ein expliziter Link kann ein sonst nicht ausgewähltes Lorebook erreichen. Dessen übrige Einträge werden dadurch nicht automatisch freigegeben.

Bekannte Schlüsselwörter werden im Chat und in einer Vorschau der Eingabe farbig, fett und kursiv markiert. Hover zeigt eine Kurzvorschau; Klick öffnet den Bibliothekseintrag. **Verwenden**, **Weglassen** und **Automatisch** gelten pro Chat und werden gespeichert. Beim Verwenden von Lore wird auch ihr Lorebook dem Chat zugeordnet. Zusätzliche Wörter werden als Schlüsselwörter beziehungsweise Charakter-Aliasse gespeichert. Über die Suche können neue Charakterkarten oder Lorebooks angelegt werden. Neue Lorebooks werden dem aktuellen Chat zugeordnet.

Die Kontextanzeige nennt jeden tatsächlich geladenen Eintrag, Aktivierungsgrund, Kurzfassung/Details und geschätzte Tokens. Der Prompt Inspector zeigt den zusammengestellten Modell-Request. Regex und CCv3-Dekoratoren bleiben als Daten erhalten, werden aber weiterhin nicht ausgeführt.

## LLM-Schreibhilfe

Charaktereditor, Lore-Editor und Szenenbereich bieten eine Schreibhilfe mit dem im Chat ausgewählten Modell. Die Anfrage enthält ausschließlich das angezeigte Arbeitsmaterial und den optionalen Auftrag. Strukturierte JSON-Ausgabe wird über Ollama `format` beziehungsweise kompatibles `response_format` angefordert und serverseitig validiert. Vorschläge lassen sich bearbeiten, übernehmen oder verwerfen; sie ändern die Bibliothek nicht automatisch. Im Editor muss anschließend gespeichert werden.

Ziel sind kurze, eindeutige Fakten und Beziehungen statt Schmuckprosa. Kryptische Abkürzungen garantieren keine Tokenersparnis und werden nicht erzwungen. Modellvorschläge können Fakten auslassen oder verändern; deshalb bleibt die Prüfung vor dem Übernehmen wichtig. Tokens sind weiterhin Schätzwerte, kein modellgenauer Tokenizer.

## Portable Felder

- Charakter: `data.extensions.storycore.{core,aliases,links}`.
- Lore-Eintrag: `extensions.storycore.{summary,detailKeys,links,secret}`; `content` enthält Details.
- Chat: `context.scene.{location,summary,participants}` und `context.{include,exclude,unlocked}`.
- Referenzen: `character:<Karten-ID>` oder `<Lorebook-ID>:<Eintrags-ID>`. Alte Einträge ohne ID verwenden vorläufig den Index. Beim Speichern über StoryCore werden fehlende Lore-IDs ergänzt.
- Projekt-ZIPs nehmen explizit verknüpfte Bibliotheken transitiv mit und schreiben deren Referenzen beim Import um. Historische Prompt-Snapshots bleiben historische Aufzeichnungen.

Andere Anwendungen können StoryCore-Erweiterungen ignorieren. Insbesondere gilt die Geheimnis-Sperre nicht automatisch in fremden Character-Card-Programmen.


## Schnittstellenreferenzen

[Ollama: strukturierte Ausgabe](https://docs.ollama.com/capabilities/structured-outputs), [LM Studio: kompatible Endpunkte](https://lmstudio.ai/docs/developer/openai-compat), [LM Studio: JSON-Schema](https://lmstudio.ai/docs/developer/openai-compat/structured-output), [llama.cpp Server](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).

## Geschichtengedächtnis

Der Kontextspeicher ersetzt nach erfolgreichem Speichern ältere Nachrichten im
Modellprompt. Der vollständige Verlauf bleibt gespeichert. Angebot ab 65 %,
dringlicher Hinweis ab 80 %. Details und Grenzen: [MEMORY.md](MEMORY.md).

## Modelltypen und Installation

Die Modellverwaltung filtert Hugging-Face-GGUFs nach Textgenerierung, Embeddings, Spracherkennung oder allen Typen. Diese Katalogauswahl ändert die Lore-Suche nicht: Sie bleibt stichwort-/verknüpfungsbasiert. Es gibt noch keine automatische Vektordatenbank oder Audio-Transkription. Installation und Ollama-Prüfung sind in [INSTALLATION-MAC.md](INSTALLATION-MAC.md) erklärt.

## Internetquellen neben Charakteren und Lore

Suchauszüge sind zusätzlicher Kontext für die aktuelle Frage. Sie ersetzen weder Charakterkern noch Lorebook. Das Recherche-Budget zählt zum gesamten Modellfenster; kürzere Auszüge lassen mehr Platz für Verlauf und Antwort. Webinhalte sind fremde Daten und werden nicht als Handlungsanweisungen behandelt. Die Schreibhilfe in den Bibliothekseditoren recherchiert nicht selbst im Internet. Für Recherche zuerst im Chat suchen und die belegten Fakten anschließend gezielt in einen Eintrag übernehmen.

## Dokumentkontext und neue Navigation · 2.0.4

Charaktere, Personas und Lorebooks liegen unter **Storytelling**. Globale Budgets unter **Einstellungen**; die rechte Leiste enthält Einstellungen für den aktuellen Chat/Story/Vergleich. Projektwissen hat ein gemeinsames Budget für Rolle, Profil, Erinnerungen und Auszüge. Gesprächs- und Vergleichsanhänge haben ein eigenes Budget (Standard 2.400 Tokens), zusätzlich begrenzt durch den verbleibenden Kontext. Ausgewählt werden passende Textabschnitte, nicht grundsätzlich ganze Dateien. [Dateien in allen Arbeitsbereichen](NUTZUNG.md#dateien-per-drag-and-drop).
