#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:04:29 2018

@author: Alex
"""
import random
import time

print("Let's play a round of rock, paper, scissors!, Ya ready?")
time.sleep(2)
choices = ["rock", "paper", "scissors"]
compChoice = random.choice(choices)

userChoice = raw_input("What will it be? rock, paper or scissors?")
userChoice = userChoice.lower()

if userChoice in choices: #is in choices list:
    if userChoice == compChoice:
        print("There is a tie!")
    elif userChoice == "rock":
        if compChoice == "paper":
            print("I win.")
        elif compChoice == "scissors":
            print("You win.")
    elif userChoice == "paper":
        if compChoice == "rock":
            print("You win.")
        elif compChoice == "scissors":
            print("I win.")
    elif userChoice == "scissors":
        if compChoice == "paper":
            print("You win.")
        elif compChoice == "rock":
            print("I win.")
else:
    print("That is not a valid selection. Please try again.")
