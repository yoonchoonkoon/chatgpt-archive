import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "md" / "bulk"


def scrub(text: str) -> str:
    text = re.sub(
        r"ntn_[A-Za-z0-9\-_]{10,400}", "REDACTED_NOTION_TOKEN", text, flags=re.MULTILINE
    )
    text = re.sub(
        r"secret_[A-Za-z0-9\-_]{3,400}",
        "REDACTED_NOTION_TOKEN",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(r"NOTION_TOKEN\s*=\s*\S+", "NOTION_TOKEN=REDACTED_NOTION_TOKEN", text)
    text = re.sub(
        r"\$env:NOTION_TOKEN\s*=\s*'[^']*'",
        "$env:NOTION_TOKEN='REDACTED_NOTION_TOKEN'",
        text,
    )
    return text


def main():
    if not MD_DIR.exists():
        raise SystemExit(f"Missing: {MD_DIR}")

    changed = 0
    for p in MD_DIR.glob("*.md"):
        s = p.read_text(encoding="utf-8", errors="ignore")
        t = scrub(s)
        if t != s:
            p.write_text(t, encoding="utf-8")
            changed += 1
    print(f"OK: scrubbed {changed} files")


if __name__ == "__main__":
    main()
