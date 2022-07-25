'''Author: Gavin Doel'''

import registers

def store(location, memory):
    word = registers.reg_get("ACC")
    memory.store(location, word)

    
