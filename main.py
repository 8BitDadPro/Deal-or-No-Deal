from tkinter import Tk
from tkinter import ttk

def gfds():
    bombs: int
    safe: int
    return

def funky_func():
    test_label.config(text=bomb_input.get())

frame = Tk()
frame.geometry("600x400")
frame.focus_force()

test_label = ttk.Label(frame, text="test")
bomb_input = ttk.Entry(frame)
input_btn1 = ttk.Button(frame, text="Accept", command=funky_func)

input_btn1.grid(column=0, row=2)
test_label.grid(column=0, row=0)
bomb_input.grid(column=0, row=1)

frame.mainloop()
