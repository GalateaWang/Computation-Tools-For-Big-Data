from mrjob.job import MRJob
import string

class MRWordFrequencyCount(MRJob):
	
	
	def mapper(self, _, line):
		words = line.translate(string.maketrans("",""), string.punctuation)
		words = words.lower().split()
		for word in words:
			yield word, 1
		
		
	def reducer(self, key, values):
		yield key, sum(values)
	
	
MRWordFrequencyCount.run()