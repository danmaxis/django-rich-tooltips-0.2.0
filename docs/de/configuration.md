# Konfiguration

Einige grundlegende Tooltip-Verhaltensweisen können durch Ändern von Konstanten am Anfang der Datei `/static/rich_tooltips/js/rich_tooltips.js` konfiguriert werden.

**Hinweis:** Zukünftige Versionen könnten diese Einstellungen über Django-Settings verfügbar machen, um die Konfiguration zu erleichtern, ohne die statischen Dateien des Plugins direkt ändern zu müssen.

*   `HOVER_DELAY_MS`: Zeit in Millisekunden, die der Benutzer über das Auslöseelement schweben muss, bevor der Tooltip fixiert wird (was die Interaktion mit seinem Inhalt ermöglicht). Standard: `1000` (1 Sekunde).
*   `HIDE_DELAY_MS`: Kurze Verzögerung in Millisekunden, bevor der Tooltip ausgeblendet wird, nachdem die Maus das Auslöseelement oder den fixierten Tooltip verlassen hat. Dies hilft, versehentliches Schließen bei leichter Mausbewegung zu verhindern. Standard: `200` (0,2 Sekunden).

