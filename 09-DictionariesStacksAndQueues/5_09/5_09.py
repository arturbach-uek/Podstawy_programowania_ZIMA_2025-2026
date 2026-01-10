import csv

province_dict = {}
with open("province.csv", "r", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        letter = row["Letter"]
        name = row["Name"]
        province_dict[letter] = name

vehicles = []
with open("vehicle.txt", "r") as file:
    vehicles = [line.strip() for line in file]

counter = {}
for vehicle in vehicles:
    first_letter = vehicle[0].upper()
    province_name = province_dict.get(first_letter, "Nieznane")

    counter[province_name] = counter.get(province_name, 0) + 1

for province, count in counter.items():
    print(f"{province}: {count}")