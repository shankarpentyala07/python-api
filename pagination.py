import requests

response = requests.get("https://api.github.com/events?per_page=1&page=0")

print(response.json())

response = requests.get("https://api.github.com/events?per_page=1&page=1")

print(response.json())