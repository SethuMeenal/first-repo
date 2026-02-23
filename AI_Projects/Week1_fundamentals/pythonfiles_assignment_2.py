import json
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
with open("inventory.json","r") as file:
    inven = json.load(file)
inven.append(new_book)
with open("inventory.json","w") as file:
    json.dump(inven,file,indent = 4)