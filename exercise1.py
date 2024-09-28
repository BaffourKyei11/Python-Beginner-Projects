# TODO: Add a line below that will read the amount from the user.
# Don't forget to convert it to an integer using int(). You
# need to store this in a variable. Something like this: 
# amount = ....
loan_amount = float(input("Enter the loan amount: "))

# TODO: Add a line below to create a variable that will represent 
# the interest rate in per cent, for example 4% will be written 
# as interest_rate = 4.
interest_rate = 4  # in percent

# TODO: Add a line below to compute the interest given the amount 
# and the interest per cent. The formula is: amount * (interest_rate / 100)
# but you will need to replace the above variables in the formula with
# the variable names you have created. Also, you
# need to store the result in a variable! So you should do something
# like this:  interest = ....
interest = loan_amount * (interest_rate / 100)

# TODO: Finally, below add a line that will print the result. Try to make
# this output nice and complete. Use f-string to inject variables in the 
# message. For example, print(f'Amount: {amount} ...') (the amount now
# is a variable that will dynamically going to be expanded by Python when
# we run our program).
print(f'The total interest to be paid in a year is: ${interest}')

