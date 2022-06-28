'''Author: Kyle Meiners'''

import load
import memory
import registers

def test_load():
    location = "00"
    load.load(location)
    assert registers.registers["ACC"] == memory.memory_dict[location]
    print("Test case passed")

test_load()
