#!/usr/bin/env python3
# coding: utf8
import time
import os

elf_table = []
cal_count = 0

input_file = open("1.input", "r")
input_lines = input_file.read().splitlines()

#
# Part 1
#

print("\n -- Part 1 -- \n")

for line in input_lines:
    if line == "":
        elf_table.append(cal_count)
        cal_count = 0
    else:
        cal_count += int(line)


max_cal = max(elf_table)
max_cal_index = elf_table.index(max_cal)

print("Max cal : "+str(max_cal))
print("At position: "+str(max_cal_index))

#
# Part 2
#

print("\n -- Part 2 -- \n")

elf_table_sorted = elf_table.copy()
elf_table_sorted.sort(reverse=True)

top3_cal = sum(elf_table_sorted[:3])

print("Top 3 calories: "+str(top3_cal))
