#! /usr/bin/python
from lib import haze
import numpy
"""
This script renders haze and rain to the driving dataset for optical flow training
Author : Ruoteng LI
Date: 5 Oct 2016
"""

h = haze.Haze()
intensity = 220

contrast = 130
h.set_haze_intensity(contrast)
h.set_rain_intensity(intensity)
left_imagefile = open('data/left.txt', 'r')
right_imagefile = open('data/right.txt', 'r')
left_dispfile = open('data/left_disp.txt', 'r')
right_dispfile = open('data/right_disp.txt', 'r')
left_rainfiles = open('data/left_rain.txt', 'r')
right_rainfiles = open('data/right_rain.txt', 'r')
left_images = left_imagefile.readlines()
right_images = right_imagefile.readlines()
left_disp = left_dispfile.readlines()
right_disp = right_dispfile.readlines()
left_rain = left_rainfiles.readlines()
right_rain = right_rainfiles.readlines()
image_num = len(left_images)

for i in range(0, image_num, 2):
    beta = numpy.random.randint(0,40, size=1)
    for j in range(2):
        print "No. : ", i+j, "beta: ", beta
        h.set_beta(beta)
        left_bg_file = left_images[i+j]
        right_bg_file = right_images[i+j]
        h.set_background(left_bg_file.strip(), right_bg_file.strip())
        left_disp_file = left_disp[i+j]
        right_disp_file = right_disp[i+j]
        h.set_disparity_map(left_disp_file.strip(), right_disp_file.strip())
        left_rain_file = left_rain[i+j]
        right_rain_file = right_rain[i+j]
        h.set_rain_file(left_rain_file.strip(), right_rain_file.strip())
        left_out_file = left_bg_file[0: left_bg_file.find('.png')] + '_rain_haze4.png'
        right_out_file = right_bg_file[0:right_bg_file.find('.png')] + '_rain_haze4.png'
        h.set_all_output(left_out_file, right_out_file)
        h.synthesize_all()
        print left_bg_file, ':', right_bg_file
        print left_out_file, ':', right_out_file


