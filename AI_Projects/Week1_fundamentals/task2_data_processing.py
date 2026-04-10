import json
import pandas as pd
import os
with open("C:/Users/sethum/data/TrendPulse.json","r") as f:
    data = json.load(f)
rows = list()
for keys,values in data.items():
    for value in values:
        rows.append({"post_id":value.get("post_id"),
                    "title":value.get("title"),
                    "category": keys,
                    "score":value.get("score"),
                    "num_comments":value.get("num_comments"),
                    "author":value.get("author"),
                    "collected_at":value.get("collected_at")
                    })
df = pd.DataFrame(rows)
print(f"number of rows is {len(df)}")
df = df.drop_duplicates(subset = ['post_id'])
print(f"dropped duplicates based on post id. curr length is  {len(df)}")
#print(f"null check: {df.isnull().sum()}")
df = df.dropna(subset = ['title','score','post_id'])
print(f"dropped rows with nulls in either title or score or post id. curr length is {len(df)}")
df['score'] = pd.to_numeric(df['score'],errors='coerce').astype('Int64')
print(f"Converted score into int {df['score'].dtype}")
df['num_comments'] = pd.to_numeric(df['num_comments'],errors='coerce').astype('Int64')
print(f"Converted num_comments into int {df['num_comments'].dtype}")
df = df[df['score']> 5]
#print(df.head(5))
df["title"] = df["title"].str.replace(r"\s+", " ", regex=True).str.strip()
new_file = df.to_csv("data/TrendPulseConverted.csv",index = False)
print("CSV saved at:", os.path.abspath("data/TrendPulse.csv"), "with ", len(df) ,"rows")
print(f"number of stories per category is {df.groupby('category').size()}")
