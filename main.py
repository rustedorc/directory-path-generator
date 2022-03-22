import pathlib
import sys
from typing import Optional

def tree_gen(*ignore, path: Optional[pathlib.Path] = None, output=sys.stdout) -> None:
    """pass in the name of any file or directory that you want to ignore when generating the syntax
    e.g. '.git' or '__pycache__' or 'secrets.py' """
    path = path if path is not None else pathlib.Path("./")
    for p in sorted(path.rglob("*")):
        parts = p.relative_to(path).parts
        if any(bool(i in parts) for i in ignore) or any(bool(i.startswith(".") for i in parts):
            continue
        depth = len(parts)
        hashes = "#" * depth
        print(hashes, p.name, file=output)

