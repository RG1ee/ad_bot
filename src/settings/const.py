import os
from dotenv import load_dotenv


try:
    load_dotenv()
finally:
    TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_IDS = tuple(map(int, os.getenv("ADMINS").split(","),))
    CHAT_ID = os.getenv("CHAT_ID")
    CHAT_LINK = os.getenv("CHAT_LINK")
    DB_NAME = os.getenv("DB_NAME", "db.sqlite3")
    PROVIDER_TOKEN = os.getenv("PAYMENT_TOKEN")
