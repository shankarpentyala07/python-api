import requests

endpoint = "https://api.github.com/events"
for i in range(1,100):
    response = requests.get(endpoint)
    print(f"{i} - {response.status_code}")
    if response.status_code != 200:
        print(response.json())
        break