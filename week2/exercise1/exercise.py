import sys

def read_array(filename):
	f = open(filename, 'r')
	matrix = []
	for line in f:
		line = line[:-1]
		points = line.split(' ');
		matrix.append(points)
		#print points
	f.close();
	return matrix

def array_to_file(twoDArray, filename):
	f = open('out.txt', 'w')
	for i in range(0, len(twoDArray)):
		for j in range(0,len(twoDArray[i])):
			f.write(str(twoDArray[i][j]) + " ")
		f.write("\n")
	

def main():
	matrix = read_array(sys.argv[1])
	print matrix
	array_to_file([[0,1,2,3],[4,5,6],[7,8,10]], sys.argv[2])


if __name__ == "__main__":
	sys.exit(main())
