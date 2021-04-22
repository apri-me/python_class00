import requests

pars = {
    'market': 'BCHBTC',
    'merge': '0',
}

r = requests.get("https://api.coinex.com/v1/market/depth", params=pars)

content = r.json()
data = content['data']
print(data.keys())