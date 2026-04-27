#!/usr/bin/env python3
"""
NiceGUI Skill - Reference Updater

Downloads the latest sitewide_index.json from nicegui.io and regenerates
the component reference file used by this skill.

Usage:
    python3 scripts/update_reference.py [--output-dir DIR]

Options:
    --output-dir DIR    Directory to write the reference file (default: ../references)
    --index-url URL     URL to the sitewide_index.json (default: https://nicegui.io/static/sitewide_index.json)
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.request import urlopen


INDEX_URL = "https://nicegui.io/static/sitewide_index.json"

# Component categories for organized reference
CATEGORIES = {
    "Text Elements": [
        "ui.label", "ui.markdown", "ui.restructured_text", "ui.code", "ui.html",
    ],
    "Input Elements": [
        "ui.input", "ui.textarea", "ui.number", "ui.select", "ui.radio",
        "ui.checkbox", "ui.switch", "ui.toggle", "ui.slider", "ui.range",
        "ui.rating", "ui.color_input", "ui.color_picker", "ui.date",
        "ui.date_input", "ui.time", "ui.time_input", "ui.upload",
        "ui.editor", "ui.codemirror",
    ],
    "Button & Action": [
        "ui.button", "ui.button_group", "ui.fab", "ui.dropdown_button",
        "ui.badge", "ui.chip", "ui.icon", "ui.avatar",
    ],
    "Layout Containers": [
        "ui.card", "ui.column", "ui.row", "ui.grid", "ui.expansion",
        "ui.scroll_area", "ui.splitter", "ui.separator", "ui.space",
        "ui.skeleton", "ui.teleport",
    ],
    "Navigation": [
        "ui.link", "ui.menu", "ui.context_menu", "ui.tabs", "ui.stepper",
        "ui.pagination", "ui.carousel", "ui.timeline", "ui.navigate", "ui.tooltip",
    ],
    "Dialog & Notification": [
        "ui.dialog", "ui.notify", "ui.notification",
    ],
    "Data Display": [
        "ui.table", "ui.aggrid", "ui.tree", "ui.log", "ui.list",
    ],
    "Charts & Visualization": [
        "ui.echart", "ui.plotly", "ui.highchart", "ui.line_plot",
        "ui.altair", "ui.matplotlib", "ui.pyplot", "ui.mermaid",
    ],
    "Maps & 3D": [
        "ui.leaflet", "ui.scene", "ui.joystick",
    ],
    "Media": [
        "ui.image", "ui.interactive_image", "ui.audio", "ui.video", "ui.parallax",
    ],
    "Special": [
        "ui.json_editor", "ui.xterm", "ui.anywidget", "ui.keyboard",
        "ui.timer", "ui.refreshable", "ui.run_javascript", "ui.download",
        "ui.status_code",
    ],
    "Styling": [
        "ui.dark_mode", "ui.colors", "ui.add_css", "ui.query",
        "ui.element", "ui.fullscreen",
    ],
}


def download_index(url: str) -> list[dict]:
    """Download the sitewide_index.json from the given URL."""
    import ssl
    print(f"Downloading {url} ...")
    context = ssl.create_default_context()
    try:
        with urlopen(url, timeout=30, context=context) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except ssl.SSLCertVerificationError:
        print("  SSL verification failed, retrying without cert check...")
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        with urlopen(url, timeout=30, context=context) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    print(f"  Got {len(data)} entries")
    return data


def build_component_map(data: list[dict]) -> dict[str, list[dict]]:
    """Group entries by component name."""
    component_map: dict[str, list[dict]] = defaultdict(list)
    for item in data:
        title = item.get("title", "")
        if ":" in title:
            comp = title.split(":")[0].strip()
            feature = title.split(":")[1].strip()
        else:
            comp = title.strip()
            feature = title.strip()
        component_map[comp].append({
            "feature": feature,
            "content": item.get("content", "").strip(),
            "demo": item.get("demo", "").strip(),
            "url": item.get("url", ""),
        })
    return component_map


def generate_reference(component_map: dict[str, list[dict]]) -> str:
    """Generate the Markdown reference file content."""
    lines: list[str] = []
    today = date.today().isoformat()

    lines.append("# NiceGUI Component Reference")
    lines.append("")
    lines.append(f"> Auto-generated from {INDEX_URL}")
    lines.append(f"> Last updated: {today}")
    lines.append("")

    # Component sections
    for cat_name, comps in CATEGORIES.items():
        lines.append(f"## {cat_name}")
        lines.append("")
        for comp in comps:
            entries = component_map.get(comp, [])
            if not entries:
                continue
            main = None
            for e in entries:
                if e["content"] and e["feature"] != "Reference":
                    main = e
                    break
            if not main:
                for e in entries:
                    if e["demo"] and e["feature"] != "Reference":
                        main = e
                        break
            if not main:
                continue

            lines.append(f"### {comp}")
            if main["content"]:
                # Truncate at sentence boundary within limit
                content = main["content"][:800]
                # Try to cut at last sentence ending
                for sep in ['. ', '.\n', '\n\n', ': ']:
                    last_sep = content.rfind(sep)
                    if 200 < last_sep < len(content):
                        content = content[:last_sep + len(sep)].rstrip()
                        break
                lines.append(content)
                lines.append("")
            if main["demo"]:
                demo_lines = main["demo"].split("\n")
                clean = [l for l in demo_lines if l.strip() != "ui.run()"]
                if clean:
                    lines.append("```python")
                    lines.extend(clean[:16])
                    lines.append("```")
                    lines.append("")
            features = [
                e["feature"]
                for e in entries
                if e["feature"] not in ("Reference", main["feature"])
            ]
            if features:
                lines.append(f'Features: {", ".join(features[:8])}')
                lines.append("")
        lines.append("---")
        lines.append("")

    # Core concepts
    lines.append("## Core Concepts")
    lines.append("")
    concept_sections = {
        "Pages & Routing": component_map.get("Pages & Routing", []),
        "Binding Properties": component_map.get("Binding Properties", []),
        "Action & Events": component_map.get("Action & Events", []),
        "Styling & Appearance": component_map.get("Styling & Appearance", []),
        "Storage": component_map.get("Storage", []),
        "Configuration & Deployment": component_map.get("Configuration & Deployment", []),
    }
    for section_name, entries in concept_sections.items():
        if not entries:
            continue
        lines.append(f"### {section_name}")
        lines.append("")
        topics = [
            e["feature"]
            for e in entries
            if e["feature"] not in ("Reference", section_name)
        ]
        if topics:
            lines.append(f'Topics: {", ".join(topics)}')
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Update NiceGUI skill reference")
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory to write the reference file (default: ../references)",
    )
    parser.add_argument(
        "--index-url",
        default=INDEX_URL,
        help=f"URL to the sitewide_index.json (default: {INDEX_URL})",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    output_dir = Path(args.output_dir) if args.output_dir else script_dir.parent / "references"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "nicegui_reference.md"

    data = download_index(args.index_url)
    component_map = build_component_map(data)
    content = generate_reference(component_map)

    output_file.write_text(content, encoding="utf-8")
    print(f"Wrote {len(content)} chars to {output_file}")
    print("Done!")


if __name__ == "__main__":
    main()
