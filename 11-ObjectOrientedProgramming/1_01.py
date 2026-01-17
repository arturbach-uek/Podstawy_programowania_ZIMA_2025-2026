class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.weight = 75

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student2.name = "Olivia"
    student2.age = 21

    student3 = Student()
    student1.weight = 100
    student2.weight = 68
    student3.name = "Adamek"
    student3.age = 22
    student3.weight = 190

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, weigth: {student1.weight}')
    print(f'{student2.name}, {student2.age} years old, weigth: {student2.weight}')
    print(f'{student3.name}, {student3.age} years old, weigth: {student3.weight}')

if __name__ == "__main__":
    main()