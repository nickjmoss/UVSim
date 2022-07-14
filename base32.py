'''Author: Kyle Meiners'''

import convertbase as convert


def dec_to_b32(decimal):
    '''input decimal integer, outputs base32 string'''
    return convert.Convertbase.to_b32(decimal)



def b32_to_dec(b32):
    '''input base32 string, outputs decimal value'''
    return convert.Convertbase.from_b32_to_dec(b32)
