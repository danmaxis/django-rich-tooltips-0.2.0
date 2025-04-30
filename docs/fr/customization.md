# Personnalisation (CSS)

L'apparence des infobulles est contrôlée par le fichier CSS situé à `/static/rich_tooltips/css/rich_tooltips.css`.

Ce fichier utilise les variables CSS de Django Admin (comme `--body-bg`, `--body-fg`, `--border-color`, `--link-fg`, etc.) pour s'adapter automatiquement aux thèmes clair et sombre configurés dans votre interface d'administration Django.

Vous pouvez surcharger ces styles dans vos propres fichiers CSS d'administration personnalisés pour modifier davantage l'apparence. Chargez votre fichier CSS personnalisé *après* le fichier CSS du plugin dans votre surcharge de `admin/base_site.html` ou en utilisant d'autres méthodes standard de personnalisation de l'administration Django.

```css
/* Exemple de surcharge dans votre CSS d'administration personnalisé */

/* Cible le conteneur principal de l'infobulle */
.rich-tooltip-container {
    /* Surcharge des variables de thème spécifiques ou des styles généraux */
    --tooltip-bg: lightyellow; /* Exemple : Force un fond jaune clair quel que soit le thème */
    background-color: var(--tooltip-bg);
    color: #333; /* Texte plus sombre */
    border: 1px solid #aaa;
    border-radius: 6px; /* Coins plus arrondis */
    box-shadow: 3px 3px 8px rgba(0,0,0,0.25);
    font-size: 1em; /* Rend le texte légèrement plus grand */
    max-width: 450px; /* Permet des infobulles plus larges */
}

/* Personnalise les liens dans l'infobulle */
.rich-tooltip-container a {
    color: darkred;
}

/* Personnalise le minuteur */
.rich-tooltip-timer {
    border: 3px solid rgba(0, 0, 0, 0.2); /* Bordure plus épaisse */
    border-top-color: darkred; /* Change la couleur de la partie tournante */
}

/* Exemple : Style différent pour le thème sombre */
body[data-theme="dark"] .rich-tooltip-container {
    --tooltip-bg: #404040; /* Fond plus sombre pour le thème sombre */
    background-color: var(--tooltip-bg);
    border-color: #777;
}

body[data-theme="dark"] .rich-tooltip-timer {
    border-top-color: lightcoral;
}
```

