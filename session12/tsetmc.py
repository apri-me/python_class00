import requests

response = requests.get("https://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0", verify=False)

with open("xl.xlsx", "wb") as f:
    f.write(response.content)
    