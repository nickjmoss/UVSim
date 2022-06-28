'''Author: Kyle Meiners'''
    
import io_ops
import memory
import mock


def test_read():
    location = "00"
    with mock.patch('builtins.input', return_value="+1008"):
        io_ops.read(location)
        assert memory.memory_dict[location] == "01008"
    print("test case passed")


test_read()