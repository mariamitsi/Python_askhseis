#!/usr/bin/env python

# Import needed libraries for the program to run
import requests
import json

t = input("Enter the movie name: ") # Writing the movie as input rom keyboard
url = "http://www.omdbapi.com/?" + t + "&y=&plot=short&r=json" # Add the movie name to the url, so as to get the movie info

data = requests.get(url).json() # Load the url and get the json data from omdbapi to use them in the program
   
for item in data['Response']: 
	print ("Movie name: ", item['Title'], "\n", "IMDB Rating: ", item['imdbRating'], "\n", "Won awards: ", item['Awards']) # Print the movie info from the omdapi response

