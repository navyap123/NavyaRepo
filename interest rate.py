initial_deposit_amount = int(raw_input("Enter the initial deposit amount: "))
interest_rate = float(raw_input("Enter the interest rate as a whole number: "))
no_of_years = int(raw_input("Enter the number of years: "))
balance_after_3_years = ((1+interest_rate/100)**no_of_years)*initial_deposit_amount
print "balance after 3 years is ${0:.2f}".format(balance_after_3_years)