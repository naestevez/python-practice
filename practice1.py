#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 22:13:54 2018

@author: Alex
"""
import datetime


name = raw_input("What's your name?")
age = raw_input("What's your age?")
yearsLeftTill100 = 100 - int(age)

now = datetime.datetime.now()
yearWhen100 = now.year + yearsLeftTill100

num = raw_input("Give me a number")
num = int(num)

for i in range(num):
    print("You will have %d more birthdays until you reach 100, which means that will be in %d! \n" % (yearsLeftTill100, yearWhen100) )
    