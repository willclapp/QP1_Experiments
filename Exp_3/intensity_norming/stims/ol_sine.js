let sine_1 = [
    {
        pair: 0,
        type: 'audio-keyboard-response',
        stimulus: 'audio/sine/sweep_00.wav',
        trial_ends_after_audio: true,
        response_allowed_while_playing: false,
        data: { test_part: 'stim'},
        post_trial_gap: 250
    }
]

let sine_2 = [
    {
        pair: 0,
        type: 'audio-keyboard-response',
        stimulus: 'audio/sine/sweep_30.wav',
        trial_ends_after_audio: true,
        response_allowed_while_playing: false,
        data: { test_part: 'stim'},
        post_trial_gap: 0
    }
]

let sine_response = [
    {
        pair: 0,
        type: 'html-keyboard-response',
        stimulus: '<div class="big-container"><div class="yes-no"><div class="option-container"><p>FIRST LOUDER</p><p>Press S</p></div><div class="option-container"><p>SECOND LOUDER</p><p>Press K</p></div></div><div class="same-container"><p>THE SAME</p><p>Space Bar</p></div></div>',
        choices: ['s', 'k', 'space'],
        // trial_duration: 4000,
        data: { test_part: 'sine'},
        post_trial_gap: 1000,
    }
]