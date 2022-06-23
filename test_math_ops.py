import math_ops
import registers
import memory

def test_num_format():
    '''Tests that integers are being converted to strings appropriately'''
    assert math_ops.num_format("3") == "0003"
    print("test_num_format - pass")

def test_final_result():
    '''Tests that sign bits are being added correctly'''
    assert math_ops.final_result(-5) == "10005"
    assert math_ops.final_result(5) == "00005"
    print("test_final_result - pass")

def test_convert():
    '''Tests that strings are converted to integers correctly'''
    assert math_ops.convert("10005") == -5
    assert math_ops.convert("00005") == 5

def test_add():
    '''Tests for correct addition with positive and negative numbers'''
    registers.registers["ACC"] = "00003"
    memory.memory_dict["05"] = "00007"
    math_ops.add("05")
    assert registers.registers["ACC"] == "00010"

    memory.memory_dict["05"] = "10002"
    math_ops.add("05")
    assert registers.registers["ACC"] == "00008"
    print("test_add - pass")

def test_subtract():
    '''Tests for correct subtraction with positive and negative numbers'''
    registers.registers["ACC"] = "00009"
    memory.memory_dict["05"] = "00002"
    math_ops.subtract("05")
    assert registers.registers["ACC"] == "00007"

    registers.registers["ACC"] = "00009"
    memory.memory_dict["05"] = "10002"
    math_ops.subtract("05")
    assert registers.registers["ACC"] == "00011"
    print("test_subtract - pass")


def test_multiply():
    '''Tests for correct multiplication with positive and negative numbers'''
    registers.registers["ACC"] = "00005"
    memory.memory_dict["05"] = "00002"
    math_ops.multiply("05")
    assert registers.registers["ACC"] == "00010"

    registers.registers["ACC"] = "10007"
    memory.memory_dict["05"] = "00003"
    math_ops.multiply("05")
    assert registers.registers["ACC"] == "10021"
    print("test_multiply - pass")

def test_divide():
    '''Tests for correct division with positive and negative numbers'''
    registers.registers["ACC"] = "00020"
    memory.memory_dict["05"] = "00005"
    math_ops.divide("05")
    print(registers.registers["ACC"])
    #assert registers.registers["ACC"] == "00004"

    registers.registers["ACC"] = "10015"
    memory.memory_dict["05"] = "00005"
    math_ops.divide("05")
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
