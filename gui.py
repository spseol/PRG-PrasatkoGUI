#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from PIL import Image, ImageTk
from prasatko import Prasatko

# from tkinter import ttk


class Application(tk.Tk):
    name = "Prasátko"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Prasátko")
        self.lbl.pack()
        imaghandler = Image.open("img/prasatko.png")
        tkimage = ImageTk.PhotoImage(imaghandler)
        self.img = tk.Label(self, image=tkimage)
        self.img.image = tkimage
        self.img.pack()
        self.entry = tk.Entry(self)
        self.entry.insert(0, 1234)
        self.entry.pack()

        text = """1000 x 1
200 x 1
20 x 1
10 x 1
2 x 2
"""
        self.message = tk.Message(self, text=text)
        self.message.pack()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
