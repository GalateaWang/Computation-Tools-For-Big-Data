#!C:/Users/Max/Anaconda/Python

import pandas as pd
import numpy as np

#TODO 1

t_movies = pd.read_table('ml-1m/movies.dat','::',engine = 'python',names=['movie_id','title','genre'])
t_ratings = pd.read_table('ml-1m/ratings.dat','::',engine = 'python',names=['user_id','movie_id','rating','timestamp'])
t_users = pd.read_table('ml-1m/users.dat','::',engine = 'python',names=['user_id','gender','age','occupation_code','zip'])


movie_data_1 = pd.merge(t_ratings, t_users,on='user_id')
movie_data = pd.merge(movie_data_1, t_movies,on = 'movie_id')
#print movie_data
#print movie_data.describe()

#TODO 2

#5 movies w/ most reviews
print movie_data['title'].value_counts()[:5]


#List of movies w/ 250+ reviews
p_table = pd.pivot_table(movie_data,values='rating',index = ['title'],aggfunc = lambda x: len(x))
p_table = p_table.sort(axis=0,inplace=False)
for i in p_table:
	if p_table[i] >= 250:
		break 
active_titles = p_table[i:]

print active_titles
