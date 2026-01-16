import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "conversations.json"
OUT = ROOT / "md" / "bulk"


def slug(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[^\w가-힣\- ]+", "", s)
    s = re.sub(r"\s+", "-", s)
    return s[:80] if s else "untitled"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    data = json.load(open(RAW, "r", encoding="utf-8"))

    n = 0
    for c in data:
        title = c.get("title") or "untitled"
        cid = (c.get("id") or "noid")[:12]
        ts = c.get("create_time") or c.get("created_at") or ""
        date = ""
        if isinstance(ts, (int, float)):
            # unix seconds -> YYYY-MM-DD (local)
            import datetime

            date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        else:
            # fallback: try YYYY-MM-DD in string
            m = re.search(r"\d{4}-\d{2}-\d{2}", str(ts))
            date = m.group(0) if m else "unknown-date"

        fname = f"{date}_{cid}_{slug(title)}.md"
        path = OUT / fname

        # 최소 본문(원본 json이 구조가 다양하니, 우선 json dump를 넣어둠)
        body = json.dumps(c, ensure_ascii=False, indent=2)

        path.write_text(
            f"# {title}\n\n- id: {c.get('id','')}\n- date: {date}\n\n```json\n{body}\n```\n",
            encoding="utf-8",
        )
        n += 1

    print(f"OK: exported {n} conversations to {OUT}")


if __name__ == "__main__":
    main()
