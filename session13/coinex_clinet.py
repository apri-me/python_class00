import requests

class CoinexClient:
    BASE_URL = "https://api.coinex.com/v1/"
    @classmethod
    def get_request(cls, path, **kwarg):
        url = cls.BASE_URL + path
        response = requests.get(url, kwarg)
        r_dict = response.json()
        if r_dict['code'] != 0:
            raise Exception("API Error code {}: {}".format(r_dict['code'], r_dict['message']))
        return r_dict['data']
    
    @classmethod
    def get_market_list(cls):
        return cls.get_request('market/list')

    @classmethod
    def get_market_stats(cls, m):
        return cls.get_request('market/ticker', market=m)

    @classmethod
    def get_all_market_stats(cls):
        return cls.get_request('market/ticker/all')