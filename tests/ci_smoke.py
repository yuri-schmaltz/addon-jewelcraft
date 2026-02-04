# SPDX-FileCopyrightText: 2026 Mikhail Rachinskiy
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

import bpy


def _parse_args() -> tuple[Path, str]:
    if "--" not in sys.argv:
        raise RuntimeError("Expected Blender args after '--': <addon_zip> <module_name>")

    args = sys.argv[sys.argv.index("--") + 1:]
    if len(args) != 2:
        raise RuntimeError("Usage: -- <addon_zip> <module_name>")

    addon_zip = Path(args[0]).resolve()
    module_name = args[1]

    if not addon_zip.exists():
        raise FileNotFoundError(f"Addon zip not found: {addon_zip}")

    if not module_name:
        raise RuntimeError("Module name cannot be empty")

    return addon_zip, module_name


def _install_from_zip(addon_zip: Path, module_name: str) -> Path:
    addons_dir = Path(bpy.utils.user_resource("SCRIPTS", path="addons", create=True))
    addon_dir = addons_dir / module_name
    prefix = f"{module_name}/"

    if addon_dir.exists():
        shutil.rmtree(addon_dir)

    with zipfile.ZipFile(addon_zip) as zf:
        names = [name for name in zf.namelist() if name.startswith(prefix)]
        if not names:
            raise RuntimeError(f"Module '{module_name}' not found inside {addon_zip.name}")

        for name in names:
            rel = Path(name[len(prefix):])
            if not rel.parts:
                continue

            target = addon_dir / rel
            if name.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
                continue

            target.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(name) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)

    return addon_dir


def _enable_addon(module_name: str) -> None:
    result = bpy.ops.preferences.addon_enable(module=module_name)
    if "FINISHED" not in result:
        raise RuntimeError(f"Failed to enable addon '{module_name}': {result}")


def _disable_addon(module_name: str) -> None:
    try:
        bpy.ops.preferences.addon_disable(module=module_name)
    except Exception:
        pass


def _run_smoke() -> None:
    result = bpy.ops.object.jewelcraft_gem_add(cut="ROUND", stone="DIAMOND", size=1.0)
    if "FINISHED" not in result:
        raise RuntimeError(f"Gem add failed: {result}")

    report_path = Path(tempfile.gettempdir()) / "jewelcraft_ci_report.json"
    if report_path.exists():
        report_path.unlink()

    result = bpy.ops.wm.jewelcraft_design_report(
        file_format="JSON",
        use_preview=False,
        show_warnings=False,
        filepath=str(report_path),
    )
    if "FINISHED" not in result:
        raise RuntimeError(f"Design report failed: {result}")

    if not report_path.exists() or report_path.stat().st_size == 0:
        raise RuntimeError("Design report file was not created")

    data = json.loads(report_path.read_text(encoding="utf-8"))
    if "gems" not in data or not data["gems"]:
        raise RuntimeError("Design report does not contain gem data")

    print("Smoke OK")


def main() -> None:
    addon_zip, module_name = _parse_args()
    _install_from_zip(addon_zip, module_name)
    _enable_addon(module_name)

    try:
        _run_smoke()
    finally:
        _disable_addon(module_name)


if __name__ == "__main__":
    main()
