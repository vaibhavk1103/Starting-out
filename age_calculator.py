# Write a program to calculate the age of the user, prompt the user for the current year and the year they were born in.

cy = input("Enter current year(YYYY):")
if cy.isdigit():
    cy = int(cy)          # converting year to an integer for calculations.
else:
    print("Please enter a valid year")
    quit()
by = input("Enter your birth year(YYYY):")
if by.isdigit():
    by = int(by)          # converting year to an integer for calculations.
    if cy < by:
        print(f'Please enter a year less than {cy}')    # negative age is not possible.
    else:
        print(f"The user's birth year is {by}")
        ca = cy - by            # calculating age.
        if ca<150 :
            print(f"The user's current age is {ca}")
        if ca>150 :
            print(f"Please enter a reasonable age")

        if 100<ca<150 :
            print(f"Congratulations on living more than a hundred years")
else:
    print('Please enter a valid year')
