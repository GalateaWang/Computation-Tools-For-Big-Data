import Cython
import time

cdef float output

start_time = time.time()

cdef int j
cdef int i
for j in range(1,501):
	sum = 0.0
	for i in range(1,10001):
		sum = sum + 1.0/(i*i)
print("--- %s seconds ---" % (time.time() - start_time))
