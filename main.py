# The main file to run UVSimulator
import memory
import math_ops
import registers
import branch
import load


def main():
	print("*** Welcome to UVSim! ***")
	memory.init()
	print("*** Program execution begins  ***\n")

	mem_dict = memory.memory_dict

	# op_codes is list with all opperand codes with "0" at beggining indecated for positive num
	op_codes = ["010","011","020","021","030","031","032","033","040","041","042","043"]

	for word in mem_dict.keys():
		op_code = mem_dict[word][:3]
		location = mem_dict[word][-2:]

		if op_code in op_codes:
			# fuctions will be called in order corrisponding to their identifiers

			if op_code == "010":
				# TODO: import Read function here
				pass

			if op_code == "011":
				# TODO: import Write function here
				pass

			if op_code == "020":
				load.load(location)
				continue

			if op_code == "021":
				# TODO: import Store function
				pass

			if op_code == "030":
				result = math_ops.add(location)
				if result is False:
					print("The sum of the values was too big too handle")
					break
				continue

			if op_code == "031":
				# TODO: import Subtract function
				pass

			if op_code == "032":
				# TODO: import Mulitiply function
				pass

			if op_code == "033":
				# TODO: import Devide function
				pass

			if op_code == "040":
				branch.branch(mem_dict[word][3:])
				continue

			if op_code == "041":
				# TODO: import BranchNeg function
				pass

			if op_code == "042":
				# TODO: import BranchZero function
				pass

			if op_code == "043":
				# TODO: import Halt function
				pass

			# TODO: PC will be updated to next memory location
	memory.read()


if __name__ == "__main__":
	main()
