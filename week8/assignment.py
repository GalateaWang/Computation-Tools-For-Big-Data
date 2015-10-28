Exercises:

Exercise 1:

Define and implement a MapReduce job to count the occurrences of each 
word in a text file. Document that it works with a small example.

Exercise 2:

Define and implement a MapReduce job that determines if a graph has an 
Euler tour (all vertices have even degree) where you can assume that the 
graph you get is connected. This file 
https://www.dropbox.com/s/usdi0wpsqm3jb7f/eulerGraphs.txt?dl=0 has 5 
graphs – for each graph, the first line tells the number of nodes N and 
the number of edges E. The next E lines tells which two nodes are 
connected by an edge. Two nodes can be connected by multiple edges.

It is fine if you split the file into 5 different files. You do not need 
to keep the node and edge counts in the top of the file.

Document that it works using a small example.

Exercise 3:

Implement the MapReduce job from the lecture which finds common friends. 
To test it out, use the example from the slides and this one 
https://www.dropbox.com/s/ln0maf3q9xa08sf/facebook_combined.txt?dl=0 
(note that for the Facebook file, you need to extend the job to convert 
from a list of edges to the format from the slides – do this with an 
additional map/reduce job).Document that it works using a small example.

Exercise 4:

Make a MapReduce job which counts the number of triangles in a graph. 
Use the following graph 
http://www.cise.ufl.edu/research/sparse/matrices/SNAP/roadNet-CA.html

Document that it works using a small example.
