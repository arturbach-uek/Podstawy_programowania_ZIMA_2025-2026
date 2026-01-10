import json

with open('reservations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    reservations = data["reservations"]

def number_of_rooms(reservations):
    return len(reservations)

def number_of_paid_reservations(reservations):
    return len([r for r in reservations if r['paid']])

def number_of_unpaid_reservations(reservations):
    return len([r for r in reservations if not r['paid']])

def total_value_paid(reservations):
    return sum(r['nights'] * r['price_per_night'] for r in reservations if r['paid'])

def total_value_unpaid(reservations):
    return sum(r['nights'] * r['price_per_night'] for r in reservations if not r['paid'])

print("Hotel Reservations Summary")
print("==========================")
print("Number of rooms:", number_of_rooms(reservations))
print("Paid reservations:", number_of_paid_reservations(reservations))
print("Unpaid reservations:", number_of_unpaid_reservations(reservations))
print("Total value of paid reservations: $", total_value_paid(reservations))
print("Total value of unpaid reservations: $", total_value_unpaid(reservations))
