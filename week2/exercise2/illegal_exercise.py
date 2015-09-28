import sys
import math
def bit_permutations(N):
	for i in range(0,2**N):
		perm = str(bin(i))[2:];
		while len(perm) < N:
			perm = '0'+perm
		print list(perm)

def main():
	bit_permutations(5)

if __name__ == "__main__":
	main();
