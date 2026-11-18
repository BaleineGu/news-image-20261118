"""Copy the entry image to the output directory.

Standard library only, no network. The image is entry.png beside this
file; it is copied to entry.png in the output directory, which is
MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    if not SRC.is_file():
        raise FileNotFoundError(f"entry image not found: {SRC}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUT_DIR / "entry.png"
    shutil.copyfile(SRC, dest)
    if dest.stat().st_size != SRC.stat().st_size:
        raise IOError("copied entry image has the wrong size")


if __name__ == "__main__":
    main()
