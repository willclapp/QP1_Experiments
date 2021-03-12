import csv
import re

def make_stims(b_csv, c_csv, output_directory, output_filename):

    exposure_set_string = "let exposure_set_trials = [\n"
    exposure_set_response_string = "let exposure_set_response = [\n"
    exposure_string = "let exposure_trials = [\n"
    exposure_response_string = "let exposure_response = [\n"
    onset_string = "let onset_trials = [\n"
    coda_string = "let coda_trials = [\n"

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
    f_onset = "test_part: 'test_onset', correct_response: '"
    f_coda = "test_part: 'test_coda', correct_response: '"
    
    # HERE GOES FOR NUMBER ZERO --- B-GROUP, ONSET-FIRST, YES LEFT

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "0" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "0" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'onset-coda', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "0" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "0" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'onset-coda', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[1] == 'test_onset':
                onset_string += a + "0" + b + line[-2] + c + line[12] + d + line[13] + e
                onset_string += "data: { yes_side: 'LEFT', block_order: 'onset-coda', "
                onset_string += f_onset + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                onset_string += "' }}, \n"
            elif line[1] == 'test_coda':
                coda_string += a + "0" + b + line[-2] + c + line[12] + d + line[13] + e
                coda_string += "data: { yes_side: 'LEFT', block_order: 'onset-coda', "
                coda_string += f_coda + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                coda_string += "' }}, \n"

    # HERE GOES FOR NUMBER TWO--- B-GROUP, ONSET-FIRST, YES RIGHT

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "2" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "2" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'onset-coda', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "2" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "2" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'onset-coda', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[1] == 'test_onset':
                onset_string += a + "2" + b + line[-2] + c + line[13] + d + line[12] + e
                onset_string += "data: { yes_side: 'RIGHT', block_order: 'onset-coda', "
                onset_string += f_onset + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                onset_string += "' }}, \n"
            elif line[1] == 'test_coda':
                coda_string += a + "2" + b + line[-2] + c + line[13] + d + line[12] + e
                coda_string += "data: { yes_side: 'RIGHT', block_order: 'onset-coda', "
                coda_string += f_coda + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                coda_string += "' }}, \n"

    # HERE GOES FOR NUMBER FOUR --- B-GROUP, CODA-FIRST, YES LEFT

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "4" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "4" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'coda-onset', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "4" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "4" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'coda-onset', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[1] == 'test_onset':
                onset_string += a + "4" + b + line[-2] + c + line[12] + d + line[13] + e
                onset_string += "data: { yes_side: 'LEFT', block_order: 'coda-onset', "
                onset_string += f_onset + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                onset_string += "' }}, \n"
            elif line[1] == 'test_coda':
                coda_string += a + "4" + b + line[-2] + c + line[12] + d + line[13] + e
                coda_string += "data: { yes_side: 'LEFT', block_order: 'coda-onset', "
                coda_string += f_coda + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                coda_string += "' }}, \n"

    # HERE GOES FOR NUMBER TWO--- B-GROUP, ONSET-FIRST, YES RIGHT

    with open(b_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "6" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "6" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'coda-onset', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "6" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "6" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'coda-onset', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[1] == 'test_onset':
                onset_string += a + "6" + b + line[-2] + c + line[13] + d + line[12] + e
                onset_string += "data: { yes_side: 'RIGHT', block_order: 'coda-onset', "
                onset_string += f_onset + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                onset_string += "' }}, \n"
            elif line[1] == 'test_coda':
                coda_string += a + "6" + b + line[-2] + c + line[13] + d + line[12] + e
                coda_string += "data: { yes_side: 'RIGHT', block_order: 'coda-onset', "
                coda_string += f_coda + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                coda_string += "' }}, \n"


    # # # # # # # # # # #
    # # # # # # # # # # #
    # # # # # # # # # # #
    # CONTROL GROUP # # # 
    # # # # # # # # # # #
    # # # # # # # # # # #
    # # # # # # # # # # #


    # HERE GOES FOR NUMBER ONE --- CONTROL, ONSET-FIRST, YES LEFT

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "1" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "1" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'onset-coda', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "1" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "1" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'onset-coda', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[1] == 'test_onset':
                onset_string += a + "1" + b + line[-2] + c + line[12] + d + line[13] + e
                onset_string += "data: { yes_side: 'LEFT', block_order: 'onset-coda', "
                onset_string += f_onset + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                onset_string += "' }}, \n"
            elif line[1] == 'test_coda':
                coda_string += a + "1" + b + line[-2] + c + line[12] + d + line[13] + e
                coda_string += "data: { yes_side: 'LEFT', block_order: 'onset-coda', "
                coda_string += f_coda + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                coda_string += "' }}, \n"

    # HERE GOES FOR NUMBER THREE --- CONTROL, ONSET-FIRST, YES RIGHT

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "3" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "3" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'onset-coda', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "3" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "3" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'onset-coda', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[1] == 'test_onset':
                onset_string += a + "3" + b + line[-2] + c + line[13] + d + line[12] + e
                onset_string += "data: { yes_side: 'RIGHT', block_order: 'onset-coda', "
                onset_string += f_onset + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                onset_string += "' }}, \n"
            elif line[1] == 'test_coda':
                coda_string += a + "3" + b + line[-2] + c + line[13] + d + line[12] + e
                coda_string += "data: { yes_side: 'RIGHT', block_order: 'onset-coda', "
                coda_string += f_coda + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                coda_string += "' }}, \n"

    # HERE GOES FOR NUMBER FIVE --- CONTROL, CODA-FIRST, YES LEFT

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "5" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "5" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_set_response_string += "data: { yes_side: 'LEFT', block_order: 'coda-onset', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "5" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[14] + nine_audio + line[15] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "5" + two + line[-1] + three + five + line[8] + seven + line[14] + nine + line[15] + eleven
                exposure_response_string += "data: { yes_side: 'LEFT', block_order: 'coda-onset', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[1] == 'test_onset':
                onset_string += a + "5" + b + line[-2] + c + line[12] + d + line[13] + e
                onset_string += "data: { yes_side: 'LEFT', block_order: 'coda-onset', "
                onset_string += f_onset + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                onset_string += "' }}, \n"
            elif line[1] == 'test_coda':
                coda_string += a + "5" + b + line[-2] + c + line[12] + d + line[13] + e
                coda_string += "data: { yes_side: 'LEFT', block_order: 'coda-onset', "
                coda_string += f_coda + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                coda_string += "' }}, \n"

    # HERE GOES FOR NUMBER SEVEN --- CONTROL, ONSET-FIRST, YES RIGHT

    with open(c_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if line[1] == 'exposure_set':
                exposure_set_string += one_audio + "7" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_set_string += " }, \n"
                exposure_set_response_string += one + "7" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_set_response_string += "data: { yes_side: 'RIGHT', block_order: 'coda-onset', "
                exposure_set_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_set_response_string += "' }}, \n"
            elif line[1] == 'exposure':
                exposure_string += one_audio + "7" + two_audio + line[-1] + three_audio + line [-2] + five_audio + " " + seven_audio + line[15] + nine_audio + line[14] + eleven_audio + twelve_audio
                exposure_string += " }, \n"
                exposure_response_string += one + "7" + two + line[-1] + three + five + line[8] + seven + line[15] + nine + line[14] + eleven
                exposure_response_string += "data: { yes_side: 'RIGHT', block_order: 'coda-onset', "
                exposure_response_string += twelve + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                exposure_response_string += "' }}, \n"
            elif line[1] == 'test_onset':
                onset_string += a + "7" + b + line[-2] + c + line[13] + d + line[12] + e
                onset_string += "data: { yes_side: 'RIGHT', block_order: 'coda-onset', "
                onset_string += f_onset + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                onset_string += "' }}, \n"
            elif line[1] == 'test_coda':
                coda_string += a + "7" + b + line[-2] + c + line[13] + d + line[12] + e
                coda_string += "data: { yes_side: 'RIGHT', block_order: 'coda-onset', "
                coda_string += f_coda + line[9] + "', group: '" + line[0] + "', type: '" + line[2] + "', audio: '" + line[3] + "', vowel: '" + line[4] + "', visual_target: '" + line[8] + "', repetition: '" + line[10] + "', normed_midpoint: '" + line[11] + "', voiced_sel: '" + line[12] + "', voiceless_sel: '" + line[13] + "', match_sel: '" + line[14] + "', mismatch_sel: '" + line[15] + "', step: '" + line[16] + "', tone_step: '" + line[17] + "', path: '" + line[-2]
                coda_string += "' }}, \n"


    



    exposure_set_string = exposure_set_string[:-3] + "]"
    exposure_set_response_string = exposure_set_response_string[:-3] + "]"
    exposure_string = exposure_string[:-2] + "]"
    exposure_response_string = exposure_response_string[:-2] + "]"
    onset_string = onset_string[:-3] + "]"
    coda_string = coda_string[:-3] + "]"

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

    onset_file = open(output_directory + "onset" + output_filename + ".js",'w')
    onset_file.write(onset_string)
    onset_file.close()

    coda_file = open(output_directory + "coda" + output_filename + ".js",'w')
    coda_file.write(coda_string)
    coda_file.close()

    print("done")





# _________________________________________________________________________________

b = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/csv/b_group.csv"
c = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/csv/c_group.csv"
out = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_3/stims/"
f = ""

make_stims(b, c, out, f)