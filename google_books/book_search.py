from common.http_utils import make_request

def search_book(search_term):
    endpoint = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": search_term , "maxResults": 3}
    response = make_request(endpoint,params)
    for book in response["items"]:
        volume = book["volumeInfo"]
        title = volume["title"]
        published = volume["publishedDate"]
        description = volume["description"]
        info_link = volume["infoLink"]
        print(f"{title} ({published})\n{description}\n")
        print(f"Link : {info_link}\n")

