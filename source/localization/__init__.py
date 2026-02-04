# SPDX-FileCopyrightText: 2015-2025 Mikhail Rachinskiy
# SPDX-License-Identifier: GPL-3.0-or-later

import json
from collections.abc import Iterator
from pathlib import Path


_LOCALE_DIR = Path(__file__).parent
_CACHE_PATH = _LOCALE_DIR / "__cache__.json"


def _po_parse(text: str) -> dict[tuple[str, str], str]:
    import re
    concat_multiline = text.replace('"\n"', "")
    entries = re.findall(r'(?:msgctxt\s*"(.+)")?\s*msgid\s*"(.+)"\s*msgstr\s*"(.*)"', concat_multiline)

    return {
        (ctxt or "*", key.replace("\\n", "\n")): msg.replace("\\n", "\n")
        for ctxt, key, msg in entries
        if msg
    }


def _walk() -> Iterator[tuple[str, dict[tuple[str, str], str]]]:
    for child in _LOCALE_DIR.iterdir():
        if child.is_file() and child.suffix == ".po":
            with open(child, "r", encoding="utf-8") as file:
                yield child.stem, _po_parse(file.read())


def _cache_read() -> dict[str, dict[tuple[str, str], str]] | None:
    if not _CACHE_PATH.exists():
        return None

    try:
        with open(_CACHE_PATH, "r", encoding="utf-8") as file:
            cache = json.load(file)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None

    if not isinstance(cache, dict):
        return None

    dictionary = {}

    for locale, entries in cache.items():
        if not isinstance(locale, str) or not isinstance(entries, list):
            return None

        translations = {}

        for entry in entries:
            if (
                not isinstance(entry, list)
                or len(entry) != 3
                or not all(isinstance(x, str) for x in entry)
            ):
                return None

            ctxt, key, msg = entry
            translations[(ctxt, key)] = msg

        dictionary[locale] = translations

    return dictionary


def _cache_write(dictionary: dict[str, dict[tuple[str, str], str]]) -> None:
    cache = {
        locale: [[ctxt, key, msg] for (ctxt, key), msg in translations.items()]
        for locale, translations in dictionary.items()
    }

    try:
        with open(_CACHE_PATH, "w", encoding="utf-8") as file:
            json.dump(cache, file, ensure_ascii=False)
    except OSError:
        pass


def _init() -> dict[str, dict[tuple[str, str], str]]:
    if (dictionary := _cache_read()) is not None:
        return dictionary

    dictionary = {locale: trnsl for locale, trnsl in _walk()}
    _cache_write(dictionary)

    return dictionary


DICTIONARY = _init()
