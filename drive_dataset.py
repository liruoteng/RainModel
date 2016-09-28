import haze


h = haze.Haze()

for beta in range(1, 21):
    print beta
    h.set_beta(beta)
    left_file = 'out/render_haze_left_' + str(beta) + '.png'
    right_file = 'out/render_haze_right_' + str(beta) + '.png'
    h.set_haze_output(left_file, right_file)
    h.synthesize_haze()
#    h.set_all_output(left_file, right_file)
#   h.synthesize_all()
