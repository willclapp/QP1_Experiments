import csv
import re

def make_stims(b_csv, c_csv, output_directory, output_filename):

    exposure_set_string = "let exposure_set_trials = [\n"
    exposure_string = "let exposure_trials = [\n"
    labial_string = "let labial_trials = [\n"
    coronal_string = "let coronal_trials = [\n"
    dorsal_string = "let dorsal_trials = [\n"

    # Do exp strings
    one = "{version: "
    three = ", type: 'audio-keyboard-response', stimulus: '"
    five = "', choices: ['s', 'k'], prompt: '<div class=\"big-container\"><p class=\"exposure-prompt\">"
    seven = "</p><div class=\"yes-no\"><div class=\"option-container\"><p>"
    nine = "</p><p>Press S</p></div><div class=\"option-container\"><p>"
    eleven = "</p><p>Press K</p></div></div></div>', trial_duration: 4000, post_trial_gap: 1000, response_allowed_while_playing: false, "
    twelve = "test_part: 'exposure', correct_response: '"

    # Do trial strings

    a = "{version: "
    b = ", type: 'audio-keyboard-response', stimulus: '"
    c = "', choices: ['s', 'k'], prompt: '<div class=\"big-container\"><div class=\"yes-no\"><div class=\"option-container\"><p>"
    d = "</p><p>Press S</p></div><div class=\"option-container\"><p>"
    e = "</p><p>Press K</p></div></div></div>', trial_duration: 4000, post_trial_gap: 1000, response_allowed_while_playing: false, "
    f = "test_part: 'exposure', correct_response: '"
    
    # HERE GOES FOR NUMBER ZERO --- B-GROUP, YES-LEFT, D-FIRST

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one + "0" + three + line[17] + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_set_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_set_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one + "0" + three + line[17] + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_string += "' }}, \n"
            elif line[12] == 'B':
                labial_string += a + "0" + b + line[17] + c + line[12] + d + line[13] + e
                labial_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                labial_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                labial_string += "' }}, \n"
            elif line[12] == 'D':
                coronal_string += a + "0" + b + line[17] + c + line[12] + d + line[13] + e
                coronal_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                coronal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                coronal_string += "' }}, \n"
            elif line[12] == 'G':
                dorsal_string += a + "0" + b + line[17] + c + line[12] + d + line[13] + e
                dorsal_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                dorsal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                dorsal_string += "' }}, \n"

    # HERE GOES FOR NUMBER TWO --- B-GROUP, YES-RIGHT, D-FIRST

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one + "2" + three + line[17] + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_set_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_set_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one + "2" + three + line[17] + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_string += "' }}, \n"
            elif line[12] == 'B':
                labial_string += a + "2" + b + line[17] + c + line[13] + d + line[12] + e
                labial_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                labial_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                labial_string += "' }}, \n"
            elif line[12] == 'D':
                coronal_string += a + "2" + b + line[17] + c + line[13] + d + line[12] + e
                coronal_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                coronal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                coronal_string += "' }}, \n"
            elif line[12] == 'G':
                dorsal_string += a + "2" + b + line[17] + c + line[13] + d + line[12] + e
                dorsal_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                dorsal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                dorsal_string += "' }}, \n"

    # HERE GOES FOR NUMBER FOUR --- B=GROUP, YES-LEFT, G-FIRST

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one + "4" + three + line[17] + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_set_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_set_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one + "4" + three + line[17] + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_string += "' }}, \n"
            elif line[12] == 'B':
                labial_string += a + "4" + b + line[17] + c + line[12] + d + line[13] + e
                labial_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                labial_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                labial_string += "' }}, \n"
            elif line[12] == 'D':
                coronal_string += a + "4" + b + line[17] + c + line[12] + d + line[13] + e
                coronal_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                coronal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                coronal_string += "' }}, \n"
            elif line[12] == 'G':
                dorsal_string += a + "4" + b + line[17] + c + line[12] + d + line[13] + e
                dorsal_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                dorsal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                dorsal_string += "' }}, \n"

    # HERE GOES FOR NUMBER SIX --- B-GROUP, YES-RIGHT, G-FIRST

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one + "6" + three + line[17] + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_set_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_set_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one + "6" + three + line[17] + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_string += "' }}, \n"
            elif line[12] == 'B':
                labial_string += a + "6" + b + line[17] + c + line[13] + d + line[12] + e
                labial_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                labial_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                labial_string += "' }}, \n"
            elif line[12] == 'D':
                coronal_string += a + "6" + b + line[17] + c + line[13] + d + line[12] + e
                coronal_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                coronal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                coronal_string += "' }}, \n"
            elif line[12] == 'G':
                dorsal_string += a + "6" + b + line[17] + c + line[13] + d + line[12] + e
                dorsal_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                dorsal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                dorsal_string += "' }}, \n"




    # AND THEN HERE ARE ALL THE ONES FOR THE CONTROL GROUP



    # HERE GOES FOR NUMBER ONE --- CONTROL-GROUP, YES-LEFT, D-FIRST

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one + "1" + three + line[17] + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_set_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_set_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one + "1" + three + line[17] + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_string += "' }}, \n"
            elif line[12] == 'B':
                labial_string += a + "1" + b + line[17] + c + line[12] + d + line[13] + e
                labial_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                labial_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                labial_string += "' }}, \n"
            elif line[12] == 'D':
                coronal_string += a + "1" + b + line[17] + c + line[12] + d + line[13] + e
                coronal_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                coronal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                coronal_string += "' }}, \n"
            elif line[12] == 'G':
                dorsal_string += a + "1" + b + line[17] + c + line[12] + d + line[13] + e
                dorsal_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                dorsal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                dorsal_string += "' }}, \n"

    # HERE GOES FOR NUMBER THREE --- CONTROL-GROUP, YES-RIGHT, D-FIRST

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one + "3" + three + line[17] + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_set_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_set_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one + "3" + three + line[17] + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_string += "' }}, \n"
            elif line[12] == 'B':
                labial_string += a + "3" + b + line[17] + c + line[13] + d + line[12] + e
                labial_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                labial_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                labial_string += "' }}, \n"
            elif line[12] == 'D':
                coronal_string += a + "3" + b + line[17] + c + line[13] + d + line[12] + e
                coronal_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                coronal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                coronal_string += "' }}, \n"
            elif line[12] == 'G':
                dorsal_string += a + "3" + b + line[17] + c + line[13] + d + line[12] + e
                dorsal_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                dorsal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                dorsal_string += "' }}, \n"

    # HERE GOES FOR NUMBER FIVE --- B=GROUP, YES-LEFT, G-FIRST

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one + "5" + three + line[17] + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_set_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_set_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one + "5" + three + line[17] + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_string += "' }}, \n"
            elif line[12] == 'B':
                labial_string += a + "5" + b + line[17] + c + line[12] + d + line[13] + e
                labial_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                labial_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                labial_string += "' }}, \n"
            elif line[12] == 'D':
                coronal_string += a + "5" + b + line[17] + c + line[12] + d + line[13] + e
                coronal_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                coronal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                coronal_string += "' }}, \n"
            elif line[12] == 'G':
                dorsal_string += a + "5" + b + line[17] + c + line[12] + d + line[13] + e
                dorsal_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                dorsal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                dorsal_string += "' }}, \n"

    # HERE GOES FOR NUMBER SEVEN --- CONTROL-GROUP, YES-RIGHT, D-FIRST

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one + "7" + three + line[17] + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_set_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_set_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one + "7" + three + line[17] + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                exposure_string += "' }}, \n"
            elif line[12] == 'B':
                labial_string += a + "7" + b + line[17] + c + line[13] + d + line[12] + e
                labial_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                labial_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                labial_string += "' }}, \n"
            elif line[12] == 'D':
                coronal_string += a + "7" + b + line[17] + c + line[13] + d + line[12] + e
                coronal_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                coronal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                coronal_string += "' }}, \n"
            elif line[12] == 'G':
                dorsal_string += a + "7" + b + line[17] + c + line[13] + d + line[12] + e
                dorsal_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                dorsal_string += f + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', path: '" + line[17]
                dorsal_string += "' }}, \n"



    exposure_set_string = exposure_set_string[:-2] + "]"
    exposure_string = exposure_string[:-2] + "]"
    labial_string = labial_string[:-2] + "]"
    coronal_string = coronal_string[:-2] + "]"
    dorsal_string = dorsal_string[:-2] + "]"


    exposure_set_file = open(output_directory + "exposure_set" + output_filename + ".js",'w')
    exposure_set_file.write(exposure_set_string)
    exposure_set_file.close()

    exposure_file = open(output_directory + "exposure" + output_filename + ".js",'w')
    exposure_file.write(exposure_string)
    exposure_file.close()

    labial_file = open(output_directory + "labial" + output_filename + ".js",'w')
    labial_file.write(labial_string)
    labial_file.close()

    coronal_file = open(output_directory + "coronal" + output_filename + ".js",'w')
    coronal_file.write(coronal_string)
    coronal_file.close()

    dorsal_file = open(output_directory + "dorsal" + output_filename + ".js",'w')
    dorsal_file.write(dorsal_string)
    dorsal_file.close()



    print("done")















# _________________________________________________________________________________

b = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/csv/b_group.csv"
c = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/csv/c_group.csv"
out = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/stims/"
f = "_test"

make_stims(b, c, out, f)