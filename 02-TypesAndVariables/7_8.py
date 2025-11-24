###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#

import random
total = 0
for i in range(3):
    dice_roll = random.randint(1, 6)
    total += dice_roll

print("\n", total)