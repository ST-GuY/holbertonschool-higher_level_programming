#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    value = [roman[char] for char in roman_string]

    sum = 0

    for i in range(len(value)):
        if i + 1 < len(value) and value[i] < value[i + 1]:
            sum -= value[i]
        else:
            sum += value[i]
    return sum
