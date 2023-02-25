import tkinter as tk
from tkinter import scrolledtext

import classes_keybord
import classes_word

win = tk.Tk()
win.geometry('300x350+1000+100')

frame_1 = tk.Frame(win, bg='red', width=300, height=250)
frame_2 = tk.Frame(win, bg='yellow', width=300, height=100)

listbox = scrolledtext.ScrolledText(frame_1, width=10, height=11)
btn_1 = tk.Button(frame_1, text='hello')

frame_1.pack(expand=True, anchor='w')
frame_2.pack(expand=True)

listbox.place(x=200, y=3)


a = classes_word.ButtonWord(frame_1, frame_2, listbox)
b = classes_keybord.ButtonKeybord(frame_2, a)

tk.mainloop()