import random
from tkinter import *
from tkinter import Tk
from tkinter import ttk

import main

global random_number
random_number = random.randrange(1, 10, 1)

class logic:

    def check_if_lose(input_value):
        input_value = input_value
        if random_number != input_value:
            return
        else:
            lose_frame = Tk()
            lose_frame.focus_force()
            lose_frame.geometry("300x175")
            lose_message = ttk.Label(lose_frame, text="Death comes for us all", font=main.standard_font)
            ttk.Button(lose_frame, text="Accept Defeat", command=quit).place(relx=0.5, rely=0.55, anchor=CENTER)
            lose_message.place(relx=0.5, rely=0.4, anchor=CENTER)
            lose_frame.mainloop()
