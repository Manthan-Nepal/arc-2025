import requests
import json

API_Key= '4a296d83-1d86-452d-88b2-bd9b19665d1b'
url= "  /v1/cryptocurrency/quotes/latest"

headers= {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_Key
}

params= {
    'symbol': 'BTC',
    'convert': 'NPR'
}

response= requests.get(url, headers= headers, params=params)
data= response.json()
price= data['data']['BTC']['quote']['NPR']['price']
print(f"Bitcoin Price: Nrs.{price:,.2f}")

def save_response():
    bitcoin={
        'Crypto': 'BTC',
        'Short for': 'Bitcoin',
        'Current Pricing in NPR': price
    }
    with open("bitcoinprice.json", "w") as file:
        json.dump(bitcoin, file, indent=4)
        
saveprice= input("Would you like to save this pricing?(y/n): ")
if saveprice=='y':
    save_response()
    print("The price has been saved.")
else:
    exit()
