# NiceGUI 开发技能

NiceGUI（Python Web UI 框架）开发技能，适用于所有 AI agent。推荐在 OpenClaw 上使用。

## 功能特性

- **组件创建** - 使用 `ui.button`、`ui.card`、`ui.dialog`、`ui.input`、`ui.table`、`ui.echart`、`ui.aggrid` 等构建 UI
- **事件处理** - 基于 lambda 的事件处理器，支持异步、定时器和键盘事件
- **样式系统** - Tailwind CSS 类、Quasar 属性、内联 CSS 样式
- **数据绑定** - `.bind_value()` 双向绑定，`_from`/`_to` 单向绑定变体
- **路由系统** - 页面装饰器、路由参数、子页面、多页面应用
- **调试支持** - 错误处理、日志记录、UI 状态检查

## 快速开始

```python
from nicegui import ui

# 基础 UI
with ui.card():
    ui.label('你好 NiceGUI!')
    ui.button('点击我', on_click=lambda: ui.notify('点击了!'))

ui.run()
```

## 核心规则

1. **始终使用 `from nicegui import ui`**
2. **组件作为上下文管理器**：布局容器（`card`、`column`、`row`、`dialog` 等）使用 `with` 语句
3. **事件处理用 lambda**：`on_click=lambda: ...`，需要异步时用 `async def`
4. **样式三件套**：`.classes()` 加 Tailwind 类、`.style()` 加内联 CSS、`.props()` 加 Quasar 属性
5. **绑定用 `.bind_value()`**：双向绑定首选，单向用 `_from`/`_to` 变体
6. **最低 Python 3.10**：NiceGUI 3.7+ 不再支持 Python 3.9

## 支持的组件

| 类别 | 组件 |
|------|------|
| **文本** | `ui.label`、`ui.markdown`、`ui.code`、`ui.html`、`ui.restructured_text` |
| **输入** | `ui.input`、`ui.textarea`、`ui.number`、`ui.select`、`ui.radio`、`ui.checkbox`、`ui.switch`、`ui.toggle`、`ui.slider`、`ui.range`、`ui.rating`、`ui.date`、`ui.date_input`、`ui.time`、`ui.time_input`、`ui.color_input`、`ui.color_picker`、`ui.upload`、`ui.editor`、`ui.codemirror` |
| **按钮** | `ui.button`、`ui.button_group`、`ui.fab`、`ui.dropdown_button`、`ui.badge`、`ui.chip` |
| **布局** | `ui.card`、`ui.column`、`ui.row`、`ui.grid`、`ui.expansion`、`ui.scroll_area`、`ui.splitter`、`ui.separator`、`ui.space`、`ui.skeleton` |
| **导航** | `ui.link`、`ui.menu`、`ui.context_menu`、`ui.tabs`、`ui.stepper`、`ui.pagination`、`ui.carousel`、`ui.timeline`、`ui.tooltip` |
| **弹窗** | `ui.dialog`、`ui.notify`、`ui.notification` |
| **数据** | `ui.table`、`ui.aggrid`、`ui.tree`、`ui.log`、`ui.list` |
| **图表** | `ui.echart`、`ui.plotly`、`ui.highchart`、`ui.line_plot`、`ui.altair`、`ui.mermaid` |
| **地图/3D** | `ui.leaflet`、`ui.scene`、`ui.joystick` |
| **媒体** | `ui.image`、`ui.interactive_image`、`ui.audio`、`ui.video`、`ui.parallax` |
| **特殊** | `ui.json_editor`、`ui.xterm`、`ui.anywidget`、`ui.timer`、`ui.refreshable`、`ui.run_javascript`、`ui.keyboard`、`ui.download`、`ui.status_code` |

## 参考资源

- [NiceGUI 官方文档](https://nicegui.io/documentation)
- [NiceGUI GitHub](https://github.com/zauberzeug/nicegui)
- [Quasar 组件](https://quasar.dev/vue-components)
- [Tailwind CSS](https://tailwindcss.com/docs)

## License

MIT