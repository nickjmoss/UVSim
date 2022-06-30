'''Author: Kyle Meiners'''

import load
import memory as mem
import registers

memory = mem.Memory()

def test_load():
    location = "00"
    load.load(location, memory)
    assert registers.registers["ACC"] == memory.memory_dict[location]
    print("Test case passed")

test_load()
