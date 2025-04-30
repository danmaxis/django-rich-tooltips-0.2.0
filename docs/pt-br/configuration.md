# Configuração

Alguns comportamentos básicos do tooltip podem ser configurados alterando constantes no topo do arquivo `/static/rich_tooltips/js/rich_tooltips.js`.

**Observação:** Versões futuras podem expor essas configurações através das settings do Django para facilitar a configuração sem modificar diretamente os arquivos estáticos do plugin.

*   `HOVER_DELAY_MS`: Tempo em milissegundos que o usuário deve pairar sobre o elemento gatilho antes que o tooltip se torne fixo (permitindo interação com seu conteúdo). Padrão: `1000` (1 segundo).
*   `HIDE_DELAY_MS`: Pequeno atraso em milissegundos antes que o tooltip se esconda após o mouse deixar o elemento gatilho ou o tooltip fixo. Isso ajuda a prevenir o fechamento acidental ao mover o mouse levemente. Padrão: `200` (0.2 segundos).

