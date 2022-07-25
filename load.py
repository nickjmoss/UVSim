'''
Author: Nick Moss
'''
import registers as reg

def load(location, memory):
	reg.reg_store("ACC", memory.get(location))
