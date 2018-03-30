# Gary Morrissey, 30-March-2018
# Topic 6 - Factorial of an integer value
# Adapted from https://www.programiz.com/python-programming/examples/factorial

x = int(input("Please enter an integer:"))

factorial = 1

if x < 0: # check if the number is negative, positive
   print("Sorry, factorial does not exist for negative numbers")
elif x == 0: # check if the number is zero
   print("The factorial of 0 is 1")
else:
   for i in range(1, x + 1):
       factorial = factorial * i
   print("The factorial of", x, "is", factorial) 
