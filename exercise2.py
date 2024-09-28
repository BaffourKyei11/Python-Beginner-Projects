# TODO: Add a line below that will read the temperature in Celsius from 
# the user. Don't forget to convert it to a float using float(). You
# need to store this in a variable. Something like this: 
# temperature_in_celsius = ....
temperature_in_celsius = float(input('What is your temperature:'))

# TODO: Now, add a line below that will compute the temperature in 
# Fahrenheit. The formula is: (temperature_in_celsius * 1.8) + 32
# Obviously, you will need to replace temperature_in_celsius with
# the variable name you have created in the line above. Also, you
# need to store the result in a variable! So you should do something
# like this: temperature_in_fahrenheit = ....
temperature_in_fahrenheit = (temperature_in_celsius * 1.8) + 32

# TODO: Finally, add a line below and use the print function to print
# the result to the user using a nice and explanatory message. Again,
# use f-string to inject dynamic values through variables (i.e., the
# temperature in fahrenheit).
print(f'Your temperature in fahrenheit is {temperature_in_fahrenheit = }')
