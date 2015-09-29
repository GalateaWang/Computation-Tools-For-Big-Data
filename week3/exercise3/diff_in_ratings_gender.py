#!C:/Users/Max/Anaconda/Python

import pandas as pd
import numpy as np

t_movies = pd.read_table('ml-1m/movies.dat','::',engine = 'python',names=['movie_id','title','genre'])
t_ratings = pd.read_table('ml-1m/ratings.dat','::',engine = 'python',names=['user_id','movie_id','rating','timestamp'])
t_users = pd.read_table('ml-1m/users.dat','::',engine = 'python',names=['user_id','gender','age','occupation_code','zip'])

movie_data = pd.merge(t_ratings,t_users)
movie_data = pd.merge(movie_data,t_movies[['movie_id','title']])

#FEMALES

females_only = movie_data[movie_data['gender']=='F']
females_pt = pd.pivot_table(females_only,values='rating',index=['title'])

top_pt = pd.pivot_table(movie_data,values='rating',index=['title'],aggfunc = lambda x: len(x))

active_females = pd.concat([top_pt, females_pt], axis=1)

active_females.columns = ['numRatings','avgRating']

active_females = active_females[(active_females['numRatings']>=250)] 



#MALES

males_only = movie_data[movie_data['gender']=='M']
males_pt = pd.pivot_table(males_only,values='rating',index=['title'])

top_pt = pd.pivot_table(movie_data,values='rating',index=['title'],aggfunc = lambda x: len(x))

active_males = pd.concat([top_pt, males_pt], axis=1)

active_males.columns = ['numRatings','avgRating']

active_males = active_males[(active_males['numRatings']>=250)]
active_males = active_males.sort('avgRating',ascending = False)

#COMBINE M/F

active_both = pd.concat([active_males['avgRating'],active_females['avgRating']], axis=1)
active_both.columns = ['menRating','womenRating']

active_both['difference(M-F)'] = active_both['menRating'] - active_both['womenRating']
print "Ten movies men liked more:"
print active_both.sort('difference(M-F)',ascending=False).head(10)

print "\n\n\nTen movies women liked more:"
print active_both.sort('difference(M-F)',ascending=True).head(10)
