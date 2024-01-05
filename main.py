# Random user Generator API - https://randomuser.me/api/

import requests

res = requests.get("https://randomuser.me/api/")
print(res)

#To view actual data 
print(f"Response data: {res.text}")

#Cat API Docs- https://developers.thecatapi.com/
print("Cat API : https://api.thecatapi.com/")


breeds = requests.get("https://api.thecatapi.com/v1/breeds")
print(f"response data : {breeds.text}")

print(f"response status code: {breeds.status_code}")

print(f"response reason: {breeds.reason}")

print(f"response headers: {breeds.headers}")

print(f"response request: {breeds.request}")

request = breeds.request

print(f"response request url : {request.url}")

print(f"response request path url: {request.path_url}")

print(f"response request method: {request.method}")

print(f"response request headers: {request.headers}")

#Custom headers
headers = {"X-Request-Id": "<my-request-id>"}
response = requests.get("https://example.org",headers=headers)
print(f"custom headers: {response.request.headers}")

#Content-Type Image-Charts API
url = "https://image-charts.com/chart?chs=700x125&cht=ls&chd=t:23,15,28"
response = requests.get(url)
print(f'response headers content type {response.headers.get("Content-Type")}')

#Response Content
# .text returns the response contents in Unicode format
# .content returns the response contents in bytes.

response = requests.get("https://api.thecatapi.com/v1/breeds/abys")
print(f'response content type: {response.headers.get("Content-Type")}')
print(f'json response: {response.json()}')
print(f'name is {response.json()["name"]}')

#Response content type: image/png

url = "https://image-charts.com/chart?chs=700x125&cht=ls&chd=t:23,15,28"
response = requests.get(url)

with open("chart.png",mode="wb") as file:
    file.write(response.content)

# Request types
res = requests.post("https://api.thecatapi.com/v1/breeds/abys")
print(res.status_code)

res = requests.get("https://api.thecatapi.com/v1/breeds/abys")
print(res.status_code)

res = requests.put("https://api.thecatapi.com/v1/breeds/abys")
print(res.status_code)

res = requests.delete("https://api.thecatapi.com/v1/breeds/abys")
print(res.status_code)
 

#Query Parameters - With the help of query parameters, you’re able to further narrow 
#your requests and specify exactly what you’re looking for
#1. Get random user
print("Random user details")
print(requests.get("https://randomuser.me/api/").json())

#2.Generate only female random user
print("female random user")
print(requests.get("https://randomuser.me/api/?gender=female").json())

#3.Generate only female random user from Germany
print("female random user from Germany")
print(requests.get("https://randomuser.me/api/?gender=female&nat=de").json())

'''
Using query parameters, you can start fetching more specific data from an API, 
making the whole experience a bit more tailored to your needs.

To avoid having to rebuild the URL over and over again, you can use the params 
attribute to send in a dictionary of all the query parameters to append to a URL
'''
query_params = {"gender": "female", "nat":"de"}
print(requests.get("https://randomuser.me/api/",params=query_params).json())

'''
When you’re reusing the same endpoint, it’s a best practice to define it as a variable at 
the top of your code. This will make your life easier when interacting with an API over and
over again
'''

query_params = {"q": "ragamuffin"}
endpoint = "https://api.thecatapi.com/v1/breeds/search"
print(requests.get(endpoint,params=query_params).json())