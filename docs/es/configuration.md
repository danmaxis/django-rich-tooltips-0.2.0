# Configuración

Algunos comportamientos básicos del tooltip se pueden configurar cambiando constantes al principio del archivo `/static/rich_tooltips/js/rich_tooltips.js`.

**Nota:** Versiones futuras podrían exponer estas configuraciones a través de los settings de Django para una configuración más fácil sin modificar directamente los archivos estáticos del plugin.

*   `HOVER_DELAY_MS`: Tiempo en milisegundos que el usuario debe pasar el cursor sobre el elemento disparador antes de que el tooltip se fije (permitiendo la interacción con su contenido). Predeterminado: `1000` (1 segundo).
*   `HIDE_DELAY_MS`: Pequeño retraso en milisegundos antes de que el tooltip se oculte después de que el ratón abandone el elemento disparador o el tooltip fijado. Esto ayuda a prevenir el cierre accidental al mover ligeramente el ratón. Predeterminado: `200` (0.2 segundos).

