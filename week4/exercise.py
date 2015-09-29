#!C:/Users/Max/Anaconda/Python

import cPickle as pickle
import sys
import numpy as np
import time
from collections import defaultdict,Counter

# Find list of neighbors for each point
def distanceMap(size, eps):
	
	# Initialize dictionary of lists
	d = defaultdict(list)
	
	# Iterate through each point and find any neighbors that are
	# eps or less distance from it
	for i in range(size):
		neighbors = []
		for j in range(size):
			if dist(i,j) <= eps:
				neighbors.append(j)
		d[i] = neighbors
	return d

# Calculate distance from point at idx1 to point at idx2
def dist(idx1,idx2):
	
	# find actual nonzero values, and their unions and intersecionts
	arr1 = dataset[idx1].indices
	arr2 = dataset[idx2].indices
	union = np.union1d(arr1,arr2)
	intersection = np.intersect1d(arr1,arr2)
	
	# account for empty set
	if len(union)==0:
		return 1

	# jaccard calculation
	jaccard_dist = 1 - (len(intersection))/float(len(union))
	return jaccard_dist

def dbscan(eps, minPts, size, distMap):
	
	# initialize array of clusters
	C = []
	
	# calculate size of cluster for visited array and clustered array
	visitedDict = [False] * size
	clusterDict = [0] * size
	
	# begin iterating, and count the index of the current point
	count = 0
	for point in dataset:
		
		# if already visited, move on
		if visitedDict[count]==True:
			count = count+1
			continue
		
		# otherwise, mark as visited and find neighbors
		visitedDict[count] = True
		neighborIdxMatrix = regionQuery(count, distMap)
		
		# if not enough neighbors, mark as noise
		if len(neighborIdxMatrix) < minPts:
			clusterDict[count] = -1
			#noise.append(count)

		# otherwise begin a new cluster
		else:
			cluster = []
			
			# expand the cluster, and add it to the matrix, then move on to the next point
			newCluster = expandCluster(count,neighborIdxMatrix, cluster, 
							  clusterDict, visitedDict, distMap, minPts)
			if(len(newCluster) >= minPts):
				C.append(newCluster)
		count = count + 1
	numNoise = 0
	for i in range(size):
		if clusterDict[i] == -1:
			numNoise = numNoise + 1
	print "Marked noise: ", numNoise
	return C

# find neighbors, return matrix of their indices in dataset
def regionQuery(idx,distMap):
	return distMap[idx]

# grow the cluster from a single "root" point
def expandCluster(count,neighborIdxMatrix, cluster, clusterDict, visitedDict, distMap, minPts):
	
	# add root point
	cluster.append(count)
	
	# mark point as clustered
	clusterDict[count] = 1
	
	# keep iterating until matrix is empty
	while len(neighborIdxMatrix) > 0:
		# look at first point. If not visited, mark visited and find neighbors
		if visitedDict[neighborIdxMatrix[0]]==False:
			visitedDict[neighborIdxMatrix[0]] = True
			neighborPtsPrime = regionQuery(neighborIdxMatrix[0], distMap)
			
			# add neighbors' indices to those yet to be explored if they have enough
			if len(neighborPtsPrime) >= minPts:
				
				# update search matrix with new neighbors to explore
				neighborIdxMatrix = np.concatenate((neighborIdxMatrix,neighborPtsPrime),0)
				
		# if current point is not in a cluster, put it in
		if clusterDict[neighborIdxMatrix[0]]==0:
 			cluster.append(neighborIdxMatrix[0])
			clusterDict[neighborIdxMatrix[0]]=1;
			
		# remove the first point
		neighborIdxMatrix = neighborIdxMatrix[1:]
	return cluster

# main
eps = .15
M = 2
#noise = []
dataset = pickle.load(open( sys.argv[1], "rb"))
start_time = time.time()
size = 0
for point in dataset:
	size = size + 1
distMap = distanceMap(size,eps)
result = dbscan(eps, M, size, distMap)
runtime = time.time() - start_time

#print result
print "Summary:\n"
print len(result)
#count = 0
#seen = set()
#for item in result:
	#for thing in item:
		#count = count + 1
		#if thing not in seen:
			#seen.add(thing)
		#else:
			#print "REPEAT: ", thing
#print "Total items: ", count+len(noise)
#print "Recorded noise: ", len(noise)

print("--- %s seconds ---" % (runtime))
maxlength = 0
maxClust = 0
clust = 0
for item in result:
	if len(item) > maxlength:
		maxlength = len(item)
		maxClust = clust
	clust+=1	
print "Cluster number", maxClust, "had the most points, coming in at", maxlength


