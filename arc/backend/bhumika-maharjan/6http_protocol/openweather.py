import requests
import json

API_KEY = "8704dc6613e365a2b4b63833d539af04"
CITY = 'Kathmandu'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent = 4))
else:
    print("Error fetching data:", response.status_code)
