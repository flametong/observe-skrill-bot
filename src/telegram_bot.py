import requests
from config import BOT_TOKEN, CHAT_ID

class TelegramBot:
    TELEGRAM_API_BASE_URL = "https://api.telegram.org/bot"

    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"{self.TELEGRAM_API_BASE_URL}{bot_token}/sendMessage"

    def send_message(self, text: str):
        payload = {
            "chat_id": self.chat_id,
            "text": text
        }

        try:
            response = requests.post(self.api_url, json=payload, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print(f"❌ Failed to send Telegram message: {e}")
