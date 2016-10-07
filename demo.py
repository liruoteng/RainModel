#! /usr/bin/python
from lib import haze
"""
Run haze/rain rendering on the background image with default settings.
Author : Ruoteng Li
Date   : 5 Oct 2016
"""

# Initialize haze model object
haze_object = haze.Haze()
# Parameter set up as followed
# haze_object.set_beta(65)
# haze_object.set_noise_param(0, 10)
# Generate haze rendered output
haze_object.synthesize_haze()
# Generate rain rendered output
haze_object.synthesize_rain()
# Generate rain and haze both rendered output
haze_object.synthesize_all()
