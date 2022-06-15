# The main file to run UVSimulator
import memory


def main():
	print("*** Welcome to UVSim! ***")
	memory.load()
	print("*** Program execution begins  ***\n")
	for operation in memory.memory_dict:
		return
	memory.read()


if __name__ == "__main__":
	main()
