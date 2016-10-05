#! /usr/bin/python
import haze
"""
haze_iteration.py
This script use iteration to systematically render haze and rain on the background images with different parameters
Author: Ruoteng Li
Date: 5 Oct 2016
"""

h = haze.Haze()
intensity = 220
h.set_rain_intensity(intensity)

for beta in range(0, 200, 5):
    h.set_beta(beta)
    for contrast in range(120, 201, 5):
        print "beta: ", beta
        print "haze intensity: ", contrast

        h.set_haze_intensity(contrast)

        left_file = 'out/render_haze_left_' + 'beta' + str(beta) + 'contrast' + str(contrast) + '.png'
        right_file = 'out/render_haze_right_' + 'beta' + str(beta) + 'contrast' + str(contrast) + '.png'
        # h.set_haze_output(left_file, right_file)
        # h.synthesize_haze()
        h.set_all_output(left_file, right_file)
        h.synthesize_all()
