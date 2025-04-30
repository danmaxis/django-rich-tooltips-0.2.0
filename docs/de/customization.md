# Anpassung (CSS)

Das Erscheinungsbild der Tooltips wird durch die CSS-Datei unter `/static/rich_tooltips/css/rich_tooltips.css` gesteuert.

Diese Datei verwendet die CSS-Variablen von Django Admin (wie `--body-bg`, `--body-fg`, `--border-color`, `--link-fg` usw.), um sich automatisch an die hellen und dunklen Themes anzupassen, die in Ihrer Django-Verwaltungsoberfläche konfiguriert sind.

Sie können diese Stile in Ihren eigenen benutzerdefinierten Admin-CSS-Dateien überschreiben, um das Erscheinungsbild weiter zu ändern. Laden Sie Ihre benutzerdefinierte CSS-Datei *nach* der CSS-Datei des Plugins in Ihrer `admin/base_site.html`-Überschreibung oder über andere Standardmethoden zur Anpassung der Django-Verwaltung.

```css
/* Beispiel für eine Überschreibung in Ihrem benutzerdefinierten Admin-CSS */

/* Ziel ist der Haupt-Tooltip-Container */
.rich-tooltip-container {
    /* Überschreiben Sie spezifische Theme-Variablen oder allgemeine Stile */
    --tooltip-bg: lightyellow; /* Beispiel: Erzwingt einen hellgelben Hintergrund unabhängig vom Theme */
    background-color: var(--tooltip-bg);
    color: #333; /* Dunklerer Text */
    border: 1px solid #aaa;
    border-radius: 6px; /* Stärker abgerundete Ecken */
    box-shadow: 3px 3px 8px rgba(0,0,0,0.25);
    font-size: 1em; /* Macht den Text etwas größer */
    max-width: 450px; /* Erlaubt breitere Tooltips */
}

/* Passen Sie Links innerhalb des Tooltips an */
.rich-tooltip-container a {
    color: darkred;
}

/* Passen Sie den Timer an */
.rich-tooltip-timer {
    border: 3px solid rgba(0, 0, 0, 0.2); /* Dickerer Rand */
    border-top-color: darkred; /* Ändert die Farbe des rotierenden Teils */
}

/* Beispiel: Anderer Stil für dunkles Theme */
body[data-theme="dark"] .rich-tooltip-container {
    --tooltip-bg: #404040; /* Dunklerer Hintergrund für dunkles Theme */
    background-color: var(--tooltip-bg);
    border-color: #777;
}

body[data-theme="dark"] .rich-tooltip-timer {
    border-top-color: lightcoral;
}
```

