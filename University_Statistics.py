'''
Bryan Dingman
Lab 3 Part 1, find word counts within files that contain urls to find more words, because I like wordceptions.
Yes, I could've used methods, but I couldn't justify it for this particular script.
'''

import requests
from collections import OrderedDict
import os

# Main
files = {"top5_BRZ", "top5_CHI", "top5_FRA", "top5_GER", "top5_IND", "top5_RUS", "top5_SAF", "top5_US"}

try:
    # Loop through all of our files
    for file in files:

        # check to see if the results file exists, delete if it does
        if os.path.isfile(file + "_results.txt"):
            os.remove(file + "_results.txt")

        # Create our new results file
        newFile = open(file + "_results.txt","a")

        # Word dictionary
        dictionary = {}

        # open our url file and read lines
        file = open(file + ".txt")
        lines = file.readlines()
        for line in lines:
            urls = line.split()

            # Process each URL
            # Catch if we can't get the URL
            try:
                for url in urls:

                    # Get the HTML
                    text = requests.get(url).text

                    # Remove a bunch of extra crap
                    text = text.replace("<"," ")
                    text = text.replace(">"," ")
                    text = text.replace('"'," ")
                    text = text.replace("'"," ")
                    text = text.replace("="," ")
                    text = text.replace("/"," ")
                    text = text.replace("\\"," ")
                    text = text.replace("."," ")
                    text = text.replace(","," ")
                    text = text.replace("("," ")
                    text = text.replace(")"," ")
                    text = text.replace(";"," ")
                    text = text.replace("{"," ")
                    text = text.replace("}"," ")
                    text = text.replace(":"," ")
                    text = text.replace("#"," ")
                    text = text.replace("-"," ")
                    text = text.replace("_"," ")
                    text = text.replace("|"," ")
                    text = text.replace("!"," ")
                    text = text.replace("["," ")
                    text = text.replace("]"," ")
                    text = text.split()

                    # Loop through the words and add it to the dictionary.
                    # I'm tired, lazy vars
                    for ugh in text:
                        if ugh != "":
                            dictionary[ugh] = dictionary.get(ugh, 0) + 1
            except IOError:
                print "Failed to open: ", url, "successfully"

        # Sort our dictionary
        dictionary = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1], reverse=True))

        # loop through, grap the first 25
        loopCount = 0
        for word,count in dictionary.items():
            if loopCount > 24:
                break

            # Write to file
            newFile.write("{} {}\n".format(word,count))
            loopCount += 1

        #Don't forget!
        newFile.close()
except IOError:
    print "Failed to open: ", file, "successfully"


