# ✅ 4. **Foydalanuvchidan ma’lumot olib JSON ga yozish**
from pprint import pprint
import json

with open("students.json","r+") as file:
    
    content = file.read()
    
    continueJson = json.loads(content)
    
    newUser = {}
    
    newUser["name"] = input("Ismni kiriting!: ")
    newUser["surname"] = input("Familiyani kiriting!: ")
    newUser["age"] = int(input("Yoshni kiriting!: "))
    
    continueJson.append(newUser)
    
    pprint(continueJson)
    
with open("students.json","w" ) as file02:
   file02.write((json.dumps(continueJson, indent=4)))