###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == "1":
        print(f"Your current balance is: €{balance}")

    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")

    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        if all(digit.isdigit() for digit in pin):
            print("PIN is correct (only digits)") 
        else:
            print("PIN contains invalid characters")

    elif choice == "5":
        current = input("Enter your current PIN: ")
        if current == pin:
            new_pin = input("Enter new PIN (only digits, 4 characters): ")
            if new_pin.isdigit() and len(new_pin) == 4:
                pin = new_pin
                print("Successfully changed PIN")
            else: 
                print("Invalid PIN! It must be exactly 4 digits.")
        else:
            print("Incorrect current PIN!")

    elif choice == "6":
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")