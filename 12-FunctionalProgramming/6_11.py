test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}
]

selected_students = list(filter(lambda s: 50 <= s["result"] <= 70, test_results))

for student in selected_students:
    print(f"{student['name']}: {student['result']}")
