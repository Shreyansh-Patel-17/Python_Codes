def prime(number):
    if number <= 1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
    
user_input= int(input("Enter a number: "))
if prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")