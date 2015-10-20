import mmh3
import math
import string
from bitarray import bitarray
import time

# Find length of file with name fname
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

class BloomFilter():
	"""Implementing a bloom filter as a class"""
	
	def __init__(self, expectedUnique, arraySize):
		"""Constructor for BloomFilter"""
		
		# Define bit array to be of arraySize parameter
		self.data = arraySize * bitarray([False])
		
		# Calculate number of hash functions needed, rounding up
		self.numHash = int(math.ceil(arraySize * math.log(2) / expectedUnique))
		
		# Set array size parameter
		self.arraySize = arraySize
		
	def add(self, toAdd):
		"""Add a word to the hash function as approved"""
		
		# Iterate through the number of hash functions necessary
		for seed in xrange(self.numHash):
			
			# Hash the word, using index as a seed, and mod it with size of array
			index = mmh3.hash(toAdd, seed) % self.arraySize
			
			# Assign value to be true
			self.data[index] = True
	
	def lookup(self, toFind):
		"""Look up the word using hash table stored to see if it is valid"""
		
		# Iterate through the number of hash functions necessary
		for seed in xrange(self.numHash):
			
			# Hash the word, using index as a seed, and mod it with size of array
			index = mmh3.hash(toFind, seed) % self.arraySize
			
			# If hash function at index contains 'False', word is invalid
			if self.data[index] == False:
				return False
		
		# If hash functions all resulted in 'True', word should be valid
		return True
		
#---------------------------------------------------------------------------#
#---------------------------    MAIN FUNCTION    ---------------------------#
#---------------------------------------------------------------------------#

print "FAST WAY"

# Set up timing mechanism
startTime = time.time()

# Find max number of unique words possible, aka n
expectedUnique = file_len('dict')

# Construct a BloomFilter object, using 1 million bits as m
filt = BloomFilter(expectedUnique, 1000000)

# Build the BloomFilter, adding every valid word to the hash table
d = open('dict','r').read().lower().split()
for word in d:
	filt.add(word)

# Begin reading through shakespeare
s = open('shakespeare.txt','r')

# Constuct list of punctuation to remove
exclude = string.punctuation

# Intialize array to store all words that passed filter
words_approved = []

# Iterate through shakespeare text
for line in s:
	
	# Remove punctuation from line, and make it lower case
	words = line.translate(string.maketrans("",""), exclude)
	words = words.lower()

	# Iterate through words and look up each one
	for word in words.split():
		
		# If word is valid, perform the necessary action
		if (filt.lookup(word)) and word not in words_approved:
			words_approved.append(word)

s.close()

# Record time for fast method
fast_time = (time.time() - startTime)

# Print results and time
print "Total words approved by filter:",len(words_approved)
count = 0

# Create array of words in dictionary for comparison later
dictionary = open('dict').read().lower().split()

# Determine which words passed filter wrongly
for word in words_approved:
	if word not in dictionary:
		count+=1

# Print results
print "Words approved that are not in dictionary:", count
print "Total real words in shakespeare:", len(words_approved)-count
print("--- %s seconds ---" % fast_time)



# SLOW WAY #

print "\n\nSLOW WAY:"

# Set up timing
startTime = time.time()

# Open shakespeare text to read
s = open('shakespeare.txt','r')

# Open dictionary as array of lowercase words
dictionary = open('dict').read().lower().split()

# Prepare to remove punct from shakespeare
exclude = string.punctuation

# Initialize array of real words to keep track while looping
real_words = []

# Iterate through every word in shakespeare
for line in s:
	
	# Modify word to remove punctuation and capitalization
	words = line.translate(string.maketrans("",""), exclude)
	words = words.lower()
	
	# Go through the individual words, see if they are in dictionary
	for word in words.split():
		if word in dictionary and word not in real_words:
			
			# If in dictionary, add to real_words array
			real_words.append(word)
s.close()

# Print results
print "Real words in shakespeare and in dictionary:", len(real_words)
print("--- %s seconds ---" % (time.time() - startTime))
