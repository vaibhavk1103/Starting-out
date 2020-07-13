# Write a program to calculate the amount to be tipped at a restaurant.


base_bill = input("Enter the amount of your bill:")
tip_percentage = input("Enter the percentage you want to tip:")
if base_bill.isdigit() and tip_percentage.isdigit() :              # Precaution - Do not enter spaces while entering
                                                                   #              bill or tip percentage.
    og_bill = int(base_bill)
    tip = (int(tip_percentage)/100)*og_bill                        # Calculation of amount to be tipped.
    final = og_bill + tip                                          # Final bill.
    print(f"your original bill is {base_bill}")
    print(f"Your tip is {tip}")
    print(f"Your final bill is {final}")
else:
    print(f"Please enter valid numbers for bill value and tip percentage")
