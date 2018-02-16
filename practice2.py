#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 22:25:01 2018

@author: Alex
"""

num = int(input("Give me a number:"))

if num % 4 == 0:
    print("You have chosen a multiple of 4.")
elif num % 2 == 0:
    print("You have chosen an even number.")
elif num % 2 == 1:
    print("You have chosen an odd number.")
else:
    print("That is not a number. Try again.")
    
num1 = int(input("Give me a first number."))
check = int(input("Give me a second number."))

if num1 % check == 0:
    print(num1, "divides evenly into ", check)
else: 
    print(num1, "does not divide evenly into ", check)