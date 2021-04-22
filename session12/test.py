from time import sleep
import requests

dates = []
for i in range(2):
    params = {
        'market': 'BCHBTC'
    }
    r = requests.get("https://api.coinex.com/v1/market/ticker", params=params)
    market_dict = r.json()
    dates.append(market_dict['data']['date'])
    sleep(1)

print(dates[1]-dates[0])
