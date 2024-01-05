When consuming APIs with Python, there’s only one library you need: requests. With it, you should be able to do most, if not all, of the actions required to consume any public API.

You can install requests by running the following command in your console:

`python -m pip install requests`

Request and Response

Requests contain relevant data regarding your API request call, such as the base URL, the endpoint,
the method used, the headers, and so on.

Responses contain relevant data returned by the server, including the data or content, the status code, and the headers.

Status Codes:
200 OK	                Your request was successful!
201 Created	            Your request was accepted, and the resource was created.
400 Bad Request         Your request is either wrong or missing some information
401 Unauthorized        Your request requires some additional permissions
404 Not Found           The requested resource doesn’t exist.
405 Method Not Allowed  The endpoint doesn’t allow for that specific HTTP method
500 Internal Server Error Your request wasn’t expected and probably broke something on the server side.

HTTP Headers: HTTP headers can define a few parameters governing requests and responses
Accept          What type of content the client can accept
Content-Type    What type of content the server will respond with
User-Agent      What software the client is using to communicate with the server
Server          What software the server is using to communicate with the client
Authentication  Who’s calling the API and what credentials they have

HTTP Methods:

HTTP Method - Description - Requests method
POST    Create a new resource.          requests.post()
GET     Read an existing resource.      requests.get()
PUT     Update an existing resource.    requests.put()
DELETE  Delete an existing resource.    requests.delete()
PATCH   make partial modifications instead of completely replacing a resource using PUT 

Authentication:

Simpler Techniques:
API keys - The most common level of authentication is the API key. These keys are used to identify you as an API user or customer and to trace your use of the API. API keys are typically sent as a request header or as a query parameter

Basic Authentication

Complex and Safer Techniques:
OAuth

Calling API without creds or with the wrong ones returns:

401 - Unauthorized
403 - Forbidden Status

API Page : https://any-api.com/

Reference: https://realpython.com/python-api/#getting-to-know-apis