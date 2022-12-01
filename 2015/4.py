#!/usr/bin/env python3
# coding: utf8
import time
import os
import hashlib

i = 0

input_file = open("4.input", "r")
input_lines = input_file.read().splitlines()


#
# Part 1
#

print("\n -- Part 1 -- \n")

for line in input_lines:
    while True:
        string = line+str(i)
        hasher = hashlib.md5(string.encode())
        hash = hasher.hexdigest()
        if (hash[:5] == "00000"):
            print("Validation number: "+str(i))
            print(string+" validate it with MD5 hash of: "+hash)
            break
        i += 1


#
# Part 2
#

print("\n -- Part 2 -- \n")

for line in input_lines:
    while True:
        string = line+str(i)
        hasher = hashlib.md5(string.encode())
        hash = hasher.hexdigest()
        if (hash[:6] == "000000"):
            print("Validation number: "+str(i))
            print(string+" validate it with MD5 hash of: "+hash)
            break
        i += 1
