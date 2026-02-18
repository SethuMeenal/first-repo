num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
opr = input("Enter the operation you want to do. It could be possible +, - , *, /: ")
if (opr == '+'):
    result = num1 + num2
elif(opr == '-'):
    result = num1 - num2
elif(opr == '*'):
    result = num1 * num2
elif(opr == '/'):
    if num2 == 0:
        print(f"Any number can't be divided by zero")
    else:
        result = num1 / num2
        if (num1 % num2 == 0):
            result = int(result)
print(f"Result = {result}")
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")