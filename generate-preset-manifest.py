import json
from pathlib import Path

VALID_EXTENSIONS = {".png", ".webp", ".jpg", ".jpeg", ".gif"}


def build_manifest(directory: Path) -> None:
    files = sorted(
        path.name
        for path in directory.iterdir()
        if path.is_file() and path.suffix.lower() in VALID_EXTENSIONS
    )
    output = directory / "manifest.json"
    output.write_text(json.dumps({"files": files}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output}")


def main() -> None:
    preset_root = Path(__file__).resolve().parent / "presets"
    for directory in sorted(path for path in preset_root.iterdir() if path.is_dir()):
        build_manifest(directory)


if __name__ == "__main__":
    main()
