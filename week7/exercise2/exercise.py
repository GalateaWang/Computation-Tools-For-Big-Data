import mmh3
from string import punctuation, maketrans
import time
import random
from bitarray import bitarray

class FlajoletMartin():
	"""Implementing a Flajolet-Martin algorithm."""
	
	def __init__(self, length, groupSize, numGroups):
		"""Constructor for the FlajoletMartin class"""
		
		# Initialize private variables
		self.groupSize = groupSize
		self.numGroups = numGroups
		self.R = []
		
		# Construct list of bitarrays of size groupSize*numGroups
		# 32 bits per bitarray, all 0
		for hashfunc in xrange(self.groupSize * self.numGroups):
			self.R.append(32 * bitarray([0]))
			
		# Generate list of random seeds, ranging from 0 to groupSize*numGroups
		# containing groupSize*numGroups elements
		self.seeds = random.sample(xrange(self.groupSize * self.numGroups), 
							 self.groupSize * self.numGroups)
	
	def trailing_zeroes(self, num):
		"""Counts the number of trailing 0 bits in num. Provided by teacher."""
		if num == 0:
			return 32 # Assumes 32 bit integer inputs!
		p = 0
		while (num >> p) & 1 == 0:
			p += 1
		return p
	
	def first_zero(self, bitarr):
		"""Finds the first zero in the bit array"""
		p = 0
		
		# Search bitarray until first 0 is encountered, as explained by algorithm
		while (bitarr[p] & 1) == 1:
			p += 1
		
		# Return final result
		return p
	
	def process(self,element):
		"""Adds an element to the data structure"""
		
		# Iterate through each hash function, from 0 to numGroups*groupSize
		for seed in xrange(self.numGroups * self.groupSize):
			
			# Hash the element
			hashedElement = mmh3.hash(element, self.seeds[seed])
			
			# Determine index of first 1
			first1Index = self.trailing_zeroes(hashedElement)
			
			# Overwrite in bitarray if not already 1
			if self.R[seed][first1Index] == 0:
				self.R[seed][first1Index] = 1
				
	def median(self, midlist):
		"""finds the median value of a list of numbers"""
		midlist.sort()
		length = len(midlist)
		
		# If odd length, take middle index
		if length % 2 != 0: 
			middle = (length / 2)
			med = midlist[middle]
			
		# If even index, take avg of middle indices
		else:
			odd = (length / 2) -1
			even = (length / 2) 
			med = float(midlist[odd] + midlist[even]) / float(2)
		return med
	
	def give_estimate(self):
		"""Gives estimate of unique values based on trailing zeros."""
		
		# Construct list of medians
		medians = self.numGroups * [0]
		
		# Start and end for chunking the big list into groups
		start = 0
		end = self.groupSize
		
		# For each group, create list of first_zero values to take median of
		for group in xrange(self.numGroups):
			values = self.R[start:end]
			
			# New array containing values of first_zeros for each bit array
			first_zeros = []
			
			# Iterate through bit arrays in the group, populate list of
			# first_zeros with the first zero values of the bit array
			for value in values:
				first_zeros.append(self.first_zero(value))
				
			# Calculate median of first_zeros list, assign to list of medians
			medians[group] = self.median(first_zeros)
			
			# Increment chunking values for next group
			start = end
			end += self.groupSize
			
		# Take mean of medians to obtain R
		meanOfMediansIndex = sum(medians)/self.numGroups
		
		# Calculate cardinality estimate and return
		cardEstimate = (2**meanOfMediansIndex)/.77351
		return cardEstimate
		
#---------------------------------------------------------------------------#
#---------------------------    MAIN FUNCTION    ---------------------------#
#---------------------------------------------------------------------------#

# Set up timing mechanism
startTime = time.time()

# Initialize instance of class
fm = FlajoletMartin(32, 10, 100)
shakespeare = open('shakespeare.txt', 'r')

# Constuct list of punctuation to remove
exclude = punctuation
# Iterate through shakespeare text
for line in shakespeare:
	
	# Remove punctuation from line, and make it lower case
	words = line.translate(maketrans("",""), exclude)
	words = words.lower()

	# Iterate through words and look up each one
	for word in words.split():
		fm.process(word)

# Obtain estimate of processed text
print fm.give_estimate()
print("--- %s seconds ---" % (time.time() - startTime))

	

