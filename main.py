# The main file to run UVSimulator
import memory as mem
import math_ops
import branch
import load
import store
import registers
import io_ops

def main():
	math = math_ops.Math_Ops()
	memory = mem.Memory()
	io = io_ops.IO()
	br = branch.Branch()

	print("*** Welcome to UVSim! ***")
	memory.init()
	print("*** Program execution begins  ***\n")

	mem_dict = memory.memory_dict

	# op_codes is list with all opperand codes with "0" at beggining indecated for positive num
	op_codes = ["010","011","020","021","030","031","032","033","040","041","042","043"]

	#iteration count is used for branching
	iter_count = 0

	while iter_count != 100:

		#If iteration less than ten, convert to string, and add zero at beginning
		if iter_count < 10:
			word = "0"+str(iter_count)
		#Else: just convert to string
		else:
			word = str(iter_count)

		op_code = memory.get(word)[:3]
		location = memory.get(word)[-2:]

		if op_code in op_codes:
			# fuctions will be called in order corrisponding to their identifiers

			if op_code == "010":
				'''Author: Melissa Dunn'''
				io.read(location, memory)

			if op_code == "011":
				'''Author: Melissa Dunn'''
				io.write(location, memory)

			if op_code == "020":
				'''Author: Nick Moss'''
				load.load(location, memory)

			if op_code == "021":
				'''Author Gavin Doel'''
				store.store(location, memory)

			if op_code == "030":
				'''Author: Nick Moss'''
				result = math.add(location, memory)
				if result is False:
					print("The sum of the values was too big or too small to handle")
					break

			if op_code == "031":
				'''Author: Nick Moss'''
				result = math.subtract(location, memory)
				if result is False:
					print("The difference of the values was too big or too small to handle")
					break

			if op_code == "032":
				'''Author: Nick Moss'''
				result = math.multiply(location, memory)
				if result is False:
					print("The product of the values was too big or too small to handle")
					break

			if op_code == "033":
				'''Author: Nick Moss'''
				result = math.divide(location, memory)
				if result is False:
					print("The difference of the values was too big or too small to handle, or there was a division by zero")
					break

			if op_code == "040":
				'''Author: Gavin Doel'''
				br.branch(location)
				iter_count = int(location)
				continue

			if op_code == "041":
				'''Author: Gavin Doel'''
				if int(registers.reg_get("ACC")) < 0:
					br.branch(location)
					iter_count = int(location)
					continue


			if op_code == "042":
				'''Author: Gavin Doel'''
				if int(registers.reg_get("ACC")) == 0:
					br.branch(location)
					iter_count = int(location)
					continue


			if op_code == "043":
				break

		#Update Iteration count and assign PC
		iter_count += 1
		registers.registers["PC"] = str(iter_count)

	print("\nMEMORY:")
	memory.read()


if __name__ == "__main__":
	main()
