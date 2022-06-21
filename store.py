import registers
import memory

def store(location):
    word = registers.registers["ACC"]
    memory.memory_dict[location] = word
    