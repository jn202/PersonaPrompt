import requests

def send_mechanizm(string_prompt):
    # URL-адрес для отправки prompt во вкладке txt2img Stable Diffusion
    url = "http://127.0.0.1:7860/api/prompt"

    # Строка prompt для отправки
    prompt_string = string_prompt

    # Отправка POST запроса с использованием библиотеки requests
    response = requests.post(url, data={"txt2img": prompt_string})

'''
    # Проверка успешности отправки
        if response.status_code == 200:
            print("Строка prompt успешно отправлена в Stable Diffusion во вкладке txt2img.")
        else:
            print("Произошла ошибка при отправке строки prompt.")
'''

