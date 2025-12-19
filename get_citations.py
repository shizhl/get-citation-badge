from scholarly import scholarly
import json

USER_ID = "4UlXbpQAAAAJ"   # 换成你的 Scholar ID

author = scholarly.search_author_id(USER_ID)
author = scholarly.fill(author)

citations = author["citedby"]

with open("citations.json", "w") as f:
    json.dump({"citations": citations}, f)

print("Citations:", citations)
