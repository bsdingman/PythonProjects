'''
Bryan Dingman
Compare multiple wiki articles under the same category and return the dictionaried words from wikis.
Use MediaWiki API to complete this
'''

import requests
from collections import OrderedDict

############################################################################
'''
Requests wiki page using mediaWiki API and requests process of the extract to be returned

INPUT:
	Name of Wiki - STRING

OUTPUT:
	extracted word dictionary - DICTIONARY
'''
def requestWiki(name):
	dictionary = {}
	response = requests.get(
	    'https://en.wikipedia.org/w/api.php',
	    params={
	            'action': 'query',
	            'format': 'json',
	            'titles': name,
	            'prop': 'extracts',
	            'exintro': True,
	            'explaintext': True,
	           }
	    ).json()
	page = next(iter(response['query']['pages'].values()))

	dictionary = processExtract(page['extract'])

	return dictionary

############################################################################
'''
Processes the extract string from a wikipedia article and counts the words.

INPUT:
	extract - STRING

OUTPUT:
	extracted word dictionary - DICTIONARY
'''
def processExtract(extract):
	dictionary = {}

	# Remove extra crap
	extract = extract.replace("."," ")
	extract = extract.replace(","," ")
	extract = extract.replace("("," ")
	extract = extract.replace(")"," ")

	words = extract.split()
	for word in words:
		dictionary[word] = dictionary.get(word, 0) + 1

	dictionary = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1], reverse=True))
	return dictionary

############################################################################

###################################################################################
# Main
###################################################################################
windowsDict = requestWiki('Microsoft_Windows')
applesDict = requestWiki('Macintosh_operating_systems')
linuxDict = requestWiki('Linux')

print "==================","Windows","=================="
for word,count in windowsDict.items():
	print word,count

print "\n","\n","==================","Mac OS","=================="
for word,count in applesDict.items():
	print word,count

print "\n","\n","==================","Linux","=================="
for word,count in linuxDict.items():
	print word,count