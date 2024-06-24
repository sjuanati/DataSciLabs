import os
import json
import requests
from sp500 import sp500
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

# indices = ['JCI','DFS','HOLX', 'MKC', 'TRMB'] # require longer time window (10:00 AM - 17:00 PM)
# indices = ["TYL"]  # require longer time window (10:00 AM - 17:00 PM)
indices = sp500


def show_ask_bid(symbol):
    start_time = 1718877600000000000  # 10:00 AM
    end_time = 1718902800000000000    # 17:00 PM

    url = f"https://api.polygon.io/v3/quotes/{symbol}?timestamp.gte={start_time}&timestamp.lte={end_time}&order=desc&limit=1&sort=timestamp&apiKey={api_key}"
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

def show_ask_bid_v2(symbol):
    # Define the time window for fetching quotes
    start_time = 1718877600000000000  # 10:00 AM (exclude open volatility)
    end_time = 1718899200000000000    # 16:00 PM (exclude close volatility)
    
    # Define the API URL with ascending sort and increased limit
    url = f"https://api.polygon.io/v3/quotes/{symbol}?timestamp.gte={start_time}&timestamp.lte={end_time}&order=asc&limit=50000&sort=timestamp&apiKey={api_key}"
    response = requests.get(url)
    # print(json.dumps(response.json(), indent=4))

    if response.status_code == 200:
        data = response.json().get("results", [])
        
        # Force same bid/ask exchanges; otherwise, spread can be too high
        filtered_data = [item for item in data if item.get('ask_exchange') == item.get('bid_exchange')]

        if filtered_data:
            ask_price = filtered_data[0]['ask_price']
            bid_price = filtered_data[0]['bid_price']
            return ask_price, bid_price
        else:
            print(f"No data found for {symbol} same bid/ask exchange")
    else:
        print(
            f"API call failed for {symbol} with status code: {response.status_code}"
        )
    
    return None, None

import requests

def show_ask_bid_v3(symbol):
    # Define the time window for fetching quotes
    start_time = 1718877600000000000  # 10:00 AM (exclude open volatility)
    end_time = 1718899200000000000    # 16:00 PM (exclude close volatility)
    
    # Define the API URL with ascending sort and increased limit
    url = f"https://api.polygon.io/v3/quotes/{symbol}?timestamp.gte={start_time}&timestamp.lte={end_time}&order=asc&limit=50000&sort=timestamp&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get("results", [])
        
        min_diff = float('inf')
        best_record = None
        
        for item in data:
            ask_price = item.get('ask_price')
            bid_price = item.get('bid_price')
            
            # Ensure both prices are available and valid (greater than zero)
            if ask_price is not None and bid_price is not None and ask_price > 0 and bid_price > 0:
                price_diff = ask_price - bid_price
                
                # Check if the difference is less than 1 and non-negative
                if 0 <= price_diff < 1:
                    return ask_price, bid_price
                
                # Otherwise, track the record with the smallest non-negative difference
                if 0 <= price_diff < min_diff:
                    min_diff = price_diff
                    best_record = (ask_price, bid_price)
        
        if best_record:
            return best_record
        else:
            print(f"No suitable data found for {symbol} with close ask/bid prices.")
    else:
        print(f"API call failed for {symbol} with status code: {response.status_code}")
    
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

    # ask_price, bid_price = show_ask_bid(symbol)
    # ask_price, bid_price = show_ask_bid_v2(symbol)
    ask_price, bid_price = show_ask_bid_v3(symbol)
    avg_volume = show_avg_volume(symbol)
    market_cap = show_market_cap(symbol)

    if ask_price and bid_price and avg_volume and market_cap:
        print(f"{symbol},{bid_price},{ask_price},{avg_volume},{market_cap}")
    else:
        print(f"Incomplete data for {symbol}.")
