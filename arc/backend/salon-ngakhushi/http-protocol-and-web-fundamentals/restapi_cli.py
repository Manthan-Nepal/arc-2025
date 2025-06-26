import requests

response= requests.get("https://reqres.in/api/users/2")

if response.status_code== 200:
    post= response.json()['data']
    print(f"Name: {user['first_name']}")
    print(f"Email: {user['email']}")
else:
    print("Fetching failed.")
    