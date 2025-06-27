# 💹 Otomatik Kripto Alım-Satım Botu (Python + Kafka + Binance API)

Bu proje, gerçek zamanlı kripto para verilerini analiz ederek, belirli alım-satım stratejilerine göre otomatik emirler veren Python tabanlı bir kripto botudur. Sistem, Binance Testnet üzerinde çalışır, böylece risksiz bir ortamda işlem algoritmaları geliştirilebilir.

---

## 🎯 Proje Amacı

- Gerçek zamanlı kripto fiyatlarını takip etmek  
- Belirli kurallara göre otomatik al/sat işlemleri gerçekleştirmek  
- Gelişmiş, esnek ve modüler bir sistem mimarisi kurmak  
- Gerçek para riski olmadan strateji test etmek

---

![s](https://github.com/user-attachments/assets/f96af9d5-bc28-495f-bb2d-739f9e30add0)


- **producer.py** → Binance'tan canlı BTC fiyatı alır, Kafka’ya yazar  
- **Kafka** → Veriyi asenkron şekilde diğer bileşenlere iletir  
- **consumer.py** → Kafka’dan veriyi alır, strateji modülüne yollar  
- **strateji.py** → Fiyatı kontrol eder, koşul uygunsa emir verir  
- **emir.py** → Binance Testnet API üzerinden market al/sat işlemi gönderir  
- **starter.py** → Producer ve consumer’ı aynı anda başlatır (multithreading)


---

## 🛠️ Kurulum

### 1. Gerekli Kütüphaneleri Yükle

```bash
pip install python-binance kafka-python python-dotenv
```
### 2. .env Dosyası Oluştur

```bash
BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret
```
API anahtarlarını Binance Testnet’ten alabilirsin: https://testnet.binance.vision/


### 3. Kafka Başlat (Docker)

```bash
docker-compose -f docker-compose.yaml up -d
```

### 4. Botu Başlat


```bash
python starter.py
```


### 4. Kullanılan Teknolojiler

| Teknoloji    | Amaç                                        |
| ------------ | ------------------------------------------- |
| Python       | Botun ana motoru ve mantığı                 |
| Binance API  | Piyasa verisi ve emir gönderimi             |
| Apache Kafka | Gerçek zamanlı veri akışı yönetimi          |
| dotenv       | API bilgilerinin gizli tutulması            |
| threading    | Producer ve consumer'ı eşzamanlı çalıştırma |

### 5. Uyarı
- Bu sistem testnet ortamı içindir; gerçek para riski yoktur.

- Gerçek alım-satım yapmadan önce tüm stratejiler test edilmelidir.

- Proje, yatırım tavsiyesi değildir

### 6. Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.







