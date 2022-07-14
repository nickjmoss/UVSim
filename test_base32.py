'''Author: Nick Moss'''

import base32

def test_dec_to_b32():
	assert base32.dec_to_b32(123456) == 'DYSA'
	print('test_dec_to_b32 passed')

def test_b32_to_dec():
	assert base32.b32_to_dec('DYSA') == 123456
	print('test_b32_to_dec passed')

test_dec_to_b32()
test_b32_to_dec()

print('All tests passed')
