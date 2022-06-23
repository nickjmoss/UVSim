
import mock

import memory


def test_memory_created():
    '''Tests that a data structure is created to hold the necessary amount of data points'''
    assert isinstance(memory.memory_dict, dict)
    assert len(memory.memory_dict) >= 100

    print("test_memory_created - pass")
    


def test_load():
    '''Tests that data can be loaded from memory'''
    assert memory.memory_dict["00"] == "00000"
    assert memory.memory_dict["01"] == "00000"
    with mock.patch('builtins.input', return_value="+1004"):
        memory.init()
        assert memory.memory_dict["00"] == "01004"

    print("test_load - pass")




test_memory_created()
test_load()

print("All test cases passed")



