# Portable Formate

Aktueller Funktionsstand: **2.0.4 Vorabversion · 7. Oktober 2026**.
[Dokumentationsübersicht](../README.md#anleitungen).

Recherchierte Primärquellen, 28. September 2026:

- [Character Card V3 specification](https://github.com/kwaroran/character-card-spec-v3/blob/main/SPEC_V3.md)
- [Character Card V2 specification](https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v2.md)
- [SillyTavern Personas](https://docs.sillytavern.app/usage/core-concepts/personas/)
- [Ollama Chat API](https://docs.ollama.com/api/chat)
- [Ollama Generate API](https://docs.ollama.com/api/generate)
- [Ollama API types, including remote_model/remote_host](https://github.com/ollama/ollama/blob/main/api/types.go)

## Character Card V3

Persistente Dateien sind unmittelbar `{"spec":"chara_card_v3","spec_version":"3.0","data":{...}}`. Pflichtfelder werden validiert. Unbekannte Top-Level-, Daten- und Extension-Felder werden nicht entfernt. Neuere Versionsstrings werden erhalten und beim Promptbau gemeldet. Assets werden als Daten erhalten, nicht geladen. Erzeugte Karten verwenden `creation_date` in Unix-Sekunden. Bestehende Karten behalten ihre Zeitfelder unverändert; die Anwendung interpretiert Export als verlustfreie Serialisierung und verändert deshalb beim Export keine Zeitfelder.

`background` und `appearance` sind **keine CCv3-Kernfelder**. Hintergrund und ergänzender Aussehen-Freitext liegen aus Kompatibilitätsgründen unter `data.extensions.still`. Die optionalen Einzelmerkmale Größe, Körperbau, Haarfarbe/-länge, Frisur, Augenfarbe, Merkmale und Kleidung stehen unter `data.extensions.storycore.appearance`. Beim Export ergänzt StoryCore diese Fakten in `description` und merkt den genauen Zusatz als `portableDescriptionSuffix`; nur ein unveränderter eigener Zusatz wird beim Reimport wieder aus der Arbeitsbeschreibung entfernt. Fremde Änderungen bleiben erhalten. Der kurze Kontextkern liegt unter `data.extensions.storycore.core`. Andere Programme dürfen Extensions ignorieren.

CCv2 wird auf `chara_card_v3` / `3.0` umgestellt und erhält `group_only_greetings: []`; fehlendes `use_regex` in Lore-Einträgen wird zu `false`. Inhalt, unbekannte Felder und Extensions bleiben erhalten. Fehlerhafte Pflichtfelder werden nicht stillschweigend erfunden.

`{{char}}`, `<char>`, `<bot>`, `{{user}}`, `<user>` werden im Prompt ersetzt. `nickname` hat Vorrang vor `name`. `{{original}}` im Character-System-Prompt setzt den Basis-System-Prompt ein. Weitere Community-Makros sind nicht implementiert. Creator Notes werden im Editor und bei Auswahl angezeigt, aber nicht an das Modell gesendet.

## Lorebooks

Stand-alone-Dateien: `{"spec":"lorebook_v3","data":Lorebook}` gemäß CCv3. Character-bound: `data.character_book` als unmittelbares Lorebook. Ein unwrapped Lorebook kann importiert werden und wird beim Export in `lorebook_v3` gehüllt.

Mehrere `keys` werden mit ODER verknüpft. `selective` plus `secondary_keys` fügt eine zusätzliche ODER-Bedingung hinzu. Matching ist Unicode-Substring-Matching, standardmäßig ohne Beachtung der Groß-/Kleinschreibung. Disabled überschreibt constant. Leere Inhalte und Schlüssel werden ignoriert. Niedrigere insertion_order erscheint früher im Prompt; größere priority gewinnt bei Budgetkonflikten. before_char wird vor dem Character-Abschnitt eingefügt, andere Einträge im LORE-Abschnitt.

Budgetierung und Nachladen sind in **Einstellungen** einstellbar: standardmäßig 800 Lore-Tokens insgesamt, 240 je Eintrag, fünf Einträge, eine Nachladeebene und vier gescannte Nachrichten. Schema-Grenzen sind maximal 16.384 Lore-Tokens, 4.096 pro Eintrag, 64 Einträge und vier Ebenen. Der verbleibende Platz im Kontext sowie Buchbudgets können diese Grenzen weiter reduzieren. Keyword-Rekursion ist standardmäßig aus. Explizite Verknüpfungen, Ein-/Ausschluss und Geheimnis-Freigaben werden zusätzlich berücksichtigt; Details unter [Kontextsteuerung](CONTEXT.md).

Referenzen verwenden `<Buch-ID>:<Eintrags-ID>`; wenn eine ältere Datei keine Eintrags-ID hat, dient zunächst deren Index als Ersatz. Beim Speichern werden fehlende IDs ergänzt. Die Buch-ID ist eine lokale Dateireferenz; Projektimport ordnet sie neu zu.

Regex und Dekoratoren werden mit Warnung übersprungen. Alle Felder bleiben erhalten. Locations und NPCs sind gewöhnliche Lore-Einträge, optional `extensions.still.type: "location" | "npc"` sowie `extensions.still.tags: string[]`.

## Eigene, ausdrücklich anwendungsspezifische JSON-Formate

Es wird **kein** universeller Standard für die folgenden Hüllen behauptet:

- `still_persona_v1`: `name`, `description`, `personality`, `background`, `notes` (Strings). Alle Felder außer `format` werden in den Persona-Prompt übernommen.
- `still_preset_v1`: `name`, `options` mit sechs Ollama-Optionen.
- `still_chat_v1`: lokale `id`, `title`, `created_at`, `updated_at`, `mode`, Komponentenreferenzen `characterId`, `personaId`, `lorebookIds`, `projectId`, Modell, Optionen, System-Prompt, Lore-Einstellungen, optional `archived_at`, `context` und `messages`. `context` enthält Szenenzustand, manuelle Ein-/Ausschlüsse, Geheimnis-Freigaben und optional `memory`; dessen Schema und Aktivierungsprüfung sind in [MEMORY.md](MEMORY.md) beschrieben.
- Nachrichten: `id`, `role`, `content`, ISO-Zeitstempel, bei Antworten optional `model`, `options`, `prompt`, `metrics`, `status`, `error`. Prompt-Snapshots enthalten die tatsächlich gesendeten Nachrichten, Optionen, sichtbaren Abschnitte, Aktivierungsgründe und Schätzungen. Spätere Änderungen an Charakterkarten ändern vergangene Snapshots nicht.
- `still_comparison_v1`: `title`, `created_at`, ursprünglicher Chat und Ergebnisse mit Inhalt, Modell, Snapshot, Status und Messwerten. Einzelergebnisse können ohne ursprünglichen Chat gespeichert werden.
- `still_project_v1`: `name`, `description`, ID-Arrays `characters`, `personas`, `lorebooks`, `presets`. Zugehörige Chats referenzieren das Projekt. Unbekannte Felder bleiben erhalten.

## Projekt-ZIP

`project.json` enthält statt lokaler IDs relative `characters/{id}.json`- und entsprechende andere Pfade sowie ein `chats`-Array. Das Archiv enthält jedes referenzierte Objekt einmal, außerdem alle von Projekt-Chats tatsächlich referenzierten Charaktere, Personas und Lorebooks. System-Prompts werden zusätzlich als `prompts/{chat-id}.txt` abgelegt; kanonisch bleibt der Wert im jeweiligen Chat-JSON. Import prüft zuerst alle Daten und Referenzen, vergibt neue IDs und schreibt nur nach erfolgreicher Validierung. Vorhandene Daten werden nicht überschrieben. Unbekannte Dateien werden ignoriert. Historische Prompt-Snapshots bleiben unangetastet.

## Modellgewichte und Pakete

LLM-Gewichte sind keine Projektbestandteile und werden weder als Character Card noch im Projekt-ZIP exportiert. GGUF ist ein Modellgewichtsformat; PNG/CHARX-Kartenimporte sind weiterhin nicht implementiert. Installer-ZIP und DMG enthalten Programmdateien und Installationshinweise, keine persönliche Bibliothek.

## Recherche-Snapshots

Antworten und Vergleiche können einen `research`-Snapshot mit Anbieter, Suchbegriffen, Abrufzeitpunkt, Quellen-IDs, Titeln, URLs, Textauszügen und geschätzten Tokens enthalten. Quellen werden nicht beim Öffnen automatisch nachgeladen. Historische Anbieterkennungen bleiben importierbar, aktivieren aber keine Suchanbindung.

Tavily-/Serper-Quellen bleiben mit der Antwort gespeichert. Brave-Auszüge und vollständige Promptkopien werden ohne bestätigte vertragliche Speicherrechte vor Speicherung/Export entfernt; die Modellantwort bleibt erhalten und kann Quellen zitieren. API-Schlüssel liegen ausschließlich in der lokalen Konfiguration und gehören nicht in Chat-, Karten- oder Projekt-Exporte. Ein manuelles Backup von `settings.json` kann hingegen Zugangsdaten enthalten.

## Dokumentanhänge · 2.0.4

Chat und Vergleich enthalten optionale Anhänge einschließlich Originalbytes (Base64), Textblöcken, Dateiname, Größe, Format und Aktivierung. Ein gemeinsames Tokenbudget steuert die Auswahl. Im Vergleich liegt dieser Kontext einmal unter `chat`; einzelne gespeicherte Ergebnisse müssen ihn nicht duplizieren. Beim Laden werden frühere Resultate mit eigenem Kontext weiterhin unterstützt. JSON-Exporte können Originaldateien und private Inhalte enthalten. Projektarchive enthalten das Projektwissen und zugeordnete Gesprächsanhänge. [Formate, Limits und Bedienung](NUTZUNG.md#dateien-per-drag-and-drop).
