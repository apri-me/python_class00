import requests

r = requests.get("https://api.coinex.com/v1/market/ticker/all")
market_stats = r.json()['data']['ticker']

