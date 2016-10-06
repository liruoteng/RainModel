#! /usr/bin/python
from lib import haze

"""
This script renders haze and rain to the driving dataset for optical flow training
Author : Ruoteng LI
Date: 5 Oct 2016
"""

h = haze.Haze()
intensity = 220
beta = 5
contrast = 130
h.set_beta(beta)
h.set_haze_intensity(contrast)
h.set_rain_intensity(intensity)
left_imagefile = open('data/left.txt', 'r')
right_imagefile = open('data/right.txt', 'r')
left_images = left_imagefile.readlines()
right_images = right_imagefile.readlines()
image_num = len(left_images)

for i in range(image_num):
    left_bg_file = left_images[i]
    right_bg_file = right_images[i]
    h.set_background(left_bg_file.strip(), right_bg_file.strip())
    left_out_file = left_bg_file[0: left_bg_file.find('.png')] + '_haze.png'
    right_out_file = right_bg_file[0:right_bg_file.find('.png')] + '_haze.png'
    h.set_haze_output(left_out_file, right_out_file)
    h.synthesize_haze()
    print left_bg_file, ':', right_bg_file
    print left_out_file, ':', right_out_file


