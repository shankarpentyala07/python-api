import requests

def make_request(endpoint,params):
    response = requests.get(endpoint,params=params)
    return response.json()