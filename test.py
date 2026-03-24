""" This script is for testing whether we can fetch data from Unsplash API """

import requests

url = "https://api.unsplash.com/search/photos"
category = "nature"

params = {
    "query": category,
    "per_page": 10,
    "client_id": "ACCESS_KEY" #use your own access key
}

response = requests.get(url, params=params)

data = response.json()

#Track the status code of the response
print(response.status_code)

#Track the rate limit of the requests
print(response.headers)
#print(data)

    