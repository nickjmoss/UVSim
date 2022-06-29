'''Author: Gavin Doel'''

import registers

def store(location, memory):
    word = registers.registers["ACC"]
    memory.memory_dict[location] = word

    