'''
Author: Melissa Dunn
'''

import re
import tkinter as tk

class IO:
    def read(self, location, memory):
        error_message = tk.Label(fg="#F0F0F0", text="Invalid input. Try again.")

        '''Read a word from the keyboard into a specific location in memory'''
        def enter():
            user_input = inputtxt.get(1.0, "end-1c")

            if(re.fullmatch("^[+-]?\d{1,4}", user_input) is None):
                error_message.config(fg="#A00")
                return
            else:
                error_message.config(fg="#F0F0F0")

            user_input = user_input.replace("+", "0").replace("-", "1")
            memory.memory_dict[location] = (user_input).zfill(5)
        tk.Label(fg="#000", text="Enter an integer:").pack()
        inputtxt = tk.Text(height = 1, width = 5, fg="#fff")
        inputtxt.pack()

        printbutton = tk.Button(text="Enter", fg="#000", command=enter)
        error_message.pack()
        printbutton.pack()

    def write(self, location, memory):
        '''Write a word from a specific location in memory to screen.'''
        output = re.sub(r'^1', "-", memory.memory_dict[location])
        tk.Label(fg="#000", text=f"Contents of {int(location)} is {int(output)}").pack()
