# ✅ 1. **Ma’lumotni JSON faylga yozish**

import json

students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]

result = json.dumps(students, indent=4)


with open('students.json','w') as file02:
    file02.write(result)