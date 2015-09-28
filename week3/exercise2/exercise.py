#import numpy as np
from scipy.interpolate import UnivariateSpline



f = open("points.txt", 'r')
x = []
y = []
for line in f:
        line = line[:-1]
        x.append(int(line.split()[0]))
	y.append(float(line.split()[1]))

f = UnivariateSpline(x,y,k=3)

roots = f.roots()

print roots
