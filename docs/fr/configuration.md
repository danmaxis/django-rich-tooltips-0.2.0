# Configuration

Certains comportements de base de l'infobulle peuvent être configurés en modifiant les constantes en haut du fichier `/static/rich_tooltips/js/rich_tooltips.js`.

**Note :** Les versions futures pourraient exposer ces paramètres via les settings de Django pour une configuration plus facile sans modifier directement les fichiers statiques du plugin.

*   `HOVER_DELAY_MS` : Temps en millisecondes pendant lequel l'utilisateur doit survoler l'élément déclencheur avant que l'infobulle ne devienne fixe (permettant l'interaction avec son contenu). Défaut : `1000` (1 seconde).
*   `HIDE_DELAY_MS` : Court délai en millisecondes avant que l'infobulle ne se masque après que la souris quitte l'élément déclencheur ou l'infobulle fixe. Cela aide à prévenir la fermeture accidentelle lors d'un léger mouvement de la souris. Défaut : `200` (0.2 secondes).

