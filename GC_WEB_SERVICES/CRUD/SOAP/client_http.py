import requests

url = "http://localhost:8000/say_hello"
params = {"name": "GCARNAB HTTP", "times": 3}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")

