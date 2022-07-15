'''
Author: Melissa Dunn
'''

import re
import base32
from tkinter import *

class Memory:

    memory_dict = {str(x).zfill(2): "A" for x in range(0,100)}

 
    def store(self,location, input):
        '''Author: Kyle Meiners'''
        input = input.replace('1','-')
        dec = int(input)
        b32 = base32.dec_to_b32(dec)
        Memory.memory_dict[location] = b32

    
    def get(self, location):
        '''Author: Kyle Meiners'''
        b32 = Memory.memory_dict[location]
        dec = base32.b32_to_dec(b32)
        if dec < 0:
            dec = str(dec)
            dec += '1'
            return dec
        else:
            dec = str(dec)
            dec = '0' + dec
            return dec


    def reset(self):
        Memory.memory_dict = {str(x).zfill(2): "00000" for x in range(0,100)}

    def read(self):
        cols = [str(x).zfill(2) for x in range(0,10)]
        rows = [str(x).zfill(2) for x in range(0,100,10)]

        print("   ", end="")
        for col in cols:
            print ("{:>6}".format(col), end=" ")
        print()

        for row in rows:
            print(row, end="  ")
            for col in cols:
                position = str(int(row) + int(col)).zfill(2)
                print("{:>6}".format(Memory.get(position)), end=" ")
            print()

    def read_gui(self, text_widget):
        def print_on_gui(*args, sep=" ", end="\n"):
            text = sep.join(args) + end
            # Set the Text widget's state to normal so that we can edit its text
            text_widget.config(state="normal")
            # Insert the text at the end
            text_widget.insert("end", text)
            # Set the Text widget's state to disabled to disallow the user changing the text
            text_widget.config(state="disabled")

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
            Memory.store(location, user_input)

    def load_gui(self, program):
        program = program.split("\n")
        try:
            for location, instruction in zip(Memory.memory_dict, program):
                if(instruction == "-99999"):
                    Label(fg="#0A0", text="*** Program loading completed ***").pack()
                    raise StopIteration

                if(re.fullmatch("^[+-]\d{4}", instruction) is None):
                    return False

                # Parse user input for memory ( + => 0 and - => 1 )
                instruction = instruction.replace("+", "0").replace("-", "1")
                Memory.memory_dict[location] = instruction
        except StopIteration:
            pass

