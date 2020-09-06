function make_slides(f) {
  preload(assetPaths, { after: function () { console.log(`all ${assetPaths.length} assets preloaded`) } })
  var slides = {};

  slides.i0 = slide({
    name: "i0",
    start: function () {
      exp.startT = Date.now();
    }
  })

  slides.general_instructions = slide({
    name: "general_instructions",
    button: function () {
      exp.go(); //use exp.go() if and only if there is no "present" data.
    }
  });

  slides.instructions = slide({
    name: "instructions",
    button: function () {
      exp.go();
    }
  })

  slides.exposure = slide({
    name: "exposure",
    present: exp.exposure_stimuli,
    present_handle: function (stim) {
      var trialT = $("<div />")
        .attr("id", "trialT")
        .attr("data-time", Date.now())
        .hide()
      $(".trial-t").append(trialT)
      $(".err").hide();
      this.stim = stim;
      $(".trial_button")
        .attr("disabled", true)
      var audio = $("<audio />")
        .attr("src", "audio/exposure_control/" + stim.path)
        .attr("autoplay", true)
        .on("ended", function () {
          $(".display_condition_exposure").children().remove()
          $(".trial_button")
            .attr("disabled", false)
        })

      var target = build_target(stim.visual_target)
      var match_option = build_exposure_option(stim.match_sel, "yes")
      var mismatch_option = build_exposure_option(stim.mismatch_sel, "no")
      var options = [match_option, mismatch_option]

      $(".display_condition_word")
        .append(audio)

      $(".target_container")
        .append(target)

      $(".exposure_options_container")
        .append(options[1])
        .append(options[0])
    },
    button: function () {
      // TODO capture val of image radio button
      this.response = $('input[name="selection"]:checked').val();
      if (this.response == undefined) {
        $(".err").show();
      } else {
        // cleanup
        $(".exposure_options_container").children().remove()
        $(".target_container").children().remove()
        this.log_responses();
        _stream.apply(this);
      }
    },
    log_responses: function () {
      var trialT = $("#trialT").attr("data-time")
      $(".trial-t").children().remove()
      exp.data_trials.push(Object.assign({
        "slide_order": exp.phase - 3,
        "participant_id": exp.uuid,
        "response": this.response,
        "trial_time": trialT
      }, this.stim));
    }
  })

  slides.second_instructions = slide({
    name: "second_instructions",
    button: function () {
      exp.go()
    }
  })

  // LABIAL TEST

  slides.labial_test = slide({
    name: "labial_test",
    present: exp.test_stimuli_lab,
    present_handle: function (stim) {
      var trialT = $("<div />")
        .attr("id", "trialT")
        .attr("data-time", Date.now())
        .hide()
      $(".trial-t").append(trialT)
      $(".err").hide();
      this.stim = stim;
      $(".trial_button")
        .attr("disabled", true)
      var audio = $("<audio />")
        .attr("src", "audio/test/" + stim.path)
        .attr("autoplay", true)
        .on("ended", function () {
          $(".display_condition_test").children().remove()
          $(".trial_button")
            .attr("disabled", false)
        })

      var voiced_option = build_trial_option(stim.voiced_sel, "yes")
      var voiceless_option = build_trial_option(stim.voiceless_sel, "no")
      var options = [voiced_option, voiceless_option]

      $(".display_condition_nonword")
        .append(audio)

      $(".labial_options_container")
        .append(options[1])
        .append(options[0])
    },
    button: function () {
      // TODO capture val of image radio button
      this.response = $('input[name="selection"]:checked').val();
      if (this.response == undefined) {
        $(".err").show();
      } else {
        // play continuation audio
        // cleanup
        $(".labial_options_container").children().remove()
        this.log_responses();
        _stream.apply(this);
      }
    },
    log_responses: function () {
      var trialT = $("#trialT").attr("data-time")
      $(".trial-t").children().remove()
      exp.data_trials.push(Object.assign({
        "slide_order": exp.phase - 3,
        "participant_id": exp.uuid,
        "response": this.response,
        "trial_time": trialT
      }, this.stim));
    }
  })

  slides.third_instructions = slide({
    name: "third_instructions",
    button: function () {
      exp.go()
    }
  })


  // DORSAL TEST

  slides.dorsal_test = slide({
    name: "dorsal_test",
    present: exp.test_stimuli_dor,
    present_handle: function (stim) {
      var trialT = $("<div />")
        .attr("id", "trialT")
        .attr("data-time", Date.now())
        .hide()
      $(".trial-t").append(trialT)
      $(".err").hide();
      this.stim = stim;
      $(".trial_button")
        .attr("disabled", true)
      var audio = $("<audio />")
        .attr("src", "audio/test/" + stim.path)
        .attr("autoplay", true)
        .on("ended", function () {
          $(".display_condition_test").children().remove()
          $(".trial_button")
            .attr("disabled", false)
        })

      var voiced_option = build_trial_option(stim.voiced_sel, "yes")
      var voiceless_option = build_trial_option(stim.voiceless_sel, "no")
      var options = [voiced_option, voiceless_option]

      $(".display_condition_nonword")
        .append(audio)

      $(".dorsal_options_container")
        .append(options[1])
        .append(options[0])
    },
    button: function () {
      // TODO capture val of image radio button
      this.response = $('input[name="selection"]:checked').val();
      if (this.response == undefined) {
        $(".err").show();
      } else {
        // play continuation audio
        // cleanup
        $(".dorsal_options_container").children().remove()
        this.log_responses();
        _stream.apply(this);
      }
    },
    log_responses: function () {
      var trialT = $("#trialT").attr("data-time")
      $(".trial-t").children().remove()
      exp.data_trials.push(Object.assign({
        "slide_order": exp.phase - 3,
        "participant_id": exp.uuid,
        "response": this.response,
        "trial_time": trialT
      }, this.stim));
    }
  })


  slides.fourth_instructions = slide({
    name: "fourth_instructions",
    button: function () {
      exp.go()
    }
  })

  // CORONAL TEST

  slides.coronal_test = slide({
    name: "coronal_test",
    present: exp.test_stimuli_cor,
    present_handle: function (stim) {
      var trialT = $("<div />")
        .attr("id", "trialT")
        .attr("data-time", Date.now())
        .hide()
      $(".trial-t").append(trialT)
      $(".err").hide();
      this.stim = stim;
      $(".trial_button")
        .attr("disabled", true)
      var audio = $("<audio />")
        .attr("src", "audio/test/" + stim.path)
        .attr("autoplay", true)
        .on("ended", function () {
          $(".display_condition_test").children().remove()
          $(".trial_button")
            .attr("disabled", false)
        })

      var voiced_option = build_trial_option(stim.voiced_sel, "yes")
      var voiceless_option = build_trial_option(stim.voiceless_sel, "no")
      var options = [voiced_option, voiceless_option]

      $(".display_condition_nonword")
        .append(audio)

      $(".coronal_options_container")
        .append(options[1])
        .append(options[0])
    },
    button: function () {
      // TODO capture val of image radio button
      this.response = $('input[name="selection"]:checked').val();
      if (this.response == undefined) {
        $(".err").show();
      } else {
        // play continuation audio
        // cleanup
        $(".coronal_options_container").children().remove()
        this.log_responses();
        _stream.apply(this);
      }
    },
    log_responses: function () {
      var trialT = $("#trialT").attr("data-time")
      $(".trial-t").children().remove()
      exp.data_trials.push(Object.assign({
        "slide_order": exp.phase - 3,
        "participant_id": exp.uuid,
        "response": this.response,
        "trial_time": trialT
      }, this.stim));
    }
  })



  slides.subj_info = slide({
    name: "subj_info",
    submit: function (e) {
      //if (e.preventDefault) e.preventDefault(); // I don't know what this means.
      exp.subj_data = {
        language: $("#language").val(),
        enjoyment: $("#enjoyment").val(),
        assess: $('input[name="assess"]:checked').val(),
        listen: $('input[name="listen"]:checked').val(),
        age: $("#age").val(),
        gender: $("#gender").val(),
        education: $("#education").val(),
        comments: $("#comments").val(),
        problems: $("#problems").val(),
        fairprice: $("#fairprice").val(),
        interruption: $('input[name="interruption"]:checked').val(),
        int_minutes: $("#int_minutes").val(),
        email: $('input[name="email"]:checked').val(),
        handed: $('input[name="hand"]:checked').val()
      };
      exp.go(); //use exp.go() if and only if there is no "present" data.
    }
  });

  slides.thanks = slide({
    name: "thanks",
    start: function () {
      exp.data = {
        "trials": exp.data_trials,
        "catch_trials": exp.catch_trials,
        "system": exp.system,
        "condition": exp.condition,
        "subject_information": exp.subj_data,
        "time_in_minutes": (Date.now() - exp.startT) / 60000
      };
      submitResults(1, exp.data, function(err, data) {
        if (err) {
          console.error(err)
        } else {
          let finishLink = $("<a>Click here to finish</a>")
          .attr("href", "https://app.prolific.co/submissions/complete?cc=1DB75173")

          $(".link-container").append(finishLink)
        }
      })
    }
  });

  return slides;
}

/// init ///
function init() {
  exp.trials = [];
  exp.catch_trials = [];


  exp.uuid = uuidv4()
  // variables imported from stims.js
  exp.exposure_stimuli = _.shuffle(exposure_stimuli)
  exp.test_stimuli_lab = _.shuffle(test_stimuli_lab)
  exp.test_stimuli_cor = _.shuffle(test_stimuli_cor)
  exp.test_stimuli_dor = _.shuffle(test_stimuli_dor)
  exp.system = {
    Browser: BrowserDetect.browser,
    OS: BrowserDetect.OS,
    screenH: screen.height,
    screenUH: exp.height,
    screenW: screen.width,
    screenUW: exp.width
  };
  //blocks of the experiment:
  exp.structure = ["i0", "general_instructions", "instructions", "exposure", "second_instructions", "labial_test", "third_instructions", "coronal_test", "fourth_instructions", "dorsal_test", 'subj_info', 'thanks'];

  exp.data_trials = [];
  //make corresponding slides:
  exp.slides = make_slides(exp);

  // exp.nQs = utils.get_exp_length(); //this does not work if there are stacks of stims (but does work for an experiment with this structure)
  //relies on structure and slides being defined

  $('.slide').hide(); //hide everything

  //make sure turkers have accepted HIT (or you're not in mturk)
  $("#start_button").click(function () {
    if (turk.previewMode) {
      $("#mustaccept").show();
    } else {
      $("#start_button").click(function () { $("#mustaccept").show(); });
      exp.go();
    }
  });

  exp.go(); //show first slide
}







