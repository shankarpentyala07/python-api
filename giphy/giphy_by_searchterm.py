
from common.http_utils import make_request
def gify_by_word(search_term,API_KEY):
    endpoint = "https://api.giphy.com/v1/gifs/search"
    params = {"api_key": API_KEY, "limit": 1 , "q": search_term, "rating": "g"}
    data = make_request(endpoint,params)
    for gif in data:
        title = gif["title"]
        url = gif["url"]
        print(f"{title} | {url}")