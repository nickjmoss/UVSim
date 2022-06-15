# The main file to run UVSimulator
import memory

def main():
    print("*** Welcome to UVSim! ***")
    memory.load()
    print("*** Program execution begins  ***\n")


    pointer = "00"

    #accumulator is a string used to store one value for use of operands
    accumulator = "00"

    #op_count is the number of opperands entered
    op_count = 0
    
    #op_codes is list with all opperand codes with "0" at beggining indecated for positive num
    op_codes = ["010", "011", "020", "021", "030", "031", "032", "033", "040", "041", "042", "043"]

    for word in mem_dict.keys():

        op_code = mem_dict[word][:3]

        if op_code in op_codes:

            #fuctions will be called in order corrisponding to their identifiers

            if op_code == "010":
                #TODO: import Read function here
                pass
            
            if op_code == "011":
                #TODO: import Write function here
                pass

            if op_code == "020":
                #TODO: import Load function
                pass

            if op_code == "021":
                #TODO: import Store function
                pass

            if op_code == "030":
                #TODO: import Add function
                pass

            if op_code == "031":
                #TODO: import Subtract function
                pass

            if op_code == "032":
                #TODO: import Mulitiply function
                pass
            
            if op_code == "033":
                #TODO: import Devide function
                pass

            if op_code == "040":
                #TODO: import Branch function
                pass

            if op_code == "041":
                #TODO: import BranchNeg function
                pass

            if op_code == "042":
                #TODO: import BranchZero function
                pass

            if op_code == "043":
                #TODO: import Halt function
                pass
    memory.read()

if __name__ == "__main__":
    main()
