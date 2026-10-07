# Datenschutz und Sicherheitsgrenzen

StoryCore speichert Inhalte und Einstellungen lokal. Keine Telemetrie. Lokale Modellanfragen gehen an den selbst gewählten Modellserver; bei einer entfernten Serveradresse verlassen die Inhalte den Mac.

Internetverbindungen entstehen für Modellkataloge, Modell-Downloads, GitHub-Update-Prüfungen und ausdrücklich aktivierte Web-Recherche. GitHub erhält übliche Verbindungsdaten, keine Chats oder Dokumente. Suchbegriffe gehen an den ausgewählten Suchdienst; nicht automatisch der gesamte Chat. Schlüssel werden lokal in zugriffsbeschränkten Dateien gespeichert, nicht im macOS-Schlüsselbund. Datensicherungen können Schlüssel und persönliche Inhalte enthalten.

Pakete sind derzeit ad-hoc signiert, nicht Apple-notarisiert. Die kryptografische Updatesignatur schützt die vom Updater akzeptierten Pakete, ist aber keine Apple-Entwickleridentität. Gatekeeper und Firewall nicht global deaktivieren. Für lokale Ollama-Nutzung sind keine Router-Portfreigaben nötig.

Keine persönlichen Daten, API-Schlüssel oder vollständigen Chat-Exporte in öffentliche GitHub-Issues stellen. Fehler mit anonymisierten Schritten und Versionsnummer melden. Sicherheitsrelevante vertrauliche Details erst nach Vereinbarung eines nichtöffentlichen Meldewegs teilen.
