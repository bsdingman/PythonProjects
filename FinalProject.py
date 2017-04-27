##############################################################
#	Bryan Dingman
#	Final Project
#	Using data from MovieLens, prove or disprove the hyptoesis 
#   that people 25 years and younger will rate fantasy movies 
#   higher than people 35 years and older
###############################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data. Wooo
# movie Data
movie_data = pd.read_csv('movielens\\movies.dat', delimiter='::', names=['MovieID','Title','Genre'], engine='python')

# Rating data, only use columns 0,1, and 2 because we don't care about the timestamp for our hypothosis
rating_data = np.genfromtxt('movielens\\ratings.dat', delimiter='::', dtype=None, names=['UserID','MovieID','Rating'], usecols=(0,1,2))

# User Data, only use columns 0, 1, and 2 because we don't care about occupation or zipcode
user_data = np.genfromtxt('movielens\\users.dat', delimiter='::', dtype=None, names=['UserID','Gender','Age'], usecols=(0,1,2))

# Used to save the data
movie_data_filtered = []
rating_data_filtered = {}
user_data_filtered_old = []
user_data_filtered_young = []

# Pull the movieID for drama movies
for index, movie in movie_data.iterrows():
	
	# Filter fantasy out
	if "fantasy" in movie["Genre"].lower():
		
		# Add the MovieID to our list
		movie_data_filtered.append(movie["MovieID"])

# Convert it back to an ndarray
movie_data_filtered = np.array(movie_data_filtered)

# Get the ratings for these movies
for rating in rating_data:

	# Check to see if the movieID is in our filtered out movies
	if rating["MovieID"] in movie_data_filtered:
		# Get their userID
		userID = rating["UserID"]
		
		# Get any previous ratings
		rating_arr = rating_data_filtered.get(userID, [])	
		
		# Add the ratings
		rating_arr.append(rating["Rating"])
		
		# Save!
		rating_data_filtered[userID] = rating_arr

# Filter out the users who rated our movies
for user in user_data:
	userID = user["UserID"]
	
	# Check to see if our user has rated a filtered movie
	if user["Age"] >= 35:
		rating = rating_data_filtered.get(userID,-1)
		if rating != -1:
			user_data_filtered_old += rating
	elif user["Age"] <= 25:
		rating = rating_data_filtered.get(userID,-1)
		if rating != -1:
			user_data_filtered_young += rating

# Calulate the mean for both groups/
oldMean = np.mean(user_data_filtered_old)
youngMean = np.mean(user_data_filtered_young)

# Print out the data so we can see it in plain text
print "35yrs and older"
print "   Mean: {}".format(oldMean)
print "   Count: {}".format(len(user_data_filtered_old))

print "25yrs and younger"
print "   Mean: {}".format(youngMean)
print "   Count: {}".format(len(user_data_filtered_young))

# Create the X-axis for both graphs
objects = ('25yrs and younger', '35yrs and older')
y_pos = np.arange(len(objects))

# Average rating graph
fig1 = plt.figure('Average Rating')
pl1 = fig1.add_subplot(1,1,1)
pl1.bar(y_pos, [youngMean, oldMean], align='center', alpha=0.5)
pl1.set_xticks((0,1))
pl1.set_xticklabels(objects)
pl1.set_yticks((1,2,3,4,5))
pl1.set_ylabel('Rating')
pl1.set_title('Average Rating for Fantasy Movies')

# Number of votes graph
fig2 = plt.figure('Number of Votes')
pl2 = fig2.add_subplot(1,1,1)
pl2.bar(y_pos, [len(user_data_filtered_young), len(user_data_filtered_old)], align='center', alpha=0.5)
pl2.set_xticks((0,1))
pl2.set_xticklabels(objects)
pl2.set_ylabel('Number of Votes')
pl2.set_title('Number of Votes')

# Show em!
plt.show()
