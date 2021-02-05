'''
This is fun little experiment of mine (i wanted to learn stego with python but ended up doing this),
this takes two arguments one green screen image and other background and then gives the combined image as a result.

Requirements:
matplotlib
pillow
tk
opencv-python
numpy

'''

#!/usr/bin/env python

from  matplotlib import pyplot as plt
import matplotlib.image as mimg
import numpy as np
import cv2
import sys

try:
    green_img = sys.argv[1]
    bg_img = sys.argv[2]
except:
    print("you dumbfuck UwU")
#green_img = input("enter file for green image")
#bg_img = input("enter file for bg image")
img = mimg.imread(green_img)
bg = mimg.imread(bg_img)

print("dimensions for green_img {}",img.shape)
print("dimensions for green_img {}",bg.shape)

width = img.shape[1]
height = img.shape[0]

bg_resize = cv2.resize(bg,(width,height))
low = np.array([0,180,0])
up = np.array([100,255,100])

mask = cv2.inRange(img,low,up)
masked_image = np.copy(img)
masked_image[mask != 0]=[0,0,0]
bgr_image = bg_resize.copy()
final_image = bgr_image + masked_image
plt.imshow(final_image)
plt.show()
