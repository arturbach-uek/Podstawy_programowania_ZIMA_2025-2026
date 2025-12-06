with open('it_company.csv') as f, open('software_engineer.txt', 'w') as out:
    [out.write(l) for l in f if 'Software Engineer' in l]
