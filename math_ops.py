import registers as reg
import memory

def convert(num):
	string_value = str(num)
	if string_value[0] == '1':
		return -(int(string_value[1:]))
	else:
		return int(string_value[1:])

def add(location):
	val1 = convert(reg.registers['ACC'])
	val2 = convert(memory.memory_dict[location])
	result = val1 + val2
	if result > 9999 or result < -9999:
		return False

	if result < 0:
		result = '1' + str(result)[1:]
	else:
		result = '0' + str(result)

	reg.registers['ACC'] = result

	return True