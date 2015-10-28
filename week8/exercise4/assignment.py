from mrjob.job import MRJob
from mrjob.step import MRStep
import string

class MRWordFrequencyCount(MRJob):

	# Helper function to find intersection of 2 friend lists
	def find_intersection(self, friend_lists):
		set1 = friend_lists.next()
		set2 = friend_lists.next()
		return list(set(set1).intersection(set(set2)))

	# Helper function to convert generator to list of mutual friends
	def values_to_friend_list(self, values):
		output = []
		for item in values:
			output.append(item)
		return output
	
	# Counts number of mutual friends
	def count_items(self, items):
		for item in items:
			yield len(item)
	
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

	
	# Same as exercise 3 and week 8 slides. Reduces both friend lists of a 
	# friend pair to a single friend list by finding the intersection
	def reducer2(self, pair, mutual):
		yield pair, self.find_intersection(mutual)
		
	
	# Yields generator of number of mutual friends per node
	def reducer3(self, _, mutual):
		yield None, sum(self.count_items(mutual))
	
	# Finds total number of mutual friends, and divides by 3 to get triangles.
	# Each mutual friendship represents a triangle, and is included 3 times.
	# Therefore, need to divide sum by 3
	def reducer4(self, _, mutual_per_individual):
		yield "Number of triangles:", sum(mutual_per_individual)/3
	
	def steps(self):
		return [
		MRStep(mapper=self.mapper1,
				reducer=self.reducer1),
		MRStep(mapper=self.mapper2,
				reducer=self.reducer2),
		MRStep(reducer=self.reducer3),
		MRStep(reducer=self.reducer4)
		]
		
		
MRWordFrequencyCount.run()