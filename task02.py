# ✅ 2. **JSON faylni o‘qish**

import json

with open("students.json","r+") as file:
    content = file.read()
    
    continueJson = json.loads(content)
    
    for name in continueJson:
        
        print(f"{name['name']} - {name["age"]} yosh!")