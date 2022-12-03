#!/usr/bin/env python3

# A = Rock; B = paper; C = Scissors
# X = Rock; Y = Paper; Z = Scissors
# Loss = 0; Draw = 3; Win = 6
# Rock = 1; Paper = 2; Scissors = 3

import time

dic_1 = {
    "AX" : 4,
    "AY" : 8,
    "AZ" : 3,
    "BX" : 1,
    "BY" : 5,
    "BZ" : 9,
    "CX" : 7,
    "CY" : 2,
    "CZ" : 6
}

# A = Rock; B = paper; C = Scissors
# X = Lose; Y = Draw; Z = Win
# Loss = 0; Draw = 3; Win = 6
# Rock = 1; Paper = 2; Scissors = 3

dic_2 = {
    "AX" : 3,
    "AY" : 4,
    "AZ" : 8,
    "BX" : 1,
    "BY" : 5,
    "BZ" : 9,
    "CX" : 2,
    "CY" : 6,
    "CZ" : 7
}

def open_file(filePath):
    with open(filePath, "r") as f:
        values = f.readlines()
    return values

def check_points(data, dic):
    points = 0
    for i in data:
        i = i.replace(" ", "")
        i = i.replace("\n", "")
        mPoints = dic[i]
        points += mPoints
    return points

tm = time.time()

first_answer = check_points(open_file("input.txt"), dic_1)
second_answer = check_points(open_file("input.txt"), dic_2)

tm2 = time.time()

print(f"The first answer is {first_answer}")
print(f"The second answer is {second_answer}")
print(f"The time was {tm2 - tm}")
