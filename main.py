# import requests
# import voicerss_tts

import PyPDF2
import tkinter as tk
from tkinter import filedialog

import pyttsx3
import pygame

pygame.mixer.init()
engine = pyttsx3.init()

# API_KEY = ""
# ENDPOINT = "http://api.voicerss.org/"

win = tk.Tk()
win.title('Text Reader')
win.rowconfigure(0, minsize=200, weight=1)
win.columnconfigure(1, minsize=300, weight=1)

txt = tk.Text(win)
txt.grid(row=0, column=1, sticky="nsew")


# Function to open the PDF file
def open_pdf():
    # Open file
    file = filedialog.askopenfilename(title='Select a PDF', filetype=(('PDF Files', '*.pdf'), ('All Files', '*.*')))
    if file:
        # Create a pdf reader object
        pdf_file = PyPDF2.PdfFileReader(file)
        # Get the number of pages
        pages = pdf_file.numPages
        global content
        content = ""

        for p in range(pages):
            page = pdf_file.getPage(p)
            content += page.extractText()
            txt.insert(1.0, content)


# Function to Quit the window
def quit_app():
    win.destroy()


# Function to read the text
def read():
    # ------------Use pyttsx3

    outfile = "temp.wav"
    engine.save_to_file(txt.get('1.0', tk.END), outfile)
    engine.runAndWait()
    pygame.mixer.music.load(outfile)
    pygame.mixer.music.play()

    # ------------Use API
    # voice = voicerss_tts.speech({
    #     "key": API_KEY,
    #     "hl": "en-us",
    #     "src": content
    # })
    # print(voice)
    # response = requests.get(ENDPOINT, params=voice)
    # response.raise_for_status()
    # print(response)


def pause():
    pygame.mixer.music.pause()


# Function to clear the text
def unpause():
    pygame.mixer.music.unpause()


frm_buttons = tk.Frame(win, relief=tk.RAISED, bd=2)
frm_buttons.grid(row=0, column=0, sticky="ns")

btn_open = tk.Button(frm_buttons, text="Open PDF", command=open_pdf)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_read = tk.Button(frm_buttons, text='Read', command=read)
btn_read.grid(row=1, column=0, sticky="ew", padx=5)

btn_stop = tk.Button(frm_buttons, text='Pause', command=pause)
btn_stop.grid(row=2, column=0, sticky="ew", padx=5)

btn_clear = tk.Button(frm_buttons, text='Unpause', command=unpause)
btn_clear.grid(row=3, column=0, sticky="ew", padx=5)

btn_quit = tk.Button(frm_buttons, text='Quit App', command=quit_app)
btn_quit.grid(row=4, column=0, sticky="ew", padx=5)

win.mainloop()
