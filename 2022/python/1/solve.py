#!/usr/bin/env python3

def read_input():
    with open("input.txt", "r") as f:
        data = f.readlines()
    return data

def print_data(data):
    for i in data:
        print(i)

def sum_data(data):
    sums = []
    current_sum = 0
    for i in data:
        if i != "\n":
            n = int(i.replace("\n", ""))
            current_sum += n
        if i == "\n":
            sums.append(current_sum)
            current_sum = 0
    return sums

def biggest_sums_f(sums):
    in_order = []
    for i in sums:
        bc = max(sums)
        in_order.append(bc)
        sums.remove(bc)
    return in_order

data_x = sum_data(read_input())
x = max(data_x)
biggest_sums = biggest_sums_f(data_x)
y = biggest_sums[0] + biggest_sums[1] + biggest_sums[2]
print(f"First answer = {x}")
print(f"Second answer = {y}")
