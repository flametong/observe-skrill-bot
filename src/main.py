import time
from config import CHECK_INTERVAL_SECONDS, BOT_TOKEN, CHAT_ID
from telegram_bot import TelegramBot
from bybit_checker import BybitChecker

def main():
    print("⏳ Monitoring started...")

    bot = TelegramBot(bot_token=BOT_TOKEN, chat_id=CHAT_ID)
    checker = BybitChecker(bot)

    while True:
        checker.fetch_and_notify()
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
