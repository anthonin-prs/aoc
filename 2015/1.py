#!/usr/bin/env python3
# coding: utf8
import time
import os

floor_count = 0

floor_count2 = 0
basement_count = 0

input_file = open("1.input", "r")
input_lines = input_file.read().splitlines()

#
# Part 1
#

print("\n -- Part 1 -- \n")

for line in input_lines:
    for char in line:
        if char == "(":
            floor_count += 1
        else:
            floor_count -= 1


print("Floor : "+str(floor_count))

#
# Part 2
#

print("\n -- Part 2 -- \n")

for line in input_lines:
    for char in line:
        basement_count += 1

        if char == "(":
            floor_count2 += 1
        else:
            floor_count2 -= 1

        if floor_count2 == -1:
            print("Achieving basement at char: "+str(basement_count))
            break
