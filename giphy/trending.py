
from common.http_utils import make_request
def top_trending_gifs(API_KEY):
    endpoint = "https://api.giphy.com/v1/gifs/trending"
    params = {"api_key": API_KEY, "limit": 3 , "rating": "g"}
    data = make_request(endpoint,params)
    for gif in data:
        title = gif["title"]
        trending_date = gif["trending_datetime"]
        url = gif["url"]
        print(f"{title} | {trending_date}\n{url}\n")