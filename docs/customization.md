# Customization (CSS)

The appearance of the tooltips is controlled by the CSS file located at `/static/rich_tooltips/css/rich_tooltips.css`.

This file uses Django Admin's CSS variables (like `--body-bg`, `--body-fg`, `--border-color`, `--link-fg`, etc.) to automatically adapt to the light and dark themes configured in your Django administration interface.

You can override these styles in your own custom admin CSS files to change the appearance further. Load your custom CSS file *after* the plugin's CSS file in your `admin/base_site.html` override or using other standard Django admin customization methods.

```css
/* Example override in your custom admin CSS */

/* Target the main tooltip container */
.rich-tooltip-container {
    /* Override specific theme variables or general styles */
    --tooltip-bg: lightyellow; /* Example: Force light yellow background regardless of theme */
    background-color: var(--tooltip-bg);
    color: #333; /* Darker text */
    border: 1px solid #aaa;
    border-radius: 6px; /* More rounded corners */
    box-shadow: 3px 3px 8px rgba(0,0,0,0.25);
    font-size: 1em; /* Make text slightly larger */
    max-width: 450px; /* Allow wider tooltips */
}

/* Customize links within the tooltip */
.rich-tooltip-container a {
    color: darkred;
}

/* Customize the timer */
.rich-tooltip-timer {
    border: 3px solid rgba(0, 0, 0, 0.2); /* Thicker border */
    border-top-color: darkred; /* Change spinning part color */
}

/* Example: Different style for dark theme */
body[data-theme="dark"] .rich-tooltip-container {
    --tooltip-bg: #404040; /* Darker background for dark theme */
    background-color: var(--tooltip-bg);
    border-color: #777;
}

body[data-theme="dark"] .rich-tooltip-timer {
    border-top-color: lightcoral;
}
```

