import requests
import json
import os


AUTHOR_ID = "4UlXbpQAAAAJ"  # 你的 Scholar ID

url = "https://serpapi.com/search.json"
params = {
    "engine": "google_scholar_author",
    "author_id": AUTHOR_ID,
    "api_key": '23cf3d2e26cb084b30d44b77776a76970a5c8fedadf6750a337a3c2be747075c'
}

data = requests.get(url, params=params).json()
citations = data["cited_by"]['table'][0]["citations"]['all']

with open("citations.json", "w") as f:
    json.dump({"citations": citations}, f)

print("Citations:", citations)
