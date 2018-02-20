#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 23:36:06 2018

@author: Alex
"""
import random
import numpy as np

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = sorted(a)
b = sorted(b)

list = []

for numA in a:
    for numB in b:
        if numA in b:
            list.append(numA)
        
list = set(list)     
            
print(list)

#Generate two random lists

numofElements = random.randint(1,21)
numofElements2 = random.randint(1,21)

list1 = []
list2 = []
sharedNums = []

for i in range(numofElements):
    list1.append(random.randint(1, 101))
    list1 = sorted(list1)
    
for i in range(numofElements2):
    list2.append(random.randint(1, 101))
    list2 = sorted(list2)
    
    
for num1 in list1:
    for num2 in list2:
        if num1 in list2:
            sharedNums.append(num1)
    
print sharedNums
    
    


