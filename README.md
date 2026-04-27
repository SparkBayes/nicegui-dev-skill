# NiceGUI Dev Skill

A skill for NiceGUI (Python Web UI framework) development. Recommended for use on Claude Code.

## Features

- **Component Creation** - Build UI with `ui.button`, `ui.card`, `ui.dialog`, `ui.input`, `ui.table`, `ui.echart`, `ui.aggrid`, and more
- **Event Handling** - Lambda-based event handlers, async support, timer and keyboard events
- **Styling** - Tailwind CSS classes, Quasar properties, inline CSS styles
- **Data Binding** - Two-way binding with `.bind_value()`, one-way with `_from`/`_to` variants
- **Routing** - Page decorators, route parameters, sub-pages, multi-page apps
- **Debugging** - Error handling, logging, UI state inspection

## Quick Start

```python
from nicegui import ui

# Basic UI
with ui.card():
    ui.label('Hello NiceGUI!')
    ui.button('Click me', on_click=lambda: ui.notify('Clicked!'))

ui.run()
```

## Core Rules

1. **Always use `from nicegui import ui`**
2. **Components as context managers**: Layout containers (`card`, `column`, `row`, `dialog`, etc.) use `with` statements
3. **Event handling with lambda**: `on_click=lambda: ...`, use `async def` when async is needed
4. **Styling triad**: `.classes()` for Tailwind, `.style()` for CSS, `.props()` for Quasar attributes
5. **Binding with `.bind_value()`**: Two-way binding is the primary choice, one-way uses `_from`/`_to` variants
6. **Python 3.10+ required**: NiceGUI 3.7+ no longer supports Python 3.9

## Supported Components

| Category | Components |
|----------|------------|
| **Text** | `ui.label`, `ui.markdown`, `ui.code`, `ui.html`, `ui.restructured_text` |
| **Input** | `ui.input`, `ui.textarea`, `ui.number`, `ui.select`, `ui.radio`, `ui.checkbox`, `ui.switch`, `ui.toggle`, `ui.slider`, `ui.range`, `ui.rating`, `ui.date`, `ui.date_input`, `ui.time`, `ui.time_input`, `ui.color_input`, `ui.color_picker`, `ui.upload`, `ui.editor`, `ui.codemirror` |
| **Buttons** | `ui.button`, `ui.button_group`, `ui.fab`, `ui.dropdown_button`, `ui.badge`, `ui.chip` |
| **Layout** | `ui.card`, `ui.column`, `ui.row`, `ui.grid`, `ui.expansion`, `ui.scroll_area`, `ui.splitter`, `ui.separator`, `ui.space`, `ui.skeleton` |
| **Navigation** | `ui.link`, `ui.menu`, `ui.context_menu`, `ui.tabs`, `ui.stepper`, `ui.pagination`, `ui.carousel`, `ui.timeline`, `ui.tooltip` |
| **Dialogs** | `ui.dialog`, `ui.notify`, `ui.notification` |
| **Data** | `ui.table`, `ui.aggrid`, `ui.tree`, `ui.log`, `ui.list` |
| **Charts** | `ui.echart`, `ui.plotly`, `ui.highchart`, `ui.line_plot`, `ui.altair`, `ui.mermaid` |
| **Maps/3D** | `ui.leaflet`, `ui.scene`, `ui.joystick` |
| **Media** | `ui.image`, `ui.interactive_image`, `ui.audio`, `ui.video`, `ui.parallax` |
| **Special** | `ui.json_editor`, `ui.xterm`, `ui.anywidget`, `ui.timer`, `ui.refreshable`, `ui.run_javascript`, `ui.keyboard`, `ui.download`, `ui.status_code` |

## License

MIT