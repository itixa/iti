#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:19:48 2023

@author: itixa
"""

import random
import string

def generate_password(length):
    """Generate a random password with the given length."""
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.sample to choose `length` characters from the possible characters
    password = ''.join(random.sample(characters, length))

    return password
password = generate_password(10)
print(password)
