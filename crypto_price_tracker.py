import requests

def fetch_cryptocurrency_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching cryptocurrency prices.")
        return None

def display_prices(prices):
    if prices:
        print("Cryptocurrency Prices (USD):")
        for currency, value in prices.items():
            print(f"{currency.capitalize()}: ${value['usd']}")
    else:
        print("No prices to display.")

if __name__ == "__main__":
    prices = fetch_cryptocurrency_prices()
    display_prices(prices)
