from Def.List_sentense import _list_sentensis
from Def.Phrases_work import *
from Def.Translator_Method import translate_to_english

# Пример фразы
input_text = """
Высокий прямоходящий муравей-химера с преобладанием черт гепарда. Конечности сегментированы, как у насекомого, ступни и ладони четырёхпалые с парными когтями. Туловище сухое мускулистое, с длинными жилами. Основной окрас желтый, на бёдрах и груди белый мех с черными леопардовыми пятнышками. Волосы малиновые короткие, на лице-морде слезные дорожки, как у гепарда. Из одежды на Читу только обрезанные джинсовые мини-шортики.
"""

main_idea = _list_sentensis(input_text)
print("Основная мысль текста с описанием внешности персонажа:")

phrases = process_sentences(main_idea)

phrases_list = sequence_phrases(phrases)
Last_Phrase=""
Rus_prompt = add_phrases_to_string(Last_Phrase, phrases_list)
print(Rus_prompt)

Translated_prompt = translate_to_english(Rus_prompt)
print("Английский промпт:\n" + Translated_prompt)
