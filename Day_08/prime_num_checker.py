#!/usr/bin/python3

def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
            break
    if not is_prime or number <= 1:
        print(f'{number} is not prime.')
    else:
        print(f'{number} is a prime.')


n = int(input("Check this number: "))
prime_checker(number=n)
