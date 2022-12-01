#!/usr/bin/env python3
# coding: utf8
import time
import os
import numpy

input_file = open("2.input", "r")
input_lines = input_file.read().splitlines()


boxes_size = []
total_size = 0


total_ribbon_size = 0

#
# Part 1
#

print("\n -- Part 1 -- \n")

for line in input_lines:
    text_size = line.split("x")
    box_size = []

    for dim in text_size:
        box_size.append(int(dim))

    boxes_size.append(box_size)

for box in boxes_size:
    box_areas = [(box[0]*box[1]), (box[1]*box[2]), (box[0]*box[2])]
    box_total_area = sum(box_areas)*2 + min(box_areas)
    total_size += box_total_area

print("Paper required: "+str(total_size))


#
# Part 2
#

print("\n -- Part 2 -- \n")

for box in boxes_size:
    box_perimeters = [2*(box[0]+box[1]), 2*(box[1]+box[2]), 2*(box[0]+box[2])]

    ribbon_size = numpy.prod(box) + min(box_perimeters)

    total_ribbon_size += ribbon_size

print("Ribbon required: "+str(total_ribbon_size))
