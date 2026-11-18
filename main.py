"""Write the v2 front-page image to the output directory.

The entry ships its finished image as entry.png beside this file.
This program only copies those bytes to the place the grader reads
them from: MAKEFUN_OUTPUT_DIR when it is set, /output otherwise.
Standard library only, no network, and the copy is byte for byte,
so two runs always write the same file.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image missing: {SOURCE}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    if target.stat().st_size != SOURCE.stat().st_size:
        raise IOError(
            f"copied image is {target.stat().st_size} bytes, "
            f"expected {SOURCE.stat().st_size}"
        )


if __name__ == "__main__":
    main()
