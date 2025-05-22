import tkinter.font as font
from tkinter import *
from tkinter import Tk
from tkinter import ttk

global standard_font

def gfds():
    bombs: int
    safe: int
    return

def funky_func():
    input_value = bomb_input.get()

    if input_value.isdigit() == True:
        test_label.config(text=input_value)
    else:
        error_frame = Tk()
        error_frame.focus_force()
        error_frame.geometry("300x175")
        error_message = ttk.Label(error_frame, text="Numbers only!", font=standard_font)
        ttk.Button(error_frame, text="Okay", command=error_frame.destroy).place(relx=0.5, rely=0.55, anchor=CENTER)
        error_message.place(relx=0.5, rely=0.4, anchor=CENTER)
        error_frame.mainloop()

frame = Tk()
frame.geometry("400x300")
frame.focus_force()

standard_font = font.Font(family='MonaspiceKr Nerd Font', size=22, weight="normal")

test_label = ttk.Label(frame, text="test", font=standard_font)
bomb_input = ttk.Entry(frame, font=standard_font)
input_btn1 = ttk.Button(frame, text="Accept", command=funky_func)

test_label.place(relx=0.5, rely=0.4, anchor=CENTER)
bomb_input.place(relx=0.5, rely=0.55, anchor=CENTER)
input_btn1.place(relx=0.5, rely=0.7, anchor=CENTER)

frame.mainloop()
