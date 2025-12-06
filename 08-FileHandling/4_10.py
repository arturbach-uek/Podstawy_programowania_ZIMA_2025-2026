import csv
with open('clothing.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if float(row['Price']) < 60 and int(row['Stock']) < 40:
            print(row['Product'])
