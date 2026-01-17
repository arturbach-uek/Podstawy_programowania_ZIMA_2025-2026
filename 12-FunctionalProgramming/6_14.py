capacity = 500
tolerance = 2
bottles = [508,500,512,499,492,511,503,476,501,509]

def is_incorrect(tolerance):
    return lambda volume: abs(volume - capacity) > (capacity * tolerance / 100)

incorrect_bottles = list(filter(is_incorrect(tolerance), bottles))

percentage_incorrect = round(len(incorrect_bottles) / len(bottles) * 100)

print(f"Bottle capacity:    {capacity}ml")
print(f"Filling tolerance:  {tolerance}%")
print(f"Filled bottles:     {','.join(map(str,bottles))}")
print(f"Incorrectly filled: {percentage_incorrect}%")
