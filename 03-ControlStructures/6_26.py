pin = "0805"
correct = False
entered_pin = ""
counter = 0
while not correct and counter < 3:
    entered_pin = input("Enter the PIN code: ")
    if entered_pin != pin:
        counter += 1
        print("Incorrect...")
        if counter == 3:
            print("Sorry, your payment card has been blocked.")
            continue
        continue
    correct = True
