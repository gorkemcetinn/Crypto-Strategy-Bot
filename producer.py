import json
import time
from kafka import KafkaProducer
from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

# API KEY gerekli değil sadece fiyat almak için
client = Client()

def get_binance_price(symbol="BTCUSDT"):
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        return float(ticker['price'])
    except Exception as e:
        print(f"❌ Binance fiyat hatası: {e}")
        return None

def start_producer():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    while True:
        price = get_binance_price()
        if price:
            data = {
                'symbol': 'BTC',
                'price': price,
                'timestamp': time.time()
            }
            producer.send('kripto-fiyatlar', value=data)
            print(f"📤 Binance gönderildi: {data}")
        time.sleep(5)
