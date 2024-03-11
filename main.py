import spacy
from googletrans import Translator

# Загрузка модели языка
nlp = spacy.load("en_core_web_sm")

#Перевод фразы
def translate_to_english(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='en')
    return translated_text.text



def extract_main_idea(text):
    # Обработка текста с помощью spaCy
    doc = nlp(text)

    # Извлечение ключевых фраз
    key_phrases = []

    # Цикл по предложениям для поиска ключевой информации
    for sentence in doc.sents:
        for token in sentence:
            if token.text.lower() in ["волосы", "рост", "кожа", "глаза", "лицо"]:
                key_phrases.append(sentence.text)

    # Удаление всех пустых строк
    key_phrases = list(filter(None, key_phrases))

    # Удаление повторяющихся фраз
    key_phrases = list(set(key_phrases))

    # Преобразование множества обратно в список
    key_phrases = list(key_phrases)

    # Возвращаем результат в виде ключевых фраз
    return key_phrases

#Переработка фразы
def process_sentences(sentences):
    phrases = []

    # Слова-союзы и слова-предлоги
    conjunctions = ['и', 'а', 'но', 'или', 'либо', 'что', 'как',
                    'между', 'над', 'под', 'за', 'перед', 'на', 'с', 'у',
                    'от', 'до', 'в', 'из', 'о', 'по']

    for sentence in sentences:
        # Разделение предложения на фразы по запятым
        split_phrases = sentence.split(',')

        # Объединение фраз с исключением, если после запятой идет слово "как"
        new_phrase = split_phrases[0]
        for phrase in split_phrases[1:]:
            if phrase.strip().startswith('как '):
                # Если после запятой идет "как", то объединяем фразы без разделения
                new_phrase += ',' + phrase
            else:
                # Добавляем фразу в список фраз
                phrases.append(new_phrase)
                new_phrase = phrase

        # Добавляем последнюю фразу в список фраз
        phrases.append(new_phrase.strip())

    # Удаление предлогов или союзов в начале фразы и точек в конце словосочетаний
    new_phrases = []
    for phrase in phrases:
        # Разделение фразы на слова
        words = phrase.split()

        # Проверка, является ли первое слово предлогом или союзом
        if words and words[0].lower() in conjunctions:
            # Удаление предлога или союза в начале фразы
            words = words[1:]

        # Удаление точки в конце, если таковая имеется
        last_word = words[-1]
        if last_word.endswith('.'):
            words[-1] = last_word.rstrip('.')

        # Формирование фразы
        new_phrase = ' '.join(words)

        # Добавление фразы в новый список
        new_phrases.append(new_phrase)

    return new_phrases

#
def check_phrases(phrases):
    phrases_to_move = []

    for phrase in phrases:
        # Проверка наличия фразы в словосочетании
        if "выглядит как" in phrase.lower() or \
        "внешность" in phrase.lower() or \
        "внешностью" in phrase.lower() or \
        "внешне" in phrase.lower():
            phrases_to_move.append(phrase)

    # Перемещение фраз в начало списка
    for phrase in phrases_to_move:
        phrases.remove(phrase)
        phrases.insert(0, phrase)

    return phrases

#Объединение Промпта
def add_phrases_to_string(input_string, phrases):
    phrases_string = ', '.join(phrases)
    output_string = input_string + ', ' + phrases_string
    return output_string


# Пример использования
input_text = """
Высокий прямоходящий муравей-химера с преобладанием черт гепарда. Конечности сегментированы, как у насекомого, ступни и ладони четырёхпалые с парными когтями. Туловище сухое мускулистое, с длинными жилами. Основной окрас желтый, на бёдрах и груди белый мех с черными леопардовыми пятнышками. Волосы малиновые короткие, на лице-морде слезные дорожки, как у гепарда. Из одежды на Читу только обрезанные джинсовые мини-шортики.
"""



main_idea = extract_main_idea(input_text)
print("Основная мысль текста с описанием внешности персонажа:")
for phrase in main_idea:
    print(phrase)