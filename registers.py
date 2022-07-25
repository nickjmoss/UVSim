#Author: Gavin Doel
# registers is a dictionary object that can be called as a global object

import base32

registers = {"R1": "00000", "R2": "00000", "R3": "00000", "R4": "00000", "R5": "00000",
"PC": "00000", "ACC": "00000"}

def reg_store(location, input):
    '''Author: Kyle Meiners'''
    dec = int(input)
    if dec > 0:
        b32 = base32.dec_to_b32(dec)
        registers[location] = b32
    else:
        dec *= -1
        b32 = base32.dec_to_b32(dec)
        data = '-' + b32
        registers[location] = data


def reg_get(location):
    '''Author: Kyle Meiners'''
    b32 = registers[location]
    if b32[0] == '-':
        b32 = b32.replace('-','')
        dec = base32.b32_to_dec(b32)
        dec = '1' + str(dec).zfill(4)
        return dec
    else:
        dec = base32.b32_to_dec(b32)
        return str(dec).zfill(5)
