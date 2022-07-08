'''
Author: Melissa Dunn
'''

import re
from tkinter import *

class IO:
    def read(self, location, memory):
        '''Read a word from the keyboard into a specific location in memor'''
        def enter():
            user_input = inputtxt.get(1.0, "end-1c")

            if(re.fullmatch("^[+-]?\d{1,4}", user_input) is None):
                print("Invalid input. Try again.")

            user_input = user_input.replace("+", "0").replace("-", "1")
            memory.memory_dict[location] = (user_input).zfill(5)
        Label(fg="#000", text="Enter an integer:").pack()
        inputtxt = Text(height = 5, width = 20, fg="#fff")
        inputtxt.pack()

        printbutton = Button(text="Enter", fg="#000", command=enter)
        printbutton.pack()

        # while True:
        #     print("Enter an integer: ", end="")

        #     user_input = input()

        #     if(re.fullmatch("^[+-]?\d{1,4}", user_input) is None):
        #         print("Invalid input. Try again.")
        #     else:
        #         break
        # user_input = user_input.replace("+", "0").replace("-", "1")
        # memory.memory_dict[location] = (user_input).zfill(5)

    def write(self, location, memory):
        '''Write a word from a specific location in memory to screen.'''

        output = re.sub(r'^1', "-", memory.memory_dict[location])
        Label(fg="#000", text=f"Contents of {int(location)} is {int(output)}").pack()
