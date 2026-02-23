import json
inven = dict()
with open("inventory.json","r") as file:
    inven = json.load(file)
for line in inven:
    print(f"Title: {line['title']} | Author: {line['author']} | Price: ${line['price']} | In-Stock: {line['in_stock']}")
