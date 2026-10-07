# Prüfprotokoll

## 2.0.4 · Dokumente in allen Arbeitsbereichen

- 226 Vitest-Tests in 23 Dateien sowie TypeScript/Vite-Build erfolgreich; 23 Installertests erfolgreich.
- Gemeinsamer Drop-Handler: PDF/DOCX/XLSX-Routing an die aktive Ablage, Sperren während Verarbeitung, Text-Dragging unverändert und Listener-Cleanup getestet.
- Browser-UI mit isolierten synthetischen Daten: PDF/DOCX/XLSX in Projektwissen und Chat, TXT in Story, PDF/DOCX im Modellvergleich. Vergleich erneut geöffnet: Originale, vollständiger Prompt und Modellwahl erhalten; Übernahme in Chat ohne doppelte Auszug-Nachrichten geprüft.
- Nativer 2.0.4-Build, Update-Signaturprüfung und Wiederherstellungstests erfolgreich (3 Rust-Tests). Gepacktes Backend ohne System-Node: leere Bibliothek, vier neutrale Presets, Authentifizierung und 733 SBOM-Komponenten geprüft. ZIP- und DMG-Integritätsprüfung erfolgreich.
- Zwei doppelte React-Komponentenschlüssel korrigiert; bei Chatwechsel und Wiederöffnung wird genau eine Dateileiste angezeigt.
- Beide Modelle erhalten im Integrationstest identische Nachrichten, keine Original-Binärdateien im Prompt. Originale werden einmal im gemeinsamen Vergleichskontext gespeichert.
- README und alle aktuellen Benutzeranleitungen aktualisiert; elf PDF-Seiten (2 Installation, 9 Nutzung) gerendert und visuell kontrolliert. Screenshots aus Version 2.0.4 mit neutraler Demo-Bibliothek.
- Die UI-Testantworten sind simuliert, kein neuer Leistungsbenchmark. Die echte lokale Ollama-Dateiprüfung aus 2.0.3 bleibt unten dokumentiert. Der tatsächliche Finder-Drag zwischen nativen Fenstern wurde nicht automatisiert ausgeführt; Drop-Routing und sichtbare Dateiauswahl sind getrennt geprüft.


## Grenzen

Geprüft auf M2 Pro mit macOS 27.0.1. Keine vollständige Testmatrix für alle Macs. Keine Apple-Notarisierung. Live-Recherche mit produktiven Tavily-/Serper-Schlüsseln bleibt separat zu prüfen. Die Datenformat-Version bleibt 1; keine Migration oder Löschung. Der tatsächliche automatische Neustart bei einem öffentlich heruntergeladenen Update bleibt separat zu prüfen.
