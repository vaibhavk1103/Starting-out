from covid import Covid                                                                                         # Importing required packages.


def ncov():                                                                                                     # Defining method to get statistics.
    covid = Covid()
    print(f"Total confirmed Covid-19 cases till date : {covid.get_total_confirmed_cases()}")                    # Function tov get total cases. [World]
    print(f"Total recoveries from Covid-19 till date : {covid.get_total_recovered()}")                          # Function to get total recovered cases. [World]
    print(f"The total number of active Covid-19 cases till date: {covid.get_total_active_cases()}")             # Function to get total active cases. [World]
    print(f"Total deaths due to the Covid-19 till date : {covid.get_total_deaths()}")                           # Function to get total deaths. [World]
    try:
        print(covid.get_status_by_country_name(
            input("Enter the name of the country for which you want the current details: ")))                   # Function to get details of a specific country.
        print("\n\nClean your hands often. Use soap and water, or an alcohol-based hand rub.\n"                       # Caution message.
                "Maintain a safe distance from anyone who is coughing or sneezing.\n"
                "Wear a mask when physical distancing is not possible.\n"
                "Don’t touch your eyes, nose or mouth.\n"
                "Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n"
                "Stay home if you feel unwell.\n"
                "If you have a fever, cough and difficulty breathing, seek medical attention.\n")
        print("All statistics have been verified and are sourced from https://www.worldometers.info/")
    except:
        print("Please input a valid country or check your spelling.")                                           # Error message.


a = (input("Do you want the latest details on Covid-19? [Y or N]: "))                                           # Prompt for iteration.
a.lower()

while a == 'y':                                                                                                 # Case to give information.
    ncov()
    a = (input("Do you want the latest details on Covid-19? [Y or N] "))
    a.lower()
else:                                                                                                           # Default case.
    print("Have a good day and stay safe.")
