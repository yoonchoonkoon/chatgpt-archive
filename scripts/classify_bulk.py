# scripts/classify_bulk.py
from __future__ import annotations

import re
import csv
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Optional

ROOT = Path(__file__).resolve().parents[1]
BULK_DIR = ROOT / "md" / "bulk"
OUT_DIR = ROOT / "md" / "by_category"
INDEX_CSV = ROOT / "md" / "index.csv"


@dataclass
class Rule:
    category: str
    patterns: List[re.Pattern]


def compile_rules() -> List[Rule]:
    def p(x: str) -> re.Pattern:
        return re.compile(x, re.IGNORECASE)

    return [
        Rule(
            "autotraderagent",
            [
                p(r"\bautotraderagent\b"),
                p(r"\bbase_ratio\b"),
                p(r"\bdd_warn\b|\bdd_cut\b|\bforce_flat\b"),
                p(r"realtime_loop|risk_profile|alert_history|engine_active_profile"),
                p(r"노션|notion|ntn_|secret_"),
            ],
        ),
        Rule(
            "finance",
            [
                p(r"\bETF\b|\bCAGR\b|\bSharpe\b|\bVaR\b|\bCAPM\b|\bGARCH\b"),
                p(r"채권|금리|스프레드|듀레이션|스왑|CDS|환율|FX|원화|달러"),
                p(r"부동산|리츠|REIT|원자재|commodity|spot price|roll yield"),
            ],
        ),
        Rule(
            "philosophy",
            [
                p(r"명상|수행|알아차림|무의식|의식|자아|진리|의미|죽음|사후"),
                p(r"판단위생|합의|규칙|침범"),
            ],
        ),
        Rule(
            "ai-dev",
            [
                p(r"\bRAG\b|retrieval|embedding|prompt|agent|llm|GPT"),
                p(r"python|fastapi|docker|github|vscode|powershell"),
            ],
        ),
        Rule(
            "life",
            [
                p(r"여행|가족|교육|아이|학교|건강|운동|사업|창업|계획"),
            ],
        ),
    ]


def parse_filename(meta_name: str) -> Tuple[Optional[str], Optional[str]]:
    # expected: YYYY-MM-DD_<id>_<title>.md
    m = re.match(r"^(\d{4}-\d{2}-\d{2})_([^_]+)_(.+)\.md$", meta_name)
    if not m:
        return None, None
    return m.group(1), m.group(3)


def detect_category(text: str, rules: List[Rule]) -> str:
    for r in rules:
        if any(pat.search(text) for pat in r.patterns):
            return r.category
    return "uncategorized"


def first_heading(md: str) -> Optional[str]:
    for line in md.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None


def main() -> None:
    if not BULK_DIR.exists():
        raise SystemExit(f"Missing: {BULK_DIR}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    rules = compile_rules()
    rows = []

    for src in sorted(BULK_DIR.glob("*.md")):
        raw = src.read_text(encoding="utf-8", errors="replace")

        date, title_from_name = parse_filename(src.name)
        h1 = first_heading(raw)
        title = h1 or title_from_name or src.stem

        # 분류 근거: 파일명 + 본문 일부
        hay = f"{src.name}\n{raw[:20000]}"
        category = detect_category(hay, rules)

        dst_dir = OUT_DIR / category
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / src.name

        # 복사(원본 bulk 유지)
        shutil.copy2(src, dst)

        # 태그(간단): 카테고리 + 비밀값 흔적 여부
        tags = [category]
        if re.search(r"\bntn_\w+|\bsecret_\w+", raw, re.IGNORECASE):
            tags.append("contains_token_like")
        if "REDACTED" in raw:
            tags.append("redacted")

        rows.append(
            {
                "date": date or "",
                "file": str(dst.relative_to(ROOT)).replace("\\", "/"),
                "title": title,
                "category": category,
                "tags": ",".join(tags),
            }
        )

    # 인덱스 CSV 생성
    with INDEX_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date", "file", "title", "category", "tags"])
        w.writeheader()
        w.writerows(rows)

    print(f"OK: categorized -> {OUT_DIR}")
    print(f"OK: index -> {INDEX_CSV}")


if __name__ == "__main__":
    main()
