""" This script is for testing whether we can fetch data from Unsplash API """

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url = "https://api.unsplash.com/search/photos"
category = "nature"
ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

params = {
    "query": category,
    "per_page": 10,
    "client_id": ACCESS_KEY
 #use your own access key
}

response = requests.get(url, params=params)

data = response.json()

#Track the status code of the response
#print(response.status_code)

#Track the rate limit of the requests
#print(response.headers)
print(data)

    