# The main file to run UVSimulator
import load_memory

def main():
    print("*** Welcome to UVSim! ***")
    load_memory.load()
    print("*** Program execution begins  ***\n")

    # TODO: This will be updated to the correct format in future work
    print(load_memory.memory_dict)

if __name__ == "__main__":
    main()
