import os
from dotenv import load_dotenv

BANNED_SELLERS = [
    "Abdel69"
]

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
ALERT_PRICE_THRESHOLD = float(os.getenv("ALERT_PRICE_THRESHOLD", 0.90))
CHECK_INTERVAL_SECONDS = int(os.getenv("CHECK_INTERVAL_SECONDS", 300))
