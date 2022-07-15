'''Author: Gavin Doel'''

import registers

def store(location, memory):
    word = registers.registers["ACC"]
    memory.store(location, word)

    
