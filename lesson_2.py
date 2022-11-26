## Задача 1
turist = 90
det_know = 30
en_know = 28
fr_know = 42
en_and_det = 8
en_and_fr = 10
det_fr = 5
all_lang = 3
v_out_all_det_fr = det_fr - all_lang
v_out_all_en_det = en_and_det - all_lang
v_out_all_en_fr = en_and_fr - all_lang
only_det = det_know - (v_out_all_det_fr + v_out_all_en_det + all_lang)
only_en = en_know - (v_out_all_en_det + v_out_all_en_fr + all_lang)
only_fr = fr_know - (v_out_all_en_fr + v_out_all_det_fr + all_lang)
no_foring_lang = turist - (only_det + only_en + only_fr + all_lang + v_out_all_det_fr +v_out_all_en_det + v_out_all_en_fr)
print(f'Туристов не говорящих на иностранных языках {no_foring_lang}')