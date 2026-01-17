class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        first_letter = self.name[0]
        if self.age >= 18:
            return f"{self.surname.upper()}{first_letter.upper()}{self.seniority}"
        else:
            return f"{self.surname.lower()}{first_letter.lower()}{self.seniority}"


employee1 = C("Anna", "May", 17, 7)
employee2 = C("George", "Brown", 21, 4)

print(employee1)
print(employee2)