# Web-Recherche in StoryCore 1.7.1

Unter **App verwalten → Web-Recherche** den Anbieter wählen, dessen API-Schlüssel eintragen, **Web-Recherche erlauben** aktivieren und **Einstellungen speichern**. Die Recherche ist anfangs ausgeschaltet. Keine Browserbedienung, kein Container und keine zusätzliche Suchsoftware erforderlich.

## Tavily: Konto und Schlüssel

1. [Tavily-Dashboard](https://app.tavily.com/) öffnen und ein Konto erstellen. Falls verlangt, die E-Mail-Adresse bestätigen.
2. Im Dashboard unter **API Keys** einen Schlüssel erstellen oder einen vorhandenen kopieren.
3. In StoryCore **Tavily · Recherche mit Textauszügen** wählen und den Schlüssel einfügen.
4. Recherche erlauben und speichern.

Tavily liefert Titel, URLs und relevante Textauszüge. StoryCore nutzt **Basic Search**, ohne zusätzliche generierte Antwort, Rohseiten oder automatische Wahl einer teureren Suchtiefe. Stand 6. Oktober 2026: 1.000 kostenlose Credits pro Monat ohne Kreditkarte; Basic kostet einen Credit pro Anfrage. Maßgeblich sind die [aktuellen Kontingente und Preise](https://docs.tavily.com/documentation/api-credits).

## Serper: Konto und Schlüssel

1. [Serper-Registrierung](https://serper.dev/signup) öffnen; Name, E-Mail-Adresse und Passwort eingeben. Falls verlangt, E-Mail bestätigen.
2. Im angemeldeten Dashboard den **API Key** kopieren.
3. In StoryCore **Serper · Google-Suchergebnisse** wählen und den Schlüssel einfügen.
4. Recherche erlauben und speichern.

Serper ist ein Drittanbieter für Google-Suchergebnisse, keine offizielle Google-API. StoryCore nutzt die normale Websuche mit deutscher Sprache/Region und übernimmt Titel, Links und Kurztexte aus den organischen Treffern. Andere Antwortbestandteile wie generierte Zusammenfassungen werden nicht als Belege übernommen. Es werden zehn Treffer angefragt; die konfigurierten Quellen- und Tokenlimits begrenzen die tatsächliche Übernahme.

Stand 6. Oktober 2026 bietet Serper 2.500 kostenlose Testabfragen ohne Kreditkarte an. Das ist ein Startkontingent, kein zugesagtes monatliches Gratis-Kontingent. [Angebot und Preise](https://serper.dev/).

## Brave und bestehendes SearXNG

Brave bleibt verfügbar: im [Brave-API-Dashboard](https://api-dashboard.search.brave.com/) registrieren, Search-Zugang auswählen, unter **API Keys** einen Schlüssel erstellen und in StoryCore bei **Brave Search API** eintragen. Der Brave-Browser ist nicht erforderlich.

Brave-Quellen werden standardmäßig nur vorübergehend für die aktuelle Anfrage verarbeitet. Ohne ausdrücklich bestätigte vertragliche Speicherrechte werden Auszüge und vollständige Prompt-Kopien aus gespeicherten Chats/Vergleichen entfernt. Die Modellantwort bleibt erhalten und kann Quellentexte zitieren. Nur bei entsprechenden Rechten **Mein Brave-Vertrag erlaubt das Speichern der Suchergebnisse** aktivieren. [Anbieterinformationen](https://brave.com/search/api/).

Bestehende SearXNG-Einstellungen bleiben kompatibel; eine bereits konfigurierte Instanz wird weiterhin angeboten. Es wird kein Container installiert. SearXNG benötigt einen separat betriebenen Dienst mit JSON-Ausgabe.

## Suchen und Quellen verwenden

1. Unter **Schreiben** oder **Modellvergleich** die Web-Recherche einschalten.
2. Eigene **Suchbegriffe** eingeben und **Im Web suchen** anklicken.
3. Quellen und Auszüge aufklappen und prüfen.
4. Die eigentliche Frage senden bzw. den Vergleich starten. Beide Vergleichsmodelle erhalten denselben vorbereiteten Quellenkontext.
5. Nach Sendebeginn ist die Recherche wieder aus; für die nächste Frage erneut bewusst einschalten.

Es werden ausschließlich die Suchbegriffe an den ausgewählten Dienst übertragen, nicht automatisch Charakterkarten oder Chatverläufe. Das gewählte LLM verarbeitet die zurückgegebenen Auszüge. Die Modelllaufzeit bleibt unverändert: lokales Ollama bleibt lokal; ein lokal konfigurierter OpenAI-kompatibler Server erhält den Prompt einschließlich Quellen; ob er selbst weiterleitet, hängt von seiner Konfiguration ab.

## Schlüssel, Wechsel und Grenzen

- Tavily, Serper und Brave haben getrennte Schlüssel. Ein Anbieterwechsel sendet keinen Schlüssel an den anderen Anbieter.
- Schlüssel liegen lokal in `settings.json` mit Dateirechten 0600, nicht im macOS-Schlüsselbund. Die Einstellungs-API liefert nur den Status „gespeichert“, keine Schlüssel zurück. Schlüssel gelangen nicht in Modell-Prompts, Chats, Projekt-Exporte oder SBOM. Manuelle Settings-Backups können sie enthalten.
- Ein leeres, unverändertes Eingabefeld erhält den gespeicherten Schlüssel. **Schlüssel entfernen beim Speichern** löscht ausschließlich den Schlüssel des ausgewählten Anbieters.
- Standard: maximal vier Quellen und 1.200 geschätzte Tokens, einstellbar auf 1–8 Quellen und 256–4.096 Tokens. Titel, URLs und Suchbegriffe zählen mit; kurze Nutzungsanweisungen kommen hinzu.
- HTTP-Antworten sind auf 1 MB begrenzt, Anfragen auf 20 Sekunden. Kein automatischer Anbieterwechsel, keine automatische Folge-Recherche oder Abrufe gefundener Webseiten.
- Ungültige Schlüssel, leere Ergebnisse und ausgeschöpfte Kontingente werden als Fehler angezeigt. Es werden keine Treffer erfunden.
- Suchentwürfe gelten maximal 30 Minuten und nur für ihren Chat. Einstellungsänderungen verwerfen diese Entwürfe.
- Beim Laden einer nicht mehr unterstützten Anbieter-Einstellung wird Tavily gewählt und die Recherche ausgeschaltet. Andere Einstellungen und historische Quellen bleiben erhalten.

## Teststand

Anbieteranbindungen wurden mit simulierten Antworten getestet. Ein erfolgreicher produktiver Tavily-/Serper-Live-Test mit einem echten Schlüssel steht noch aus. Suchauszüge sind kein Echtzeit-Börsenkursfeed.

## Wenn die Suche nicht startet

| Anzeige / Situation | Nächster Schritt |
| --- | --- |
| Recherche ausgeschaltet | Global unter App verwalten erlauben und speichern; danach zusätzlich im Chat/Modellvergleich einschalten. |
| API-Schlüssel fehlt / Zugriff verweigert | Den Schlüssel des ausgewählten Anbieters prüfen, neu einfügen und speichern. Ein Schlüssel für Tavily funktioniert nicht bei Serper. |
| Suchlimit oder Guthaben aufgebraucht | Verbrauch und Kontingent im Anbieter-Dashboard prüfen; nicht wiederholt blind suchen. |
| Keine verwertbaren Treffer | Suchbegriffe konkreter formulieren; gegebenenfalls Quellen-/Tokenbudget anpassen. |
| Recherche abgelaufen | Nach 30 Minuten oder nach geänderten Einstellungen erneut suchen. |
| Kontextfenster voll | Recherche-Budget verkleinern, Verlauf komprimieren oder einen passenden größeren Kontext wählen. |

Ein Suchlauf startet keine LLM-Antwort. Erst **Senden** beziehungsweise **Vergleich starten** übergibt die geprüften Quellen an die Modelle. Nach Sendebeginn ist der Recherche-Schalter wieder aus. Ohne Web-Recherche verwendet das Modell sein vorhandenes Wissen und den lokalen Gesprächskontext.

Die bebilderte [Nutzungsanleitung](https://github.com/YorkStack/StoryCore-Releases/releases/download/v2.0.2/StoryCore-Erste-Schritte.pdf) führt durch Einrichtung und eine Beispielrecherche. Kurzfassung als Text: [Nutzung](NUTZUNG.md).
