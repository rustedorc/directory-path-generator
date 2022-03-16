import pathlib
import sys
from typing import Optional

def tree_gen(*ignore, path: Optional[pathlib.Path] = None, output=sys.stdout) -> str:
    path = path if path is not None else pathlib.Path("./")
    for p in sorted(path.rglob("*")):
        parts = p.relative_to(path).parts
        if any(bool(i in parts) for i in ignore):
            continue
        depth = len(parts)
        hashes = "#" * depth
        print(hashes, p.name, file=output)

