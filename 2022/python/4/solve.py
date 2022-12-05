#!/usr/bin/env python3

def read_file():
    with open("input.txt", 'r') as f:
        data = f.readlines()
    return data

def solve_1(a, b, x ,y):
    if a <= x and b >= y:
        return 1
    elif x <= a and y >= b:
        return 1
    else:
        return 0

def solve_2(a, b, x, y):
    if a <= x and b >= y:
        return 1
    if x <= a and y >= b:
        return 1
    if x <= b and x >= a:
        return 1
    if b <= x and a >= x:
        return 1
    if y >= a and y <= b:
        return 1
    if a >= y and b <= y:
        return 1
    if a == y:
        return 1
    return 0

def solve(data):
    s1 = 0
    s2 = 0
    for i in data:
        digits = i.replace("\n", "").split(',')
        a, b, x, y = [int(digit) for digit in digits[0].split('-')] + [int(digit) for digit in digits[1].split('-')]
        s1 += solve_1(a, b, x, y)
        s2 += solve_2(a, b, x, y)

    return(s1, s2)

solve = solve(read_file())
print(f"The first answer was {solve[0]}")
print(f"The second answer was {solve[1]}")
