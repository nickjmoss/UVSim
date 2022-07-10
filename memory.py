'''
Author: Melissa Dunn
'''

import re
from tkinter import *

class Memory:

    memory_dict = {str(x).zfill(2): "00000" for x in range(0,100)}

    def read(self):
        cols = [str(x).zfill(2) for x in range(0,10)]
        rows = [str(x).zfill(2) for x in range(0,100,10)]

        print("   ", end="")
        for col in cols:
            print ("{:>6}".format(col), end="")
        print()

        for row in rows:
            print(row, end="  ")
            for col in cols:
                position = str(int(row) + int(col)).zfill(2)
                print(Memory.memory_dict[position], end=" ")
            print()

    def read_program(self, root):
        def print_on_gui(*args, sep=" ", end="\n"):
            text = sep.join(args) + end
            # Set the Text widget's state to normal so that we can edit its text
            text_widget.config(state="normal")
            # Insert the text at the end
            text_widget.insert("end", text)
            # Set the Text widget's state to disabled to disallow the user changing the text
            text_widget.config(state="disabled")

        # Create a new `Text` widget
        text_widget = Text(root, state="disabled")
        # Show the widget on the screen
        text_widget.pack(fill="both", expand=True)

        cols = [str(x).zfill(2) for x in range(0,10)]
        rows = [str(x).zfill(2) for x in range(0,100,10)]

        print_on_gui("   ", end="")
        for col in cols:
            print_on_gui("{:>6}".format(col), end="")
        print_on_gui()

        for row in rows:
            print_on_gui(row, end="  ")
            for col in cols:
                position = str(int(row) + int(col)).zfill(2)
                print_on_gui(Memory.memory_dict[position], end=" ")
            print_on_gui()

    def init(self):
        print(
            "*** Please enter your program one instruction ***\n"\
            "*** ( or data word) at a time into the input  ***\n"\
            "*** text field. I will display the location   ***\n"\
            "*** number and a question mark (?). You then  ***\n"\
            "*** type the word for that location. Enter    ***\n"\
            "*** -99999 to stop entering your program.     ***\n"\
        )

        for location in Memory.memory_dict:
            while True:
                print(f"{location} ? ", end="")

                user_input = input()

                if(user_input == "-99999"):
                    print("\n*** Program loading completed ***")
                    break

                if(re.fullmatch("^[+-]\d{4}", user_input) is None):
                    print("Invalid input. Try again.")
                else:
                    break

            if(user_input == "-99999"):
                break

            # Parse user input for memory ( + => 0 and - => 1 )
            user_input = user_input.replace("+", "0").replace("-", "1")
            Memory.memory_dict[location] = user_input

    def load_program(self, program, root):
        program = program.split("\n")
        try:
            for location, instruction in zip(Memory.memory_dict, program):
                if(instruction == "-99999"):
                    Label(fg="#0A0", text="*** Program loading completed ***").pack()
                    raise StopIteration

                if(re.fullmatch("^[+-]\d{4}", instruction) is None):
                    lbl = Label(root, fg = "#F00", text = "Invalid Entry. Re-enter program.")
                    lbl.pack()
                    break

                # Parse user input for memory ( + => 0 and - => 1 )
                instruction = instruction.replace("+", "0").replace("-", "1")
                Memory.memory_dict[location] = instruction
        except StopIteration:
            pass
