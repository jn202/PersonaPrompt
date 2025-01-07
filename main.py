from Def.List_sentense import _list_sentensis
from Def.Phrases_work import *
from Def.Translator_Method import translate_to_english
import requests, base64, os
from tkinter import Tk, Text,Frame, Button, Label, messagebox

'''
# Пример фразы
input_text = """
Высокий прямоходящий муравей-химера с преобладанием черт гепарда. Конечности сегментированы, как у насекомого, ступни и ладони четырёхпалые с парными когтями. Туловище сухое мускулистое, с длинными жилами. Основной окрас желтый, на бёдрах и груди белый мех с черными леопардовыми пятнышками. Волосы малиновые короткие, на лице-морде слезные дорожки, как у гепарда. Из одежды на Читу только обрезанные джинсовые мини-шортики.

Сон Джин Ву - персонаж из манхвы Solo Leveling. Работает "Охотником". Суть работы заключается в уничтожении монстров из порталов. По национальности - Южный Кореец. Рост высокий, телосложение спортивное. Цвет волос чёрный, глаза ярко синие. Длина волос средняя. Одет обычно в чёрное пальто, черную рубашку, чёрные брюки и чёрные туфли. Обладает силой управлять тенями, поэтому часто появляется с особой теневой аурой. 
"""'''


def analyze_text():
    text = input_text.get("1.0", "end-1c")
    # поиск ои=писывающих предложений
    main_idea = _list_sentensis(text)
    # работа над промптом
    phrases = process_sentences(main_idea)
    phrases_list = sequence_phrases(phrases)
    # дополняющачя фраза (опционально)
    Last_Phrase = ""

    # Промпт на русском
    Rus_prompt = add_phrases_to_string(Last_Phrase, phrases_list)

    # Промпт на английском
    Translated_prompt = translate_to_english(Rus_prompt)


    label1.config(text=Rus_prompt)
    label2.config(text=Translated_prompt)

def copy_text():
    # selected_text = label1.cget("text") or label2.cget("text")
    selected_text = label2.cget("text")
    root.clipboard_clear()
    root.clipboard_append(selected_text)
    messagebox.showinfo("Копирование", "Текст скопирован в буфер обмена")

def paste_text():
    clipboard_text = root.clipboard_get()
    input_text.delete("1.0", "end")
    input_text.insert("1.0", clipboard_text)

def send_text():
    selected_text = label2.cget("text")
    root.clipboard_clear()
    root.clipboard_append(selected_text)
    # URL-адрес для отправки prompt во вкладке txt2img Stable Diffusion
    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    # Строка prompt для отправки
    prompt_string = selected_text
    # Отправка POST запроса с использованием библиотеки requests
    payload = {'prompt': prompt_string,
               'steps': 30}

    response = requests.post(url, json=payload)

    # Проверка успешности отправки
    if response.status_code == 200:
        answer = "Строка prompt успешно отправлена в Stable Diffusion во вкладке txt2img."
    else:
        answer = "Произошла ошибка при отправке строки prompt."
    messagebox.showinfo("Ответ", answer)
    response_json = response.json()

    # Получить список всех файлов в папке
    files = os.listdir("Images")

    # Подсчитать количество файлов JPG
    num_jpg_files = 0

    for filename in files:
        # Разбиваем название файла по '_' и '.jpg'
        parts = filename.split('_')[1].split('.')[0]

        # Проверяем, является ли часть названия числом
        if parts.isdigit():
            number = int(parts)
            if number > num_jpg_files:
                num_jpg_files = number

    # сохранение файлов JPG
    img_name=os.path.join("Images", f"image_{num_jpg_files+1}.jpg")
    with open(img_name, 'wb') as f:
        f.write(base64.b64decode(response_json['images'][0]))
    os.startfile(img_name)


root = Tk()
root.title("PersonaPrompt")
root.geometry("400x600")

input_height = int(root.winfo_height() * 0.3)
label_height = int(root.winfo_height() * 0.2)

input_text = Text(root, height=input_height, wrap="word")
input_text.pack(fill="both", expand=True)

button_frame = Frame(root)
button_frame.pack()

analyze_button = Button(button_frame, text="Анализ", command=analyze_text)
analyze_button.pack(side="left", padx=10)

paste_button = Button(button_frame, text="Вставить текст", command=paste_text)
paste_button.pack(side="left", padx=10)

label_frame = Frame(root, padx=10)
label_frame.pack(fill="both", expand=True)

label1 = Label(label_frame, text="", height=label_height, wraplength=380, justify="center", anchor="center", bd=1, relief="solid")
label1.pack(fill="both", expand=True)

label2 = Label(label_frame, text="", height=label_height, wraplength=380, justify="center", anchor="center", bd=1, relief="solid")
label2.pack(fill="both", expand=True)

copy_button = Button(root, text="Копировать", command=copy_text)
copy_button.pack(side="left", padx=10)

send_button = Button(root, text="Отправить текст", command=send_text)
send_button.pack(side="right", padx=10)

root.mainloop()
