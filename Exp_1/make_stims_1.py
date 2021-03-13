import csv
import re

def make_stims(b_csv, c_csv, p_csv, output_directory, output_filename):

    exposure_set_string = "let exposure_set_trials = [\n"
    exposure_set_response_string = "let exposure_set_response = [\n"
    exposure_string = "let exposure_trials = [\n"
    exposure_response_string = "let exposure_response = [\n"
    BP_string = "let BP_trials = [\n"
    DT_string = "let DT_trials = [\n"
    GK_string = "let GK_trials = [\n"

    # Do exp strings
    one_audio = "{version: "
    two_audio = ", code: "
    three_audio = ", type: 'audio-keyboard-response', stimulus: '"
    five_audio = "', trial_ends_after_audio: true, prompt: '<div class=\"big-container\"><p class=\"exposure-prompt\">"
    seven_audio = "</p><div class=\"yes-no\"><div class=\"option-container\"><p>"
    nine_audio = "</p><p>Press S</p></div><div class=\"option-container\"><p>"
    eleven_audio = "</p><p>Press K</p></div></div></div>', post_trial_gap: 0, response_allowed_while_playing: false, "
    twelve_audio = "test_part: 'exposure_garbage'"


    # Do exp response strings
    one = "{version: "
    two = ", code: "
    three = ", type: \'html-keyboard-response\', choices: ['s', 'k'], stimulus: "
    five = "'<div class=\"big-container\"><p class=\"exposure-prompt\">"
    seven = "</p><div class=\"yes-no\"><div class=\"option-container\"><p>"
    nine = "</p><p>Press S</p></div><div class=\"option-container\"><p>"
    eleven = "</p><p>Press K</p></div></div></div>', trial_duration: 4000, post_trial_gap: 1000, "
    twelve = "test_part: 'exposure', correct_response: '"

    # Do trial strings

    a = "{version: "
    b = ", type: 'audio-keyboard-response', stimulus: '"
    c = "', choices: ['s', 'k'], prompt: '<div class=\"big-container\"><div class=\"yes-no\"><div class=\"option-container\"><p>"
    d = "</p><p>Press S</p></div><div class=\"option-container\"><p>"
    e = "</p><p>Press K</p></div></div></div>', trial_duration: 4000, post_trial_gap: 1000, response_allowed_while_playing: false, "
    f_BP = "test_part: 'BP_test', correct_response: '"
    f_DT = "test_part: 'DT_test', correct_response: '"
    f_GK = "test_part: 'GK_test', correct_response: '"


    # # # # # # # # # # #
    # # # # # # # # # # #
    # # # # # # # # # # #
    # #   B GROUP   # # # 
    # # # # # # # # # # #
    # # # # # # # # # # #
    # # # # # # # # # # #
    
    # HERE GOES FOR NUMBER ZERO --- B-GROUP, DG, YES LEFT

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "0" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "0" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "0" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "0" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "0" + b + line[-2] + c + line[12] + d + line[13] + e
                BP_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "0" + b + line[-2] + c + line[12] + d + line[13] + e
                DT_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "0" + b + line[-2] + c + line[12] + d + line[13] + e
                GK_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"

    # HERE GOES FOR NUMBER THREE--- B-GROUP, DG, YES RIGHT

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "3" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "3" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "3" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "3" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "3" + b + line[-2] + c + line[13] + d + line[12] + e
                BP_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "3" + b + line[-2] + c + line[13] + d + line[12] + e
                DT_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "3" + b + line[-2] + c + line[13] + d + line[12] + e
                GK_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"

    

    # HERE GOES FOR NUMBER SIX --- B-GROUP, GD, YES LEFT

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "6" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "6" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "6" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "6" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "6" + b + line[-2] + c + line[12] + d + line[13] + e
                BP_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "6" + b + line[-2] + c + line[12] + d + line[13] + e
                DT_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "6" + b + line[-2] + c + line[12] + d + line[13] + e
                GK_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"

    

    # HERE GOES FOR NUMBER NINE--- B-GROUP, GD, YES RIGHT

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "9" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "9" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "9" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "9" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "9" + b + line[-2] + c + line[13] + d + line[12] + e
                BP_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "9" + b + line[-2] + c + line[13] + d + line[12] + e
                DT_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "9" + b + line[-2] + c + line[13] + d + line[12] + e
                GK_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"

    


    # # # # # # # # # # #
    # # # # # # # # # # #
    # # # # # # # # # # #
    # CONTROL GROUP # # # 
    # # # # # # # # # # #
    # # # # # # # # # # #
    # # # # # # # # # # #


    # HERE GOES FOR NUMBER ONE --- CONTROL, DG, YES LEFT

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "1" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "1" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "1" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "1" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "1" + b + line[-2] + c + line[12] + d + line[13] + e
                BP_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "1" + b + line[-2] + c + line[12] + d + line[13] + e
                DT_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "1" + b + line[-2] + c + line[12] + d + line[13] + e
                GK_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"


    # HERE GOES FOR NUMBER FOUR --- CONTROL, DG, YES RIGHT

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "4" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "4" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "4" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "4" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "4" + b + line[-2] + c + line[13] + d + line[12] + e
                BP_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "4" + b + line[-2] + c + line[13] + d + line[12] + e
                DT_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "4" + b + line[-2] + c + line[13] + d + line[12] + e
                GK_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"


    # HERE GOES FOR NUMBER SEVEN --- CONTROL, GD, YES LEFT

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "7" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "7" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "7" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "7" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "7" + b + line[-2] + c + line[12] + d + line[13] + e
                BP_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "7" + b + line[-2] + c + line[12] + d + line[13] + e
                DT_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "7" + b + line[-2] + c + line[12] + d + line[13] + e
                GK_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"

    
    # HERE GOES FOR NUMBER TEN --- CONTROL, GD, YES RIGHT

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "10" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "10" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "10" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "10" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "10" + b + line[-2] + c + line[13] + d + line[12] + e
                BP_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "10" + b + line[-2] + c + line[13] + d + line[12] + e
                DT_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "10" + b + line[-2] + c + line[13] + d + line[12] + e
                GK_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"


    # # # # # # # # # # #
    # # # # # # # # # # #
    # # # # # # # # # # #
    # #   P GROUP   # # # 
    # # # # # # # # # # #
    # # # # # # # # # # #
    # # # # # # # # # # #


    # HERE GOES FOR NUMBER TWO --- CONTROL, DG, YES LEFT

    with open(p_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "2" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "2" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "2" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "2" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "2" + b + line[-2] + c + line[12] + d + line[13] + e
                BP_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "2" + b + line[-2] + c + line[12] + d + line[13] + e
                DT_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "2" + b + line[-2] + c + line[12] + d + line[13] + e
                GK_string += "data: { yes_side: 'LEFT', block_order: 'DG', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"


    # HERE GOES FOR NUMBER FIVE --- CONTROL, DG, YES RIGHT

    with open(p_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "5" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "5" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "5" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "5" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "5" + b + line[-2] + c + line[13] + d + line[12] + e
                BP_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "5" + b + line[-2] + c + line[13] + d + line[12] + e
                DT_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "5" + b + line[-2] + c + line[13] + d + line[12] + e
                GK_string += "data: { yes_side: 'RIGHT', block_order: 'DG', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"


    # HERE GOES FOR NUMBER EIGHT --- CONTROL, GD, YES LEFT

    with open(p_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "8" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "8" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "8" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "8" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "8" + b + line[-2] + c + line[12] + d + line[13] + e
                BP_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "8" + b + line[-2] + c + line[12] + d + line[13] + e
                DT_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "8" + b + line[-2] + c + line[12] + d + line[13] + e
                GK_string += "data: { yes_side: 'LEFT', block_order: 'GD', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"

    
    # HERE GOES FOR NUMBER ELEVEN --- CONTROL, GD, YES RIGHT

    with open(p_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "11" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "11" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "11" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "11" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[2] == 'BP_test':
                BP_string += a + "11" + b + line[-2] + c + line[13] + d + line[12] + e
                BP_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                BP_string += f_BP + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                BP_string += "' }}, \n"
            elif line[2] == 'DT_test':
                DT_string += a + "11" + b + line[-2] + c + line[13] + d + line[12] + e
                DT_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                DT_string += f_DT + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                DT_string += "' }}, \n"
            elif line[2] == 'GK_test':
                GK_string += a + "11" + b + line[-2] + c + line[13] + d + line[12] + e
                GK_string += "data: { yes_side: 'RIGHT', block_order: 'GD', "
                GK_string += f_GK + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                GK_string += "' }}, \n"



    exposure_set_string = exposure_set_string[:-3] + "]"
    exposure_set_response_string = exposure_set_response_string[:-3] + "]"
    exposure_string = exposure_string[:-2] + "]"
    exposure_response_string = exposure_response_string[:-2] + "]"
    BP_string = BP_string[:-3] + "]"
    DT_string = DT_string[:-3] + "]"
    GK_string = GK_string[:-3] + "]"

    exposure_set_file = open(output_directory + "exposure_set" + output_filename + ".js",'w')
    exposure_set_file.write(exposure_set_string)
    exposure_set_file.close()

    exposure_set_response_file = open(output_directory + "exposure_set_response" + output_filename + ".js",'w')
    exposure_set_response_file.write(exposure_set_response_string)
    exposure_set_response_file.close()

    exposure_file = open(output_directory + "exposure" + output_filename + ".js",'w')
    exposure_file.write(exposure_string)
    exposure_file.close()

    exposure_response_file = open(output_directory + "exposure_response" + output_filename + ".js",'w')
    exposure_response_file.write(exposure_response_string)
    exposure_response_file.close()

    BP_file = open(output_directory + "BP" + output_filename + ".js",'w')
    BP_file.write(BP_string)
    BP_file.close()

    DT_file = open(output_directory + "DT" + output_filename + ".js",'w')
    DT_file.write(DT_string)
    DT_file.close()

    GK_file = open(output_directory + "GK" + output_filename + ".js",'w')
    GK_file.write(GK_string)
    GK_file.close()

    print("done")





# _________________________________________________________________________________

b = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_1/csv/b_group.csv"
c = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_1/csv/c_group.csv"
p = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_1/csv/p_group.csv"
out = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_1/stims/"
f = ""

make_stims(b, c, p, out, f)