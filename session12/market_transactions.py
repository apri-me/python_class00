import requests

params = {
    'market': 'BCHBTC',
}

url = "https://api.coinex.com/v1/market/deals"

r = requests.get(url, params=params)

print(r.json())