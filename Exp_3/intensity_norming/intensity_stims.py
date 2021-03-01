import csv
import re

def make_stims(sine_csv, syll_csv, output_directory):
    sine_1_string = "let sine_1 = [\n"
    sine_2_string = "let sine_2 = [\n"
    sine_response_string = "let sine_response = [\n"

    with open(sine_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            sine_1_string += '{pair: ' + line[0] + ', type: \'audio-keyboard-response\', stimulus: \'' + line[3] + '\', trial_ends_after_audio: true, response_allowed_while_playing: false, post_trial_gap: 250, data: { test_part: \'sine_garbage\'}}, \n'
            sine_2_string += '{pair: ' + line[0] + ', type: \'audio-keyboard-response\', stimulus: \'' + line[4] + '\', trial_ends_after_audio: true, response_allowed_while_playing: false, post_trial_gap: 250, data: { test_part: \'sine_garbage\'}}, \n'
            sine_response_string += '{pair: ' + line[0] + ', type: \'html-keyboard-response\', stimulus: \'<div class="big-container"><div class="yes-no"><div class="option-container"><p>FIRST LOUDER</p><p>Press S</p></div><div class="option-container"><p>SECOND LOUDER</p><p>Press K</p></div></div><div class="same-container"><p>THE SAME</p><p>Space Bar</p></div></div>\', choices: [\'s\', \'k\', \'space\'], trial_duration: 4000, post_trial_gap: 1000, data: {test_part: \'sine\', first_sound: \'' + line[1] + '\', second_sound: \'' + line[2] + '\' }}, \n'

    sine_1_string = sine_1_string[:-3] + "]"
    sine_2_string = sine_2_string[:-3] + "]"
    sine_response_string = sine_response_string[:-3] + "]"
    
    out_sine = sine_1_string + "\n\n" +sine_2_string + "\n\n" + sine_response_string

    sine_out_file = open(output_directory + "sine.js", 'w')
    sine_out_file.write(out_sine)
    sine_out_file.close()

    syll_1_string = "let syll_1 = [\n"
    syll_2_string = "let syll_2 = [\n"
    syll_response_string = "let syll_response = [\n"

    with open(syll_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            syll_1_string += '{pair: ' + line[0] + ', type: \'audio-keyboard-response\', stimulus: \'' + line[3] + '\', trial_ends_after_audio: true, response_allowed_while_playing: false, post_trial_gap: 250, data: { test_part: \'syll_garbage\'}}, \n'
            syll_2_string += '{pair: ' + line[0] + ', type: \'audio-keyboard-response\', stimulus: \'' + line[4] + '\', trial_ends_after_audio: true, response_allowed_while_playing: false, post_trial_gap: 250, data: { test_part: \'syll_garbage\'}}, \n'
            syll_response_string += '{pair: ' + line[0] + ', type: \'html-keyboard-response\', stimulus: \'<div class="big-container"><div class="yes-no"><div class="option-container"><p>FIRST LOUDER</p><p>Press S</p></div><div class="option-container"><p>SECOND LOUDER</p><p>Press K</p></div></div><div class="same-container"><p>THE SAME</p><p>Space Bar</p></div></div>\', choices: [\'s\', \'k\', \'space\'], trial_duration: 4000, post_trial_gap: 1000, data: {test_part: \'syll\', type: \'' + line[6] + '\', first_sound: \'' + line[1] + '\', second_sound: \'' + line[2] + '\' }}, \n'

    syll_1_string = syll_1_string[:-3] + "]"
    syll_2_string = syll_2_string[:-3] + "]"
    syll_response_string = syll_response_string[:-3] + "]"
    
    out_syll = syll_1_string + "\n\n" +syll_2_string + "\n\n" + syll_response_string

    syll_out_file = open(output_directory + "syll.js", 'w')
    syll_out_file.write(out_syll)
    syll_out_file.close()





sine_file = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/intensity_norming/csv/sine.csv"
syll_file = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/intensity_norming/csv/syll.csv"
out = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/intensity_norming/stims/"
make_stims(sine_file, syll_file, out)