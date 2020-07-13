# Write a program to classify a person as a kid, a teenager or an adult.

age = input("Enter your age :")      # Taking inout from user.
if age.isdigit():                    # Precaution do not use spaces while entering age as that will produce a traceback.
    print(f"User's age is :{age}")   # Printing user's age.
    age = int(age)
    if age<13:
        print("You are a kid.")      # Classification 1.
    elif age<20:
     print("You are a teenager.")    # Classification 2.
    else :
        print("You are an adult.")   # Classification 3.
else:
 print(f"{age} is not a valid number, please enter a valid number.")