employee_data = [
    ("Smith", "Lucy"),
    ("Jones", "Janet"),
    ("Lee", "Jerry"),
    ("Jackson", "Peter"),
    ("Johnson", "Rick"),
    ("Lewis", "Terry"),
    ("Clarke", "Robin")
]
formatted_employees = list(map(lambda e: f"{e[0].upper()}, {e[1]}", employee_data))
for employee in formatted_employees:
    print(employee)