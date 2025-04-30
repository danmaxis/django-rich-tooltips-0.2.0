# Customização (CSS)

A aparência dos tooltips é controlada pelo arquivo CSS localizado em `/static/rich_tooltips/css/rich_tooltips.css`.

Este arquivo usa as variáveis CSS do Django Admin (como `--body-bg`, `--body-fg`, `--border-color`, `--link-fg`, etc.) para se adaptar automaticamente aos temas claro e escuro configurados na sua interface de administração do Django.

Você pode sobrescrever esses estilos em seus próprios arquivos CSS personalizados do admin para alterar ainda mais a aparência. Carregue seu arquivo CSS personalizado *após* o arquivo CSS do plugin na sua sobrescrita de `admin/base_site.html` ou usando outros métodos padrão de customização do admin do Django.

```css
/* Exemplo de sobrescrita no seu CSS personalizado do admin */

/* Alvo do container principal do tooltip */
.rich-tooltip-container {
    /* Sobrescreve variáveis de tema específicas ou estilos gerais */
    --tooltip-bg: lightyellow; /* Exemplo: Força fundo amarelo claro independentemente do tema */
    background-color: var(--tooltip-bg);
    color: #333; /* Texto mais escuro */
    border: 1px solid #aaa;
    border-radius: 6px; /* Cantos mais arredondados */
    box-shadow: 3px 3px 8px rgba(0,0,0,0.25);
    font-size: 1em; /* Torna o texto ligeiramente maior */
    max-width: 450px; /* Permite tooltips mais largos */
}

/* Customiza links dentro do tooltip */
.rich-tooltip-container a {
    color: darkred;
}

/* Customiza o timer */
.rich-tooltip-timer {
    border: 3px solid rgba(0, 0, 0, 0.2); /* Borda mais espessa */
    border-top-color: darkred; /* Muda a cor da parte giratória */
}

/* Exemplo: Estilo diferente para tema escuro */
body[data-theme="dark"] .rich-tooltip-container {
    --tooltip-bg: #404040; /* Fundo mais escuro para tema escuro */
    background-color: var(--tooltip-bg);
    border-color: #777;
}

body[data-theme="dark"] .rich-tooltip-timer {
    border-top-color: lightcoral;
}
```

