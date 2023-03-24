#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:17:17 2023

@author: itixa
"""

import requests
import random
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia "random article" page
url = "https://en.wikipedia.org/wiki/Special:Random"

# Send a GET request to the URL
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# Extract the title of the article from the parsed HTML
title = soup.find("title").text

# Print the title of the article
print(title)
