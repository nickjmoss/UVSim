import re

class Memory:
    memory_dict = {str(x).zfill(2): "00000" for x in range(0,100)}

    def load(self):
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

Memory()
