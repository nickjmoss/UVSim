'''Author: Gavin Doel'''

import registers 

#The branch operation will change PC to target memory location
class Branch:
    def __init__(self) -> None:
        pass
    def branch(self, target_mem):
        registers.registers["PC"] = target_mem
