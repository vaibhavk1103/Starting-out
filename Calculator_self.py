# Creating a calculator.
num1 = input("Enter the first number:")
try:
    num1 = int(num1)                                                                # Converting to integer type for calulations.
except:
    print(f"{num1} is not a valid number, please enter a valid number.")
    quit()
num2 = input("Enter the second number:")
try:
    num2 = int(num2)                                                                # Converting to integer type for calulations.
except:
    print(f"{num2} is not a valid number, please enter a valid number.")
    quit()
print("List of available operations\n"
      "1 for Addition.\n"
      "2 for Subtraction.\n"
      "3 for Multiplication.\n"
      "4 for Division.\n"
      "5 for Modulus.\n")
op = input("Enter the number corresponding to the operation you want to perform:")
try:
    op = int(op)                                                                    # Converting to integer type.
except:
    print(f"{op} doesn't correspond to any of the available operations, please enter a number corresponding to the available options.")
    quit()
def addition():                                                                     # Defining the addition function to perform addition.
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}.")

def subtraction():                                                                  # Defining the subtraction function to perform subtraction.
    difference = num1 - num2
    print(f"The difference of {num1} and {num2} is {difference}.")

def multiplication():                                                               # Defining the multiplication function to perform multiplication.
    multi = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {multi}.")

def division():                                                                     # Defining the division function to perform division.
    div = num1 / num2
    print(f"The quotient of {num1} divided by {num2} is {div}.")

def modulo():                                                                      # Defining the modulo function to perform modulus of two numbers.
    mod = num1 % num2
    print(f"The remainder of {num1} and {num2} is {mod}.")

if op == 1:
    addition()
elif op == 2:
    subtraction()
elif op == 3:
    multiplication()
elif op == 4:
    division()
elif op == 5:
    modulo()


