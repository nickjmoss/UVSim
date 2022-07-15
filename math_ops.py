'''
Author: Nick Moss
'''
import registers

class Math_Ops:
	def num_format(self, num):
		while len(num) < 4:
			num = '0' + num
		return num

	def final_result(self,num):
		if num < 0:
			formatted_num = self.num_format(str(num)[1:])
			num = '1' + formatted_num
		else:
			formatted_num = self.num_format(str(num))
			num = '0' + formatted_num
		
		return num

	def convert(self, num):
		string_value = str(num)
		if string_value[0] == '1':
			return -(int(string_value[1:]))
		else:
			return int(string_value[1:])

	def add(self, location, memory):
		val1 = self.convert(registers.registers['ACC'])
		val2 = self.convert(memory.get(location))
		result = val1 + val2
		if result > 9999 or result < -9999:
			return False

		registers.registers['ACC'] = self.final_result(result)

		return True

	def subtract(self, location, memory):
		val1 = self.convert(registers.registers['ACC'])
		val2 = self.convert(memory.get(location))
		result = val1 - val2
		if result > 9999 or result < -9999:
			return False

		registers.registers['ACC'] = self.final_result(result)

		return True

	def multiply(self, location, memory):
		val1 = self.convert(registers.registers['ACC'])
		val2 = self.convert(memory.get(location))
		result = val1 * val2
		if result > 9999 or result < -9999:
			return False

		registers.registers['ACC'] = self.final_result(result)

		return True

	def divide(self, location, memory):
		val1 = self.convert(registers.registers['ACC'])
		val2 = self.convert(memory.get(location))
		if val2 == 0:
			return False
		result = val1 // val2
		if result > 9999 or result < -9999:
			return False

		registers.registers['ACC'] = self.final_result(result)

		return True
