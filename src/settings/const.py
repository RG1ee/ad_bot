import os
from dotenv import load_dotenv


try:
    load_dotenv()
finally:
    TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_IDS = (os.getenv("ADMINS").split(","),)
    print(ADMIN_IDS)
    CHAT_ID = os.getenv("CHAT_ID")
    CHAT_LINK = os.getenv("CHAT_LINK")
