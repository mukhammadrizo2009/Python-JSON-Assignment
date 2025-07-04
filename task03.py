# ✅ 3. **Yangi element qo‘shish**
from pprint import pprint
import json

with open("students.json","r+") as file:
    content = file.read()
    
    continueJson = json.loads(content)
    newUser = {}
    
    newUser["name"] = "Shahzoda"
    newUser["surname"] = "Nazarova"
    newUser["age"] = 22
    
    continueJson.append(newUser)
    pprint(continueJson)
with open("students.json","w" ) as file02:
   file02.write((json.dumps(continueJson, indent=4)))