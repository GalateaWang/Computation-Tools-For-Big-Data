import sys
import math

def bit_permutations(N):
	for i in range(0,2**N):
		list = [0] * N
		for j in range(0,N):
			curr_place = 2**j
			if (i % (2*curr_place) >= curr_place):
				list[N-1-j] = 1
		print ''.join(str(list))
def main():
	number = raw_input("Please enter the number: ")
	bit_permutations(int(number))

if __name__ == "__main__":
	main();
