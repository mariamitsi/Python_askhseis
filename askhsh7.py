#!/usr/bin/env python

n = int(input("Enter your number: ")) # Writing the number as input from keyboard 
nint = int(n ** 0.5) # Setting the nint variable as the square root of input number in integer form
if (n ** 0.5 == nint): # Checking if the square root of input number is equal to nint
    print ("True") # If the square root of input number is equal to nint, then "True" is printed as output
else:
    print ("False") # If the square root of input number is not equal to nint, then "False" is printed as output
