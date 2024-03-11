#Переработка фразы
def process_sentences(sentences):
    phrases = []

    # Слова-союзы и слова-предлоги
    conjunctions = ['и', 'а', 'но', 'или', 'либо', 'что', 'у',
                    'между', 'над', 'под', 'за', 'перед',
                    'от', 'до', 'в', 'о', 'с', 'по' ]

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

#Задание последовательности фраз
def sequence_phrases(phrases):
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

#Объединение в Промпт
def add_phrases_to_string(input_string, phrases):
    phrases_string = ', '.join(phrases)
    output_string = phrases_string + ', ' + input_string
    return output_string