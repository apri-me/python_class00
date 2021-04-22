from coinex_clinet import CoinexClient


ans = 0
while ans != '3':
    ans = 0
    while ans not in ['1', '2', '3']:
        print("""
        1. Market List
        2. Market Detail
        3. Quite
        """)
        ans = input("Enter the number of your choice: ")
    if ans == '1':
        print(CoinexClient.get_market_list())
    elif ans == '2':
        market_name = input("Enter market name: ")
        print(CoinexClient.get_market_stats(market_name))

print("Khodafez")


