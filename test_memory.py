'''Author: Kyle Meiners'''

import mock
import memory as mem

memory = mem.Memory()

def test_memory_created():
    assert isinstance(memory.memory_dict, dict)
    assert len(memory.memory_dict) >= 100

    print("test_memory_created - pass")
    


def test_init():
    assert memory.memory_dict["00"] == "00000"
    assert memory.memory_dict["01"] == "00000"
    with mock.patch('builtins.input', return_value="+1004"):
        memory.init()
        assert memory.memory_dict["00"] == "01004"

    print("test_load - pass")


def test_reset():
	'''Author: Nick Moss'''
	memory.memory_dict["00"] = "11111"
	memory.reset();
	assert memory.memory_dict["00"] == "00000"

	print("Memory reset test passed")



test_memory_created()
test_init()
test_reset()

print("All test cases passed")



