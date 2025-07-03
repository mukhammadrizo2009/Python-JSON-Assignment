# ✅ 5. **Yosh bo‘yicha filtr qilish**

import json

with open("students.json","r+") as file:
    content = json.load(file)
    
    for age in content:
        old = age["age"]
        if old > 20:
            print(f"{age["name"]} {old} - yoshda!")