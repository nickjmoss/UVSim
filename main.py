# The main file to run UVSimulator
import memory
from math_ops import Math_ops
import branch
import load
import store
import registers
from io_ops import Io_ops

def main():
	print("*** Welcome to UVSim! ***")
	memory.init()
	print("*** Program execution begins  ***\n")

	mem_dict = memory.memory_dict

	# op_codes is list with all opperand codes with "0" at beggining indecated for positive num
	op_codes = ["010","011","020","021","030","031","032","033","040","041","042","043"]

	#iteration count is used for branching
	iter_count = 0
	calc = Math_ops()
	io = Io_ops()

	while iter_count != 100:

		#If iteration less than ten, convert to string, and add zero at beginning
		if iter_count < 10:
			word = "0"+str(iter_count)
		#Else: just convert to string
		else:
			word = str(iter_count)

		op_code = mem_dict[word][:3]
		location = mem_dict[word][-2:]

		if op_code in op_codes:
			# fuctions will be called in order corrisponding to their identifiers

			if op_code == "010":
				'''Author: Melissa Dunn'''
				io.read(location)

			if op_code == "011":
				'''Author: Melissa Dunn'''
				io.write(location)

			if op_code == "020":
				'''Author: Nick Moss'''
				load.load(location)

			if op_code == "021":
                #Author Gavin Doel
				store.store(mem_dict[word][3:])

			if op_code == "030":
				'''Author: Nick Moss'''
				result = calc.add(location)
				if result is False:
					print("The sum of the values was too big or too small to handle")
					break

			if op_code == "031":
				'''Author: Nick Moss'''
				result = calc.subtract(location)
				if result is False:
					print("The difference of the values was too big or too small to handle")
					break

			if op_code == "032":
				'''Author: Nick Moss'''
				result = calc.multiply(location)
				if result is False:
					print("The product of the values was too big or too small to handle")
					break

			if op_code == "033":
				'''Author: Nick Moss'''
				result = calc.divide(location)
				if result is False:
					print("The difference of the values was too big or too small to handle, or there was a division by zero")
					break

			if op_code == "040":
                #Author: Gavin Doel
				branch.branch(mem_dict[word][3:])
				iter_count = int(mem_dict[word][3:])

			if op_code == "041":
                #Author: Gavin Doel
				if int(registers.registers["ACC"]) < 0:
					branch.branch(mem_dict[word][3:])
					iter_count = int(mem_dict[word][3:])


			if op_code == "042":
                #Author: Gavin Doel
				if int(registers.registers["ACC"]) == 0:
					branch.branch(mem_dict[word][3:])
					iter_count = int(mem_dict[word][3:])


			if op_code == "043":
				break

		#Update Iteration count and assign PC
		iter_count += 1
		registers.registers["PC"] = str(iter_count)

	print("\nMEMORY:")
	memory.read()

if __name__ == "__main__":
	main()
