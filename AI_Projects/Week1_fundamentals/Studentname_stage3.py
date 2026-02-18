name = input("Please enter student name ")
mark1 = int(input("Enter your marks in subject1 "))
mark2 = int(input("Enter your marks in subject2 "))
mark3 = int(input("Enter your marks in subject3 "))
total = mark1+mark2+mark3
percentage = (total/300) * 100
if percentage >= 75:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
elif percentage < 40:
    grade = 'F'
print(f"{name}")
print(f"Total: {total}/300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")