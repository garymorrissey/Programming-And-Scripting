# Gary Morrissey, 11-02-2018
# The Collatz Conjecture program

i = int(input("Please enter any integer:"))

while i > 1:
    if i % 2 == 0:
        i = i / 2
        print(i)
    else:
        i = (3 * i) + 1
        print(i)
