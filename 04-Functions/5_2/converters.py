def m_to_cm(n):
    return n * 100

def cm_to_m(n):
    return n / 100

def cm_to_inch(cm):
    return cm / 2.54

def ft_in_to_cm(feet, inches=0):
    total_inches = feet * 12 + inches
    return total_inches * 2.54

if __name__ == "__main__":
    print(f'2 m = {m_to_cm(2)} cm')
    print(f'532 cm = {cm_to_m(532)} m')
    print(f'100 cm = {cm_to_inch(100):.2f} inches')
    print(f'5 ft 8 in = {ft_in_to_cm(5, 8):.2f} cm')
