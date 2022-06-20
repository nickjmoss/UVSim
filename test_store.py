import store
import registers
import memory

def test_store():
    registers.registers["ACC"] = "01007"
    store.store("05")
    assert memory.memory_dict["05"] == "01007"
    print("test_store - pass")

test_store()

print("All test cases passed")