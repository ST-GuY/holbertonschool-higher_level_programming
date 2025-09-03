#!/usr/bin/python3

def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:  # multiple de 3 et 5
            print("FizzBuzz", end=' ')
        elif a % 3 == 0: # multiple de 3
            print("Fizz", end=' ')
        elif a % 5 == 0: # multiple de 5
            print("Buzz", end=' ')
        else:
            print(a, end=' ')
