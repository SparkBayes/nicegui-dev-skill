# NiceGUI Component Reference

> Auto-generated from https://nicegui.io/static/sitewide_index.json
> Last updated: 2026-04-21

## Text Elements

### ui.label
Displays some text.

:param text: the content of the label

```python
from nicegui import ui

ui.label('some label')

```

Features: Change Appearance Depending on the Content

### ui.markdown
Renders Markdown onto the page.

:param content: the Markdown content to be displayed
:param extras: list of `markdown2 extensions <https://github.com/trentm/python-markdown2/wiki/Extras#implemented-extras>`_ (default: `['fenced-code-blocks', 'tables']`)
:param sanitize:

```python
from nicegui import ui

ui.markdown('This is **Markdown**.')

```

Features: Markdown with indentation, Markdown with code blocks, Markdown tables, Mermaid diagrams, LaTeX formulas, Change Markdown content, Styling elements inside Markdown

### ui.restructured_text
Renders ReStructuredText onto the page.

:param content: the ReStructuredText content to be displayed

```python
from nicegui import ui

ui.restructured_text('This is **reStructuredText**.')

```

Features: reStructuredText with indentation, reStructuredText with code blocks, reStructuredText with tables

### ui.code
This element displays a code block with syntax highlighting.

In secure environments (HTTPS or localhost), a copy button is displayed to copy the code to the clipboard.

:param content: code to display
:param language: language of the code (default:

```python
from nicegui import ui

ui.code('''
    from nicegui import ui

    ui.label('Code inception!')

''').classes('w-full')

```

### ui.html
Renders arbitrary HTML onto the page, wrapped in the specified tag.
`Tailwind <https://tailwindcss.com/>`_ can be used for styling.
You can also use `ui.add_head_html` to add html code into the head of the document and `ui.add_body_html`
to add it into the body.

```python
from nicegui import ui

ui.html('This is <strong>HTML</strong>.', sanitize=False)

```

Features: Producing in-line elements, Other HTML Elements

---

## Input Elements

### ui.input
This element is based on Quasar's `QInput <https://quasar.dev/vue-components/input>`_ component.

The `on_change` event is called on every keystroke and the value updates accordingly.
If you want to wait until the user confirms the input, you can register a custom event callback, e.g.
`ui.input(...).on('keydown.enter', ...)` or `ui.input(...).on('blur', ...)`.

You can use the `validation` parameter to define a dictionary of validation rules,
e.g.

```python
from nicegui import ui

ui.input(label='Text', placeholder='start typing',
         on_change=lambda e: result.set_text('you typed: ' + e.value),
         validation={'Input too long': lambda value: len(value) < 20})
result = ui.label()

```

Features: Autocompletion, Clearable, Styling, Input validation, Lazy validation, Client-side validation

### ui.textarea
This element is based on Quasar's `QInput <https://quasar.dev/vue-components/input>`_ component.
The ``type`` is set to ``textarea`` to create a multi-line text input.

You can use the `validation` parameter to define a dictionary of validation rules,
e.g.

```python
from nicegui import ui

ui.textarea(label='Text', placeholder='start typing',
            on_change=lambda e: result.set_text('you typed: ' + e.value))
result = ui.label()

```

Features: Clearable

### ui.number
This element is based on Quasar's `QInput <https://quasar.dev/vue-components/input>`_ component.

You can use the `validation` parameter to define a dictionary of validation rules,
e.g. ``{'Too small!': lambda value: value > 3}``.
The key of the first rule that fails will be displayed as an error message.
Alternatively, you can pass a callable that returns an optional error message.
To disable the automatic validation on every value change, you can use the `without_auto_validation` method.

```python
from nicegui import ui

ui.number(label='Number', value=3.1415927, format='%.2f',
          on_change=lambda e: result.set_text(f'you entered: {e.value}'))
result = ui.label()

```

Features: Clearable, Number of decimal places

### ui.select
This element is based on Quasar's `QSelect <https://quasar.dev/vue-components/select>`_ component.

The options can be specified as a list of values, or as a dictionary mapping values to labels.
After manipulating the options, call `update()` to update the options in the UI.

If `with_input` is True, an input field is shown to filter the options.

If `new_value_mode` is not None, it implies `with_input=True` and the user can enter new values in the input field.
See `Quasar's documentation <https://quasar.dev/vue-components/select#the-new-value-mode-prop>`_ for details.
Note that this mode is ineffective when setting the `value` property programmatically.

You can use the `validation` parameter to define a dictionary of validation rules,
e.g.

```python
from nicegui import ui

select1 = ui.select([1, 2, 3], value=1)
select2 = ui.select({1: 'One', 2: 'Two', 3: 'Three'}).bind_value(select1, 'value')

```

Features: Search-as-you-type, Multi selection, Update options

### ui.radio
This element is based on Quasar's `QOptionGroup <https://quasar.dev/vue-components/option-group>`_ component.

The options can be specified as a list of values, or as a dictionary mapping values to labels.
After manipulating the options, call `update()` to update the options in the UI.

```python
from nicegui import ui

radio1 = ui.radio([1, 2, 3], value=1).props('inline')
radio2 = ui.radio({1: 'A', 2: 'B', 3: 'C'}).props('inline').bind_value(radio1, 'value')

```

Features: Inject arbitrary content

### ui.checkbox
This element is based on Quasar's `QCheckbox <https://quasar.dev/vue-components/checkbox>`_ component.

:param text: the label to display next to the checkbox
:param value: whether it should be checked initially (default: `False`)
:param on_change:

```python
from nicegui import ui

checkbox = ui.checkbox('check me')
ui.label('Check!').bind_visibility_from(checkbox, 'value')

```

Features: Handle User Interaction

### ui.switch
This element is based on Quasar's `QToggle <https://quasar.dev/vue-components/toggle>`_ component.

:param text: the label to display next to the switch
:param value: whether it should be active initially (default: `False`)
:param on_change:

```python
from nicegui import ui

switch = ui.switch('switch me')
ui.label('Switch!').bind_visibility_from(switch, 'value')

```

Features: Handle User Interaction

### ui.toggle
This element is based on Quasar's `QBtnToggle <https://quasar.dev/vue-components/button-toggle>`_ component.

The options can be specified as a list of values, or as a dictionary mapping values to labels.
After manipulating the options, call `update()` to update the options in the UI.

```python
from nicegui import ui

toggle1 = ui.toggle([1, 2, 3], value=1)
toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(toggle1, 'value')

```

### ui.slider
This element is based on Quasar's `QSlider <https://quasar.dev/vue-components/slider>`_ component.

:param min: lower bound of the slider
:param max: upper bound of the slider
:param step: step size
:param value: initial value to set position of the slider
:param on_change:

```python
from nicegui import ui

slider = ui.slider(min=0, max=100, value=50)
ui.label().bind_text_from(slider, 'value')

```

Features: Throttle events with leading and trailing options, Disable slider

### ui.range
This element is based on Quasar's `QRange <https://quasar.dev/vue-components/range>`_ component.

:param min: lower bound of the range
:param max: upper bound of the range
:param step: step size
:param value: initial value to set min and max position of the range (default: ``min`` to ``max``)
:param on_change:

```python
from nicegui import ui

min_max_range = ui.range(min=0, max=100, value={'min': 20, 'max': 80})
ui.label().bind_text_from(min_max_range, 'value',
                          backward=lambda v: f'min: {v["min"]}, max: {v["max"]}')

```

Features: Customize labels, Change range limits

### ui.rating
This element is based on Quasar's `QRating <https://quasar.dev/vue-components/rating>`_ component.

*Added in version 2.12.0*

:param value: initial value (default: ``None``)
:param max: maximum rating, number of icons (default: 5)
:param icon: name of icons to be displayed (default: star)
:param icon_selected: name of an icon to be displayed when selected (default: same as ``icon``)
:param icon_half: name of an icon to be displayed when half-selected (default: same as ``icon``)
:param color: color(s) of the icons (Quasar, Tailwind, or CSS colors or ``None``, default: "primary")
:param size: size in CSS units, including unit name or standard size name (xs|sm|md|lg|xl), examples: 16px, 2rem
:param on_change:

```python
from nicegui import ui

ui.rating(value=4)

```

Features: Customize icons, Customize color, Maximum rating

### ui.color_input
This element extends Quasar's `QInput <https://quasar.dev/vue-components/input>`_ component with a color picker.

:param label: displayed label for the color input
:param placeholder: text to show if no color is selected
:param value: the current color value
:param on_change: callback to execute when the value changes
:param preview: change button background to selected color (default:

```python
from nicegui import ui

label = ui.label('Change my color!')
ui.color_input(label='Color', value='#000000',
               on_change=lambda e: label.style(f'color:{e.value}'))

```

### ui.color_picker
This element is based on Quasar's `QMenu <https://quasar.dev/vue-components/menu>`_ and
`QColor <https://quasar.dev/vue-components/color-picker>`_ components.

:param on_pick: callback to execute when a color is picked
:param value: whether the menu is already opened (default:

```python
from nicegui import ui

with ui.button(icon='colorize') as button:
    ui.color_picker(on_pick=lambda e: button.classes(f'!bg-[{e.color}]'))

```

Features: Customize the Color Picker

### ui.date
This element is based on Quasar's `QDate <https://quasar.dev/vue-components/date>`_ component.
The date is a string in the format defined by the `mask` parameter.

You can also use the `range` or `multiple` props to select a range of dates or multiple dates::

    ui.date({'from': '2023-01-01', 'to': '2023-01-05'}).props('range')
    ui.date(['2023-01-01', '2023-01-02', '2023-01-03']).props('multiple')
    ui.date([{'from': '2023-01-01', 'to': '2023-01-05'}, '2023-01-07']).props('multiple range')

```python
from nicegui import ui

ui.date(value='2023-01-01', on_change=lambda e: result.set_text(e.value))
result = ui.label()

```

Features: Input element with date picker, Date range input, Date filter

### ui.date_input
This element extends Quasar's `QInput <https://quasar.dev/vue-components/input>`_ component with a date picker.

*Added in version 3.3.0*

:param label: displayed label for the date input
:param range_input: if True, allows selecting a range of dates (value will be a dictionary with "from" and "to" keys)
:param placeholder: text to show if no date is selected
:param value: the current date value
:param on_change:

```python
from nicegui import ui

date = ui.date_input('Date', value='2025-05-31')
ui.label().bind_text_from(date, 'value', lambda v: f'date: {v}')

```

Features: Date Range Input, Date Input with Date Filter

### ui.time
This element is based on Quasar's `QTime <https://quasar.dev/vue-components/time>`_ component.
The time is a string in the format defined by the `mask` parameter.

:param value: the initial time
:param mask: the format of the time string (default: 'HH:mm')
:param on_change:

```python
from nicegui import ui

ui.time(value='12:00', on_change=lambda e: result.set_text(e.value))
result = ui.label()

```

Features: Input element with time picker

### ui.time_input
This element extends Quasar's `QInput <https://quasar.dev/vue-components/input>`_ component with a time picker.

*Added in version 3.3.0*

:param label: displayed label for the time input
:param placeholder: text to show if no time is selected
:param value: the current time value
:param on_change:

```python
from nicegui import ui

time = ui.time_input('Time', value='12:30')
ui.label().bind_text_from(time, 'value', lambda v: f'time: {v}')

```

### ui.upload
Based on Quasar's `QUploader <https://quasar.dev/vue-components/uploader>`_ component.

Upload event handlers are called in the following order:

1. ``on_begin_upload``: The client begins uploading one or more files to the server.
2. ``on_upload``: The upload of an individual file is complete.
3.

```python
from nicegui import ui

ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.file.name}')).classes('max-w-full')

```

Features: Upload event arguments, Upload restrictions, Show file content, Uploading large files, Reference for ui.upload, Reference for ui.upload.FileUpload

### ui.editor
A WYSIWYG editor based on `Quasar's QEditor <https://quasar.dev/vue-components/editor>`_.
The value is a string containing the formatted text as HTML code.

:param value: initial value
:param on_change:

```python
from nicegui import ui

editor = ui.editor(placeholder='Type something here')
ui.markdown().bind_content_from(editor, 'value',
                                backward=lambda v: f'HTML code:\n```\n{v}\n```')

```

### ui.codemirror
An element to create a code editor using `CodeMirror <https://codemirror.net/>`_.

It supports syntax highlighting for over 140 languages, more than 30 themes, line numbers, code folding, (limited) auto-completion, and more.

Supported languages and themes:
    - Languages: A list of supported languages can be found in the `@codemirror/language-data <https://github.com/codemirror/language-data/blob/main/src/language-data.ts>`_ package.
    - Themes: A list can be found in the `@uiw/codemirror-themes-all <https://github.com/uiwjs/react-codemirror/tree/master/themes/all>`_ package.

At runtime, the methods `supported_languages` and `supported_themes` can be used to get supported languages and themes.

```python
from nicegui import ui

editor = ui.codemirror('print("Edit me!")', language='Python').classes('h-32')
ui.select(editor.supported_languages, label='Language', clearable=True) \
    .classes('w-32').bind_value(editor, 'language')
ui.select(editor.supported_themes, label='Theme') \
    .classes('w-32').bind_value(editor, 'theme')
ui.checkbox('Wrap Lines', value=editor.line_wrapping,
            on_change=lambda e: editor.set_line_wrapping(e.value))

```

Features: Preserving Cursor Position

---

## Button & Action

### ui.button
This element is based on Quasar's `QBtn <https://quasar.dev/vue-components/button>`_ component.

The ``color`` parameter accepts a Quasar color, a Tailwind color, or a CSS color.
If a Quasar color is used, the button will be styled according to the Quasar theme including the color of the text.
Note that there are colors like "red" being both a Quasar color and a CSS color.
In such cases the Quasar color will be used.

```python
from nicegui import ui

ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))

```

Features: Icons, Await button click, Disable button with a context manager, Custom toggle button, Floating Action Button, Expandable Floating Action Button

### ui.button_group
This element is based on Quasar's `QBtnGroup <https://quasar.dev/vue-components/button-group>`_ component.
You must use the same design props on both the parent button group and the children buttons.

```python
from nicegui import ui

with ui.button_group():
    ui.button('One', on_click=lambda: ui.notify('You clicked Button 1!'))
    ui.button('Two', on_click=lambda: ui.notify('You clicked Button 2!'))
    ui.button('Three', on_click=lambda: ui.notify('You clicked Button 3!'))

```

Features: Button group with dropdown button, Button group styling

### ui.fab
A floating action button that can be used to trigger an action.
This element is based on Quasar's `QFab <https://quasar.dev/vue-components/floating-action-button#qfab-api>`_ component.

:param icon: icon to be displayed on the FAB
:param value: whether the FAB is already opened (default: ``False``)
:param label: optional label for the FAB
:param color: background color of the FAB (default: "primary")
:param direction: direction of the FAB ("up", "down", "left", "right", default:

```python
from nicegui import ui

with ui.fab('navigation', label='Transport'):
    ui.fab_action('train', on_click=lambda: ui.notify('Train'))
    ui.fab_action('sailing', on_click=lambda: ui.notify('Boat'))
    ui.fab_action('rocket', on_click=lambda: ui.notify('Rocket'))

```

Features: Styling, Reference for ui.fab, Reference for ui.fab_action

### ui.dropdown_button
This element is based on Quasar's `QBtnDropDown <https://quasar.dev/vue-components/button-dropdown>`_ component.

The ``color`` parameter accepts a Quasar color, a Tailwind color, or a CSS color.
If a Quasar color is used, the button will be styled according to the Quasar theme including the color of the text.
Note that there are colors like "red" being both a Quasar color and a CSS color.
In such cases the Quasar color will be used.

```python
from nicegui import ui

with ui.dropdown_button('Open me!', auto_close=True):
    ui.item('Item 1', on_click=lambda: ui.notify('You clicked item 1'))
    ui.item('Item 2', on_click=lambda: ui.notify('You clicked item 2'))

```

Features: Custom elements inside dropdown button

### ui.badge
A badge element wrapping Quasar's
`QBadge <https://quasar.dev/vue-components/badge>`_ component.

:param text: the initial value of the text field
:param color: the color name for component (either a Quasar, Tailwind, or CSS color or `None`, default: "primary")
:param text_color: text color (either a Quasar, Tailwind, or CSS color or `None`, default: `None`)
:param outline: use 'outline' design (colored text and borders only) (default:

```python
from nicegui import ui

with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
    badge = ui.badge('0', color='red').props('floating')

```

### ui.chip
A chip element wrapping Quasar's `QChip <https://quasar.dev/vue-components/chip>`_ component.
It can be clickable, selectable and removable.

:param text: the initial value of the text field (default: "")
:param icon: the name of an icon to be displayed on the chip (default: `None`)
:param color: the color name for component (either a Quasar, Tailwind, or CSS color or `None`, default: "primary")
:param text_color: text color (either a Quasar, Tailwind, or CSS color or `None`, default: `None`)
:param on_click: callback which is invoked when chip is clicked.

```python
from nicegui import ui

with ui.row().classes('gap-1'):
    ui.chip('Click me', icon='ads_click', on_click=lambda: ui.notify('Clicked'))
    ui.chip('Selectable', selectable=True, icon='bookmark', color='orange')
    ui.chip('Removable', removable=True, icon='label', color='indigo-3')
    ui.chip('Styled', icon='star', color='green').props('outline square')
    ui.chip('Disabled', icon='block', color='red').set_enabled(False)

```

Features: Dynamic chip elements as labels/tags

### ui.icon
This element is based on Quasar's `QIcon <https://quasar.dev/vue-components/icon>`_ component.

`Here <https://fonts.google.com/icons?icon.set=Material+Icons>`_ is a reference of possible names.

:param name: name of the icon (snake case, e.g.

```python
from nicegui import ui

ui.icon('thumb_up', color='primary').classes('text-5xl')

```

Features: Material icons and symbols, Eva icons, Other icon sets, Lottie files

### ui.avatar
A avatar element wrapping Quasar's
`QAvatar <https://quasar.dev/vue-components/avatar>`_ component.

:param icon: name of the icon or image path with "img:" prefix (e.g. "map", "img:path/to/image.png")
:param color: background color (either a Quasar, Tailwind, or CSS color or `None`, default: "primary")
:param text_color: color name from the Quasar Color Palette (e.g. "primary", "teal-10")
:param size: size in CSS units, including unit name or standard size name (xs|sm|md|lg|xl) (e.g. "16px", "2rem")
:param font_size: size in CSS units, including unit name, of the content (icon, text) (e.g.

```python
from nicegui import ui

ui.avatar('favorite_border', text_color='grey-11', square=True)
ui.avatar('img:https://nicegui.io/logo_square.png', color='blue-2')

```

Features: Photos

---

## Layout Containers

### ui.card
This element is based on Quasar's `QCard <https://quasar.dev/vue-components/card>`_ component.
It provides a container with a dropped shadow.

Note:
In contrast to this element,
the original QCard has no padding by default and hides outer borders and shadows of nested elements.
If you want the original behavior, use the `tight` method.

```python
from nicegui import ui

with ui.card().tight():
    ui.image('https://picsum.photos/id/684/640/360')
    with ui.card_section():
        ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

```

Features: Card without shadow, Tight card layout

### ui.column
Provides a container which arranges its child in a column.

:param wrap: whether to wrap the content (default: `False`)
:param align_items: alignment of the items in the column ("start", "end", "center", "baseline", or "stretch"; default:

```python
from nicegui import ui

with ui.column():
    ui.label('label 1')
    ui.label('label 2')
    ui.label('label 3')

```

Features: Masonry or Pinterest-Style Layout

### ui.row
Provides a container which arranges its child in a row.

:param wrap: whether to wrap the content (default: `True`)
:param align_items: alignment of the items in the row ("start", "end", "center", "baseline", or "stretch"; default:

```python
from nicegui import ui

with ui.row():
    ui.label('label 1')
    ui.label('label 2')
    ui.label('label 3')

```

### ui.grid
Provides a container which arranges its child in a grid.

:param rows: number of rows in the grid or a string with the grid-template-rows CSS property (e.g. 'auto 1fr')
:param columns: number of columns in the grid or a string with the grid-template-columns CSS property (e.g.

```python
from nicegui import ui

with ui.grid(columns=2):
    ui.label('Name:')
    ui.label('Tom')

    ui.label('Age:')
    ui.label('42')

    ui.label('Height:')
    ui.label('1.80m')

```

Features: Custom grid layout, Cells spanning multiple columns

### ui.expansion
Provides an expandable container based on Quasar's `QExpansionItem <https://quasar.dev/vue-components/expansion-item>`_ component.

:param text: title text
:param caption: optional caption (or sub-label) text
:param icon: optional icon (default: None)
:param group: optional group name for coordinated open/close state within the group a.k.a.

```python
from nicegui import ui

with ui.expansion('Expand!', icon='work').classes('w-full'):
    ui.label('inside the expansion')

```

Features: Expansion with Custom Header, Expansion with Custom Caption, Expansion with Grouping

### ui.scroll_area
A way of customizing the scrollbars by encapsulating your content.
This element exposes the Quasar `ScrollArea <https://quasar.dev/vue-components/scroll-area/>`_ component.

:param on_scroll: function to be called when the scroll position changes

```python
from nicegui import ui

with ui.row():
    with ui.scroll_area().classes('size-32 border'):
        ui.label('I scroll. ' * 20)
    with ui.column().classes('p-4 size-32 border'):
        ui.label('I will not scroll. ' * 10)

```

Features: Handling Scroll Events, Setting the scroll position

### ui.splitter
The `ui.splitter` element divides the screen space into resizable sections,
allowing for flexible and responsive layouts in your application.

Based on Quasar's Splitter component:
`Splitter <https://quasar.dev/vue-components/splitter>`_

It provides three customizable slots, ``before``, ``after``, and ``separator``,
which can be used to embed other elements within the splitter.

```python
from nicegui import ui

with ui.splitter() as splitter:
    with splitter.before:
        ui.label('This is some content on the left hand side.').classes('mr-2')
    with splitter.after:
        ui.label('This is some content on the right hand side.').classes('ml-2')

```

Features: Advanced usage, Image fun

### ui.separator
This element is based on Quasar's `QSeparator <https://quasar.dev/vue-components/separator>`_ component.

It serves as a separator for cards, menus and other component containers and is similar to HTML's <hr> tag.

```python
from nicegui import ui

ui.label('text above')
ui.separator()
ui.label('text below')

```

### ui.space
This element is based on Quasar's `QSpace <https://quasar.dev/vue-components/space>`_ component.

Its purpose is to simply fill all available space inside of a flexbox element.

```python
from nicegui import ui

with ui.row().classes('w-full border'):
    ui.label('Left')
    ui.space()
    ui.label('Right')

```

Features: Vertical space

### ui.skeleton
This element is based on Quasar's `QSkeleton <https://quasar.dev/vue-components/skeleton>`_ component.
It serves as a placeholder for loading content in cards, menus and other component containers.
See the `Quasar documentation <https://quasar.dev/vue-components/skeleton/#predefined-types>`_ for a list of available types.

```python
from nicegui import ui

ui.skeleton().classes('w-full')

```

Features: Styling and animation, YouTube Skeleton

### ui.teleport
An element that allows us to transmit the content from within a component to any location on the page.

:param to: NiceGUI element or CSS selector of the target element for the teleported content

```python
from nicegui import ui

markdown = ui.markdown('Enter your **name**!')

def inject_input():
    with ui.teleport(f'#{markdown.html_id} strong'):
        ui.input('name').classes('inline-flex').props('dense outlined')

ui.button('inject input', on_click=inject_input)

```

Features: Radio element with arbitrary content, Injecting a graph into a table cell

---

## Navigation

### ui.link
Create a hyperlink.

To jump to a specific location within a page you can place linkable anchors with `ui.link_target("name")`
and link to it with `ui.link(target="#name")`.

:param text: display text
:param target: page function, NiceGUI element on the same page or string that is a an absolute URL or relative path from base URL
:param new_tab: open link in new tab (default:

```python
from nicegui import ui

ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

```

Features: Navigate on large pages, Links to other pages, Link from images and other elements

### ui.menu
Creates a menu based on Quasar's `QMenu <https://quasar.dev/vue-components/menu>`_ component.
The menu should be placed inside the element where it should be shown.

Advanced tip:
Use the `auto-close` prop to automatically close the menu on any click event directly without a server round-trip.

```python
from nicegui import ui

with ui.row().classes('w-full items-center'):
    result = ui.label().classes('mr-auto')
    with ui.button(icon='menu'):
        with ui.menu() as menu:
            ui.menu_item('Menu item 1', lambda: result.set_text('Selected item 1'))
            ui.menu_item('Menu item 2', lambda: result.set_text('Selected item 2'))
            ui.menu_item('Menu item 3 (keep open)',
                         lambda: result.set_text('Selected item 3'), auto_close=False)
            ui.separator()
            ui.menu_item('Close', menu.close)

```

Features: Client-side auto-close, Menu with sub-menus, Reference for ui.menu, Reference for ui.menu_item

### ui.context_menu
Creates a context menu based on Quasar's `QMenu <https://quasar.dev/vue-components/menu>`_ component.
The context menu should be placed inside the element where it should be shown.
It is automatically opened when the user right-clicks on the element and appears at the mouse position.

```python
from nicegui import ui

with ui.image('https://picsum.photos/id/377/640/360'):
    with ui.context_menu():
        ui.menu_item('Flip horizontally')
        ui.menu_item('Flip vertically')
        ui.separator()
        ui.menu_item('Reset', auto_close=False)

```

Features: Context menus with dynamic content

### ui.stepper
This element represents `Quasar's QStepper <https://quasar.dev/vue-components/stepper#qstepper-api>`_ component.
It contains individual steps.

To avoid issues with dynamic elements when switching steps,
this element uses Vue's `keep-alive <https://vuejs.org/guide/built-ins/keep-alive.html>`_ component.
If client-side performance is an issue, you can disable this feature.

```python
from nicegui import ui

with ui.stepper().props('vertical').classes('w-full') as stepper:
    with ui.step('Preheat'):
        ui.label('Preheat the oven to 350 degrees')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)
    with ui.step('Ingredients'):
        ui.label('Mix the ingredients')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)
            ui.button('Back', on_click=stepper.previous).props('flat')
    with ui.step('Bake'):
        ui.label('Bake for 20 minutes')
        with ui.stepper_navigation():
            ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
```

Features: Dynamic Stepper

### ui.pagination
A pagination element wrapping Quasar's `QPagination <https://quasar.dev/vue-components/pagination>`_ component.

:param min: minimum page number
:param max: maximum page number
:param direction_links: whether to show first/last page links
:param value: initial page (defaults to `min` if no value is provided)
:param on_change:

```python
from nicegui import ui

p = ui.pagination(1, 5, direction_links=True)
ui.label().bind_text_from(p, 'value', lambda v: f'Page {v}')

```

### ui.carousel
This element represents `Quasar's QCarousel <https://quasar.dev/vue-components/carousel#qcarousel-api>`_ component.
It contains individual carousel slides.

:param value: `ui.carousel_slide` or name of the slide to be initially selected (default: `None` meaning the first slide)
:param on_value_change: callback to be executed when the selected slide changes
:param animated: whether to animate slide transitions (default: `False`)
:param arrows: whether to show arrows for manual slide navigation (default: `False`)
:param navigation: whether to show navigation dots for manual slide navigation (default:

```python
from nicegui import ui

with ui.carousel(animated=True, arrows=True, navigation=True).props('height=180px'):
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/30/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/31/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/32/270/180').classes('w-[270px]')

```

### ui.timeline
This element represents `Quasar's QTimeline <https://quasar.dev/vue-components/timeline#qtimeline-api>`_ component.

:param side: Side ("left" or "right"; default: "left").
:param layout: Layout ("dense", "comfortable" or "loose"; default: "dense").

```python
from nicegui import ui

with ui.timeline(side='right'):
    ui.timeline_entry('Rodja and Falko start working on NiceGUI.',
                      title='Initial commit',
                      subtitle='May 07, 2021')
    ui.timeline_entry('The first PyPI package is released.',
                      title='Release of 0.1',
                      subtitle='May 14, 2021')
    ui.timeline_entry('Large parts are rewritten to remove JustPy '
                      'and to upgrade to Vue 3 and Quasar 2.',
                      title='Release of 1.0',
                      subtitle='December 15, 2022',
                      icon='rocket')

```

### ui.navigate
These functions allow you to navigate within the browser history and to external URLs.

*Added in version 2.0.0*

```python
from nicegui import ui

with ui.row():
    ui.button('Back', on_click=ui.navigate.back)
    ui.button('Forward', on_click=ui.navigate.forward)
    ui.button('Reload', on_click=ui.navigate.reload)
    ui.button(icon='savings',
              on_click=lambda: ui.navigate.to('https://github.com/sponsors/zauberzeug'))

```

Features: ui.navigate.to (formerly ui.open), Push and replace URLs

### ui.tooltip
This element is based on Quasar's `QTooltip <https://quasar.dev/vue-components/tooltip>`_ component.
It can be placed in another element to show additional information on hover.

Instead of passing a string as the first argument, you can also nest other elements inside the tooltip.

```python
from nicegui import ui

with ui.button(icon='thumb_up'):
    ui.tooltip('I like this').classes('bg-green')

```

Features: Tooltip method, Tooltip with HTML, Tooltip with other content

---

## Dialog & Notification

### ui.dialog
Creates a dialog based on Quasar's `QDialog <https://quasar.dev/vue-components/dialog>`_ component.
By default it is dismissible by clicking or pressing ESC.
To make it persistent, set `.props('persistent')` on the dialog element.

NOTE: The dialog is an element.
That means it is not removed when closed, but only hidden.
You should either create it only once and then reuse it, or remove it with `.clear()` after dismissal.

```python
from nicegui import ui

with ui.dialog() as dialog, ui.card():
    ui.label('Hello world!')
    ui.button('Close', on_click=dialog.close)

ui.button('Open a dialog', on_click=dialog.open)

```

Features: Awaitable dialog, Replacing content, Events

### ui.notify
Displays a notification on the screen.

:param message: content of the notification
:param position: position on the screen ("top-left", "top-right", "bottom-left", "bottom-right", "top", "bottom", "left", "right" or "center", default: "bottom")
:param close_button: optional label of a button to dismiss the notification (default: `False`)
:param type: optional type ("positive", "negative", "warning", "info" or "ongoing")
:param color: optional color name
:param multi_line: enable multi-line notifications

```python
from nicegui import ui

ui.button('Say hi!', on_click=lambda: ui.notify('Hi!', close_button='OK'))

```

Features: Notification Types, Multiline Notifications

### ui.notification
Displays a notification on the screen.
In contrast to `ui.notify`, this element allows to update the notification message and other properties once the notification is displayed.
The notification can be removed with `dismiss()`.

```python
import asyncio
from nicegui import ui

async def compute():
    n = ui.notification(timeout=None)
    for i in range(10):
        n.message = f'Computing {i/10:.0%}'
        n.spinner = True
        await asyncio.sleep(0.2)
    n.message = 'Done!'
    n.spinner = False
    await asyncio.sleep(1)
    n.dismiss()

ui.button('Compute', on_click=compute)

```

---

## Data Display

### ui.table
A table based on Quasar's `QTable <https://quasar.dev/vue-components/table>`_ component.
Updates can be pushed to the table by updating the ``rows`` or ``columns`` properties.

If ``selection`` is "single" or "multiple", then a ``selected`` property is accessible containing the selected rows.

Note:
Cells in ``rows`` must not contain lists because they can cause the browser to crash.
To display complex data structures, convert them to strings first (e.g., using ``str()`` or custom formatting).

```python
from nicegui import ui

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol'},
]
ui.table(columns=columns, rows=rows, row_key='name')

```

Features: Omitting columns, Default column parameters, Selection, Table with expandable rows, Show and hide columns, Table with buttons, Table with drop down selection, Table from Pandas DataFrame

### ui.aggrid
An element to create a grid using `AG Grid <https://www.ag-grid.com/>`_.
Updates can be pushed to the grid by updating the ``options`` property.

The methods ``run_grid_method`` and ``run_row_method`` can be used to interact with the AG Grid instance on the client.

```python
from nicegui import ui

grid = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age'},
        {'headerName': 'Parent', 'field': 'parent', 'hide': True},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18, 'parent': 'David'},
        {'name': 'Bob', 'age': 21, 'parent': 'Eve'},
        {'name': 'Carol', 'age': 42, 'parent': 'Frank'},
    ],
    'rowSelection': {'mode': 'multiRow'},
})

```

Features: Adding rows, Select AG Grid Rows, Filter Rows using Mini Filters, AG Grid with Conditional Cell Formatting, Create Grid from Pandas DataFrame, Create Grid from Polars DataFrame, Render columns as HTML, Respond to an AG Grid event

### ui.tree
Display hierarchical data using Quasar's `QTree <https://quasar.dev/vue-components/tree>`_ component.
Updates can be pushed to the tree by updating ``.props['nodes']``.

If using IDs, make sure they are unique within the whole tree.

To use checkboxes and ``on_tick``, set the ``tick_strategy`` parameter to "leaf", "leaf-filtered" or "strict".

```python
from nicegui import ui

ui.tree([
    {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id', on_select=lambda e: ui.notify(e.value))

```

Features: Updating nodes, Tree with custom header and body, Tree with checkboxes, Expand/collapse programmatically, Select/deselect programmatically, Tick/untick programmatically, Filter nodes

### ui.log
Create a log view that allows to add new lines without re-transmitting the whole history to the client.

:param max_lines: maximum number of lines before dropping oldest ones (default: `None`)

```python
from datetime import datetime
from nicegui import ui

log = ui.log(max_lines=10).classes('w-full h-20')
ui.button('Log time', on_click=lambda: log.push(datetime.now().strftime('%X.%f')[:-5]))

```

Features: Attach to a logger, Styling lines

### ui.list
A list element based on Quasar's `QList <https://quasar.dev/vue-components/list-and-list-items#qlist-api>`_ component.
It provides a container for ``ui.item`` elements.

```python
from nicegui import ui

with ui.list().props('dense separator'):
    ui.item('3 Apples')
    ui.item('5 Bananas')
    ui.item('8 Strawberries')
    ui.item('13 Walnuts')

```

Features: Items, Sections and Labels, Reference for ui.list, Reference for ui.item, Reference for ui.item_section, Reference for ui.item_label

---

## Charts & Visualization

### ui.echart
An element to create a chart using `ECharts <https://echarts.apache.org/>`_.
Updates can be pushed to the chart by changing the `options` property.

:param options: dictionary of EChart options
:param on_point_click: callback that is invoked when a point is clicked
:param on_click: callback that is invoked when any component is clicked (*added in version 3.5.0*)
:param enable_3d: enforce importing the echarts-gl library
:param renderer: renderer to use ("canvas" or "svg", *added in version 2.7.0*)
:param theme:

```python
from nicegui import ui
from random import random

echart = ui.echart({
    'xAxis': {'type': 'value'},
    'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
    'legend': {'textStyle': {'color': 'gray'}},
    'series': [
        {'type': 'bar', 'name': 'Alpha', 'data': [0.1, 0.2]},
        {'type': 'bar', 'name': 'Beta', 'data': [0.3, 0.4]},
    ],
})

def update():
    echart.options['series'][0]['data'][0] = random()

```

Features: EChart with clickable points, EChart with clickable components, EChart with dynamic properties, EChart with custom theme, EChart from pyecharts, Run methods, Arbitrary chart events, 3D Graphing

### ui.plotly
Renders a Plotly chart.
There are two ways to pass a Plotly figure for rendering, see parameter `figure`:

* Pass a `go.Figure` object, see https://plotly.com/python/

* Pass a Python `dict` object with keys `data`, `layout`, `config` (optional), see https://plotly.com/javascript/

For best performance, use the declarative `dict` approach for creating a Plotly chart.

:param figure: Plotly figure to be rendered.

```python
import plotly.graph_objects as go
from nicegui import ui

fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 2.5]))
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
ui.plotly(fig).classes('w-full h-40')

```

Features: Dictionary interface, Plot updates, Plot events

### ui.highchart
An element to create a chart using `Highcharts <https://www.highcharts.com/>`_.
Updates can be pushed to the chart by changing the ``options`` property.

Due to Highcharts' restrictive license, this element is not part of the standard NiceGUI package.
It is maintained in a `separate repository <https://github.com/zauberzeug/nicegui-highcharts/>`_
and can be installed with ``pip install nicegui[highcharts]``.

By default, a ``Highcharts.chart`` is created.
To use, e.g., ``Highcharts.stockChart`` instead, set the ``type`` property to "stockChart".

:param options: dictionary of Highcharts options
:param type: chart type (e.g. "chart", "stockChart", "mapChart", ...; default: "chart")
:param extras: list of extra dependencies to include (e.g.

```python
from nicegui import ui
from random import random

chart = ui.highchart({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': ['A', 'B']},
    'series': [
        {'name': 'Alpha', 'data': [0.1, 0.2]},
        {'name': 'Beta', 'data': [0.3, 0.4]},
    ],
}).classes('w-full h-64')

def update():
    chart.options['series'][0]['data'][0] = random()

```

Features: Chart with extra dependencies, Chart with draggable points

### ui.line_plot
Create a line plot using pyplot.
The `push` method provides live updating when utilized in combination with `ui.timer`.

:param n: number of lines
:param limit: maximum number of datapoints per line (new points will displace the oldest)
:param update_every: update plot only after pushing new data multiple times to save CPU and bandwidth
:param close: whether the figure should be closed after exiting the context; set to `False` if you want to update it later (default: `True`)
:param kwargs:

```python
import math
from datetime import datetime
from nicegui import ui

line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
    .with_legend(['sin', 'cos'], loc='upper center', ncol=2)

def update_line_plot() -> None:
    now = datetime.now()
    x = now.timestamp()
    y1 = math.sin(x)
    y2 = math.cos(x)
    line_plot.push([now], [[y1], [y2]], y_limits=(-1.5, 1.5))

line_updates = ui.timer(0.1, update_line_plot, active=False)
line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')
```

### ui.altair
Wrap an Altair chart in NiceGUI via anywidget.

Refer to the `altair documentation <https://altair-viz.github.io/user_guide/interactions/jupyter_chart.html#accessing-variable-params>`_
for more information about synchronizing Altair parameters with Python.

```python
import altair as alt
from altair.datasets import data
from nicegui import ui

cars = data.cars()

chart = alt.Chart(cars).mark_point() \
    .encode(x='Horsepower', y='Miles_per_Gallon', color='Origin') \
    .interactive()

ui.altair(chart)

```

Features: Interactive charts

### ui.matplotlib
Create a `Matplotlib <https://matplotlib.org/>`_ element rendering a Matplotlib figure.
The figure is automatically updated when leaving the figure context.

:param kwargs: arguments like `figsize` which should be passed to `matplotlib.figure.Figure <https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure>`_

```python
import numpy as np
from nicegui import ui

with ui.matplotlib(figsize=(3, 2)).figure as fig:
    x = np.linspace(0.0, 5.0)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    ax = fig.gca()
    ax.plot(x, y, '-')

```

### ui.pyplot
Create a context to configure a `Matplotlib <https://matplotlib.org/>`_ plot.

:param close: whether the figure should be closed after exiting the context; set to `False` if you want to update it later (default: `True`)
:param kwargs:

```python
import numpy as np
from matplotlib import pyplot as plt
from nicegui import ui

with ui.pyplot(figsize=(3, 2)):
    x = np.linspace(0.0, 5.0)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    plt.plot(x, y, '-')

```

### ui.mermaid
Renders diagrams and charts written in the Markdown-inspired `Mermaid <https://mermaid.js.org/>`_ language.
The mermaid syntax can also be used inside Markdown elements by providing the extension string 'mermaid' to the ``ui.markdown`` element.

The optional configuration dictionary is passed directly to mermaid before the first diagram is rendered.
This can be used to set such options as

    ``{'securityLevel': 'loose', ...}`` - allow running JavaScript when a node is clicked
    ``{'logLevel': 'info', ...}`` - log debug info to the console

Refer to the Mermaid documentation for the ``mermaid.initialize()`` method for a full list of options.

```python
from nicegui import ui

ui.mermaid('''
    graph LR;
        A --> B;
        A --> C;
''')

```

Features: Handle click events, Handle click events with JS, Handle errors

---

## Maps & 3D

### ui.leaflet
This element is a wrapper around the `Leaflet <https://leafletjs.com/>`_ JavaScript library.

:param center: initial center location of the map (latitude/longitude, default: (0.0, 0.0))
:param zoom: initial zoom level of the map (default: 13)
:param draw_control: whether to show the draw toolbar (default: False)
:param options: additional options passed to the Leaflet map (default: {})
:param hide_drawn_items: whether to hide drawn items on the map (default: False, *added in version 2.0.0*)
:param additional_resources: additional resources like CSS or JS files to load (default:

```python
from nicegui import ui

m = ui.leaflet(center=(51.505, -0.09))
ui.label().bind_text_from(m, 'center', lambda center: f'Center: {center[0]:.3f}, {center[1]:.3f}')
ui.label().bind_text_from(m, 'zoom', lambda zoom: f'Zoom: {zoom}')

with ui.grid(columns=2):
    ui.button('London', on_click=lambda: m.set_center((51.505, -0.090)))
    ui.button('Berlin', on_click=lambda: m.set_center((52.520, 13.405)))
    ui.button(icon='zoom_in', on_click=lambda: m.set_zoom(m.zoom + 1))
    ui.button(icon='zoom_out', on_click=lambda: m.set_zoom(m.zoom - 1))

```

Features: Changing the Map Style, Add Markers on Click, Move Markers, Image Overlays, Video Overlays, Vector Layers, Disable Pan and Zoom, Draw on Map

### ui.scene
Display a 3D scene using `three.js <https://threejs.org/>`_.
Currently NiceGUI supports boxes, spheres, cylinders/cones, extrusions, straight lines, curves and textured meshes.
Objects can be translated, rotated and displayed with different color, opacity or as wireframes.
They can also be grouped to apply joint movements.

```python
from nicegui import ui

with ui.scene().classes('w-full h-64') as scene:
    scene.axes_helper()
    scene.sphere().material('#4488ff').move(2, 2)
    scene.cylinder(1, 0.5, 2, 20).material('#ff8800', opacity=0.5).move(-2, 1)
    scene.extrusion([[0, 0], [0, 1], [1, 0.5]], 0.1).material('#ff8888').move(2, -1)

    with scene.group().move(z=2):
        scene.box().move(x=2)
        scene.box().move(y=2).rotate(0.25, 0.5, 0.75)
        scene.box(wireframe=True).material('#888888').move(x=2, y=2)

    scene.line([-4, 0, 0], [-4, 2, 0]).material('#ff0000')
    scene.curve([-4, 0, 0], [-4, -1, 0], [-3, -1, 0], [-3, 0, 0]).material('#008800')

```

Features: Handling Click Events, Context menu for 3D objects, Draggable objects, Subscribe to the drag event, Rendering point clouds, Wait for Initialization, Changing Controls, Scene View

### ui.joystick
Create a joystick based on `nipple.js <https://yoannmoi.net/nipplejs/>`_.

:param on_start: callback for when the user touches the joystick
:param on_move: callback for when the user moves the joystick
:param on_end: callback for when the user releases the joystick
:param throttle: throttle interval in seconds for the move event (default: 0.05)
:param options:

```python
from nicegui import ui

ui.joystick(
    color='blue', size=50,
    on_move=lambda e: coordinates.set_text(f'{e.x:.3f}, {e.y:.3f}'),
    on_end=lambda _: coordinates.set_text('0, 0'),
).classes('bg-slate-300')
coordinates = ui.label('0, 0')

```

---

## Media

### ui.image
Displays an image.
This element is based on Quasar's `QImg <https://quasar.dev/vue-components/img>`_ component.

:param source: the source of the image; can be a URL, local file path, a base64 string or a PIL image

```python
from nicegui import ui

ui.image('https://picsum.photos/id/377/640/360')

```

Features: Local files, Base64 string, PIL image, Lottie files, Image link, Force reload

### ui.interactive_image
Create an image with an SVG overlay that handles mouse events and yields image coordinates.
It is also the best choice for non-flickering image updates.
If the source URL changes faster than images can be loaded by the browser, some images are simply skipped.
Thereby repeatedly updating the image source will automatically adapt to the available bandwidth.
See `OpenCV Webcam <https://github.com/zauberzeug/nicegui/tree/main/examples/opencv_webcam/main.py>`_ for an example.

```python
from nicegui import events, ui

def mouse_handler(e: events.MouseEventArguments):
    color = 'SkyBlue' if e.type == 'mousedown' else 'SteelBlue'
    ii.content += f'<circle cx="{e.image_x}" cy="{e.image_y}" r="15" fill="none" stroke="{color}" stroke-width="4" />'
    ui.notify(f'{e.type} at ({e.image_x:.1f}, {e.image_y:.1f})')

src = 'https://picsum.photos/id/565/640/360'
ii = ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup'], cross=True, sanitize=False)

```

Features: Adding layers, Nesting elements, Force reload, Blank canvas, Loaded event, Crosshairs, SVG events

### ui.audio
Displays an audio player.

:param src: URL or local file path of the audio source
:param controls: whether to show the audio controls, like play, pause, and volume (default: `True`)
:param autoplay: whether to start playing the audio automatically (default: `False`)
:param muted: whether the audio should be initially muted (default: `False`)
:param loop: whether the audio should loop (default: `False`)

```python
from nicegui import ui

a = ui.audio('https://cdn.pixabay.com/download/audio/2022/02/22/audio_d1718ab41b.mp3')
a.on('ended', lambda _: ui.notify('Audio playback completed'))

ui.button(on_click=lambda: a.props('muted'), icon='volume_off').props('outline')
ui.button(on_click=lambda: a.props(remove='muted'), icon='volume_up').props('outline')

```

Features: Control the audio element, Event subscription

### ui.video
Displays a video.

:param src: URL or local file path of the video source
:param controls: whether to show the video controls, like play, pause, and volume (default: `True`)
:param autoplay: whether to start playing the video automatically (default: `False`)
:param muted: whether the video should be initially muted (default: `False`)
:param loop: whether the video should loop (default: `False`)

```python
from nicegui import ui

v = ui.video('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4')
v.on('ended', lambda _: ui.notify('Video playback completed'))

```

Features: Control the video element

### ui.parallax
Displays an image with a parallax effect.
This element is based on Quasar's `Parallax <https://quasar.dev/vue-components/parallax>`_ component.

*Added in version 3.9.0.*

:param source: the source of the image; can be a URL, local file path, a base64 string or a PIL image
:param height: the height of the parallax image in pixels (default: 500.0)
:param speed: the speed (0 to 1) of the parallax effect (default:

```python
from nicegui import ui

with ui.scroll_area():
    ui.label('Some text above...').classes('border h-32 w-full')
    with ui.parallax('https://cdn.quasar.dev/img/parallax2.jpg', height=200):
        ui.label('Text').classes('text-white')
    ui.label('Some text below...').classes('border h-32 w-full')

```

---

## Special

### ui.json_editor
An element to create a JSON editor using `JSONEditor <https://github.com/josdejong/svelte-jsoneditor>`_.
Updates can be pushed to the editor by changing the `properties` property.

:param properties: dictionary of JSONEditor properties
:param on_select: callback which is invoked when some of the content has been selected
:param on_change: callback which is invoked when the content has changed
:param schema:

```python
from nicegui import ui

json = {
    'array': [1, 2, 3],
    'boolean': True,
    'color': '#82b92c',
    None: None,
    'number': 123,
    'object': {
        'a': 'b',
        'c': 'd',
    },
    'time': 1575599819000,
    'string': 'Hello World',
}
ui.json_editor({'content': {'json': json}},
```

Features: Update content, Validation, Run methods

### ui.xterm
This element is a wrapper around `xterm.js <https://github.com/xtermjs/xterm.js>`_ to emulate a terminal.
Note: This element provides only a front-end component without an underlying shell.

*Added in version 3.1.0*

:param options: A dictionary of options to configure the terminal, see the
                `xterm.js documentation <https://xtermjs.org/docs/api/terminal/classes/terminal/#constructor>`_.
:param on_bell: Optional callback to be invoked when the terminal's bell is triggered (*added in version 3.10.0*).
:param on_data: Optional callback to be invoked when the user types or pastes into the terminal (*added in version 3.10.0*).
                In a typical setup, this should be passed on to the backing pty.

```python
from nicegui import ui

terminal = ui.xterm({'cols': 30, 'rows': 9})
ui.timer(0, lambda: terminal.write('Hello NiceGUI!'), once=True)

```

Features: Using ANSI escape codes, Subscribing to events, Auto-resizing the terminal, Showing output of a subprocess

### ui.anywidget
`anywidget <https://anywidget.dev/en/getting-started/>`_ is a library that allows you to
embed arbitrary JavaScript widgets in a cross-frontend friendly manner.

There are many publicly available examples of anywidget widgets
in the `anywidget gallery <https://try.anywidget.dev/>`_, including
`altair.JupyterChart <https://altair-viz.github.io/user_guide/interactions/jupyter_chart.html>`_,
and `quak <https://github.com/manzt/quak>`_.

Implementation: The ``nicegui.anywidget`` element takes an ``AnyWidget`` and observes all ``sync=True`` traits
of the widget, trigger JS updates when the traits change.
Conversely, changes on the frontend will be synced back to the widget,
using ``ValueElement``'s handling to listen to changes on ``traits``.

```python
import anywidget
import traitlets
from nicegui import ui

class CounterWidget(anywidget.AnyWidget):
    _esm = '''
        function render({ model, el }) {
            const button = document.createElement("button");
            button.innerHTML = `Count is ${model.get("value")}`;
            button.addEventListener("click", () => {
                model.set("value", model.get("value") + 1);
                model.save_changes();
            });
            model.on("change:value", () => {
                button.innerHTML = `Count is ${model.get("value")}`;
            });
```

Features: Altair charts with AnyWidget

### ui.keyboard
Adds global keyboard event tracking.

The ``on_key`` callback receives a ``KeyEventArguments`` object with the following attributes:

- ``sender``: the ``Keyboard`` element
- ``client``: the client object
- ``action``: a ``KeyboardAction`` object with the following attributes:
    - ``keydown``: whether the key was pressed
    - ``keyup``: whether the key was released
    - ``repeat``: whether the key event was a repeat
- ``key``: a ``KeyboardKey`` object with the following attributes:
    - ``name``: the name of the key (e.g. "a", "Enter", "ArrowLeft"; see `here <https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values>`_ for a list of possible values)
    - ``code``: the code of the key (e.g.

```python
from nicegui import events, ui

def handle_key(e: events.KeyEventArguments):
    if e.key == 'f' and not e.action.repeat:
        if e.action.keyup:
            ui.notify('f was just released')
        elif e.action.keydown:
            ui.notify('f was just pressed')
    if e.modifiers.shift and e.action.keydown:
        if e.key.arrow_left:
            ui.notify('going left')
        elif e.key.arrow_right:
            ui.notify('going right')
        elif e.key.arrow_up:
            ui.notify('going up')
        elif e.key.arrow_down:
```

Features: Prevent default and stop propagation

### ui.timer
One major drive behind the creation of NiceGUI was the necessity to have a simple approach to update the interface in regular intervals,
for example to show a graph with incoming measurements.
A timer will execute a callback repeatedly with a given interval.

```python
from datetime import datetime
from nicegui import ui

label = ui.label()
ui.timer(1.0, lambda: label.set_text(f'{datetime.now():%X}'))

```

Features: Activate, deactivate and cancel a timer, Cancel current invocation, Call a function after a delay, Don't start immediately, Global app timer

### ui.refreshable
The ``@ui.refreshable`` decorator allows you to create functions that have a ``refresh`` method.
This method will automatically delete all elements created by the function and recreate them.

For decorating refreshable methods in classes, there is a ``@ui.refreshable_method`` decorator,
which is equivalent but prevents static type checking errors.

```python
import random
from nicegui import ui

numbers = []

@ui.refreshable
def number_ui() -> None:
    ui.label(', '.join(str(n) for n in sorted(numbers)))

def add_number() -> None:
    numbers.append(random.randint(0, 100))
    number_ui.refresh()

number_ui()
ui.button('Add random number', on_click=add_number)

```

Features: Refreshable UI with parameters, Refreshable UI for input validation, Refreshable UI with reactive state, Awaitable refresh, Global scope, Local scope (variant A), Local scope (variant B), Local scope (variant C)

### ui.run_javascript
This function runs arbitrary JavaScript code on a page that is executed in the browser.
To access a client-side Vue component or HTML element by ID,
use the JavaScript functions `getElement()` or `getHtmlElement()` (*added in version 2.9.0*).

If the function is awaited, the result of the JavaScript code is returned.
Otherwise, the JavaScript code is executed without waiting for a response.

Obviously the JavaScript code is only executed after the client is connected.
Internally, ``await client.connected()`` is called before the JavaScript code is executed (*since version 3.0.0*).
This might delay the execution of the JavaScript code and is not covered by the ``timeout`` parameter.

```python
from nicegui import ui

def alert():
    ui.run_javascript('alert("Hello!")')

async def get_date():
    time = await ui.run_javascript('Date()')
    ui.notify(f'Browser time: {time}')

def access_elements():
    ui.run_javascript(f'getHtmlElement({label.id}).innerText += " Hello!"')

ui.button('fire and forget', on_click=alert)
ui.button('receive result', on_click=get_date)
ui.button('access elements', on_click=access_elements)
label = ui.label()
```

Features: Run async JavaScript

### ui.download
These functions allow you to download files, URLs or raw data.

*Added in version 2.14.0*

```python
from nicegui import ui

ui.button('Local file', on_click=lambda: ui.download.file('main.py'))
ui.button('From URL', on_click=lambda: ui.download.from_url('/logo.png'))
ui.button('Content', on_click=lambda: ui.download.content('Hello World', 'hello.txt'))

```

Features: Download from a relative URL, Download raw bytes or string content, Download file from local path

### ui.status_code
Set the HTTP status code for the current page response.
Must be called during page building, before the response is sent to the client.

*Added in version 3.10.0*

:param code: HTTP status code (e.g. 200, 404, 503)

```python
from nicegui import ui

@ui.page('/teapot')
def teapot_page():
    ui.status_code(418)
    ui.label("I'm a teapot")

@ui.page('/')
def page():
    ui.link('Visit the teapot page', '/teapot')

```

Features: Conditional 404

---

## Styling

### ui.dark_mode
You can use this element to enable, disable or toggle dark mode on the page.
The value `None` represents auto mode, which uses the client's system preference.

Note that this element overrides the `dark` parameter of the `ui.run` function and page decorators.

:param value: Whether dark mode is enabled.

```python
from nicegui import ui

dark = ui.dark_mode()
ui.label('Switch mode:')
ui.button('Dark', on_click=dark.enable)
ui.button('Light', on_click=dark.disable)

```

Features: Binding to a switch, Disable Dark Reader extension

### ui.colors
Sets the main colors (primary, secondary, accent, ...) used by `Quasar <https://quasar.dev/style/theme-builder>`_ on a per-page basis.

Note: This takes precedence over the global color configuration set via ``app.colors()``.

```python
from nicegui import ui

ui.button('Default', on_click=lambda: ui.colors())
ui.button('Gray', on_click=lambda: ui.colors(primary='#555'))

```

Features: Custom colors, App-wide colors

### ui.add_css
This function can be used to add CSS style definitions to the head of the HTML page.

*Added in version 2.0.0*

:param content: CSS content (string or file path)
:param shared: whether to add the code to all pages (default:

```python
from nicegui import ui

ui.add_css('''
    .red {
        color: red;
    }
''')
ui.label('This is red with CSS.').classes('red')

```

Features: Add SCSS style definitions to the page (deprecated), Add SASS style definitions to the page (deprecated)

### ui.query
To manipulate elements like the document body, you can use the `ui.query` function.
With the query result you can add classes, styles, and attributes like with every other UI element.
This can be useful for example to change the background color of the page (e.g. `ui.query('body').classes('bg-green')`).

:param selector: the CSS selector (e.g.

```python
from nicegui import ui

def set_background(color: str) -> None:
    ui.query('body').style(f'background-color: {color}')

ui.button('Blue', on_click=lambda: set_background('#ddeeff'))
ui.button('Orange', on_click=lambda: set_background('#ffeedd'))

```

Features: Set background gradient, Modify default page padding

### ui.element
This class is the base class for all other UI elements.
But you can use it to create elements with arbitrary HTML tags.

:param tag: HTML tag of the element
:param _client: client for this element (for internal use only)

```python
from nicegui import ui

with ui.element('div').classes('p-2 bg-blue-100'):
    ui.label('inside a colored div')

```

Features: Register event handlers, Move elements, Move elements to slots, Default props, Default classes, Default style

### ui.fullscreen
This element is based on Quasar's `AppFullscreen <https://quasar.dev/quasar-plugins/app-fullscreen>`_ plugin
and provides a way to enter, exit and toggle the fullscreen mode.

Important notes:

* Due to security reasons, the fullscreen mode can only be entered from a previous user interaction such as a button click.
* The long-press escape requirement only works in some browsers like Google Chrome or Microsoft Edge.

```python
from nicegui import ui

fullscreen = ui.fullscreen()

ui.button('Enter Fullscreen', on_click=fullscreen.enter)
ui.button('Exit Fullscreen', on_click=fullscreen.exit)
ui.button('Toggle Fullscreen', on_click=fullscreen.toggle)

```

Features: Requiring long-press to exit, Tracking fullscreen state

---

## Core Concepts

### Pages & Routing

Topics: Page, Page Layout, Sub Pages, Script Mode, , Parameter injection, Page title, Status code, Navigation functions, ui.open, Download functions, Add a directory of static files, Add directory of media files, Add HTML to the page, API Responses

### Binding Properties

Topics: Bindings, Transformation functions, Bind to dictionary, Bind to nested properties, Bind to variable, Bind to storage, Check for non-existing bound attributes, Bindable properties for maximum performance, Bindable dataclass

### Action & Events

Topics: Timer, Keyboard, UI Updates, Refreshable UI functions, Async event handlers, Generic Events, Running CPU-bound tasks, Running I/O-bound tasks, Run JavaScript, Read and write to the clipboard, Event, Error handling, Lifecycle events, Custom error page, ui.on_exception, Shut down NiceGUI, Storage

### Styling & Appearance

Topics: Styling, Try styling NiceGUI elements!, None, , CSS Layers, Tailwind CSS Layers, UnoCSS engine, ElementFilter, Query Selector, Color Theming, CSS Variables, Overwrite Tailwind's Default Style, Dark mode, Add CSS style definitions to the page, Using other Vue UI frameworks

### Storage

Topics: Counting page visits, Storing UI state, Storing data per browser tab, Maximum age of tab storage, Short-term memory, Indentation, Redis storage

### Configuration & Deployment

Topics: URLs, ui.run, Native Mode, Native Window Events, , None, , Environment Variables, Background Tasks, Custom Vue Components, Server Hosting, None, , None, , None, , Package for Installation, None, , None, , , Documentation Index, None, , NiceGUI On Air
