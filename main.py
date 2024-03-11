import spacy

# Загрузка модели языка
nlp = spacy.load("en_core_web_sm")

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




# Пример использования
input_text = """
Высокий прямоходящий муравей-химера с преобладанием черт гепарда. Конечности сегментированы, как у насекомого, ступни и ладони четырёхпалые с парными когтями. Туловище сухое мускулистое, с длинными жилами. Основной окрас желтый, на бёдрах и груди белый мех с черными леопардовыми пятнышками. Волосы малиновые короткие, на лице-морде слезные дорожки, как у гепарда. Из одежды на Читу только обрезанные джинсовые мини-шортики.
"""



main_idea = extract_main_idea(input_text)
print("Основная мысль текста с описанием внешности персонажа:")
for phrase in main_idea:
    print(phrase)