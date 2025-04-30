# Personalización (CSS)

La apariencia de los tooltips se controla mediante el archivo CSS ubicado en `/static/rich_tooltips/css/rich_tooltips.css`.

Este archivo utiliza las variables CSS de Django Admin (como `--body-bg`, `--body-fg`, `--border-color`, `--link-fg`, etc.) para adaptarse automáticamente a los temas claro y oscuro configurados en tu interfaz de administración de Django.

Puedes sobrescribir estos estilos en tus propios archivos CSS personalizados de administración para cambiar aún más la apariencia. Carga tu archivo CSS personalizado *después* del archivo CSS del plugin en tu sobrescritura de `admin/base_site.html` o utilizando otros métodos estándar de personalización de administración de Django.

```css
/* Ejemplo de sobrescritura en tu CSS de administración personalizado */

/* Apunta al contenedor principal del tooltip */
.rich-tooltip-container {
    /* Sobrescribe variables de tema específicas o estilos generales */
    --tooltip-bg: lightyellow; /* Ejemplo: Fuerza un fondo amarillo claro independientemente del tema */
    background-color: var(--tooltip-bg);
    color: #333; /* Texto más oscuro */
    border: 1px solid #aaa;
    border-radius: 6px; /* Esquinas más redondeadas */
    box-shadow: 3px 3px 8px rgba(0,0,0,0.25);
    font-size: 1em; /* Hace el texto ligeramente más grande */
    max-width: 450px; /* Permite tooltips más anchos */
}

/* Personaliza los enlaces dentro del tooltip */
.rich-tooltip-container a {
    color: darkred;
}

/* Personaliza el temporizador */
.rich-tooltip-timer {
    border: 3px solid rgba(0, 0, 0, 0.2); /* Borde más grueso */
    border-top-color: darkred; /* Cambia el color de la parte giratoria */
}

/* Ejemplo: Estilo diferente para tema oscuro */
body[data-theme="dark"] .rich-tooltip-container {
    --tooltip-bg: #404040; /* Fondo más oscuro para tema oscuro */
    background-color: var(--tooltip-bg);
    border-color: #777;
}

body[data-theme="dark"] .rich-tooltip-timer {
    border-top-color: lightcoral;
}
```

