import os
import telebot
from dotenv import load_dotenv

load_dotenv()

host_stage = os.getenv("URL_STAGE")
host_prod = os.getenv("URL_PROD")
pol_url = os.getenv("POL_PROD_URL")
mol_url = os.getenv("MOL_PROD_URL")
headless = os.getenv("HEADLESS_ENV")

_bot_token = (os.getenv("BOT_TOKEN") or "").strip()
_chat_id_raw = (os.getenv("CHAT_ID") or "").strip()

bot = telebot.TeleBot(_bot_token) if _bot_token else None
try:
    chat_id = int(_chat_id_raw) if _chat_id_raw else None
except Exception:
    chat_id = None
