# Program to search through a file for numbers and print the sum of all of them.
import re                                             # importing regular expressions.

a = input("Enter the file to be opened:")
b = open(a)
c = list()                                            # Creating an empty list.
for line in b:
    if not re.findall('([0-9]+)',line): continue      # Skipping lines which do not have numbers in them.
    x = re.findall('([0-9]+)',line)                   # Creating a list of all the numbers in the opened file.
    c = c + x                                         # Appending the list into the empty list.
sum = 0
for z in c:
    sum = sum + int(z)                                # Finding the sum of all the numbers in the file.

print("Sum is: ",sum)