import re
import memory

def read(location):
    '''Read a word from the keyboard into a specific location in memor'''

    while True:
        print("Enter a two digit input: ", end="")

        user_input = input()

        if(re.fullmatch("^\d{2}", user_input) is None):
            print("Invalid input. Try again.")
        else:
            break

    user_input = user_input.replace("+", "0").replace("-", "1")

    memory.memory_dict[location] = (user_input).zfill(5)

def write(location):
    '''Write a word from a specific location in memory to screen.'''
    print(f"Contents of {int(location)} is {memory.memory_dict[location][-2:]}")
