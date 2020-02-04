#!/usr/bin/env python

#import matplotlib.pyplot as plt
from  matplotlib import pyplot as plt
import matplotlib.image as mimg
import numpy as np
import cv2

img = mimg.imread("green_imag.jpg")
bg = mimg.imread("bg.jpg")

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
#plt.imshow(masked_image)
bgr_image = bg_resize.copy()
#plt.imshow(bgr_image)
final_image = bgr_image + masked_image
plt.imshow(final_image)
