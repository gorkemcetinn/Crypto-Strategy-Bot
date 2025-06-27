from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'  # Testnet endpoint

def market_buy(symbol="BTCUSDT", miktar=0.001):
    try:
        order = client.order_market_buy(
            symbol=symbol,
            quantity=miktar
        )
        print(f"✅ ALIM EMRİ GÖNDERİLDİ: {order}")
        return order
    except Exception as e:
        print(f"❌ ALIM hatası: {e}")

def market_sell(symbol="BTCUSDT", miktar=0.001):
    try:
        order = client.order_market_sell(
            symbol=symbol,
            quantity=miktar
        )
        print(f"✅ SATIM EMRİ GÖNDERİLDİ: {order}")
        return order
    except Exception as e:
        print(f"❌ SATIM hatası: {e}")
