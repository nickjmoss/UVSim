# The main file to run UVSimulator
import memory
import branch
import registers

def main():
    print("*** Welcome to UVSim! ***")
    memory.load()
    print("*** Program execution begins  ***\n")

    mem_dict = memory.memory_dict
    
    #op_codes is list with all opperand codes with "0" at beggining indecated for positive num
    op_codes = ["010", "011", "020", "021", "030", "031", "032", "033", "040", "041", "042", "043"]

    #iteration count is used for branching
    iter_count = 0

    while iter_count != 100:
        
        #If iteration less than ten, convert to string, and add zero at beginning
        if iter_count < 10:
            word = "0"+str(iter_count)
        #Else: just convert to string
        else:
            word = str(iter_count)
        
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
                branch.branch(mem_dict[word][3:])
                iter_count = int(mem_dict[word][3:])
                continue      

            if op_code == "041":
                if int(registers.registers["ACC"]) < 0:
                    branch.branch(mem_dict[word][3:])
                    iter_count = int(mem_dict[word][3:])
                    continue

            if op_code == "042":
                if int(registers.registers["ACC"]) == 0:
                    branch.branch(mem_dict[word][3:])
                    iter_count = int(mem_dict[word][3:])
                    continue

            if op_code == "043":
                break
 
        #Update Iteration count and assign PC

        iter_count += 1
        registers.registers["PC"] = str(iter_count)
    
    memory.read()

if __name__ == "__main__":
    main()
