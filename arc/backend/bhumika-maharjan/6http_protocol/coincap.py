import requests
import json

API_URL = 'https://openapiv1.coinstats.app/coins/bitcoin'

API_KEY = 'FuX7eBZaHW1Ar34u9x8BokqbtwLFwa4Vx5E317FwSd8='

COIN_INFO= 'coins.json'

def get_bitcoin_price():
    headers = {
        'X-API-KEY': API_KEY
    }
    
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        with open(COIN_INFO, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")

def main():
    print("Fetching Bitcoin price from CoinStats API...")
    get_bitcoin_price()

if __name__ == "__main__":
    main()
