###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
age = int(input('Enter age: '))
tax_exemption = "YES" if age < 26 else "NO"
print(f'Exemption from paying taxes: {tax_exemption}')
