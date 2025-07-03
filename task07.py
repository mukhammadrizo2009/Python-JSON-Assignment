# ✅ 7. **Statistika chiqarish**

import json

with open("students.json","r+") as file:
    content = json.load(file)
    
    result = 0
    
    for age in content:
        result += int(age["age"])
        all_age = result / len(content)
        
    print(f"Foydalanuvchilarning o'rtacha yoshi {all_age} !")