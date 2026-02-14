#numbers = [5, 2, 8, 2, 9, 2, 1, 2]
nums = input("Please enter any list to search the target number")
numbers = []
num = nums.split()
for nums in num:
    numbers.append(int(nums))
target = int(input(f"Please enter target number to search in the list"))
result_list = []
for index,num in enumerate(numbers):
    if num == target:
        result_list.append(index)
print(f"Value {target} found at positions: {result_list}")