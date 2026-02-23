#task-1
import json
#with open("inventory.json","r") as file:
#     count_lines = 0
#     for line in file:
#         count_lines += 1
# the above method only counts the raw lines in the file (based on format, not based on Data/books in it, so pls find the alternative in line 11)
with open("inventory.json","r") as file:        
    inventory = dict()
    inventory = json.load(file)
    count_lines = len(inventory)
#testing whether the dictionary has acquired the right data in it
# print(f"title of 1st book in dictionary: {inventory[0]["title"]}")    
print(f"number of lines in inventory dictionary: {count_lines}")