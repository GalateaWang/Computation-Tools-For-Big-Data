import numpy as np

f = open("matrix.txt", 'r')
matrix = []
A = []
b = []
for line in f:
	line = line[:-1]
	matrix.append(line.split(','))
for row in matrix:
	A.append(row[:-1])
	b.append(row[-1])

A = np.array(A)
b = np.array(b)

print A
print b

print np.linalg.solve(A,b)
