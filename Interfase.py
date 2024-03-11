from Def.List_sentense import _list_sentensis
from Def.Phrases_work import *
from Def.Translator_Method import translate_to_english

from tkinter import Tk, Text,Frame, Button, Label, messagebox

def analyze_text():
    text = input_text.get("1.0", "end-1c")
    label1.config(text=text)
    label2.config(text=text)

def copy_text():
    selected_text = label1.cget("text") or label2.cget("text")
    root.clipboard_clear()
    root.clipboard_append(selected_text)
    messagebox.showinfo("Копирование", "Текст скопирован в буфер обмена")

def paste_text():
    clipboard_text = root.clipboard_get()
    input_text.delete("1.0", "end")
    input_text.insert("1.0", clipboard_text)

root = Tk()
root.title("")
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

label1 = Label(label_frame, text="", height=label_height, wraplength=int(root.winfo_width() * 0.8), justify="center", anchor="center", bd=1, relief="solid")
label1.pack(fill="both", expand=True)

label2 = Label(label_frame, text="", height=label_height, wraplength=int(root.winfo_width() * 0.8), justify="center", anchor="center", bd=1, relief="solid")
label2.pack(fill="both", expand=True)

copy_button = Button(root, text="Копировать", command=copy_text)
copy_button.pack()

root.mainloop()
