'''Author: Kyle Meiners'''

from branch import Branch
import registers

def test_branch():
    br = Branch()
    target_mem = "05"
    br.branch(target_mem)
    assert registers.registers["PC"] == target_mem
    print("Test case passed")

test_branch()

