import math

# Request the user to choose their choice of a menu for an investment or a bond
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
choice = input("would you like to carry out an investment or bond? ")

# Create an if and else statement to calculate the users total amount based on a variety of factors 
if choice.lower() == "investment":
    deposit = float(input("Enter the amount of money you are depositing "))
    interest_rate = float(input("Enter the interest rate that will be applied on the amount "))
    years = int(input("Enter the number of years you plan on investing "))
    interest = input("Would you like simple interest or compound interest? ")

    if interest.lower() == "simple interest":
        total_amount = deposit*(1+(interest_rate/100)*years)
        print (total_amount)
    
    elif interest.lower() == "compound interest":
        total_amount = deposit* math.pow((1+(interest_rate/100)),years)
        print (round(total_amount,2))

elif choice.lower() == "bond":
    value = int(input("Enter the present value of the house "))
    interest_rate = float(input("Enter the interest rate that will be applied on the amount "))
    number_of_months = int(input("Enter the number of months you will take to re-pay the bond "))
    total_amount = (interest_rate*value)/(1- (1+ interest_rate)**(- number_of_months))
    print (round(total_amount,2))
