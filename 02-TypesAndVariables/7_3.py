###
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
#

number = int(input('Enter number: '))
parity = "even" if number % 2 == 0 else "odd"
print(f'Number is {parity}')