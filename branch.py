from registers import registers 

#The branch operation will change PC to target memory location
def branch(target_mem):
    registers["PC"] = target_mem
