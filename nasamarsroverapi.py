import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2024-01-01"}
response = requests.get(endpoint, params = query_params)
photos = response.json()['photos']
for i in range(len(photos)):
    print("photo",i,photos[i]['img_src'])
