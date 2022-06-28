'''
Author: Nick Moss
'''
import registers
import memory

class Math_ops:


	def num_format(self, num):
		while len(num) < 4:
			num = '0' + num
		return num

	def final_result(self, num):
		if num < 0:
			formatted_num = num_format(str(num)[1:])
			num = '1' + formatted_num
		else:
			formatted_num = num_format(str(num))
			num = '0' + formatted_num

		return num

	def convert(self, num):
		string_value = str(num)
		if string_value[0] == '1':
			return -(int(string_value[1:]))
		else:
			return int(string_value[1:])

	def add(self, location):
		val1 = convert(registers.registers['ACC'])
		val2 = convert(memory.memory_dict[location])
		result = val1 + val2
		if result > 9999 or result < -9999:
			return False

		registers.registers['ACC'] = final_result(result)

		return True

	def subtract(self, location):
		val1 = convert(registers.registers['ACC'])
		val2 = convert(memory.memory_dict[location])
		result = val1 - val2
		if result > 9999 or result < -9999:
			return False

		registers.registers['ACC'] = final_result(result)

		return True

	def multiply(self, location):
		val1 = convert(registers.registers['ACC'])
		val2 = convert(memory.memory_dict[location])
		result = val1 * val2
		if result > 9999 or result < -9999:
			return False

		registers.registers['ACC'] = final_result(result)

		return True

	def divide(self, location):
		val1 = convert(registers.registers['ACC'])
		val2 = convert(memory.memory_dict[location])
		if val2 == 0:
			return False
		result = val1 // val2
		if result > 9999 or result < -9999:
			return False

		registers.registers['ACC'] = final_result(result)

		return True
