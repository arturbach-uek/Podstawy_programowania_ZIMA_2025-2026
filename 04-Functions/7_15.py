def max_people_at_least_3(detector):
    count = 0
    for c in detector:
        if c == "+":
            count += 1
        if c == "-":
            count = 0
        if count >= 3:
            return True
    return False

print(max_people_at_least_3("+-+++-+---"))