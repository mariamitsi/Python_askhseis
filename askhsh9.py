#!/usr/bin/env python

n = int(input("Enter your number: ")) # Writing the number as input from keyboard
count = 0 # Setting the innitial value of count to 0

while (n > 9):
    product = 1 # Setting the innitial value of product to 1
    while (n):
        product *= n % 10 # get the last digit of input number and multiply it to product
        n //= 10 # Remove last digit form input number
    n = product # Set the number equal to product
    count = count + 1 # Increase the count of loops by one with each loop that is completed

print ("The count is: " , count ) # Print the count of the loops performed
