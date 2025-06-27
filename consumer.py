# consumer.py

import json
from kafka import KafkaConsumer
from strateji import kontrol_et

def start_consumer():
    consumer = KafkaConsumer(
        'kripto-fiyatlar',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest',
        enable_auto_commit=True
    )

    for msg in consumer:
        data = msg.value
        print(f"📥 Alındı (Kafka): {data}")
        kontrol_et(data)  # strateji.py içinde strateji çalıştırılır
