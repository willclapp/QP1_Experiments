
let timeline = [];

let irb = {
    type: 'html-button-response',
    stimulus: `<div class="gen_ins"><p>In this experiment, you will hear recordings and will make simple decisions about them.<br><br>Press the button below to continue.</p></div>`,
    choices: ['Continue']
};

timeline.push(irb);


let instructions = {
    type: 'html-keyboard-response',
    stimulus: `<div class="spec_ins"><p>This experiment has two parts. In both sections, you will hear two sounds and select which was louder. In the first section you'll hear pure-tone sine waves, and in the second section, you'll hear spoken syllables.<br><br>The two sounds will play automatically in succession. If the FIRST sound is louder, press the "S" key. If the SECOND sound is louder, press the "K" key. If the two are the same volume, press the space bar.<br><br>Please answer as quickly and accurately as possible.<br><br>A response cannot be made until the audio has played entirely. Once a selection is made, the slide will advance after a brief pause. If no response is made after several seconds, the slide will advance automatically.<br><br>Please press the space bar to begin.</p></div>`,
    choices: ['space'],
    post_trial_gap: 1000
};

timeline.push(instructions)

// Sine waves

// for (i = 0; i < sine_1.length; i++) {
for (i = 0; i < 3; i++) {
    timeline.push(sine_1[i])
    for (j = 0; j < sine_1.length; j++) {
        if (sine_2[j].pair == sine_1[i].pair) {
            timeline.push(sine_2[j])
        }
    }
    for (j = 0; j < sine_1.length; j++) {
        if (sine_response[j].pair == sine_1[i].pair) {
            timeline.push(sine_response[j])
        }
    }
}


// TEST INSTRUCTIONS

let second_instructions = {
    type: 'html-keyboard-response',
    stimulus: '<div class="pre-test-container"><p>Great Job! You finished the first part of the Experiment!<br><br>The second part of the experiment will be the same except that you will hear the talker say syllables, like <em>ahb</em> or <em>ahp</em>.<br><br>Again, press "S" if the first sound is louder, "K" if the second sound is louder, and the space bar if the two sounds are the same volume.<br><br>Press the space bar to continue to the trials.',
    choices: ['space'],
    post_trial_gap: 1000
}

timeline.push(second_instructions)

// Syllables


// for (i = 0; i < 150; i++) {
for (i = 0; i < 3; i++) {
    timeline.push(syll_1[i])
    for (j = 0; j < syll_1.length; j++) {
        if (syll_2[j].pair == syll_1[i].pair) {
            timeline.push(syll_2[j])
        }
    }
    for (j = 0; j < syll_1.length; j++) {
        if (syll_response[j].pair == syll_1[i].pair) {
            timeline.push(syll_response[j])
        }
    }
}



jsPsych.init({
    // preload_audio: audio,
    timeline: timeline,
    show_progress_bar: true,
    // on_finish: function () {
    //     jsPsych.data.displayData();
    // }
    on_finish: function(data) {
        proliferate.submit({"trials": data.values()});
      }
});
