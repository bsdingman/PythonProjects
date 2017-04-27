#############################################################
# Bryan Dingman
# Using a names and counts from 1880 to 2010, find statistical 
# information about names and their popularities
#############################################################

import os
import pandas as pd
import numpy as np
from sys import platform
from collections import OrderedDict

###################################################################################
def prettyPrints(infoArray):

	for name, mean, median, std, skew, kurt in infoArray:
		print "{}'s stats: \n".format(name), \
			  "    Mean: {} \n".format(mean), \
			  "    Median: {} \n".format(median), \
			  "    Standard Deviation: {} \n".format(std), \
			  "    Skewness: {} \n".format(skew), \
			  "    Kurtosis: {} \n".format(kurt)

###################################################################################

def findAnswersPart1(dataframe, names):

	# It's the final Answer
	answers = []

	for name in names:
		# literally just a placeholder
		placeholder = []

		# Append the name so we know who's data it is
		placeholder.append(name)

		# Get the values for this name across the years
		worldSeries = pd.Series(dataframe[name])

		# Self explainatory, returns mean, median, standard deviation, skew and kurt
		placeholder.append(worldSeries.mean())
		placeholder.append(worldSeries.median())
		placeholder.append(worldSeries.std())
		placeholder.append(worldSeries.skew())
		placeholder.append(worldSeries.kurt())

		# Once we are done, add it to our answers
		answers.append(placeholder)

	# RETURN IT
	return answers

###################################################################################

def findObscurity(dataframe):
	# We want to remember everything
	dictionary = {}

	# Loop through our dataframe. I'm using iteritems because I need the column name and the data
	for name, data in dataframe.iteritems():
		# Get the kurtosis from the data
		kurt = data.kurt()

		# Make sure we don't have any nan values
		if pd.notnull(kurt):

			# Save it!
			dictionary[name] = kurt

	# Sort it so our max is at the top
	dictionary = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1], reverse=True))

	# Return the kertosis.
	return dictionary.items()[0]

###################################################################################

def findFame(dataframe):
	# We want to remember everything
	dictionary = {}

	# Loop through our dataframe. I'm using iteritems because I need the column name and the data
	for name, data in dataframe.iteritems():

		# Get the mean and median from the data
		mean = data.mean()
		median = data.median()

		# Make sure we don't have any nan values
		if (pd.notnull(mean) and pd.notnull(median)):

			# Check to see if they are equal to each other
			if mean == median:
				# Save it!
				dictionary[name] = [mean, median]

	# Sort it so our max is at the top
	dictionary = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1][0], reverse=True))

	# Return the answer.
	return dictionary.items()[0]


###################################################################################
#									MAIN!!!
###################################################################################
# Set these up ahead of time
females = {}
males = {}

# Loop through all of our files in the names folder
for file in os.listdir("names"):

	# Get the filename and ext so we can do stuff
	fileName, ext = os.path.splitext(file)

	# Make sure we are only accessing ".txt" files and not ".pdf"s
	if ext == ".txt":
		# Subset off the year (yob1880 -> 1880)
		yearName = fileName[3:]

		# Create a dictionary for this year
		yearDictMale = {}
		yearDictFemale = {}

		# Just because I code on a mac and a pc. This is for mac/linux
		csvName = "names/{}".format(file)

		# Change if we are on windows
		if platform == "win32":
			csvName = "names\\{}".format(file)

		# Read in our data
		df = pd.read_csv(csvName, names=["Name", "Gender", "Count"])

		# Loop through
		for index, row in df.iterrows():

			# Separate off the female's from the males
			if row["Gender"] == "F":
				yearDictFemale[row["Name"]] = row["Count"]
			elif row["Gender"] == "M":
				yearDictMale[row["Name"]] = row["Count"]

		# Add it to our dictionary
		females[yearName] = yearDictFemale
		males[yearName] = yearDictMale

# Convert from dictionaries to dataframes so we can do magic!
femalesDF = pd.DataFrame.from_dict(females, orient='index')
malesDF = pd.DataFrame.from_dict(males, orient='index')

# Get our answers for part 1
maleAnswers = findAnswersPart1(malesDF,["Felix", "Tom", "Leon"])
femaleAnwers = findAnswersPart1(femalesDF,["Ella", "Bertha", "Lida"])

# Get our answers for part 2!
femaleObscruity = findObscurity(femalesDF)
maleObscruity = findObscurity(malesDF)

femaleFame = findFame(femalesDF)
maleFame = findFame(malesDF)

# Pretty prints returns for another exciting adventure!
print "========== Three Male Stats =========="
prettyPrints(maleAnswers)

print "========== Three Female Stats =========="
prettyPrints(femaleAnwers)

# Part 1 answer
print "========== Answer for Part 1 ==========\n\n", \
	  "If the skewness value is positive, the data is right skewed. If the value is negative, it is left skewed. \n", \
	  "Skewness for our data would mean that the name is more popular either at the beginning or the end of the data. \n\n", \
	  "Kurtosis, from what I understand of it, is how distibuted the data is in the outliers. A positive kurtosis would show an influx of data at point, then disappearing. The the pandas kurt uses Fishers definition, the values are based off 0, not 3.\n\n", \
	  "Felix's stats: \n", \
	  "Felix's data is fairly symmetrical but it is left skewed since it's between 0.5 and -0.5 \n", \
	  "His kurtosis tells me that it's slightly off 'normal' on the negative side\n", \
	  "    Skewness: -0.478220731152\n", \
	  "    Kurtosis: -0.790946451649\n", \
	  "Tom's stats:\n", \
	  "Tom's data is highly skewed to the right since it's greater than 1\n", \
	  "HIs kurtosis is off normal, more on the positive side\n", \
	  "    Skewness: 1.63553299666\n", \
	  "    Kurtosis: 2.14996051873\n", \
	  "Leon's stats:\n", \
	  "Leon's data is closer to normal distribution with a slight skew to the right\n", \
	  "His kurtosis is more uniform than normal\n", \
	  "    Skewness: 0.353048378837\n", \
	  "    Kurtosis: -1.4972081473\n", \
	  "Ella's stats:\n", \
	  "Ella's skew is highly skewed to the right with a large kurtosis making her name more of a canidate for obscurity.\n", \
	  "    Skewness: 2.7116133404\n", \
	  "    Kurtosis: 7.75079435566\n", \
	  "Bertha's stats:\n", \
	  "Bertha's skew is closer to normal with a slight skew to the right and her kurtosis is closer to normal\n", \
	  "    Skewness: 0.719032396015\n", \
	  "    Kurtosis: -0.222081397401\n", \
	  "Lida's stats:\n", \
	  "Lida's skewness is about the same as Bertha's with a slight skew to the right and her kurtosis is closer to normal\n", \
	  "    Skewness: 0.708984947951\n", \
	  "    Kurtosis: -0.0955514528549\n\n"

print "========== Part 2 Answers =========="

print "The most consistently popular male name between 1880 and 2010 is: {} \n".format(maleFame[0]), \
	  "Why is that? It's because it's mean of {} and it's median of {} are equal to each other. \n".format(maleFame[1][0], maleFame[1][1])

print "The most consistently popular female name between 1880 and 2010 is: {} \n".format(femaleFame[0]), \
  	  "Why is that? It's because it's mean of {} and it's median of {} are equal to each other. \n".format(femaleFame[1][0], femaleFame[1][1])

print "The male name that found extreme fame and then disppeared is: {} \n".format(maleObscruity[0]), \
	  "Why is that? It's because it's kurtosis of {} is the highest of all the male names.\n".format(maleObscruity[1])

print "The female name that found extreme fame and then disppeared is: {} \n".format(femaleObscruity[0]), \
  	  "Why is that? It's because it's kurtosis of {} is the highest of all the female names.\n".format(femaleObscruity[1])
