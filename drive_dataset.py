#! /usr/bin/python
import haze
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


print "beta: ", beta
print "haze intensity: ", contrast

h.set_haze_intensity(contrast)

left_file = 'out/render_haze_left_' + 'beta' + str(beta) + 'contrast' + str(contrast) + '.png'
right_file = 'out/render_haze_right_' + 'beta' + str(beta) + 'contrast' + str(contrast) + '.png'
# h.set_haze_output(left_file, right_file)
# h.synthesize_haze()
h.set_all_output(left_file, right_file)
h.synthesize_all()
