# Gary Morrissey, 11-02-2018
# The Collatz Conjecture program

i = int(input("Please enter any integer:")) # Prompts you to choose a number, with the next term being obtained from the previous term 

while i > 1: 
    if i % 2 == 0: 
        i = i / 2 # If the previous term is even, the next term is one half the previous term
        print(i) 
    else:
        i = (3 * i) + 1 # Otherwise, the next term is 3 times the previous term plus 1
        print(i) # The conjecture is that no matter what value of n, the sequence will always reach 1
