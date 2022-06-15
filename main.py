# The main file to run UVSimulator
import memory


def main():
    print("*** Welcome to UVSim! ***")
    memory.load()
    print("*** Program execution begins  ***\n")

    memory.read()


if __name__ == "__main__":
    main()
