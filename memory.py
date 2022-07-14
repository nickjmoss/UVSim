'''
Author: Melissa Dunn
'''

import re
import base32
class Memory:

    memory_dict = {str(x).zfill(2): "00000" for x in range(0,100)}

    def store(location, input):
        '''Author: Kyle Meiners'''
        dec = int(input)
        b32 = base32.dec_to_b32(dec)
        Memory.memory_dict[location] = b32

    def get(location):
        '''Author: Kyle Meiners'''
        b32 = Memory.memory_dict[location]
        dec = base32.b32_to_dec(b32)
        dec = str(dec)
        return dec


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
            Memory.store(location, user_input)
