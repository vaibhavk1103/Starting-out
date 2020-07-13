# Write a program to calculate the weekly, monthly and yearly salary of a person (in dollars).

hs = input("Enter your hourly wage:")
hpw = input("Enter the number of hours you work per week:")
if hs.isdigit() and hpw.isdigit():               # Checking whether the entered strings are number or not.
    hs = int(hs)
    hpw = int(hpw)
    ws = hs * hpw                                # Calculating weekly salary.
    print(f"Your weekly salary is ${ws}.")
    ms = ws * 4                                  # Calculating monthly salary.
    print(f"Your monthly salary is ${ms}.")

    # Yearly salary can also be calculated by using the formula ys = ms * 12

    ys = ws * 48                                 # calculating yearly salary.
    print(f"Your yearly salary is ${ys}.")
else:
    print("Please enter numbers for hours per week and hourly salary")
    quit()