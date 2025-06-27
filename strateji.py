# strateji.py

from emir import market_buy, market_sell

ALIM_SEVIYESI = 107423  # 107000 altına inerse al
SATIM_SEVIYESI = 108000  # 108000 üstüne çıkarsa sat

MİKTAR = 0.001
symbol_binance = "BTCUSDT"

def kontrol_et(data):
    fiyat = data['price']
    print(f"🎯 Fiyat kontrolü: {fiyat} USD")

    if fiyat < ALIM_SEVIYESI:
        print(f"🟢 Şart sağlandı: ALIM → {fiyat}")
        market_buy(symbol=symbol_binance, miktar=MİKTAR)

    elif fiyat > SATIM_SEVIYESI:
        print(f"🔴 Şart sağlandı: SATIM → {fiyat}")
        market_sell(symbol=symbol_binance, miktar=MİKTAR)

    else:
        print("⚪ Koşul sağlanmadı, bekleniyor...")
