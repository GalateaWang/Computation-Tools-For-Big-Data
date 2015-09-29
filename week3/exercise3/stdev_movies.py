#!C:/Users/Max/Anaconda/Python

import pandas as pd
import numpy as np

t_movies = pd.read_table('ml-1m/movies.dat','::',engine = 'python',names=['movie_id','title','genre'])
t_ratings = pd.read_table('ml-1m/ratings.dat','::',engine = 'python',names=['user_id','movie_id','rating','timestamp'])
t_users = pd.read_table('ml-1m/users.dat','::',engine = 'python',names=['user_id','gender','age','occupation_code','zip'])

movie_data = pd.merge(t_ratings,t_users)
movie_data = pd.merge(movie_data,t_movies[['movie_id','title']])

stdev_pt = pd.pivot_table(movie_data,values='rating',index=['title'],aggfunc = lambda x: np.std(x))
top_pt = pd.pivot_table(movie_data,values='rating',index=['title'],aggfunc = lambda x: len(x))
top_stdev = pd.concat([top_pt,stdev_pt],axis=1)

top_stdev.columns = ['numRatings','stdev']
top_stdev = top_stdev[top_stdev['numRatings'] >= 250]
print top_stdev.sort('stdev',ascending=False).head(5)

