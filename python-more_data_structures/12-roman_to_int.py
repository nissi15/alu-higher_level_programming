#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    highest = 0
    for letter in reversed(roman_string):
        value = values.get(letter, 0)
        if value < highest:
            total -= value
        else:
            total += value
            highest = value
    return total
