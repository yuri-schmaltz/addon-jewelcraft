#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import re
import zipfile
from pathlib import Path


def _parse_version(manifest_path: Path) -> str:
    text = manifest_path.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)

    if match is None:
        return "dev"

    return match.group(1)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    source_dir = repo_root / "source"
    manifest_path = source_dir / "blender_manifest.toml"
    assets_dir = source_dir / "assets"

    missing_paths = [path for path in (source_dir, manifest_path, assets_dir) if not path.exists()]
    if missing_paths:
        print("Cannot build developer zip: required paths are missing.")
        for path in missing_paths:
            print(f"- {path}")
        print("Tip: use the official release zip or populate source/assets before packaging.")
        return 2

    version = _parse_version(manifest_path)
    dist_dir = repo_root / "dist"
    dist_dir.mkdir(exist_ok=True)
    output_zip = dist_dir / f"jewelcraft-dev-{version}.zip"

    if output_zip.exists():
        output_zip.unlink()

    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in source_dir.rglob("*"):
            if path.is_file():
                arcname = Path("jewelcraft") / path.relative_to(source_dir)
                zf.write(path, arcname)

    print(f"Created: {output_zip}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
