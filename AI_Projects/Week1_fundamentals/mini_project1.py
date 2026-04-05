import requests
import json
import time
from datetime import datetime
import os
# import certifi


url1 = 'https://hacker-news.firebaseio.com/v0/topstories.json'
headers = {"User-Agent": "TrendPulse/1.0"}

category = {
    "technology": ["AI","software","tech","code","computer","data","cloud","API","GPU","LLM"],
    "worldnews": ["war","government","country","president","election","climate","attack","global"],
    "sports": ["NFL","NBA","FIFA","sport","game","team","player","league","championship"],
    "science": ["research","study","space","physics","biology","discovery","NASA","genome"],
    "entertainment": ["movie","film","music","Netflix","game","book","show","award","streaming"]
}

new_result = {cat: [] for cat in category.keys()}

# Fetch top story IDs
id_responses = requests.get(url1, headers=headers)
if id_responses.status_code != 200:
    print("Issue - notified in API success code")
else:
    print("Success")
    responses = id_responses.json()[:500]
    print(responses)
    for response in responses:
        url2 = f'https://hacker-news.firebaseio.com/v0/item/{response}.json'
        try:
            story_responses = requests.get(url2, headers=headers, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching url")
            continue

        if story_responses.status_code != 200:
            print("2ndIssue - notified in API success code")
            continue

        s_responses = story_responses.json()
        if not s_responses or "title" not in s_responses:
            continue

        tit_low = s_responses.get("title", "").lower()
        curr_timestamp = datetime.now().isoformat()
        got_match = None

        # Match category
        for key, value_list in category.items():
            for value in value_list:
                if value.lower() in tit_low:
                    got_match = key
                    break
            if got_match:
                break

        # Append story if matched
        if got_match and len(new_result[got_match]) < 25:
            new_result[got_match].append({
                "post_id": s_responses.get("id"),
                "title": s_responses.get("title"),
                "category": got_match,
                "score": s_responses.get("score"),
                "num_comments": s_responses.get("descendants"),
                "author": s_responses.get("by"),
                "collected_at": curr_timestamp
            })
            print(f"Collected story in {got_match}: {s_responses.get('title')}")
            if len(new_result[got_match]) == 25:
                print(f"Done collecting for {got_match}")

        #time.sleep(2)

# Save results
os.makedirs("data", exist_ok=True)
with open("data/TrendPulse.json", "w", encoding="utf-8") as f:
    json.dump(new_result, f, indent=2)

print("File saved at:", os.path.abspath("data/TrendPulse.json"))