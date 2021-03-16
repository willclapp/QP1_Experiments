
// NEW

//          ORDER           YES_SIDE    GROUP
// 0        onset_coda      LEFT        EXP
// 1        onset_coda      LEFT        CON
// 2        onset_coda      RIGHT       EXP
// 3        onset_coda      RIGHT       CON
// 4        coda_onset      LEFT        EXP
// 5        coda_onset      LEFT        CON
// 6        coda_onset      RIGHT       EXP
// 7        coda_onset      RIGHT       CON


let timeline = [];

let irb = {
    type: 'html-button-response',
    stimulus: '<div class ="irb"><img src="imgs/SUSig_2color_Stree_Stacked_Left.png" alt="Stanford University Logo" class="logo"><p id="legal"><font size="3">We invite you to participate in a research study on language production and comprehension. Your experimenter will ask you to do a linguistic task such as reading sentences or words, naming pictures or describing scenes, making up sentences of your own, or participating in a simple language game. <br><br>There are no risks or benefits of any kind involved in this study. <br><br>You will be paid for your participation at the posted rate.<br><br>If you have read this form and have decided to participate in this experiment, please understand your participation is voluntary and you have the right to withdraw your consent or discontinue participation at anytime without penalty or loss of benefits to which you are otherwise entitled. You have the right to refuse to do particular tasks. Your individual privacy will be maintained in all published and written data resulting from the study. You may print this form for your records.<br><br>CONTACT INFORMATION: If you have any questions, concerns or complaints about this research study, its procedures, risks and benefits, you should contact the Protocol Director Meghan Sumner at (650)-725-9336. If you are not satisfied with how this study is being conducted, or if you have any concerns, complaints, or general questions about the research or your rights as a participant, please contact the Stanford Institutional Review Board (IRB) to speak to someone independent of the research team at (650)-723-2480 or toll free at 1-866-680-2906. You can also write to the Stanford IRB, Stanford University, 3000 El Camino Real, Five Palo Alto Square, 4th Floor, Palo Alto, CA 94306 USA.<br><br>If you agree to participate, please proceed to the study tasks.</font></p></div>',
    choices: ['Continue']
};

timeline.push(irb);

let general_instructions = {
    type: 'html-keyboard-response',
    stimulus: `<div class="gen_ins"><p>In this experiment, you will hear recordings and will make simple decisions about them.<br><br>IMPORTANT: Please only accept this task if you are listening through headphones and working in a quiet environment.<br><br>Press the space bar to continue.</p></div>`,
    choices: ['space']
};

//

timeline.push(general_instructions);


let left_instructions = {
    type: 'html-keyboard-response',
    stimulus: `<div class="spec_ins"><p>This experiment has two parts. In this first part, you will see a printed word, and then hear a spoken word.  Sometimes the printed and spoken words will be the same (see FASHION; hear <em>fashion</em>); other times the printed and spoken words will be different (see FASHION; hear <em>turkey</em>).<br><br>YOUR JOB: Decide whether the printed and spoken words are the SAME or DIFFERENT. To do this, place your fingers on the S and K keys. <br><br>If the words are the SAME press the S key.<br><br>If the words are DIFFERENT, press the K key.<br><br>Please answer as quickly and accurately as possible.<br><br>A response cannot be made until the audio has played entirely. Once a selection is made, the slide will advance after a brief pause. If no response is made after several seconds, the slide will advance automatically.<br><br>Please press the space bar to begin.</p></div>`,
    choices: ['space']
};

let right_instructions = {
    type: 'html-keyboard-response',
    stimulus: `<div class="spec_ins"><p>This experiment has two parts. In this first part, you will see a printed word, and then hear a spoken word.  Sometimes the printed and spoken words will be the same (see FASHION; hear <em>fashion</em>); other times the printed and spoken words will be different (see FASHION; hear <em>turkey</em>).<br><br>YOUR JOB: Decide whether the printed and spoken words are DIFFERENT or the SAME. To do this, place your fingers on the S and K keys.<br><br>If the words are DIFFERENT press the S key.<br><br>If the words are the SAME, press the K key.<br><br>Please answer as quickly and accurately as possible.<br><br>A response cannot be made until the audio has played entirely. Once a selection is made, the slide will advance after a brief pause. If no response is made after several seconds, the slide will advance automatically.<br><br>Please press the space bar to begin.</p></div>`,
    choices: ['space']
};


if (v_no < 2 | v_no === 4 | v_no === 5) {
    timeline.push(left_instructions);
} else {
    timeline.push(right_instructions)
}

// EXPOSURE STIMULI

for (i = 0; i < exposure_set_trials.length; i++) {
// for (i = 0; i < 16; i++) {
    if (exposure_set_trials[i].version === v_no) {
        timeline.push(exposure_set_trials[i])
        for (j = 0; j < exposure_set_trials.length; j++) {
            if (exposure_set_trials[i].code === exposure_set_response[j].code && exposure_set_response[j].version === v_no) {
                timeline.push(exposure_set_response[j])
            }
        }
    }
}

for (i = 0; i < exposure_trials.length; i++) {
// for (i = 0; i < 80; i++) {
    if (exposure_trials[i].version === v_no) {
        timeline.push(exposure_trials[i])
        for (j = 0; j < exposure_trials.length; j++) {
            if (exposure_trials[i].code === exposure_response[j].code && exposure_response[j].version === v_no) {
                timeline.push(exposure_response[j])
            }
        }
    }
}

// TEST INSTRUCTIONS

let onset_first_instructions = {
    type: 'html-keyboard-response',
    stimulus: '<div class="pre-test-container"><p>Great Job! You finished the first part of the Experiment!<br><br>In the second part of the experiment, you will hear the talker say syllables, like <em>ba</em> or <em>pa</em> Your job is to tell us what the first sound of each syllable is.<br><br> You will hear a lot of syllables that sound quite similar.<br><br>Do your best, and respond as quickly and accurately as you can, identifying the first sound of the syllable.<br><br>Please place your fingers again on the S and K buttons, and follow the prompts to make your choices.<br><br>Press the space bar to continue.</p></div>',
    choices: ['space'],
    post_trial_gap: 1000
}

let coda_first_instructions = {
    type: 'html-keyboard-response',
    stimulus: '<div class="pre-test-container"><p>Great Job! You finished the first part of the Experiment!<br><br>In the second part of the experiment, you will hear the talker say syllables, like <em>ahb</em> or <em>ahp</em> Your job is to tell us what the last sound of each syllable is.<br><br> You will hear a lot of syllables that sound quite similar.<br><br>Do your best, and respond as quickly and accurately as you can, identifying the last sound of the syllable.<br><br>Please place your fingers again on the S and K buttons, and follow the prompts to make your choices.<br><br>Press the space bar to continue.</p></div>',
    choices: ['space'],
    post_trial_gap: 1000
}
let coda_second_instructions = {
    type: 'html-keyboard-response',
    stimulus: '<div class="pre-test-container"><p>In the next round, you\'ll hear single syllables again. You can expect to hear syllables like <em>ahb</em> or <em>ahp</em>.<br><br>Select the sound that ended the syllable by pressing S or K.<br><br>Press the space bar to continue.</p></div>',
    choices: ['space'],
    post_trial_gap: 1000
}

let onset_second_instructions = {
    type: 'html-keyboard-response',
    stimulus: '<div class="pre-test-container"><p>In the next round, you\'ll hear single syllables again. You can expect to hear syllables like <em>pa</em> or <em>ba</em>.<br><br>Select the sound that started the syllable by pressing S or K.<br><br>Press the space bar to continue.</p></div>',
    choices: ['space'],
    post_trial_gap: 1000
}


if (v_no < 4) {
    timeline.push(onset_first_instructions)
} else {
    timeline.push(coda_first_instructions)
}

// FIRST BLOCK

if (v_no < 4) {
    // for (i = 0; i < 16; i++) {
    for (i = 0; i < onset_trials.length; i++) {
        if (onset_trials[i].version === v_no) {
            timeline.push(onset_trials[i])
        }
    }
} else {
    for (i = 0; i < coda_trials.length; i++) {
    // for (i = 0; i < 16; i++) {
        if (coda_trials[i].version === v_no) {
            timeline.push(coda_trials[i])
        }
    }
}

// // SECOND INSTRUCTIONS
if (v_no < 4) {
    timeline.push(coda_second_instructions)
} else {
    timeline.push(onset_second_instructions)
}

// // SECOND BLOCK

if (v_no < 4) {
    // for (i = 0; i < 16; i++) {
    for (i = 0; i < coda_trials.length; i++) {
        if (coda_trials[i].version === v_no) {
            timeline.push(coda_trials[i])
        }
    }
} else {
    for (i = 0; i < onset_trials.length; i++) {
    // for (i = 0; i < 16; i++) {
        if (onset_trials[i].version === v_no) {
            timeline.push(onset_trials[i])
        }
    }
}



// DEMOGRAPHIC SURVEY


let social_instructions = {
    type: 'html-keyboard-response',
    stimulus: '<div class="pre-test-container"><p>Great Job! You finished the Experiment.<br><br>To help us interpret our results, it would be helpful to learn a little more about you. Please answer the following questions if you have time. None of the questions are required.</p><br><br>Press the space bar to continue.</div>',
    choices: ['space'],
    post_trial_gap: 250
}

timeline.push(social_instructions)


var survey1 = {
    type: 'survey-html-form',
    preamble: '<p>We would like you to answer answer the following questions.</p>',
    html: '<ol class="input-wrapper">' +
        hand +
        audio +
        gender +
        age +
        language +
        '</ol>'
};


var survey2 = {
    type: 'survey-html-form',
    preamble: '<p>We would like you to answer answer the following questions.</p>',
    html: '<ol class="input-wrapper">' +
        assess +
        interruption +
        interruption_time +
        problems +
        fair_price +
        comments +
        '</ol>'
};


timeline.push(survey1)
timeline.push(survey2)



jsPsych.init({
    timeline: timeline,
    show_progress_bar: true,
    on_finish: function(data) {
        proliferate.submit({"trials": data.values()});
      }
    // on_finish: function () {
    //     jsPsych.data.displayData('csv');
    // }
});
