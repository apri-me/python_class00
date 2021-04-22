import requests

r = requests.get("https://api.coinex.com/v1/market/list")
market_dict = r.json()

if market_dict['code'] != 0:
    raise Exception("API error")

data = market_dict['data']

print(data)