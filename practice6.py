#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 23:02:40 2018

@author: Alex
"""

word = raw_input("Give me a word:")
string = list(word)
reversedString = []


print string

for c in reversed(string):
    reversedString.append(c)
    
print reversedString

if string == reversedString:
    print "Congratulations, " + word + " is a palindrome!"
else:
    print "The word you chose is not a palindrome."