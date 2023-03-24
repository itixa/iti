#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:59:01 2023

@author: itixa
"""

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term
    """
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Example usage
print(fibonacci(20))  # prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
