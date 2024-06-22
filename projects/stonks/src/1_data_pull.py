import os
import json
import requests
from sp500 import sp500
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

# indices = ['JCI','DFS','HOLX', 'MKC', 'TRMB'] # require longer time window (10:00 AM - 17:00 PM)
indices = sp500


def show_ask_bid(symbol):
    # 10:00 AM - 10:30 AM
    # url = f"https://api.polygon.io/v3/quotes/{symbol}?timestamp.gte=1718877600000000000&timestamp.lte=1718879400000000000&order=desc&limit=1&sort=timestamp&apiKey={api_key}"
    # A few stonks didn't have bid/ask during certain periods, so extending range
    # 10:00 AM - 17:00 AM
    url = f"https://api.polygon.io/v3/quotes/{symbol}?timestamp.gte=1718877600000000000&timestamp.lte=1718902800000000000&order=desc&limit=5000&sort=timestamp&apiKey={api_key}"
    response = requests.get(url)
    # print(json.dumps(response.json(), indent=4))
    if response.status_code == 200 and response.json()["results"]:
        data = response.json()["results"][0]
        return data["ask_price"], data["bid_price"]
    else:
        print(
            f"Ask/Bid data not available or API call failed for {symbol} with status code: {response.status_code}"
        )
    return None, None


def show_avg_volume(symbol):
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2024-06-07/2024-06-21?adjusted=true&sort=asc&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if len(results) == 10:
            total_volume = sum(item["v"] for item in results)
            avg_volume = total_volume / 10
            return avg_volume
        else:
            print(
                f"Volume data count mismatch for {symbol}. Expected 10, got {len(results)}"
            )
    else:
        print(
            f"Volume data API call failed for {symbol}. Status code: {response.status_code}"
        )
    return None


def show_market_cap(symbol):
    url = f"https://api.polygon.io/v3/reference/tickers/{symbol}?date=2024-06-20&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results", {})
        if "market_cap" in results:
            return results["market_cap"]
        else:
            print(f"Market cap data missing for {symbol}.")
    else:
        print(
            f"Market cap API call failed for {symbol}. Status code: {response.status_code}"
        )
    return None


print("stonk,bid_price,ask_price,avg_vol_10d,market_cap")
for symbol in indices:
    ask_price, bid_price = show_ask_bid(symbol)
    avg_volume = show_avg_volume(symbol)
    market_cap = show_market_cap(symbol)
    if ask_price and bid_price and avg_volume and market_cap:
        print(f"{symbol},{bid_price},{ask_price},{avg_volume},{market_cap}")
    else:
        print(f"Incomplete data for {symbol}.")
