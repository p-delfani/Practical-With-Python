import speech_recognition as sr
from translate import Translator
import tkinter as tk

# Initialize the recognizer
r = sr.Recognizer()
window = tk.Tk()
window.minsize(400,400)
window.maxsize(400,400)

window.title("مبدل متن")

global counter
counter = 2

def widgets():
    lbl_start = tk.Label(window, text="صحبت کنید")
    lbl_start.config(font=("Lalezar",22,"bold"), bg="lime", width=24)
    lbl_start.grid(sticky="ne")

    frm = tk.Frame(window)
    frm.grid(row=1, pady=10)
    btn_start = tk.Button(frm, text="شروع", command=get_voice)
    btn_start.config(height=1, width=10, font=("aviny", 16), bg="blue", fg="white")
    btn_start.grid(row=1, sticky="ne")

def show_text(text):
    global counter
    lbl_name = f"lbl_{counter}"
    lbl_name = tk.Label(text=text)
    lbl_name.config(font=("aviny", 22, "bold"))
    lbl_name.grid(row=counter, column=0)
    counter += 1


def get_voice():
        try:
            with sr.Microphone() as src:
                r.adjust_for_ambient_noise(src, duration=0.2)
                audio = r.listen(src)
                
                text = r.recognize_google(audio)
                text = text.lower()
                translator = Translator(to_lang="fa")
                translation = translator.translate(text)
    
                show_text(translation)
                

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            show_text("درست تشخیص داده نشد")

widgets()
window.mainloop()