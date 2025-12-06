job_title = "Software Engineer"

with open("it_company.csv", "r") as file:
    print(sum((1 if job_title in line else 0) for line in file))
