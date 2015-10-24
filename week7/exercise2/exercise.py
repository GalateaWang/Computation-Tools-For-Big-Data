import mmh3
from string import punctuation, maketrans


class FlajoletMartin():
	"""Implementing a Flajolet-Martin algorithm"""
	
	def __init__(self, length):
		self.maxNum = 2**(length)-1
		self.groupSize = 10
		self.numGroups = 100
		self.R = (self.groupSize * self.numGroups) * [0]
	
	def trailing_zeroes(self, num):
		"""Counts the number of trailing 0 bits in num."""
		if num == 0:
			return 32 # Assumes 32 bit integer inputs!
		p = 0
		while (num >> p) & 1 == 0:
			p += 1
		return p		
	
	def process(self,element):
		for seed in xrange(len(self.R)):
			hashX = mmh3.hash(element,seed) % self.maxNum
			numZeros = self.trailing_zeroes(hashX)
			if(numZeros > self.R[seed]):
				self.R[seed] = numZeros
	
	def give_estimate(self):
		medians = self.numGroups * [0]
		start = 0
		end = self.groupSize
		for i in xrange(len(self.R)):
			self.R[i] = 2**self.R[i]/.77351
		for group in xrange(self.numGroups):
			values = self.R[start:end]
			medians[group] = self.median(values)
			start = end
			end += self.groupSize
			
		meanOfMedians = sum(medians)/float(self.numGroups)
		return meanOfMedians
		
	def median(self, midlist):
		midlist.sort()
		length = len(midlist)
		if length % 2 != 0: 
			middle = (length / 2)
			med = midlist[middle]
		else:
			odd = (length / 2) -1
			even = (length / 2) 
			med = float(midlist[odd] + midlist[even]) / float(2)
		return med
	

		
		
#---------------------------------------------------------------------------#
#---------------------------    MAIN FUNCTION    ---------------------------#
#---------------------------------------------------------------------------#
fm = FlajoletMartin(32)

shakespeare = open('shakespeare.txt', 'r')

# Constuct list of punctuation to remove
exclude = punctuation

# Intialize array to store all words that passed filter
words_approved = []

# Iterate through shakespeare text
for line in shakespeare:
	
	# Remove punctuation from line, and make it lower case
	words = line.translate(maketrans("",""), exclude)
	words = words.lower()

	# Iterate through words and look up each one
	for word in words.split():
		fm.process(word)
print fm.give_estimate()



