# The main file to run UVSimulator
def main():
    print(
        "*** Welcome to UVSim! ***\n"\
        "*** Please enter your program one instruction ***\n"\
        "*** ( or data word) at a time into the input  ***\n"\
        "*** text field. I will display the location   ***\n"\
        "*** number and a question mark (?). You then  ***\n"\
        "*** type the word for that location. Enter    ***\n"\
        "*** -99999 to stop entering your program.     ***\n"\
        )

    memory = {str(x).zfill(2): "00000" for x in range(0,100)}

    for location in memory:
        print(f"{location} ? ", end="")
        user_input = input()

        if(user_input == "-99999"):
            print(
                "\n*** Program loading completed ***\n"\
                "*** Program execution begins  ***\n"\
            )
            break

        # Parse user input for memory ( + => 0 and - => 1 )
        user_input = user_input.replace("+", "0").replace("-", "1")
        memory[location] = user_input

    # TODO: This will be updated to the correct format in future work
    print(memory)

main()
