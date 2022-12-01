#!/usr/bin/env python3
# coding: utf8
import time
import os

input_file = open("3.input", "r")
input_lines = input_file.read().splitlines()

current_location = [0, 0]
locations_visited = [[0, 0]]

#
# Part 1
#

print("\n -- Part 1 -- \n")

for line in input_lines:
    for char in line:
        if char == "^":
            current_location[1] += 1
        elif char == "v":
            current_location[1] -= 1
        elif char == ">":
            current_location[0] += 1
        elif char == "<":
            current_location[0] -= 1

        if current_location not in locations_visited:
            locations_visited.append(current_location.copy())

print("Gifts : "+str(len(locations_visited)))

#
# Part 2
#

is_santa = 1

current_location = [[0, 0], [0, 0]]
locations_visited = [[[0, 0]], [[0, 0]]]

total_locations = []

print("\n -- Part 2 -- \n")

for line in input_lines:
    for char in line:
        if char == "^":
            current_location[is_santa][1] += 1
        elif char == "v":
            current_location[is_santa][1] -= 1
        elif char == ">":
            current_location[is_santa][0] += 1
        elif char == "<":
            current_location[is_santa][0] -= 1

        if current_location[is_santa] not in locations_visited[is_santa]:
            locations_visited[is_santa].append(
                current_location[is_santa].copy())

        if is_santa == 1:
            is_santa = 0
        else:
            is_santa = 1

total_locations = locations_visited[0].copy()

for location in locations_visited[1]:
    if location not in total_locations:
        total_locations.append(location)

print("Total houses: "+str(len(total_locations)))
