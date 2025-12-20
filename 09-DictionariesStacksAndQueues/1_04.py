person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobbys": [
       "swimming",
       "excursions"
    ],
   "married": True,
   "phone": {
       "landline": "123444321",
       "mobile": "777888999"
    }
}
print(person["name"])
for hobby in person["hobbys"]: print(hobby)
for key, value in person.items():
    print(f"{key}: {value}")
person["surname"] = "Nowak"
person["married"] = False
person["gender"] = "male"
person["hobbys"].append("bicycle")
person["phone"]["work_phone"] = "313131444"
for key, value in person.items():
    print(f"{key}: {value}")
