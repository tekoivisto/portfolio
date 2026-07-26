"""
Assembles index.html from index.template.html by inlining each
<!-- INCLUDE: path/to/file.html --> marker with the referenced file's
contents. Run this after editing index.template.html or any file in
projects/.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "index.template.html"
OUTPUT = ROOT / "index.html"

INCLUDE_RE = re.compile(r"<!--\s*INCLUDE:\s*(.+?)\s*-->")


def main():
    template = TEMPLATE.read_text()

    def resolve(match):
        include_path = ROOT / match.group(1)
        return include_path.read_text().rstrip("\n")

    output = INCLUDE_RE.sub(resolve, template)

    OUTPUT.write_text(output)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
