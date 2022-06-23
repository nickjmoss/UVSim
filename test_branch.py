'''Author: Kyle Meiners'''

import branch
import registers

def test_branch():
    target_mem = "05"
    branch.branch(target_mem)
    assert registers.registers["PC"] == target_mem
    print("Test case passed")

test_branch()

