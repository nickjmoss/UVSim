#Author: Gavin Doel
import registers 

#The branch operation will change PC to target memory location
def branch(target_mem):
    registers.registers["PC"] = target_mem
