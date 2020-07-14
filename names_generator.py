# Write a program to make a list of names that start with a particular letter.

import names                                                                # Importing the directory which generates random names.
a = list()                                                                  # Creating an empty list to contain the names.
x = input("Enter the letter with which you want the names to begin:")
if x.isupper():                                                             # Used because the names package generates names which start with an uppercase letter.
    for number in range(1,100):
        tempName = names.get_first_name()                                   # Statement to set whether the names will be male,female or gender-neutral.[to be entered like 'male']
        if tempName.startswith(x):
            a.append(tempName)                                              # Appending the name to the list.

    l = len(a)
    print(f"These are the names starting with the letter {x}:\n")
    for index in range(0,l):                                                # Going through all the names in the list and printing them in an vertical fashion.
        print(a[index])
else :
    print(f"Please enter the letter in uppercase.")

# The same code can be repeated as many times as you please to give out as many lists as you please.
