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

def _now_msk():
    return datetime.now(timezone(timedelta(hours=3)))

def _msk_day_window(now_msk: datetime, *, start_hour: int = 0):
    """Return (start_utc, end_utc, start_msk, end_msk) for current MSK day window.

    Window starts at start_hour:00 MSK. Default 00:00.
    End is the earlier of (now) and (next day start).
    """
    if now_msk.tzinfo is None:
        now_msk = now_msk.replace(tzinfo=timezone(timedelta(hours=3)))
    start_msk = now_msk.replace(hour=start_hour, minute=0, second=0, microsecond=0)
    # if report runs before start_hour, use previous day window
    if now_msk < start_msk:
        start_msk = start_msk - timedelta(days=1)
    end_msk = start_msk + timedelta(days=1)
    start_utc = start_msk.astimezone(timezone.utc)
    end_utc = min(_now_utc(), end_msk.astimezone(timezone.utc))
    return start_utc, end_utc, start_msk, end_msk


def _read_runs(run_log_path: Path, since_utc: datetime, until_utc: datetime | None = None):
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
                if ts >= since_utc and (until_utc is None or ts < until_utc):
                    runs.append(rec)
            except Exception:
                continue
    return runs


def _format_daily_summary(
    landings_count: int,
    pages: int,
    passed: int,
    failed: int,
    details_url: str | None = None,
    *,
    now_msk_str: str | None = None,
    period_msk: str | None = None,
):
    total = pages
    success = passed
    errors = failed
    pct = int(round((success / total) * 100)) if total else 0
    now_str = now_msk_str or _now_msk().strftime("%Y-%m-%d %H:%M") + " (MSK)"
    lines = []
    lines.append(f"✅ Автотест форм заявок с лендингов завершён ({now_str})")
    if period_msk:
        lines.append(f"🗓 Период: {period_msk}")
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
    # Use only REPORT_URL for details link per user requirement
    details_url = os.getenv("REPORT_URL")

    # MSK day window (default 00:00–23:59 MSK). You can shift start via MSK_DAY_START_HOUR (e.g. 1).
    start_hour = int(os.getenv("MSK_DAY_START_HOUR", "0"))
    now_msk = _now_msk()
    since_utc, until_utc, start_msk, end_msk = _msk_day_window(now_msk, start_hour=start_hour)
    runs = _read_runs(run_log_path, since_utc, until_utc)

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

    period_str = f"{start_msk.strftime('%Y-%m-%d %H:%M')}–{min(now_msk, end_msk).strftime('%Y-%m-%d %H:%M')} (MSK)"
    now_msk_str = now_msk.strftime("%Y-%m-%d %H:%M") + " (MSK)"
    text = _format_daily_summary(
        len(landings),
        pages,
        passed,
        failed,
        details_url,
        now_msk_str=now_msk_str,
        period_msk=period_str,
    )
    try:
        bot.send_message(chat_id, text)
    except Exception:
        # Fail silently to avoid cron noise; logs can be added here if needed
        pass


if __name__ == "__main__":
    main()

