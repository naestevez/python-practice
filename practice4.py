#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 23:25:31 2018

@author: Alex
"""
list = []
num = int(raw_input("Pick a number: "))

for i in range(1, num + 1):
    if num % i == 0:
        list.append(i)
    
print(list)
        