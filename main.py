import requests
import time
from datetime import datetime

api_url = 'https://api.binance.com/api/v3/ticker/price'

coin_list = ['BTC', 'ETH', 'LTC', 'DF', 'CVP', 'COS', 'COCOS', 'AVAX', 'JOE', 'DEGO', 'ERN', 'HIGH', 'TVK', 'TLM', 'LOKA', 'VOXEL', 'MANA', 'SAND', 'ENJ', 'AXS', 'SLP', 'LUNA', 'ANC', 'MIR', 'PORTO', 'LAZIO', 'ALPINE', 'ATM', 'ACM', 'PSG', 'CITY', 'OG', 'ASR', 'SANTOS', 'PERL', 'PNT']

busd_coin_list = ['SNM', 'VIB', 'PROS', 'AERGO','ONE', 'CELR', 'SFP', 'C98', 'TWT', 'WING', 'BOND', 'SHIB', 'DOGE', 'AUTO', 'BIFI', 'GAS', 'NEO', 'QUICK', 'FARM', 'JST', 'SUN']

while True:
    for coin in coin_list:
        params = {'symbol': coin + 'USDT'}
        response = requests.get(api_url, params=params)
        data = response.json()
        price = float(data['price'])
        # print(f"{datetime.now()} - {coin} fiyatı: {price}")

        # Son 3 dakika içinde fiyat artışı %3'ten fazla mı?
        klines_url = 'https://api.binance.com/api/v3/klines'
        klines_params = {'symbol': coin + 'USDT', 'interval': '3m', 'limit': 1}
        klines_response = requests.get(klines_url, params=klines_params)
        klines_data = klines_response.json()
        prev_close_price = float(klines_data[0][4])
        price_diff = (price - prev_close_price) / prev_close_price

        if price_diff > 0.015:
            percent_change = price_diff * 100
            print(f"{datetime.now()} - {coin} fiyatı son 3 dakika içinde %{percent_change:.2f} artış gösterdi! Yeni fiyat: {price}")

    for coin in busd_coin_list:
        try:
            params = {'symbol': coin + 'BUSD'}
            response = requests.get(api_url, params=params)
            data = response.json()
            price = float(data['price'])
            # print(f"{datetime.now()} - {coin} fiyatı: {price}")

            # Son 3 dakika içinde fiyat artışı %3'ten fazla mı?
            klines_url = 'https://api.binance.com/api/v3/klines'
            klines_params = {'symbol': coin + 'BUSD', 'interval': '3m', 'limit': 1}
            klines_response = requests.get(klines_url, params=klines_params)
            klines_data = klines_response.json()
            prev_close_price = float(klines_data[0][4])
            price_diff = (price - prev_close_price) / prev_close_price
            if price_diff > 0.015:
                percent_change = price_diff * 100
                print(f"{datetime.now()} - {coin} fiyatı son 3 dakika içinde %{percent_change:.2f} artış gösterdi! Yeni fiyat: {price}")

        except KeyError:
            print(f"{datetime.now()} - {coin} fiyatı alınamadı. Sonraki döngüde tekrar denenecek.")

    time.sleep(30) # 30 saniye bekleyin
