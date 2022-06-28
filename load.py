'''
Author: Nick Moss
'''
import memory
import registers as reg

def load(location):
	reg.registers["ACC"] = memory.memory_dict[location]
