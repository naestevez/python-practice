#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 22:49:37 2018

@author: Alex
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
moreThanFive = []

for i in a:
    if i > 5:
        moreThanFive.append(i)
        
print(moreThanFive)
   
#number chosen     
numChosen = int(raw_input("Pick a number:"))

underNum = []

for each_num_array in a:
    if each_num_array < numChosen:
        underNum.append(each_num_array)
        
print(underNum)
        

        

