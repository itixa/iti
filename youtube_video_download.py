#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:08:09 2023

@author: itixa
"""

from pytube import YouTube

# Input the YouTube video URL
url = input("Enter the video URL: ")

# Create a YouTube object with the URL
yt = YouTube(url)

# Get the first stream with the highest resolution
stream = yt.streams.get_highest_resolution()

# Download the video
print("Downloading...")
stream.download()
print("Download complete!")
