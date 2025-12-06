import csv
print("GRAPHIC DESIGNERS\n=================")
with open('it_company.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")