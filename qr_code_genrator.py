#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 12:25:25 2023

@author: itixa
"""

import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4)
qr.add_data("https://www.youtube.com/watch?v=qpaGUAtbZ40")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="white")
img.save("QR_Code.png")