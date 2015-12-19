import sys
import re
from itertools import chain

def countUniqueWords(filename):
        f = open(filename, 'r')
        return len(set(chain(*(line.split() for line in f if line))))
	f.close()

def bag(filename, N):
        f = open(filename, 'r');
        content = f.readlines()

	#Create output matrix of length 12*** x 4040
        output = [[0]*(N+1) for _ in range(len(content))]
	
	#Create list to hold discovered words
        bag_dict = []
	
	#create var to keep count of line
	count = 0

	#iterate through all lines in processed file
        for line in content:
		#replace newlines
		line = line.replace("\n",' ')
                words = line.split(' ')
                
		#iterate through every words in line
		for word in words:
                        #print len(output[count]), len(bag_dict)
                        
			#if not previously discovered word, add to bag and increment count
			if word not in bag_dict:
                                bag_dict.append(word)
                                output[count][len(bag_dict)-1] = 1

			#if previously discovered word, find index and increment count
                        else:
                                spot = bag_dict.index(word)
                                output[count][spot] = output[count][spot] + 1
			#print bag_dict
	
		count = count+1
        f.close()
	print output


def main():
	f = open(sys.argv[1],'r')
	r = open("requests.txt",'w+')
	
	#iterate through file to clean it up
	for line in f:
		#find proper lines
		if '"request_text":' in line:
			processed = line.lower()

			#remove excess symbols
			processed = re.sub('[\[\]!~*\-,><}{;)(:#$"&%.?]',' ',processed)

			#remove "\n"s
			processed = processed.replace("\\n",' ')

			#remove slashes, now that "\n" is gone
                	processed = re.sub('[\\/]',' ',processed)

			#attempt at removing whitespace
			array = [w for w in processed.split() if not re.search(r'\d', w)]
			#array = processed.split()

			#remove first item in line, "request_text"
			body = array[1:]

			#remove digits, emails, money, mmmm, and URLs, and write to file
			r.write(' '.join([i for i in body if not (i.isdigit() or "@" in i or '$' in i or "http" in i or "mmm" in i)]) + '\n')

	f.close()
	r.close()
	N = countUniqueWords("requests.txt")

	#Call the function
	bag("requests.txt", N);


if __name__ == "__main__":
	main()
