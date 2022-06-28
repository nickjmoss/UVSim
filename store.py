'''Author: Gavin Doel'''

import registers
import memory

class Store:
    def __init__(self) -> None:
        pass
    def store(location):
        word = registers.registers["ACC"]
        memory.memory_dict[location] = word
    