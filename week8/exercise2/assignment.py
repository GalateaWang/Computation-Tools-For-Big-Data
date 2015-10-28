from mrjob.job import MRJob
from mrjob.step import MRStep
import string

class MRWordFrequencyCount(MRJob):
	
	# Function to go through generator
	# to see if edge counts are even
	def checkEven(self, edgeCounts):
		for node in edgeCounts:
			if node % 2 == 1:
				return False
		return True
	
	# Split each line into separate nodes
	# Count how many times each node is mentioned
	def mapper(self, _, line):
		nodes = line.split()
		for node in nodes:
			yield node, 1
		
	# Reduce list of nodes + mentions into
	# edge counts for each node
	def reducer(self, key, values):
		yield None, sum(values)
	
	# Reduces to a single output, checks if counts are all even
	def reducer_if_euler(self, _, edge_count_pairs):
		yield "Graph has a Euler Tour:", self.checkEven(edge_count_pairs)
	
	def steps(self):
		return [
		MRStep(mapper=self.mapper,
				reducer=self.reducer),
		MRStep(reducer=self.reducer_if_euler)
		]
		
		
MRWordFrequencyCount.run()