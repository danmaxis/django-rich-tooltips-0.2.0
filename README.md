# Django Rich Tooltips

[![Version](https://img.shields.io/badge/version-0.2.0-blue)](.)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Django plugin to add rich, interactive HTML and Markdown tooltips to the admin interface, inspired by interfaces like Crusader Kings.

## Screenshots
![image](https://github.com/user-attachments/assets/fa073eb3-28af-448b-9e67-b424150197bf)
![image](https://github.com/user-attachments/assets/47161c3e-dacf-4f5d-b7de-f913bcfbfabc)




## Features

*   **Rich Content:** Display tooltips with raw HTML or Markdown.
*   **Interactive:** Tooltips can be "fixed" by hovering, allowing interaction.
*   **Visual Timer:** A spinning circle indicates the time until the tooltip is fixed.
*   **Theme Aware:** Automatically adapts to Django Admin's light/dark themes.
*   **Dynamic List Tooltips:** Tooltip content in `list_display` can come from model fields or methods.
*   **Nested Tooltips:** Supports tooltips within fixed tooltips.
*   **Admin Integration:** Works in list, add, and change views.
*   **Customizable:** Appearance controlled via CSS.

## Documentation

Full documentation is available in the `docs/` directory:

*   **[Installation](./docs/installation.md)**: How to install and set up the plugin.
*   **[Usage](./docs/usage.md)**: Examples of how to add tooltips in `admin.py` and templates.
*   **[Configuration](./docs/configuration.md)**: Details on configurable JavaScript variables.
*   **[Customization](./docs/customization.md)**: How to customize the appearance using CSS.
*   **[Development & Testing](./docs/development.md)**: Instructions for setting up a development environment and running tests.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

