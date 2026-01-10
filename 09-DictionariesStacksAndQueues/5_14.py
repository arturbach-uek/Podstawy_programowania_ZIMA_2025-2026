import queue

customer_q = queue.Queue()
ticket_number = 0

while True:
    print("\n--- Menu ---")
    print("1. Get a ticket")
    print("0. Quit")
    menu = input("Select an option: ").strip()

    if menu == '1':
        ticket_number += 1 
        customer_q.put(ticket_number)
        print(f"You received ticket #{ticket_number}. There are {customer_q.qsize() - 1} people ahead of you.")

    elif menu == '0':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 0.")
