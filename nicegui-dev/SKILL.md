---
name: nicegui-dev
description: "NiceGUI (Python Web UI framework) development expert. Use when building UI with NiceGUI, creating components (ui.button, ui.card, ui.dialog, etc.), handling events, styling with Tailwind/Quasar, routing, data binding, or debugging NiceGUI apps. Triggers: nicegui, ui.button, ui.card, ui.dialog, ui.input, ui.table, ui.echart, ui.aggrid, ui.anywidget, NiceGUI layout, NiceGUI styling, NiceGUI component errors, NiceGUI API questions."
---

# NiceGUI 开发专家

编写 NiceGUI 代码时，始终参考 `references/nicegui_reference.md` 确保使用正确的组件、参数和方法。

## 核心规则

1. **始终使用 `from nicegui import ui` 导入**，不要使用其他导入方式
2. **组件作为上下文管理器**：布局容器（card、column、row、grid、dialog、expansion 等）使用 `with` 语句
3. **事件处理优先用 lambda**：`on_click=lambda: ...`，需要异步时用 `async def`
4. **样式三件套**：`.classes()` 加 Tailwind 类、`.style()` 加内联 CSS、`.props()` 加 Quasar 属性
5. **绑定用 `.bind_value()`**：双向绑定首选 `bind_value`，单向用 `_from` / `_to` 变体
6. **app 级导入**：`from nicegui import app, ui`（使用 app.timer、app.storage 等时）
7. **最低 Python 3.10**：NiceGUI 3.7+ 不再支持 Python 3.9

## 快速参考

### 布局模式

```python
# 基础布局
with ui.card():
    ui.label('Title')
    with ui.row():
        ui.button('OK')
        ui.button('Cancel')

# 响应式网格
with ui.grid(columns=3):
    for i in range(6):
        ui.card().classes('p-4')

# 页面框架
@ui.page('/')
def index():
    with ui.header().classes('bg-primary'):
        ui.label('Header')
    with ui.left_drawer():
        ui.label('Sidebar')
    with ui.footer():
        ui.label('Footer')
```

### 事件与交互

```python
# 按钮点击
ui.button('Click', on_click=lambda: ui.notify('Clicked!'))

# 等待按钮点击（async）
async def step():
    btn = ui.button('Next')
    await btn.clicked()
    ui.label('Done')

# 输入变化
ui.input('Name', on_change=lambda e: ui.notify(f'Hello {e.value}'))

# 定时器
ui.timer(1.0, lambda: update_clock())

# 刷新装饰器
@ui.refreshable
def dashboard():
    ui.label(f'Count: {counter}')
dashboard()  # 刷新时调用 dashboard.refresh()
```

### 数据绑定

```python
# 双向绑定
slider = ui.slider(min=0, max=100, value=50)
label = ui.label()
slider.bind_value(label, 'text')

# 绑定到变量
name = ui.input('Name')
greeting = ui.label()
name.bind_value(greeting, 'text', forward=lambda v: f'Hello {v}!')

# 绑定到 storage
app.storage.user['count'] = 0
```

### 样式系统

```python
# Tailwind CSS 类
ui.label('Big text').classes('text-2xl font-bold text-red-500')

# Quasar 属性
ui.button('Flat').props('flat color=teal')
ui.button('Round').props('round icon=home')

# 内联样式
ui.label('Styled').style('color: red; font-size: 24px;')

# 暗色模式
dark = ui.dark_mode()
ui.button('Toggle', on_click=lambda: dark.toggle())
```

### 对话框

```python
# 简单对话框
with ui.dialog() as dialog, ui.card():
    ui.label('Hello!')
    ui.button('Close', on_click=dialog.close)

ui.button('Open', on_click=dialog.open)

# 等待对话框结果
with ui.dialog() as dialog, ui.card():
    ui.label('Continue?')
    with ui.row():
        ui.button('Yes', on_click=lambda: dialog.submit(True))
        ui.button('No', on_click=lambda: dialog.submit(False))

result = await dialog
```

### 路由

```python
@ui.page('/')
def index():
    ui.label('Home')

@ui.page('/about')
def about():
    ui.label('About')

ui.run()
```

## 组件速查表

> 完整组件参考见 `references/nicegui_reference.md`

| 类别 | 组件 |
|------|------|
| **文本** | `ui.label`, `ui.markdown`, `ui.code`, `ui.html`, `ui.restructured_text` |
| **输入** | `ui.input`, `ui.textarea`, `ui.number`, `ui.select`, `ui.radio`, `ui.checkbox`, `ui.switch`, `ui.toggle`, `ui.slider`, `ui.range`, `ui.rating`, `ui.date`, `ui.date_input`, `ui.time`, `ui.time_input`, `ui.color_input`, `ui.color_picker`, `ui.upload`, `ui.editor`, `ui.codemirror` |
| **按钮** | `ui.button`, `ui.button_group`, `ui.fab`, `ui.dropdown_button`, `ui.badge`, `ui.chip` |
| **布局** | `ui.card`, `ui.column`, `ui.row`, `ui.grid`, `ui.expansion`, `ui.scroll_area`, `ui.splitter`, `ui.separator`, `ui.space`, `ui.skeleton` |
| **导航** | `ui.link`, `ui.menu`, `ui.context_menu`, `ui.tabs`, `ui.stepper`, `ui.pagination`, `ui.carousel`, `ui.timeline`, `ui.tooltip` |
| **弹窗** | `ui.dialog`, `ui.notify`, `ui.notification` |
| **数据** | `ui.table`, `ui.aggrid`, `ui.tree`, `ui.log`, `ui.list` |
| **图表** | `ui.echart`, `ui.plotly`, `ui.highchart`, `ui.line_plot`, `ui.altair`, `ui.mermaid` |
| **地图/3D** | `ui.leaflet`, `ui.scene`, `ui.joystick` |
| **媒体** | `ui.image`, `ui.interactive_image`, `ui.audio`, `ui.video`, `ui.parallax` |
| **特殊** | `ui.json_editor`, `ui.xterm`, `ui.anywidget`, `ui.timer`, `ui.refreshable`, `ui.run_javascript`, `ui.keyboard`, `ui.download`, `ui.status_code` |
| **样式** | `ui.dark_mode`, `ui.colors`, `ui.add_css`, `ui.element`, `ui.fullscreen` |

## 页面框架组件

```python
@ui.page('/')
def page():
    with ui.header(): ...        # 顶部栏
    with ui.left_drawer(): ...   # 左侧抽屉
    with ui.right_drawer(): ...  # 右侧抽屉
    with ui.footer(): ...        # 底部栏
    ui.page_sticky(...)          # 粘性定位
    ui.page_scroller(...)        # 回到顶部
```

## ui.run() 启动参数

```python
ui.run(
    host='0.0.0.0',          # 监听地址（默认 'localhost'，生产环境用 '0.0.0.0'）
    port=8080,                # 端口号（默认 8080）
    title='My App',           # 浏览器标签页标题
    favicon='🚀',             # favicon（emoji 或文件路径）
    reload=True,              # 代码变更自动重载（默认 True，仅开发模式）
    show=True,                # 自动打开浏览器（默认 True）
    dark=None,                # 暗色模式：True/False/None（自动）
    storage_secret='xxx',     # storage 加密密钥（生产环境必设！）
    tailwind=True,            # 启用 Tailwind CSS（默认 True）
    prod=False,               # 生产模式（关闭 reload，优化性能）
    viewport='width=device-width, initial-scale=1',  # 移动端适配
)
```

⚠️ **生产部署**：必须设置 `storage_secret`，使用 `ui.run(prod=True)` 或通过环境变量 `NICEGUI_PROD=1`。

## @ui.page 装饰器参数

```python
@ui.page('/',                          # 路由路径
          title='My Page',             # 页面标题（覆盖 ui.run 的 title）
          dark=True,                   # 此页使用暗色模式
          response_timeout=30,         # 响应超时秒数（默认 3.0）
          favicon='custom.ico',        # 页面专属 favicon
          reconnect_timeout=3.0,       # WebSocket 重连超时
)
async def index():
    ui.label('Hello')

# 路由参数注入
@ui.page('/user/{user_id}')
def user_page(user_id: str):
    ui.label(f'User: {user_id}')
```

## 多页面应用架构

```python
from nicegui import app, ui

# ========== 共享状态（跨页面） ==========
# 方式1：app.storage.general（全局，需 storage_secret）
@ui.page('/')
def page1():
    app.storage.general['count'] = app.storage.general.get('count', 0) + 1
    ui.label(f'Visits: {app.storage.general["count"]}')

# 方式2：app.storage.user（按用户，需 @ui.page + storage_secret）
@ui.page('/dashboard')
async def dashboard():
    app.storage.user['name'] = 'Alice'
    ui.label(f"Hello {app.storage.user['name']}")

# ========== 子页面（Sub Pages） ==========
@ui.page('/docs')
class DocsPage:
    def __init__(self):
        ui.label('Documentation')
        # 子页面路由
        self.content = ui.column()

    @ui.page('/docs/{section}')
    class SectionPage:
        def __init__(self, section: str):
            ui.label(f'Section: {section}')

# ========== 生命周期 ==========
@app.on_startup
async def startup():
    """服务启动时执行：初始化数据库连接、加载配置等"""
    print('Server started')

@app.on_shutdown
async def shutdown():
    """服务关闭时执行：清理资源"""
    print('Server shutting down')

@app.on_connect
async def on_connect():
    """新客户端连接时执行"""
    print('Client connected')

@app.on_disconnect
async def on_disconnect():
    """客户端断开时执行"""
    print('Client disconnected')
```

## Tabs + Tab Panels 组合

```python
# 常用标签页切换模式
with ui.tabs() as tabs:
    ui.tab('Home', icon='home')
    ui.tab('Settings', icon='settings')
    ui.tab('About', icon='info')

with ui.tab_panels(tabs, value='Home').classes('w-full'):
    with ui.tab_panel('Home'):
        ui.label('Welcome home!')
    with ui.tab_panel('Settings'):
        ui.label('Adjust settings')
    with ui.tab_panel('About'):
        ui.label('About this app')
```

## 表单提交与验证

```python
# 完整表单模式
with ui.card().classes('w-96'):
    ui.label('Registration').classes('text-xl font-bold')
    name = ui.input('Name', validation={'Too short': lambda v: len(v) >= 2})
    email = ui.input('Email', validation={'Invalid email': lambda v: '@' in v})
    password = ui.input('Password', password=True, password_toggle_button=True)
    
    async def submit():
        # 触发所有输入验证
        for field in [name, email, password]:
            if not field.value:
                ui.notify(f'{field.label} is required', type='warning')
                return
        ui.notify(f'Registered: {name.value}', type='positive')
    
    ui.button('Submit', on_click=submit)
```

## 异步任务处理

```python
from nicegui import run

# CPU 密集型任务（在独立进程中运行，不阻塞 UI）
def heavy_computation(n):
    return sum(i*i for i in range(n))

async def on_compute():
    result = await run.cpu_bound(heavy_computation, 10_000_000)
    ui.notify(f'Result: {result}')

ui.button('Compute', on_click=on_compute)

# I/O 密集型任务（在独立线程中运行）
async def fetch_data():
    import httpx
    async with httpx.AsyncClient() as client:
        resp = await run.io_bound(client.get, 'https://httpbin.org/get')
        ui.notify(f'Status: {resp.status_code}')

ui.button('Fetch', on_click=fetch_data)
```

## 新 API 速查（v3.4+）

### 全局颜色配置（v3.6.0+）

```python
from nicegui import app

app.colors.primary = '#1654a0'     # 主色
app.colors.secondary = '#26a69a'   # 辅色
app.colors.accent = '#9c27b0'      # 强调色
app.colors.dark = '#1d1d1d'        # 暗色背景

# 颜色绑定
label = ui.label('Hello')
label.bind_text_color_from(some_element, 'value')
```

### 异常处理（v3.6.0+）

```python
from nicegui import ui

# ui.on_exception — 处理页面级未捕获异常
@ui.on_exception
def handle_exception(exc):
    ui.notify(f'Error: {exc}', type='negative')
    print(f'Uncaught: {exc}')
```

### ui.anywidget（v3.5.0+）

```python
# 嵌入任意 Jupyter/ipywidget 组件
import anywidget
import traitlets

class MyWidget(anywidget.AnyWidget):
    _esm = """
    export function render({ model, el }) {
      el.innerText = model.get('value');
      model.on('change:value', () => { el.innerText = model.get('value'); });
    }
    """
    value = traitlets.Unicode('Hello').tag(sync=True)

widget = ui.anywidget(MyWidget(value='NiceGUI!'))
```

### ui.echart 事件（v3.5.0+）

```python
chart = ui.echart({
    'xAxis': {'type': 'category', 'data': ['A', 'B', 'C']},
    'yAxis': {'type': 'value'},
    'series': [{'type': 'bar', 'data': [10, 20, 30]}],
})
chart.on('click', lambda e: ui.notify(f'Clicked: {e}'))
```

### ui.input / ui.number 增强（v3.5.0+）

```python
ui.number('Price', value=99.9, prefix='$', suffix='USD')
ui.input('Search', prefix='🔍', placeholder='type here...')
ui.input('Password', password=True, password_toggle_button=True)
```

### ui.status_code（v3.10.0+）

```python
# 从页面构建器设置 HTTP 状态码
@ui.page('/not-found')
def not_found():
    ui.status_code(404)
    ui.label('Page not found')
```

## 存储系统

| 存储 | 作用域 | 跨标签 | 跨浏览器 | 跨重启 |
|------|--------|--------|----------|--------|
| `app.storage.client` | 单客户端 | ❌ | ❌ | ❌ |
| `app.storage.tab` | 单标签页 | ❌ | ❌ | ❌ |
| `app.storage.browser` | 单浏览器 | ✅ | ❌ | ✅ |
| `app.storage.user` | 单用户 | ✅ | ✅ | ✅ |
| `app.storage.general` | 全局 | ✅ | ✅ | ✅ |

## 部署方式

```python
# 1. 直接运行（开发模式）
ui.run(reload=True, show=True)

# 2. 生产模式
ui.run(prod=True, storage_secret='your-secret-key')

# 3. 嵌入 FastAPI
from fastapi import FastAPI
from nicegui import ui

app = FastAPI()
ui.run_with(app)  # 将 NiceGUI 挂载到现有 FastAPI 应用

# 4. Docker 部署
# Dockerfile 示例：
# FROM python:3.14-slim
# RUN pip install nicegui
# COPY . /app
# WORKDIR /app
# EXPOSE 8080
# CMD ["python", "main.py"]

# 5. 环境变量
# NICEGUI_PROD=1          — 等同于 ui.run(prod=True)
# STORAGE_SECRET=xxx       — 等同于 ui.run(storage_secret=xxx)
```

## 常见陷阱

1. **不要忘记 `ui.run()`**：开发模式下需要，生产部署可能不需要
2. **事件中修改 UI**：所有 UI 更新必须在 NiceGUI 的事件循环内，async 函数可以直接用
3. **CSS 类覆盖**：`.classes()` 默认追加，要替换用 `.classes(replace='...')`
4. **Quasar 属性格式**：`.props('flat color=primary')` 不是 `.props(flat=True, color='primary')`
5. **select 的值**：`ui.select` 的 `value` 是选项的 key，不是显示文本
6. **table 更新**：修改 `table.rows` 后需要调用 `table.update()` 刷新
7. **dialog 内部元素**：dialog 内部元素在 dialog 关闭后仍然存在，可以复用
8. **storage.user 需要 `@ui.page`**：`app.storage.user` 只能在 `@ui.page` 装饰的函数内使用
9. **storage_secret 必设**：使用 `app.storage.user` 或 `app.storage.general` 时，`ui.run()` 必须设置 `storage_secret`，否则运行时报错
10. **耗时操作阻塞 UI**：CPU 密集用 `run.cpu_bound()`，I/O 密集用 `run.io_bound()`，不要直接在事件回调里跑长时间同步操作
11. **动态添加元素**：在 `with` 块外创建元素需要 `element.parent_slot` 或手动指定 parent，否则元素不会出现在页面上
12. **bind_value 循环**：两个元素双向绑定时避免 `A.bind_value(B).bind_value(A)` 死循环，用单向绑定或 `forward` 函数
13. **run_method() 不再支持 JS 表达式**（v3.8.0 Breaking）— 只能传实际方法名，不能传 lambda/JS 表达式。如需执行 JS 代码，改用 `ui.run_javascript()`
14. **弃用 API**：`ui.add_scss` / `ui.add_sass` 已弃用（v3.4.0），改用 `ui.add_css`；`app.storage.individual` 已弃用，改用 `app.storage.user`
15. **element.clear() 返回 self**（v3.4.0+）— 支持链式调用：`container.clear().classes('...')`

## 更新参考数据

当 NiceGUI 发布新版本或需要最新组件信息时，执行以下步骤更新：

```bash
# 方法1：运行更新脚本（自动下载并重新生成参考文件）
python3 scripts/update_reference.py

# 方法2：手动下载并生成
curl -o nicegui_index.json https://nicegui.io/static/sitewide_index.json
python3 scripts/update_reference.py --index-url file:///path/to/nicegui_index.json
```

更新后，检查 `references/nicegui_reference.md` 的日期是否更新。

## 参考资源

- `references/nicegui_reference.md` — 完整组件参考（从官方索引自动生成）
- [NiceGUI 官方文档](https://nicegui.io/documentation)
- [NiceGUI GitHub](https://github.com/zauberzeug/nicegui)
- [Quasar 组件](https://quasar.dev/vue-components) — NiceGUI 底层 Vue 组件
- [Tailwind CSS](https://tailwindcss.com/docs) — `.classes()` 使用的 CSS 框架
