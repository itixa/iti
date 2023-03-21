#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:41:44 2023

@author: itixa
"""

import random

secret_number = random.randint(1, 100)
guess = None
num_guesses = 0

while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    num_guesses += 1
    
    if guess < secret_number:
        print("Too low, try again!")
    elif guess > secret_number:
        print("Too high, try again!")
    else:
        print(f"Congratulations, you guessed the number in {num_guesses} tries!")
