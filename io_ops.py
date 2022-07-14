'''
Author: Melissa Dunn
'''

import re

class IO:
    def read(self, location, memory):
        '''Read a word from the keyboard into a specific location in memor'''

        while True:
            print("Enter an integer: ", end="")

            user_input = input()

            if(re.fullmatch("^[+-]?\d{1,4}", user_input) is None):
                print("Invalid input. Try again.")
            else:
                break
        user_input = user_input.replace("+", "0").replace("-", "1")
        memory.store(location, (user_input).zfill(5)

    def write(self, location, memory):
        '''Write a word from a specific location in memory to screen.'''

        output = re.sub(r'^1', "-", memory.memory_dict[location])
        output = re.sub(r'^1', "-", memory.get(location))
        print(f"Contents of {int(location)} is {int(output)}")
