import requests

def make_request(endpoint,params):
    response = requests.get(endpoint,params=params).json()
    return response["data"]