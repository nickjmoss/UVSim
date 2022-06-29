'''Author: Kyle Meiners'''

from math_ops import Math_Ops
import registers
import memory as mem

memory = mem.Memory()

def test_num_format():
    '''Tests that integers are being converted to strings appropriately'''
    math = Math_Ops()
    assert math.num_format("3") == "0003"
    print("test_num_format - pass")

def test_final_result():
    '''Tests that sign bits are being added correctly'''
    math = Math_Ops()
    assert math.final_result(-5) == "10005"
    assert math.final_result(5) == "00005"
    print("test_final_result - pass")

def test_convert():
    '''Tests that strings are converted to integers correctly'''
    math = Math_Ops()
    assert math.convert("10005") == -5
    assert math.convert("00005") == 5

def test_add():
    '''Tests for correct addition with positive and negative numbers'''
    math = Math_Ops()
    registers.registers["ACC"] = "00003"
    memory.memory_dict["05"] = "00007"
    math.add("05")
    assert registers.registers["ACC"] == "00010"

    memory.memory_dict["05"] = "10002"
    math.add("05")
    assert registers.registers["ACC"] == "00008"
    print("test_add - pass")

def test_subtract():
    '''Tests for correct subtraction with positive and negative numbers'''
    math = Math_Ops()
    registers.registers["ACC"] = "00009"
    memory.memory_dict["05"] = "00002"
    math.subtract("05")
    assert registers.registers["ACC"] == "00007"

    registers.registers["ACC"] = "00009"
    memory.memory_dict["05"] = "10002"
    math.subtract("05")
    assert registers.registers["ACC"] == "00011"
    print("test_subtract - pass")


def test_multiply():
    '''Tests for correct multiplication with positive and negative numbers'''
    math = Math_Ops()
    registers.registers["ACC"] = "00005"
    memory.memory_dict["05"] = "00002"
    math.multiply("05")
    assert registers.registers["ACC"] == "00010"

    registers.registers["ACC"] = "10007"
    memory.memory_dict["05"] = "00003"
    math.multiply("05")
    assert registers.registers["ACC"] == "10021"
    print("test_multiply - pass")

def test_divide():
    '''Tests for correct division with positive and negative numbers'''
    math = Math_Ops()
    registers.registers["ACC"] = "00020"
    memory.memory_dict["05"] = "00005"
    math.divide("05")
    assert registers.registers["ACC"] == "00004"
    print("test_divide - pass")

    registers.registers["ACC"] = "10015"
    memory.memory_dict["05"] = "00005"
    math.divide("05")
    assert registers.registers["ACC"] == "10003"
    print("test_multiply - pass")




test_num_format()
test_final_result()
test_convert()
test_add()
test_subtract()
test_multiply()
test_divide()


print("All test cases passed")
