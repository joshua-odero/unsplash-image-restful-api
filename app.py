from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

# Function to fetch images
def get_photos(category):
    url = "https://api.unsplash.com/search/photos"

    params = {
        "query": category,
        "per_page": 10,
        "client_id": ACCESS_KEY
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print("Error:", response.status_code)
            return []

        data = response.json()
        return data.get("results", [])

    except Exception as e:
        print("Request failed:", e)
        return []


# HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html')


# CATEGORY ROUTE (DYNAMIC)
@app.route('/category/<name>')
def category(name):
    photos = get_photos(name)
    return render_template('gallery.html', photos=photos, category=name)


if __name__ == '__main__':
    app.run(debug=True)