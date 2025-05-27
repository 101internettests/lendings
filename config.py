import os
import telebot
from dotenv import load_dotenv

load_dotenv()

host_stage = os.getenv("URL_STAGE")
host_prod = os.getenv("URL_PROD")
pol_url = os.getenv("POL_PROD_URL")
mol_url = os.getenv("MOL_PROD_URL")
headless = os.getenv("HEADLESS_ENV")

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))