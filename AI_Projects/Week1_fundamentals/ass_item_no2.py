names = ["Alice","Bob","Emily","David","Sarah"]
result_names = []
for name in names:
    if(name.startswith('A') or name.startswith('E') or name.startswith('I') or name.startswith('O') or name.startswith('U')):
        result_names.append(name)
count_of_result = len(result_names)
print(f"Names starting with vowels: {count_of_result}")