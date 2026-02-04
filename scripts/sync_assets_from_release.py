#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import argparse
import shutil
import tempfile
import urllib.request
import zipfile
from pathlib import Path


DEFAULT_RELEASE_URL = (
    "https://github.com/mrachinskiy/jewelcraft/releases/download/"
    "v2.18.0-blender4.2.0/jewelcraft-2_18_0.zip"
)


def _download_zip(url: str, target: Path) -> None:
    with urllib.request.urlopen(url) as response, open(target, "wb") as file:
        shutil.copyfileobj(response, file)


def _extract_assets(zip_path: Path, assets_dir: Path, force: bool) -> int:
    prefix = "jewelcraft/assets/"
    extracted = 0

    with zipfile.ZipFile(zip_path) as zf:
        names = [name for name in zf.namelist() if name.startswith(prefix)]

        if not names:
            raise RuntimeError("Release zip does not contain jewelcraft/assets/")

        if assets_dir.exists() and force:
            shutil.rmtree(assets_dir)

        assets_dir.mkdir(parents=True, exist_ok=True)

        for name in names:
            relative = Path(name[len(prefix):])
            if not relative.parts:
                continue

            target = assets_dir / relative
            if name.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
                continue

            target.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(name) as source, open(target, "wb") as dest:
                shutil.copyfileobj(source, dest)
            extracted += 1

    return extracted


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync source/assets from official JewelCraft release zip.",
    )
    parser.add_argument(
        "--zip",
        dest="zip_path",
        type=Path,
        help="Local path to JewelCraft release zip.",
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_RELEASE_URL,
        help="Release zip URL used when --zip is not provided.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing source/assets before extraction.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    assets_dir = repo_root / "source" / "assets"

    if args.zip_path is not None:
        zip_path = args.zip_path.resolve()
        if not zip_path.exists():
            raise FileNotFoundError(f"Zip not found: {zip_path}")
        extracted = _extract_assets(zip_path, assets_dir, args.force)
        print(f"Synced {extracted} files into: {assets_dir}")
        return 0

    with tempfile.TemporaryDirectory() as tempdir:
        zip_path = Path(tempdir) / "jewelcraft-release.zip"
        print(f"Downloading: {args.url}")
        _download_zip(args.url, zip_path)
        extracted = _extract_assets(zip_path, assets_dir, args.force)

    print(f"Synced {extracted} files into: {assets_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
