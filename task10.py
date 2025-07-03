from pprint import pprint 
# ✅ 10. **Tartiblab chiqish**

import json

with open("students.json","r+") as file:
    content = json.load(file)
   
result = sorted(content, key = lambda x: x["age"])
pprint(result)