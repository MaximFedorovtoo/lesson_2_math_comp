## Задача 1
turist = 90 # количество туристов
det_know = 30 # знают немецки   
en_know = 28 # знают англиский
fr_know = 42 # знают француский
en_and_det = 8 # ают англиский и немецкий
en_and_fr = 10 # знают англиский и француский
det_fr = 5 # знают немецкий и француский
all_lang = 3 # знают все языки
v_out_all_det_fr = det_fr - all_lang # знают только немецкий и француский
v_out_all_en_det = en_and_det - all_lang # знают только англиский и немеций
v_out_all_en_fr = en_and_fr - all_lang # знают только англиский и француский
only_det = det_know - (v_out_all_det_fr + v_out_all_en_det + all_lang) # только немецкий
only_en = en_know - (v_out_all_en_det + v_out_all_en_fr + all_lang) # только англиский
only_fr = fr_know - (v_out_all_en_fr + v_out_all_det_fr + all_lang) # только француский
no_foring_lang = turist - (only_det + only_en + only_fr + all_lang + v_out_all_det_fr +v_out_all_en_det + v_out_all_en_fr) # не знают иностранных языков
print(f'Туристов не говорящих на иностранных языках {no_foring_lang}')
