import requests
import json

url = 'https://catfact.ninja/facts'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  
    pretty_data = json.dumps(data, indent=4)  
    print(pretty_data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
