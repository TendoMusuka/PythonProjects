# Author : Rutendo Musuka
# Purpose : Checks if input number is a prime number

def prime_checker(number1):
    prime_number = True
    for num in range(2, number1):
        if number1 % num == 0:
            print("It is not a prime number")
            return None
    print("It is a prime number")


number = input("Hello! Give me a number and I will tell you if it is a prime number or not.\n")
prime_checker(int(number))
