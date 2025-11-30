import os
import sys
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
# Ensure project root is on sys.path when running as a script (python tools/daily_report.py)
_THIS_DIR = Path(__file__).resolve().parent
_ROOT = _THIS_DIR.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from dotenv import load_dotenv
from config import bot, chat_id


def _now_utc():
    return datetime.now(timezone.utc)


def _read_runs(run_log_path: Path, since_utc: datetime):
    if not run_log_path.exists():
        return []
    runs = []
    with run_log_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                ts_str = rec.get("ts")
                if not ts_str:
                    continue
                # Parse as UTC
                ts = datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                if ts >= since_utc:
                    runs.append(rec)
            except Exception:
                continue
    return runs


def _format_daily_summary(landings_count: int, pages: int, passed: int, failed: int, details_url: str | None = None):
    total = pages
    success = passed
    errors = failed
    pct = int(round((success / total) * 100)) if total else 0
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    lines = []
    lines.append(f"✅ Автотест проверки лендингов завершён ({now_str}) ")
    lines.append("")
    lines.append(f"🌐 Лендингов проверено: {landings_count}")
    lines.append("")
    lines.append(f"🔗 Страниц: {total}")
    lines.append("")
    lines.append(f"✔️ Успешных: {success} ({pct}%)")
    lines.append("")
    lines.append(f"❌ Ошибок: {errors} ({100 - pct if total else 0}%)")
    lines.append("")
    if details_url:
        lines.append(f"📊 Детали: {details_url}")
    else:
        lines.append("📊 Детали: (доработаем позже)")
    return "\n".join(lines)


def main():
    load_dotenv()
    run_log_path = Path(os.getenv("RUN_LOG_PATH", ".run_summaries.jsonl").strip())
    # Prefer DAILY_REPORT_URL for daily summaries; fallback to REPORT_URL if provided
    details_url = os.getenv("DAILY_REPORT_URL") or os.getenv("REPORT_URL")

    now = _now_utc()
    since = now - timedelta(days=1)
    runs = _read_runs(run_log_path, since)

    pages = sum(int(r.get("pages", 0)) for r in runs)
    passed = sum(int(r.get("passed", 0)) for r in runs)
    failed = sum(int(r.get("failed", 0)) for r in runs)
    landings = set()
    for r in runs:
        try:
            for d in r.get("landings", []):
                if d:
                    landings.add(d)
        except Exception:
            continue

    text = _format_daily_summary(len(landings), pages, passed, failed, details_url)
    try:
        bot.send_message(chat_id, text)
    except Exception:
        # Fail silently to avoid cron noise; logs can be added here if needed
        pass


if __name__ == "__main__":
    main()

