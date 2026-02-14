numbers = input("Enter the list of numbers separated by spaces")
nums = numbers.split()
int_nums = []
for num in nums:
    int_nums.append(int(num))
highest = int_nums[0]
for index,num in enumerate(int_nums):
    if int_nums[index] > highest:
        highest = int_nums[index]
print(f"Maximum value : {highest}")
print(f"Position : {index}")