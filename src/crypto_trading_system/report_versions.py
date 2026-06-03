from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path


def next_report_version(directories: Iterable[Path | None], filename_prefix: str) -> int:
    pattern = re.compile(rf"^{re.escape(filename_prefix)}_v(\d+)\.md$")
    highest = 0
    for directory in directories:
        if directory is None or not directory.exists():
            continue
        for path in directory.iterdir():
            if not path.is_file():
                continue
            match = pattern.match(path.name)
            if match:
                highest = max(highest, int(match.group(1)))
    return highest + 1


def versioned_markdown_filename(filename_prefix: str, version: int) -> str:
    return f"{filename_prefix}_v{version}.md"
