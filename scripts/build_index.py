# scripts/build_index.py
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_CSV = ROOT / "md" / "index.csv"
INDEX_DIR = ROOT / "index"

# index/*.md 파일명(버킷)
BUCKETS = {
    "autotrader": "AutoTraderAgent",
    "philosophy": "Philosophy",
    "topics": "Topics",
    "finance": "Finance",
}


def read_rows():
    if not INDEX_CSV.exists():
        raise FileNotFoundError(f"Missing: {INDEX_CSV}")
    with INDEX_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def normalize_category(cat: str) -> str:
    c = (cat or "").strip().lower()
    if c in ("autotrader", "philosophy", "topics", "finance"):
        return c
    return "topics"


def main():
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    rows = read_rows()

    buckets = {k: [] for k in BUCKETS.keys()}
    for r in rows:
        cat = normalize_category(r.get("category", ""))
        title = (r.get("title") or "").strip()
        relpath = (r.get("relpath") or r.get("path") or "").strip()
        if not title or not relpath:
            continue
        buckets[cat].append((title, relpath))

    for cat, label in BUCKETS.items():
        out = INDEX_DIR / f"{cat}.md"
        items = sorted(buckets.get(cat, []), key=lambda x: x[0])
        lines = [f"# {label}", ""]
        for title, relpath in items:
            # GitHub 상대링크
            lines.append(f"- [{title}](../{relpath})")
        lines.append("")
        out.write_text("\n".join(lines), encoding="utf-8")

    print("OK: rebuilt index/*.md from md/index.csv")


if __name__ == "__main__":
    main()
