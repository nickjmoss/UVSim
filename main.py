# The main file to run UVSimulator
import memory
import math_ops
import branch
import load
import store
import registers
import io_ops

def main():
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

		op_code = mem_dict[word][:3]
		location = mem_dict[word][-2:]

		if op_code in op_codes:
			# fuctions will be called in order corrisponding to their identifiers

			if op_code == "010":
				io_ops.read(location)
			
			if op_code == "011":
				io_ops.write(location)

			if op_code == "020":
				load.load(location)

			if op_code == "021":
				store.store(mem_dict[word][3:])

			if op_code == "030":
				result = math_ops.add(location)
				if result is False:
					print("The sum of the values was too big or too small to handle")
					break

			if op_code == "031":
				result = math_ops.subtract(location)
				if result is False:
					print("The difference of the values was too big or too small to handle")
					break

			if op_code == "032":
				result = math_ops.multiply(location)
				if result is False:
					print("The product of the values was too big or too small to handle")
					break

			if op_code == "033":
				result = math_ops.divide(location)
				if result is False:
					print("The difference of the values was too big or too small to handle, or there was a division by zero")
					break

			if op_code == "040":
				branch.branch(mem_dict[word][3:])
				iter_count = int(mem_dict[word][3:])      

			if op_code == "041":
				if int(registers.registers["ACC"]) < 0:
					branch.branch(mem_dict[word][3:])
					iter_count = int(mem_dict[word][3:])


			if op_code == "042":
				if int(registers.registers["ACC"]) == 0:
					branch.branch(mem_dict[word][3:])
					iter_count = int(mem_dict[word][3:])


			if op_code == "043":
				break

		#Update Iteration count and assign PC
		iter_count += 1
		registers.registers["PC"] = str(iter_count)

	memory.read()

if __name__ == "__main__":
	main()
