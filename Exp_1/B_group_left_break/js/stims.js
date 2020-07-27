
var exposure_stimuli = [
  {
    "index": "1",
    "group": "B_group",
    "side": "left",
    "phase": "exposure",
    "target": "[B?]allerina",
    "type": "crit_amb",
    "word_sel": "Yes",
    "nonword_sel": "No",
    "set": "Ballerina_Pallerina_1",
    "step": "15",
    "recording": "1",
    "path": "ambiguous/Ballerina_Pallerina_1_15.mp3"
  },
  {
    "index": "2",
    "group": "B_group",
    "side": "left",
    "phase": "exposure",
    "target": "[B?]alloon",
    "type": "crit_amb",
    "word_sel": "Yes",
    "nonword_sel": "No",
    "set": "Balloon_Palloon_3",
    "step": "12",
    "recording": "3",
    "path": "ambiguous/Balloon_Palloon_3_12.mp3"
  }
]

var test_stimuli = [
  {
    "index": "1",
    "group": "B_group",
    "side": "left",
    "phase": "test",
    "set": "BAA_PAA_3",
    "repetition": "1",
    "normed_midpoint": "25",
    "voiced_sel": "B",
    "voiceless_sel": "P",
    "recording": "3",
    "step": "0",
    "path": "BAA_PAA_3_0.mp3"
  },
  {
    "index": "2",
    "group": "B_group",
    "side": "left",
    "phase": "test",
    "set": "BAH_PAH_3",
    "repetition": "1",
    "normed_midpoint": "23",
    "voiced_sel": "B",
    "voiceless_sel": "P",
    "recording": "3",
    "step": "0",
    "path": "BAH_PAH_3_0.mp3"
  }
]

var assetPaths = [
  "audio/exposure_B_group/ambiguous/Ballerina_Pallerina_1_15.mp3",
  "audio/exposure_B_group/ambiguous/Balloon_Palloon_3_12.mp3",
  "audio/exposure_B_group/ambiguous/Baloney_Paloney_1_10.mp3",
  "audio/exposure_B_group/ambiguous/Banana_Panana_3_17.mp3",
  "audio/exposure_B_group/ambiguous/Barely_Parely_1_7.mp3",
  "audio/exposure_B_group/ambiguous/Barn_Parn_1_20.mp3",
  "audio/exposure_B_group/ambiguous/Barren_Parren_3_17.mp3",
  "audio/exposure_B_group/ambiguous/Belly_Pelly_3_17.mp3",
  "audio/exposure_B_group/ambiguous/Benign_Penign_3_14.mp3",
  "audio/exposure_B_group/ambiguous/Biannual_Piannual_3_7.mp3",
  "audio/exposure_B_group/ambiguous/Billion_Pillion_3_18.mp3",
  "audio/exposure_B_group/ambiguous/Billionaire_Pillionaire_3_8.mp3",
  "audio/exposure_B_group/ambiguous/Blue_Plue_3_17.mp3",
  "audio/exposure_B_group/ambiguous/Boil_Poil_1_15.mp3",
  "audio/exposure_B_group/ambiguous/Boom_Poom_1_15.mp3",
  "audio/exposure_B_group/ambiguous/Brain_Prain_3_19.mp3",
  "audio/exposure_B_group/ambiguous/Brewery_Prewery_1_13.mp3",
  "audio/exposure_B_group/ambiguous/Brown_Prown_3_11.mp3",
  "audio/exposure_B_group/ambiguous/Burial_Purial_1_17.mp3",
  "audio/exposure_B_group/ambiguous/Burrow_Purrow_3_9.mp3",
  "audio/exposure_B_group/unambiguous/Barallel_Parallel_4.mp3",
  "audio/exposure_B_group/unambiguous/Barlor_Parlor_4.mp3",
  "audio/exposure_B_group/unambiguous/Bawn_Pawn_2.mp3",
  "audio/exposure_B_group/unambiguous/Beninsula_Peninsula_2.mp3",
  "audio/exposure_B_group/unambiguous/Berform_Perform_2.mp3",
  "audio/exposure_B_group/unambiguous/Bioneer_Pioneer_4.mp3",
  "audio/exposure_B_group/unambiguous/Blanner_Planner_2.mp3",
  "audio/exposure_B_group/unambiguous/Blea_Plea_2.mp3",
  "audio/exposure_B_group/unambiguous/Blyer_Plyer_2.mp3",
  "audio/exposure_B_group/unambiguous/Bollen_Pollen_2.mp3",
  "audio/exposure_B_group/unambiguous/Bolymer_Polymer_2.mp3",
  "audio/exposure_B_group/unambiguous/Brayer_Prayer_2.mp3",
  "audio/exposure_B_group/unambiguous/Breliminary_Preliminary_2.mp3",
  "audio/exposure_B_group/unambiguous/Bremier_Premier_2.mp3",
  "audio/exposure_B_group/unambiguous/Brimal_Primal_2.mp3",
  "audio/exposure_B_group/unambiguous/Brime_Prime_2.mp3",
  "audio/exposure_B_group/unambiguous/Brior_Prior_2.mp3",
  "audio/exposure_B_group/unambiguous/Browl_Prowl_2.mp3",
  "audio/exposure_B_group/unambiguous/Bry_Pry_2.mp3",
  "audio/exposure_B_group/unambiguous/Bylon_Pylon_2.mp3",
  "audio/exposure_B_group/word/Aisle_1.mp3",
  "audio/exposure_B_group/word/Ally_1.mp3",
  "audio/exposure_B_group/word/Area_1.mp3",
  "audio/exposure_B_group/word/Arena_1.mp3",
  "audio/exposure_B_group/word/Arrow_1.mp3",
  "audio/exposure_B_group/word/Assume_1.mp3",
  "audio/exposure_B_group/word/Aware_1.mp3",
  "audio/exposure_B_group/word/Enemy_1.mp3",
  "audio/exposure_B_group/word/Ensure_1.mp3",
  "audio/exposure_B_group/word/Error_1.mp3",
  "audio/exposure_B_group/word/Eye_1.mp3",
  "audio/exposure_B_group/word/Failure_1.mp3",
  "audio/exposure_B_group/word/Famous_1.mp3",
  "audio/exposure_B_group/word/Flower_1.mp3",
  "audio/exposure_B_group/word/Frame_1.mp3",
  "audio/exposure_B_group/word/Funnel_1.mp3",
  "audio/exposure_B_group/word/Hallway_1.mp3",
  "audio/exposure_B_group/word/Hang_1.mp3",
  "audio/exposure_B_group/word/Harmony_1.mp3",
  "audio/exposure_B_group/word/Hill_1.mp3",
  "audio/exposure_B_group/word/Hole_1.mp3",
  "audio/exposure_B_group/word/Horn_1.mp3",
  "audio/exposure_B_group/word/Jelly_1.mp3",
  "audio/exposure_B_group/word/Jewel_1.mp3",
  "audio/exposure_B_group/word/Lawyer_1.mp3",
  "audio/exposure_B_group/word/Layer_1.mp3",
  "audio/exposure_B_group/word/Learning_1.mp3",
  "audio/exposure_B_group/word/Low_1.mp3",
  "audio/exposure_B_group/word/Main_1.mp3",
  "audio/exposure_B_group/word/Marine_1.mp3",
  "audio/exposure_B_group/word/Memory_1.mp3",
  "audio/exposure_B_group/word/Money_1.mp3",
  "audio/exposure_B_group/word/Name_1.mp3",
  "audio/exposure_B_group/word/Narrow_1.mp3",
  "audio/exposure_B_group/word/Normal_1.mp3",
  "audio/exposure_B_group/word/Nun_1.mp3",
  "audio/exposure_B_group/word/Phenomenon_1.mp3",
  "audio/exposure_B_group/word/Rally_1.mp3",
  "audio/exposure_B_group/word/Range_1.mp3",
  "audio/exposure_B_group/word/Real_1.mp3",
  "audio/exposure_B_group/word/Reign_1.mp3",
  "audio/exposure_B_group/word/Ring_1.mp3",
  "audio/exposure_B_group/word/Roar_1.mp3",
  "audio/exposure_B_group/word/Royal_1.mp3",
  "audio/exposure_B_group/word/Ruin_1.mp3",
  "audio/exposure_B_group/word/Rumor_1.mp3",
  "audio/exposure_B_group/word/Runner_1.mp3",
  "audio/exposure_B_group/word/Sailor_1.mp3",
  "audio/exposure_B_group/word/Seal_1.mp3",
  "audio/exposure_B_group/word/Shell_1.mp3",
  "audio/exposure_B_group/word/Similar_1.mp3",
  "audio/exposure_B_group/word/Soil_1.mp3",
  "audio/exposure_B_group/word/Valley_1.mp3",
  "audio/exposure_B_group/word/Vary_1.mp3",
  "audio/exposure_B_group/word/Venue_1.mp3",
  "audio/exposure_B_group/word/Violin_1.mp3",
  "audio/exposure_B_group/word/Volume_1.mp3",
  "audio/exposure_B_group/word/Sewer_1.mp3",
  "audio/exposure_B_group/word/Swear_1.mp3",
  "audio/exposure_B_group/word/Throne_1.mp3",
  "audio/exposure_B_group/nonword/Alinomy_1.mp3",
  "audio/exposure_B_group/nonword/Aller_1.mp3",
  "audio/exposure_B_group/nonword/Arema_1.mp3",
  "audio/exposure_B_group/nonword/Chame_1.mp3",
  "audio/exposure_B_group/nonword/Charle_1.mp3",
  "audio/exposure_B_group/nonword/Cheel_1.mp3",
  "audio/exposure_B_group/nonword/Churr_1.mp3",
  "audio/exposure_B_group/nonword/Eamer_1.mp3",
  "audio/exposure_B_group/nonword/Eelam_1.mp3",
  "audio/exposure_B_group/nonword/Elammer_1.mp3",
  "audio/exposure_B_group/nonword/Enlow_1.mp3",
  "audio/exposure_B_group/nonword/Eynam_1.mp3",
  "audio/exposure_B_group/nonword/Fairdon_1.mp3",
  "audio/exposure_B_group/nonword/Feen_1.mp3",
  "audio/exposure_B_group/nonword/Felmy_1.mp3",
  "audio/exposure_B_group/nonword/Fime_1.mp3",
  "audio/exposure_B_group/nonword/Finneran_1.mp3",
  "audio/exposure_B_group/nonword/Flangle_1.mp3",
  "audio/exposure_B_group/nonword/Fonnow_1.mp3",
  "audio/exposure_B_group/nonword/Foon_1.mp3",
  "audio/exposure_B_group/nonword/Hallen_1.mp3",
  "audio/exposure_B_group/nonword/Hame_1.mp3",
  "audio/exposure_B_group/nonword/Harl_1.mp3",
  "audio/exposure_B_group/nonword/Harn_1.mp3",
  "audio/exposure_B_group/nonword/Harnomy_1.mp3",
  "audio/exposure_B_group/nonword/Heln_1.mp3",
  "audio/exposure_B_group/nonword/Hemmerle_1.mp3",
  "audio/exposure_B_group/nonword/Hemmery_1.mp3",
  "audio/exposure_B_group/nonword/Heon_1.mp3",
  "audio/exposure_B_group/nonword/Heyn_1.mp3",
  "audio/exposure_B_group/nonword/Hing_1.mp3",
  "audio/exposure_B_group/nonword/Hino_1.mp3",
  "audio/exposure_B_group/nonword/Hollin_1.mp3",
  "audio/exposure_B_group/nonword/Hoy_1.mp3",
  "audio/exposure_B_group/nonword/Hurn_1.mp3",
  "audio/exposure_B_group/nonword/Immel_1.mp3",
  "audio/exposure_B_group/nonword/Jare_1.mp3",
  "audio/exposure_B_group/nonword/Jeel_1.mp3",
  "audio/exposure_B_group/nonword/Jum_1.mp3",
  "audio/exposure_B_group/nonword/Jurio_1.mp3",
  "audio/exposure_B_group/nonword/Lahm_1.mp3",
  "audio/exposure_B_group/nonword/Lail_1.mp3",
  "audio/exposure_B_group/nonword/Lamurre_1.mp3",
  "audio/exposure_B_group/nonword/Lar_1.mp3",
  "audio/exposure_B_group/nonword/Larrow_1.mp3",
  "audio/exposure_B_group/nonword/Lemmela_1.mp3",
  "audio/exposure_B_group/nonword/Lennim_1.mp3",
  "audio/exposure_B_group/nonword/Leonie_1.mp3",
  "audio/exposure_B_group/nonword/Lermie_1.mp3",
  "audio/exposure_B_group/nonword/Loanler_1.mp3",
  "audio/exposure_B_group/nonword/Loff_1.mp3",
  "audio/exposure_B_group/nonword/Lum_1.mp3",
  "audio/exposure_B_group/nonword/Mallon_1.mp3",
  "audio/exposure_B_group/nonword/Mang_1.mp3",
  "audio/exposure_B_group/nonword/Mannow_1.mp3",
  "audio/exposure_B_group/nonword/Marn_1.mp3",
  "audio/exposure_B_group/nonword/Mawen_1.mp3",
  "audio/exposure_B_group/nonword/Mawn_1.mp3",
  "audio/exposure_B_group/nonword/Mayin_1.mp3",
  "audio/exposure_B_group/nonword/Memmel_1.mp3",
  "audio/exposure_B_group/nonword/Mewry_1.mp3",
  "audio/exposure_B_group/nonword/Minnin_1.mp3",
  "audio/exposure_B_group/nonword/Morial_1.mp3",
  "audio/exposure_B_group/nonword/Moyer_1.mp3",
  "audio/exposure_B_group/nonword/Mun_1.mp3",
  "audio/exposure_B_group/nonword/Munnel_1.mp3",
  "audio/exposure_B_group/nonword/Nallow_1.mp3",
  "audio/exposure_B_group/nonword/Nellon_1.mp3",
  "audio/exposure_B_group/nonword/Neoma_1.mp3",
  "audio/exposure_B_group/nonword/Ner_1.mp3",
  "audio/exposure_B_group/nonword/Norlin_1.mp3",
  "audio/exposure_B_group/nonword/Noron_1.mp3",
  "audio/exposure_B_group/nonword/Noy_1.mp3",
  "audio/exposure_B_group/nonword/Orn_1.mp3",
  "audio/exposure_B_group/nonword/Rame_1.mp3",
  "audio/exposure_B_group/nonword/Rannel_1.mp3",
  "audio/exposure_B_group/nonword/Rawl_1.mp3",
  "audio/exposure_B_group/nonword/Reen_1.mp3",
  "audio/exposure_B_group/nonword/Rhinen_2.mp3",
  "audio/exposure_B_group/nonword/Ria_1.mp3",
  "audio/exposure_B_group/nonword/Saln_1.mp3",
  "audio/exposure_B_group/nonword/Sare_1.mp3",
  "audio/exposure_B_group/nonword/Selmer_1.mp3",
  "audio/exposure_B_group/nonword/Siller_1.mp3",
  "audio/exposure_B_group/nonword/Slomb_1.mp3",
  "audio/exposure_B_group/nonword/Smong_1.mp3",
  "audio/exposure_B_group/nonword/Snoll_1.mp3",
  "audio/exposure_B_group/nonword/Snyre_1.mp3",
  "audio/exposure_B_group/nonword/Somb_1.mp3",
  "audio/exposure_B_group/nonword/Thim_1.mp3",
  "audio/exposure_B_group/nonword/Threen_1.mp3",
  "audio/exposure_B_group/nonword/Vainyl_1.mp3",
  "audio/exposure_B_group/nonword/Vallon_1.mp3",
  "audio/exposure_B_group/nonword/Vunn_1.mp3",
  "audio/exposure_B_group/nonword/Werro_1.mp3",
  "audio/exposure_B_group/nonword/Winal_1.mp3",
  "audio/exposure_B_group/nonword/Woony_1.mp3",
  "audio/exposure_B_group/nonword/Wyan_1.mp3",
  "audio/exposure_B_group/nonword/Yorn_1.mp3",
  "audio/exposure_B_group/nonword/Ven_1.mp3",
  "audio/test/BAA_PAA_3_0.mp3",
  "audio/test/BAH_PAH_3_0.mp3",
  "audio/test/BIH_PIH_1_0.mp3",
  "audio/test/BUH_PUH_3_0.mp3",
  "audio/test/DAA_TAA_3_0.mp3",
  "audio/test/DAH_TAH_3_0.mp3",
  "audio/test/DIH_TIH_3_0.mp3",
  "audio/test/DUH_TUH_3_0.mp3",
  "audio/test/GAA_KAA_5_0.mp3",
  "audio/test/GAH_KAH_3_0.mp3",
  "audio/test/GIH_KIH_5_0.mp3",
  "audio/test/GUH_KUH_3_0.mp3",
  "audio/test/BAA_PAA_3_0.mp3",
  "audio/test/BAH_PAH_3_0.mp3",
  "audio/test/BIH_PIH_1_0.mp3",
  "audio/test/BUH_PUH_3_0.mp3",
  "audio/test/DAA_TAA_3_0.mp3",
  "audio/test/DAH_TAH_3_0.mp3",
  "audio/test/DIH_TIH_3_0.mp3",
  "audio/test/DUH_TUH_3_0.mp3",
  "audio/test/GAA_KAA_5_0.mp3",
  "audio/test/GAH_KAH_3_0.mp3",
  "audio/test/GIH_KIH_5_0.mp3",
  "audio/test/GUH_KUH_3_0.mp3",
  "audio/test/BAA_PAA_3_0.mp3",
  "audio/test/BAH_PAH_3_0.mp3",
  "audio/test/BIH_PIH_1_0.mp3",
  "audio/test/BUH_PUH_3_0.mp3",
  "audio/test/DAA_TAA_3_0.mp3",
  "audio/test/DAH_TAH_3_0.mp3",
  "audio/test/DIH_TIH_3_0.mp3",
  "audio/test/DUH_TUH_3_0.mp3",
  "audio/test/GAA_KAA_5_0.mp3",
  "audio/test/GAH_KAH_3_0.mp3",
  "audio/test/GIH_KIH_5_0.mp3",
  "audio/test/GUH_KUH_3_0.mp3",
  "audio/test/BAA_PAA_3_5.mp3",
  "audio/test/BAH_PAH_3_5.mp3",
  "audio/test/BIH_PIH_1_5.mp3",
  "audio/test/BUH_PUH_3_5.mp3",
  "audio/test/DAA_TAA_3_5.mp3",
  "audio/test/DAH_TAH_3_5.mp3",
  "audio/test/DIH_TIH_3_5.mp3",
  "audio/test/DUH_TUH_3_5.mp3",
  "audio/test/GAA_KAA_5_5.mp3",
  "audio/test/GAH_KAH_3_5.mp3",
  "audio/test/GIH_KIH_5_5.mp3",
  "audio/test/GUH_KUH_3_5.mp3",
  "audio/test/BAA_PAA_3_5.mp3",
  "audio/test/BAH_PAH_3_5.mp3",
  "audio/test/BIH_PIH_1_5.mp3",
  "audio/test/BUH_PUH_3_5.mp3",
  "audio/test/DAA_TAA_3_5.mp3",
  "audio/test/DAH_TAH_3_5.mp3",
  "audio/test/DIH_TIH_3_5.mp3",
  "audio/test/DUH_TUH_3_5.mp3",
  "audio/test/GAA_KAA_5_5.mp3",
  "audio/test/GAH_KAH_3_5.mp3",
  "audio/test/GIH_KIH_5_5.mp3",
  "audio/test/GUH_KUH_3_5.mp3",
  "audio/test/BAA_PAA_3_5.mp3",
  "audio/test/BAH_PAH_3_5.mp3",
  "audio/test/BIH_PIH_1_5.mp3",
  "audio/test/BUH_PUH_3_5.mp3",
  "audio/test/DAA_TAA_3_5.mp3",
  "audio/test/DAH_TAH_3_5.mp3",
  "audio/test/DIH_TIH_3_5.mp3",
  "audio/test/DUH_TUH_3_5.mp3",
  "audio/test/GAA_KAA_5_5.mp3",
  "audio/test/GAH_KAH_3_5.mp3",
  "audio/test/GIH_KIH_5_5.mp3",
  "audio/test/GUH_KUH_3_5.mp3",
  "audio/test/BAA_PAA_3_10.mp3",
  "audio/test/BAH_PAH_3_10.mp3",
  "audio/test/BIH_PIH_1_10.mp3",
  "audio/test/BUH_PUH_3_10.mp3",
  "audio/test/DAA_TAA_3_10.mp3",
  "audio/test/DAH_TAH_3_10.mp3",
  "audio/test/DIH_TIH_3_10.mp3",
  "audio/test/DUH_TUH_3_10.mp3",
  "audio/test/GAA_KAA_5_10.mp3",
  "audio/test/GAH_KAH_3_10.mp3",
  "audio/test/GIH_KIH_5_10.mp3",
  "audio/test/GUH_KUH_3_10.mp3",
  "audio/test/BAA_PAA_3_10.mp3",
  "audio/test/BAH_PAH_3_10.mp3",
  "audio/test/BIH_PIH_1_10.mp3",
  "audio/test/BUH_PUH_3_10.mp3",
  "audio/test/DAA_TAA_3_10.mp3",
  "audio/test/DAH_TAH_3_10.mp3",
  "audio/test/DIH_TIH_3_10.mp3",
  "audio/test/DUH_TUH_3_10.mp3",
  "audio/test/GAA_KAA_5_10.mp3",
  "audio/test/GAH_KAH_3_10.mp3",
  "audio/test/GIH_KIH_5_10.mp3",
  "audio/test/GUH_KUH_3_10.mp3",
  "audio/test/BAA_PAA_3_10.mp3",
  "audio/test/BAH_PAH_3_10.mp3",
  "audio/test/BIH_PIH_1_10.mp3",
  "audio/test/BUH_PUH_3_10.mp3",
  "audio/test/DAA_TAA_3_10.mp3",
  "audio/test/DAH_TAH_3_10.mp3",
  "audio/test/DIH_TIH_3_10.mp3",
  "audio/test/DUH_TUH_3_10.mp3",
  "audio/test/GAA_KAA_5_10.mp3",
  "audio/test/GAH_KAH_3_10.mp3",
  "audio/test/GIH_KIH_5_10.mp3",
  "audio/test/GUH_KUH_3_10.mp3",
  "audio/test/BAA_PAA_3_15.mp3",
  "audio/test/BAH_PAH_3_15.mp3",
  "audio/test/BIH_PIH_1_15.mp3",
  "audio/test/BUH_PUH_3_15.mp3",
  "audio/test/DAA_TAA_3_15.mp3",
  "audio/test/DAH_TAH_3_15.mp3",
  "audio/test/DIH_TIH_3_15.mp3",
  "audio/test/DUH_TUH_3_15.mp3",
  "audio/test/GAA_KAA_5_15.mp3",
  "audio/test/GAH_KAH_3_15.mp3",
  "audio/test/GIH_KIH_5_15.mp3",
  "audio/test/GUH_KUH_3_15.mp3",
  "audio/test/BAA_PAA_3_15.mp3",
  "audio/test/BAH_PAH_3_15.mp3",
  "audio/test/BIH_PIH_1_15.mp3",
  "audio/test/BUH_PUH_3_15.mp3",
  "audio/test/DAA_TAA_3_15.mp3",
  "audio/test/DAH_TAH_3_15.mp3",
  "audio/test/DIH_TIH_3_15.mp3",
  "audio/test/DUH_TUH_3_15.mp3",
  "audio/test/GAA_KAA_5_15.mp3",
  "audio/test/GAH_KAH_3_15.mp3",
  "audio/test/GIH_KIH_5_15.mp3",
  "audio/test/GUH_KUH_3_15.mp3",
  "audio/test/BAA_PAA_3_15.mp3",
  "audio/test/BAH_PAH_3_15.mp3",
  "audio/test/BIH_PIH_1_15.mp3",
  "audio/test/BUH_PUH_3_15.mp3",
  "audio/test/DAA_TAA_3_15.mp3",
  "audio/test/DAH_TAH_3_15.mp3",
  "audio/test/DIH_TIH_3_15.mp3",
  "audio/test/DUH_TUH_3_15.mp3",
  "audio/test/GAA_KAA_5_15.mp3",
  "audio/test/GAH_KAH_3_15.mp3",
  "audio/test/GIH_KIH_5_15.mp3",
  "audio/test/GUH_KUH_3_15.mp3",
  "audio/test/BAA_PAA_3_18.mp3",
  "audio/test/BAH_PAH_3_18.mp3",
  "audio/test/BIH_PIH_1_18.mp3",
  "audio/test/BUH_PUH_3_18.mp3",
  "audio/test/DAA_TAA_3_18.mp3",
  "audio/test/DAH_TAH_3_18.mp3",
  "audio/test/DIH_TIH_3_18.mp3",
  "audio/test/DUH_TUH_3_18.mp3",
  "audio/test/GAA_KAA_5_18.mp3",
  "audio/test/GAH_KAH_3_18.mp3",
  "audio/test/GIH_KIH_5_18.mp3",
  "audio/test/GUH_KUH_3_18.mp3",
  "audio/test/BAA_PAA_3_18.mp3",
  "audio/test/BAH_PAH_3_18.mp3",
  "audio/test/BIH_PIH_1_18.mp3",
  "audio/test/BUH_PUH_3_18.mp3",
  "audio/test/DAA_TAA_3_18.mp3",
  "audio/test/DAH_TAH_3_18.mp3",
  "audio/test/DIH_TIH_3_18.mp3",
  "audio/test/DUH_TUH_3_18.mp3",
  "audio/test/GAA_KAA_5_18.mp3",
  "audio/test/GAH_KAH_3_18.mp3",
  "audio/test/GIH_KIH_5_18.mp3",
  "audio/test/GUH_KUH_3_18.mp3",
  "audio/test/BAA_PAA_3_18.mp3",
  "audio/test/BAH_PAH_3_18.mp3",
  "audio/test/BIH_PIH_1_18.mp3",
  "audio/test/BUH_PUH_3_18.mp3",
  "audio/test/DAA_TAA_3_18.mp3",
  "audio/test/DAH_TAH_3_18.mp3",
  "audio/test/DIH_TIH_3_18.mp3",
  "audio/test/DUH_TUH_3_18.mp3",
  "audio/test/GAA_KAA_5_18.mp3",
  "audio/test/GAH_KAH_3_18.mp3",
  "audio/test/GIH_KIH_5_18.mp3",
  "audio/test/GUH_KUH_3_18.mp3",
  "audio/test/BAA_PAA_3_20.mp3",
  "audio/test/BAH_PAH_3_20.mp3",
  "audio/test/BIH_PIH_1_20.mp3",
  "audio/test/BUH_PUH_3_20.mp3",
  "audio/test/DAA_TAA_3_20.mp3",
  "audio/test/DAH_TAH_3_20.mp3",
  "audio/test/DIH_TIH_3_20.mp3",
  "audio/test/DUH_TUH_3_20.mp3",
  "audio/test/GAA_KAA_5_20.mp3",
  "audio/test/GAH_KAH_3_20.mp3",
  "audio/test/GIH_KIH_5_20.mp3",
  "audio/test/GUH_KUH_3_20.mp3",
  "audio/test/BAA_PAA_3_20.mp3",
  "audio/test/BAH_PAH_3_20.mp3",
  "audio/test/BIH_PIH_1_20.mp3",
  "audio/test/BUH_PUH_3_20.mp3",
  "audio/test/DAA_TAA_3_20.mp3",
  "audio/test/DAH_TAH_3_20.mp3",
  "audio/test/DIH_TIH_3_20.mp3",
  "audio/test/DUH_TUH_3_20.mp3",
  "audio/test/GAA_KAA_5_20.mp3",
  "audio/test/GAH_KAH_3_20.mp3",
  "audio/test/GIH_KIH_5_20.mp3",
  "audio/test/GUH_KUH_3_20.mp3",
  "audio/test/BAA_PAA_3_20.mp3",
  "audio/test/BAH_PAH_3_20.mp3",
  "audio/test/BIH_PIH_1_20.mp3",
  "audio/test/BUH_PUH_3_20.mp3",
  "audio/test/DAA_TAA_3_20.mp3",
  "audio/test/DAH_TAH_3_20.mp3",
  "audio/test/DIH_TIH_3_20.mp3",
  "audio/test/DUH_TUH_3_20.mp3",
  "audio/test/GAA_KAA_5_20.mp3",
  "audio/test/GAH_KAH_3_20.mp3",
  "audio/test/GIH_KIH_5_20.mp3",
  "audio/test/GUH_KUH_3_20.mp3",
  "audio/test/BAA_PAA_3_22.mp3",
  "audio/test/BAH_PAH_3_22.mp3",
  "audio/test/BIH_PIH_1_22.mp3",
  "audio/test/BUH_PUH_3_22.mp3",
  "audio/test/DAA_TAA_3_22.mp3",
  "audio/test/DAH_TAH_3_22.mp3",
  "audio/test/DIH_TIH_3_22.mp3",
  "audio/test/DUH_TUH_3_22.mp3",
  "audio/test/GAA_KAA_5_22.mp3",
  "audio/test/GAH_KAH_3_22.mp3",
  "audio/test/GIH_KIH_5_22.mp3",
  "audio/test/GUH_KUH_3_22.mp3",
  "audio/test/BAA_PAA_3_22.mp3",
  "audio/test/BAH_PAH_3_22.mp3",
  "audio/test/BIH_PIH_1_22.mp3",
  "audio/test/BUH_PUH_3_22.mp3",
  "audio/test/DAA_TAA_3_22.mp3",
  "audio/test/DAH_TAH_3_22.mp3",
  "audio/test/DIH_TIH_3_22.mp3",
  "audio/test/DUH_TUH_3_22.mp3",
  "audio/test/GAA_KAA_5_22.mp3",
  "audio/test/GAH_KAH_3_22.mp3",
  "audio/test/GIH_KIH_5_22.mp3",
  "audio/test/GUH_KUH_3_22.mp3",
  "audio/test/BAA_PAA_3_22.mp3",
  "audio/test/BAH_PAH_3_22.mp3",
  "audio/test/BIH_PIH_1_22.mp3",
  "audio/test/BUH_PUH_3_22.mp3",
  "audio/test/DAA_TAA_3_22.mp3",
  "audio/test/DAH_TAH_3_22.mp3",
  "audio/test/DIH_TIH_3_22.mp3",
  "audio/test/DUH_TUH_3_22.mp3",
  "audio/test/GAA_KAA_5_22.mp3",
  "audio/test/GAH_KAH_3_22.mp3",
  "audio/test/GIH_KIH_5_22.mp3",
  "audio/test/GUH_KUH_3_22.mp3",
  "audio/test/BAA_PAA_3_24.mp3",
  "audio/test/BAH_PAH_3_24.mp3",
  "audio/test/BIH_PIH_1_24.mp3",
  "audio/test/BUH_PUH_3_24.mp3",
  "audio/test/DAA_TAA_3_24.mp3",
  "audio/test/DAH_TAH_3_24.mp3",
  "audio/test/DIH_TIH_3_24.mp3",
  "audio/test/DUH_TUH_3_24.mp3",
  "audio/test/GAA_KAA_5_24.mp3",
  "audio/test/GAH_KAH_3_24.mp3",
  "audio/test/GIH_KIH_5_24.mp3",
  "audio/test/GUH_KUH_3_24.mp3",
  "audio/test/BAA_PAA_3_24.mp3",
  "audio/test/BAH_PAH_3_24.mp3",
  "audio/test/BIH_PIH_1_24.mp3",
  "audio/test/BUH_PUH_3_24.mp3",
  "audio/test/DAA_TAA_3_24.mp3",
  "audio/test/DAH_TAH_3_24.mp3",
  "audio/test/DIH_TIH_3_24.mp3",
  "audio/test/DUH_TUH_3_24.mp3",
  "audio/test/GAA_KAA_5_24.mp3",
  "audio/test/GAH_KAH_3_24.mp3",
  "audio/test/GIH_KIH_5_24.mp3",
  "audio/test/GUH_KUH_3_24.mp3",
  "audio/test/BAA_PAA_3_24.mp3",
  "audio/test/BAH_PAH_3_24.mp3",
  "audio/test/BIH_PIH_1_24.mp3",
  "audio/test/BUH_PUH_3_24.mp3",
  "audio/test/DAA_TAA_3_24.mp3",
  "audio/test/DAH_TAH_3_24.mp3",
  "audio/test/DIH_TIH_3_24.mp3",
  "audio/test/DUH_TUH_3_24.mp3",
  "audio/test/GAA_KAA_5_24.mp3",
  "audio/test/GAH_KAH_3_24.mp3",
  "audio/test/GIH_KIH_5_24.mp3",
  "audio/test/GUH_KUH_3_24.mp3",
  "audio/test/BAA_PAA_3_27.mp3",
  "audio/test/BAH_PAH_3_27.mp3",
  "audio/test/BIH_PIH_1_27.mp3",
  "audio/test/BUH_PUH_3_27.mp3",
  "audio/test/DAA_TAA_3_27.mp3",
  "audio/test/DAH_TAH_3_27.mp3",
  "audio/test/DIH_TIH_3_27.mp3",
  "audio/test/DUH_TUH_3_27.mp3",
  "audio/test/GAA_KAA_5_27.mp3",
  "audio/test/GAH_KAH_3_27.mp3",
  "audio/test/GIH_KIH_5_27.mp3",
  "audio/test/GUH_KUH_3_27.mp3",
  "audio/test/BAA_PAA_3_27.mp3",
  "audio/test/BAH_PAH_3_27.mp3",
  "audio/test/BIH_PIH_1_27.mp3",
  "audio/test/BUH_PUH_3_27.mp3",
  "audio/test/DAA_TAA_3_27.mp3",
  "audio/test/DAH_TAH_3_27.mp3",
  "audio/test/DIH_TIH_3_27.mp3",
  "audio/test/DUH_TUH_3_27.mp3",
  "audio/test/GAA_KAA_5_27.mp3",
  "audio/test/GAH_KAH_3_27.mp3",
  "audio/test/GIH_KIH_5_27.mp3",
  "audio/test/GUH_KUH_3_27.mp3",
  "audio/test/BAA_PAA_3_27.mp3",
  "audio/test/BAH_PAH_3_27.mp3",
  "audio/test/BIH_PIH_1_27.mp3",
  "audio/test/BUH_PUH_3_27.mp3",
  "audio/test/DAA_TAA_3_27.mp3",
  "audio/test/DAH_TAH_3_27.mp3",
  "audio/test/DIH_TIH_3_27.mp3",
  "audio/test/DUH_TUH_3_27.mp3",
  "audio/test/GAA_KAA_5_27.mp3",
  "audio/test/GAH_KAH_3_27.mp3",
  "audio/test/GIH_KIH_5_27.mp3",
  "audio/test/GUH_KUH_3_27.mp3",
  "audio/test/BAA_PAA_3_30.mp3",
  "audio/test/BAH_PAH_3_30.mp3",
  "audio/test/BIH_PIH_1_30.mp3",
  "audio/test/BUH_PUH_3_30.mp3",
  "audio/test/DAA_TAA_3_30.mp3",
  "audio/test/DAH_TAH_3_30.mp3",
  "audio/test/DIH_TIH_3_30.mp3",
  "audio/test/DUH_TUH_3_30.mp3",
  "audio/test/GAA_KAA_5_30.mp3",
  "audio/test/GAH_KAH_3_30.mp3",
  "audio/test/GIH_KIH_5_30.mp3",
  "audio/test/GUH_KUH_3_30.mp3",
  "audio/test/BAA_PAA_3_30.mp3",
  "audio/test/BAH_PAH_3_30.mp3",
  "audio/test/BIH_PIH_1_30.mp3",
  "audio/test/BUH_PUH_3_30.mp3",
  "audio/test/DAA_TAA_3_30.mp3",
  "audio/test/DAH_TAH_3_30.mp3",
  "audio/test/DIH_TIH_3_30.mp3",
  "audio/test/DUH_TUH_3_30.mp3",
  "audio/test/GAA_KAA_5_30.mp3",
  "audio/test/GAH_KAH_3_30.mp3",
  "audio/test/GIH_KIH_5_30.mp3",
  "audio/test/GUH_KUH_3_30.mp3",
  "audio/test/BAA_PAA_3_30.mp3",
  "audio/test/BAH_PAH_3_30.mp3",
  "audio/test/BIH_PIH_1_30.mp3",
  "audio/test/BUH_PUH_3_30.mp3",
  "audio/test/DAA_TAA_3_30.mp3",
  "audio/test/DAH_TAH_3_30.mp3",
  "audio/test/DIH_TIH_3_30.mp3",
  "audio/test/DUH_TUH_3_30.mp3",
  "audio/test/GAA_KAA_5_30.mp3",
  "audio/test/GAH_KAH_3_30.mp3",
  "audio/test/GIH_KIH_5_30.mp3",
  "audio/test/GUH_KUH_3_30.mp3"
]