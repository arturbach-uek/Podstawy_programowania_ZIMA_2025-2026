import random
dice_rolled = random.randint(1, 6)
is_special = dice_rolled == 1 or dice_rolled == 6
print(f"Dice rolled: {dice_rolled}")
print(f"Special number (1 or 6): {is_special}")
