import tkinter as tk
from tkinter import scrolledtext
import classes_word

win = tk.Tk()
win.geometry('300x350+1000+100')

frame_1 = tk.Frame(win, bg='red', width=300, height=250)
frame_2 = tk.Frame(win, bg='yellow', width=300, height=100)
listbox = scrolledtext.ScrolledText(frame_1, width=10, height=11)
entry = tk.Entry(frame_2, width=10)

frame_1.pack(expand=True, anchor='w')
frame_2.pack(expand=True)
listbox.place(x=200, y=3)
entry.place(x=50, y=40)

a = classes_word.ButtonWord(frame_1, frame_2, listbox, entry)


tk.mainloop()
