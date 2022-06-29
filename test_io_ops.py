'''Author: Kyle Meiners'''
    
from io_ops import IO
import memory as mem
import mock

memory = mem.Memory()


def test_read():
    io = IO()
    location = "00"
    with mock.patch('builtins.input', return_value="+1008"):
        io.read(location,memory)
        assert memory.memory_dict[location] == "01008"
    print("test case passed")


test_read()
