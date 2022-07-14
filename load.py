'''
Author: Nick Moss
'''
import registers as reg

def load(location, memory):
	reg.registers["ACC"] = memory.get(location)
