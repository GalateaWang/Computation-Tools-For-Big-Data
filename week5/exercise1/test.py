def bitexploder(num):
	return [[int(2**bit & i != 0) for bit in xrange(num ‐1, ‐1, ‐1)] 
for i in xrange(2**num)]
print bitexploder(3)

