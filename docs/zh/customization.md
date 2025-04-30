# 自定义 (CSS)

工具提示的外观由位于 `/static/rich_tooltips/css/rich_tooltips.css` 的 CSS 文件控制。

该文件使用 Django Admin 的 CSS 变量（如 `--body-bg`、`--body-fg`、`--border-color`、`--link-fg` 等）来自动适应您在 Django 管理界面中配置的浅色和深色主题。

您可以在自己的自定义管理 CSS 文件中覆盖这些样式，以进一步更改外观。在您的 `admin/base_site.html` 覆盖中或使用其他标准的 Django 管理自定义方法，在插件的 CSS 文件*之后*加载您的自定义 CSS 文件。

```css
/* 在您的自定义管理 CSS 中的覆盖示例 */

/* 目标主工具提示容器 */
.rich-tooltip-container {
    /* 覆盖特定的主题变量或通用样式 */
    --tooltip-bg: lightyellow; /* 示例：无论主题如何，强制使用浅黄色背景 */
    background-color: var(--tooltip-bg);
    color: #333; /* 较深的文本 */
    border: 1px solid #aaa;
    border-radius: 6px; /* 更圆的边角 */
    box-shadow: 3px 3px 8px rgba(0,0,0,0.25);
    font-size: 1em; /* 使文本稍大 */
    max-width: 450px; /* 允许更宽的工具提示 */
}

/* 自定义工具提示内的链接 */
.rich-tooltip-container a {
    color: darkred;
}

/* 自定义计时器 */
.rich-tooltip-timer {
    border: 3px solid rgba(0, 0, 0, 0.2); /* 更粗的边框 */
    border-top-color: darkred; /* 更改旋转部分的颜色 */
}

/* 示例：深色主题的不同样式 */
body[data-theme="dark"] .rich-tooltip-container {
    --tooltip-bg: #404040; /* 深色主题的较暗背景 */
    background-color: var(--tooltip-bg);
    border-color: #777;
}

body[data-theme="dark"] .rich-tooltip-timer {
    border-top-color: lightcoral;
}
```

