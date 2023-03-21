#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:20:11 2023

@author: itixa
"""

import random

# Define the characters and their traits
characters = [
    {'name': 'Alice', 'gender': 'female', 'age': 25},
    {'name': 'Bob', 'gender': 'male', 'age': 30},
    {'name': 'Charlie', 'gender': 'male', 'age': 40},
    {'name': 'Diana', 'gender': 'female', 'age': 28},
    {'name': 'Eve', 'gender': 'female', 'age': 35}
]

# Define the plot points
plot_points = [
    "A stranger appears",
    "A mystery needs to be solved",
    "A new opportunity arises",
    "A conflict arises between two characters",
    "A character must make a difficult decision"
]

# Choose a random character and plot point
character = random.choice(characters)
plot_point = random.choice(plot_points)

# Generate the story
story = f"{character['name']} is a {character['gender']} character who is {character['age']} years old.\n"
story += f"{plot_point} and {character['name']} is faced with a difficult situation.\n"
story += f"{character['name']} must make a decision that will change their life forever."

print(story)
