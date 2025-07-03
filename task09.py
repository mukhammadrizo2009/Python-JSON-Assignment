# ✅ 9. **Studentlar sonini hisoblash**

import json

with open("students.json","r+") as file:
    content = json.load(file)
    
    result = len(content)
    
    print(f"Talabalar soni {result}-ta!")