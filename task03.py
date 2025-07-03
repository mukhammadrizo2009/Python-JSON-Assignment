# ✅ 3. **Yangi element qo‘shish**

import json

with open("students.json","r+") as file:
    content = file.read()
    
    continueJson = json.loads(content)
    newUser = {}
    
    newUser["name"] = "Shahzoda"
    newUser["surname"] = "Nazarova"
    newUser["age"] = 22
    
    continueJson.append(newUser)
    print(continueJson)
with open("students.json","w" ) as file02:
   file02.write((json.dumps(continueJson, indent=4)))