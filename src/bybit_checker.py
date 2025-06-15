import requests
from config import ALERT_PRICE_THRESHOLD, BANNED_SELLERS
from telegram_bot import TelegramBot

class BybitChecker:
    BYBIT_API_URL = "https://api2.bybit.com/fiat/otc/item/online"

    def __init__(self, bot: TelegramBot):
        self.bot = bot

    def fetch_and_notify(self):
        payload = {
            "userId": "",
            "tokenId": "USDT",
            "currencyId": "EUR",
            "payment": [
                "162"
            ],
            "side": "1",
            "size": "",
            "page": "1",
            "amount": "",
            "rows": "10",
            "order": ""
        }

        try:
            res = requests.post(self.BYBIT_API_URL, json=payload, timeout=10)
            res.raise_for_status()
            offers = res.json().get("result", {}).get("items", [])

            for offer in offers:
                price = float(offer["price"])
                nickname = offer["nickName"]

                if nickname in BANNED_SELLERS:
                    continue

                if price >= ALERT_PRICE_THRESHOLD:
                    continue

                self._notify_offer(offer, price)

        except Exception as e:
            print(f"❌ Error fetching offers: {e}")

    def _notify_offer(self, offer: dict, price: float):
        nickname = offer["nickName"]
        min_amount = offer["minAmount"]
        max_amount = offer["maxAmount"]
        completion_rate = offer.get("recentExecuteRate", "N/A")

        message = (
            f"🔥 *New Offer Below €{ALERT_PRICE_THRESHOLD:.2f}*\n\n"
            f"👤 Seller: `{nickname}`\n"
            f"💶 Price: *€{price}* per USDT\n"
            f"📊 Completion: {completion_rate}%\n"
            f"💰 Range: {min_amount} - {max_amount} EUR\n"
            f"[👉 Open P2P](https://www.bybit.com/fiat/trade/otc/buy/USDT/EUR)"
        )

        print(message)
        self.bot.send_message(message)
