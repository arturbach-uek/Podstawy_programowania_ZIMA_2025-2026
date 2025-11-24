###
# A program that prints your height both in cm and in feet and inches.
###

cm = 170

# 1 inch = 2.54 cm
total_inches = cm / 2.54

# calculate the number of feet
feet = int(total_inches // 12)  # full feet
inches = round(total_inches % 12)  # remaining inches

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
