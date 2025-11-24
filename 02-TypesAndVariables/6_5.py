###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
phone_formatted = "-".join(phone[i:i+3] for i in range(0, 9, 3))
print(f"Formatted phone number: {phone_formatted}")