import requests

params = {
    'market': 'BCHBTC'
}

r = requests.get("https://api.coinex.com/v1/market/ticker", params=params)


market_dict = r.json()

if market_dict['code'] != 0:
    raise Exception("API error")

data = market_dict['data']
# print(data)
date = data['date']
# ticker = data['ticker']
# print()
print(date)
# print()
# print(ticker)
# print()
# print(ticker['buy'])

high = data['ticker']['high']
print(float(high))