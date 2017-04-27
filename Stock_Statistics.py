#############################################################
# Bryan Dingman
# Using stocks from 4 different companys, run statistical 
# functions using numpy. 
#############################################################

import numpy as np

#############################################################
#					FUNCTIONS
#############################################################

"""
	FUNCTION: applyData
	INPUT:
		col - ndarray
	OUTPUT:
		formatted values - ARRAY

	applyData takes in a numpy array of stocks that match the year values from our CSV
	Then runs our statistical functions on them, pushing each returned value to our array
	to be returned back so we can print it out
"""
def applyData(col):
	array = []

	# Remove the "Stock tag"
	col = np.delete(col,0)

	# Convert to floats from strings
	col = col.astype(np.float32)

	# Do overalls first (not the clothing)
	#min
	array.append(col.min())

	#max
	array.append(col.max())

	#mean
	array.append(np.mean(col))

	#median
	array.append(np.median(col))

	#variance
	array.append(np.var(col))

	# Bdingman Score
	array.append(np.std(col))

	# Just for ease of printings
	array.append([])

	# Process for per year
	for year, count in years:

		# Separate out the values for the year only
		year_stock = col[0:count]

		# Create the array for the year with the year in the front
		year_arr = [year]

		#min
		year_arr.append(year_stock.min())

		#max
		year_arr.append(year_stock.max())

		#mean
		year_arr.append(np.mean(year_stock))

		#median
		year_arr.append(np.median(year_stock))

		#variance
		year_arr.append(np.var(year_stock))

		# Bdingman Score
		year_arr.append(np.std(col))

		# Append it to our return so we can use it later
		array[6].append(year_arr)

		# Remove the already touched values
		col = np.delete(col,np.s_[0:count])

	# Return our numbers!
	"""
	[
		overall_min,
		overall_max,
		overall_mean,
		overall_median,
		overall_variance,
		[
			year,
			yr_min,
			yr_max,
			yr_mean,
			yr_median,
			yr_variance
		],
		...
	]
	"""
	return array

#############################################################
#############################################################
#############################################################

"""
	FUNCTION: prettyPrints
	INPUT:
		formated values - ARRAY
		name - STRING
		stock_tag - STRING
	OUTPUT:
		None

	prettyPrints (A running joke from my time at Kroger), this function takes in our formatted values array
	and prints out the overall scores and yearly scores in a pretty printed format!
"""
def prettyPrints(array, name, stock_tag):
	print "{} ({})\n".format(name, stock_tag), \
			"Overall scores: \n", \
			"	Min: {:.2f}\n".format(array[0]), \
			"	Max: {:.2f}\n".format(array[1]), \
			"	Mean: {:.2f}\n".format(array[2]), \
			"	Median: {:.2f}\n".format(array[3]), \
			"	Variance: {:.2f}\n".format(array[4]), \
			"    Bsdingman Score (Standard Deviation): {:.2f}".format(array[5])

	for year, yr_min, yr_max, yr_mean, yr_median, yr_variance, yr_bsdscore in array[6]:
		print "{}'s {} scores: \n".format(name, year), \
			"	Min: {:.2f}\n".format(yr_min), \
			"	Max: {:.2f}\n".format(yr_max), \
			"	Mean: {:.2f}\n".format(yr_mean), \
			"	Median: {:.2f}\n".format(yr_median), \
			"	Variance: {:.2f}\n".format(yr_variance), \
			"    Bsdingman Score (Standard Deviation): {:.2f}".format(yr_bsdscore)

	print "__________________________________________"


#############################################################
#					MAIN SCRIPT
#############################################################

# Read from our CSV
csv = np.genfromtxt('stock_px.csv', delimiter=',', dtype=None)

# Calculated numpy array for figuring out indices (Dynamic maybe?)
years = np.array([])

# Declare these arrays for storage
aapl_stock = []
msft_stock = []
xom_stock = []
spx_stock = []

# Trim out dates
for ind, val in enumerate(csv):

	if (ind != 0):

		# Trim out the dates
		val[0] = val[0][:4]

		# Adjust the original array (holy sh*t, we can do this in python???)
		csv[ind][0] = val[0]

		# Take our years into an array so we can figure out the indexes for them
		years = np.hstack((years,val[0]))

		# convert from string to int16
		years = years.astype(np.int16)

# get the frequency of the years
binC = np.bincount(years)

# Return our non-zero elements
binC2 = np.nonzero(binC)[0]

# Return an ndarray with [year, count]
years = np.vstack((binC2,binC[binC2])).T

# Get our calculated values back for apple
aapl_stock = applyData(csv[:,1])

# Get our calculated values back for Microsoft
msft_stock = applyData(csv[:,2])

# Get our calculated values back for Exxon
xom_stock = applyData(csv[:,3])

# Get our calculated values back for SPX
spx_stock = applyData(csv[:,4])

# All that fancy stuff
# Print Apple
prettyPrints(aapl_stock,"Apple","AAPL")

# Print Microsoft
prettyPrints(msft_stock,"Microsoft","MSFT")

# Print Exxon
prettyPrints(xom_stock,"Exxon","XOM")

# Print SPX
prettyPrints(spx_stock,"SPX","SPX")