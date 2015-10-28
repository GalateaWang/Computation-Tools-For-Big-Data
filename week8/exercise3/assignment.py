from mrjob.job import MRJob
from mrjob.step import MRStep
import string

class MRWordFrequencyCount(MRJob):

	def find_intersection(self, friend_lists):
		set1 = friend_lists.next()
		set2 = friend_lists.next()
		return list(set(set1).intersection(set(set2)))

	def values_to_friend_list(self, values):
		output = []
		for item in values:
			output.append(item)
		return output
	
	# Split each line into separate nodes
	# Count how many times each node is mentioned
	def mapper1(self, _, line):
		nodes = line.split()
		yield int(nodes[0]), int(nodes[1])
		yield int(nodes[1]), int(nodes[0])
		
	# Reduce list of nodes + mentions into
	# edge counts for each node
	def reducer1(self, key, values):
		yield key, self.values_to_friend_list(values)
		
	# Second mapping function, lists sorted pairs of friends to the
	# friends of one member of the pair
	def mapper2(self, key, friends):
		for friend in friends:
			yield sorted([key, friend]), friends

	
	# Reduces to a single output, checks if counts are all even
	def reducer2(self, pair, mutual):
		yield pair, self.find_intersection(mutual)
	
	def steps(self):
		return [
		MRStep(mapper=self.mapper1,
				reducer=self.reducer1),
		MRStep(mapper=self.mapper2,
				reducer=self.reducer2)
		]
		
		
MRWordFrequencyCount.run()