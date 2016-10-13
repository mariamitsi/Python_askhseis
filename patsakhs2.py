#!/usr/bin/env python

# Import needed libraries and modules for the program to run
from urllib.request import urlopen
import json
import time

date = time.strftime("%d/%m/%Y") # Set date format to DD-MM-YYYY and assign it to the "date" variable

url = "http://applications.opap.gr/DrawsRestServices/Kino/drawDate/" + date + ".json" # Assign the url with the current date's results to the "url" variable
draw_kino = urllib.urlopen(url) # Create the object to open the url
data = json.load(draw_kino) # Load the json data from the url to use them in the program

n = 1

# Create the function to find the 7 numbers with the highest frequency
def highest_frequency_numbers(seq = data["results"]): 
	 "dict items"
    c = dict()
    while (n < 7):
		for item in seq:
			c[item] = c.get(item, 0) + 1
		seq.remove(max(seq)) # Remove the highest number in seq, so as to not count it more than once in the while loop
		n = n + 1
	return max(c.items(), key=itemgetter(1))


# Create the function to find the 7 numbers with the lowest frequency
def lowest_frequency_numbers(seq = data["results"]): 
	 "dict items"
    c = dict()
    while (n < 7):
		for item in seq:
			c[item] = c.get(item, 0) + 1
		seq.remove(min(seq)) # Remove the lowest number in seq, so as to not count it more than once in the while loop
		n = n + 1
	return min(c.items(), key=itemgetter(1))

print ("The 7 most frequent numbers are: ", max(c.items()) /n, "The 7 least frequent numbers are: ", min(c.items()))
	