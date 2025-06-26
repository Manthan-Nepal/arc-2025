import http
import requests

city_name= 'Bhaktapur'
API_key= '3a6ce7b595772436c298d842f43a0200' 
api_url= "http://api.openweathermap.org/geo/1.0/direct?q={city_name},{NP}&limit={2}&appid={API_key}&units=metric"

response= requests.get(api_url)
# if response.status_code == 200:
data= response.json()
print(data)
