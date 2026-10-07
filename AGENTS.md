# Release-Freigaben

Diese Vorgaben stammen ausdrücklich vom Projekteigentümer (7. Oktober 2026).

- Neue Veröffentlichungen sind standardmäßig **Beta**: GitHub `prerelease=true`, `make_latest=false`; im Titel „Beta“ nennen. Numerische Versionsnummern beibehalten, weil der bestehende Updater numerische Versionen erwartet.
- Eine Version darf nur nach ausdrücklicher Freigabe des Eigentümers als **stabil und bereit für Updates** markiert werden. Erfolgreiche Tests, fertige Dokumentation oder ein allgemeiner Auftrag zur Veröffentlichung sind keine stabile Freigabe. Ohne solche Freigabe die fertig geprüfte Beta veröffentlichen, keine unnötige Rückfrage.
- Nur eine ausdrücklich freigegebene neue stabile Version wird `Latest`. Ein historischer stabiler Vorgänger bleibt `make_latest=false`.
- Die App prüft standardmäßig nur auf die neueste stabile Version. Betas sind nur nach bewusstem Aktivieren von „Auch Vorabversionen“ (Beta-Kanal) zulässig. Die bestehende Benutzerauswahl nicht stillschweigend ändern.
- Aktuell freigegeben: **2.0.7** (aktuell stabil / Latest; ausdrücklich am 7. Oktober 2026 freigegeben), **2.0.4** (ältere stabile Version), **2.0.2** (stabiler Vorgänger, erster öffentlicher Updater). Intern existierte der Updater schon in 2.0.1, aber noch mit privater Repository-Adresse. Öffentliche Versionsübersichten beginnen bei 2.0.2; 1.7.1 wird nicht mehr öffentlich gelistet.
- Eine neu installierte Beta darf nicht automatisch zur älteren stabilen App zurückgestuft werden. Der Kanalwechsel steuert künftige Angebote, nicht einen Downgrade.
- Nach einer Freigabe Release-Flags, Titel, README und Update-Hinweise konsistent halten und den Standardkanal mit der Update-Logik prüfen.
