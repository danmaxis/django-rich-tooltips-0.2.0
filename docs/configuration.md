# Configuration

Some basic tooltip behavior can be configured by changing constants at the top of the `/static/rich_tooltips/js/rich_tooltips.js` file.

**Note:** Future versions might expose these settings via Django settings for easier configuration without modifying the plugin's static files directly.

*   `HOVER_DELAY_MS`: Time in milliseconds the user must hover over the trigger element before the tooltip becomes fixed (allowing interaction with its content). Default: `1000` (1 second).
*   `HIDE_DELAY_MS`: Short delay in milliseconds before the tooltip hides after the mouse leaves the trigger element or the fixed tooltip. This helps prevent accidental closing when moving the mouse slightly. Default: `200` (0.2 seconds).

