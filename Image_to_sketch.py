# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:26:02 2022

@author: SaadMuzammil
"""

import cv2
import numpy as np
import scipy.ndimage
import imageio

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.289,0.5870,0.1140])
def dodge(front,back):
    final_sketch = front * 255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back == 255]=255
    return final_sketch.astype('uint8')

image = 'C:/Users/SaadMuzammil/Downloads/BeautyPlus_20190708075307275_save.jpg'
read = imageio.imread(image)
gray = rgb2gray(read)
i = 255-gray    #0,0,0 is for darkest and 255,255,255 for brightest colors

blur = scipy.ndimage.filters.gaussian_filter(i, sigma = 15)   #sigma is the intensity
r = dodge(blur,gray)     #to convert image to a sketch

cv2.imwrite('Saad.png', r)