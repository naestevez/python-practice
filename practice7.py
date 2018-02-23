#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 08:11:42 2018

@author: Alex
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print "list a: ", a

#uses list comprehension to assign even numbers from list a to list b then print
b = [i for i in a if i % 2 == 0] 
print "list b: ", b
