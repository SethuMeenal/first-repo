def is_prime_number():
    num = 17
    for i in range(1,17,1):
        rem = num // i
        if (rem == 0):
            print(f"{num} is not a prime number")
            break
        else:
            print(f"{num} is a prime number")
        break
is_prime_number()