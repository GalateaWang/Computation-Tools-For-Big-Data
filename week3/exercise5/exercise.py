import Cython
import time


start_time = time.time()

for j in range(1,501):
	sum = 0.0
	for i in range(1,10001):
		sum = sum + 1.0/(i*i)
print("--- %s seconds ---" % (time.time() - start_time))
