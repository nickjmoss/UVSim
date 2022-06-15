from registers import registers as rgst

#The branch operation will change PC to target memory location
def branch(target_mem):
    rgst["PC"] = target_mem
