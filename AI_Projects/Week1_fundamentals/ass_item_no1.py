numbers = (input("Enter your list of numbers to find average"))
nums = numbers.split()
# print(f"contents of list nums are {nums}")
total = 0
int_nums = []
for num in nums:
    int_nums.append(int(num))
# print(f"content of list int numbers are {int_nums}")
total = sum(int_nums)
# print(f"total: {total}")
length_of_input = len(int_nums)
# print(f"len: {length_of_input}")
average = int(total/len(int_nums))
print(f"Average score: {average}")