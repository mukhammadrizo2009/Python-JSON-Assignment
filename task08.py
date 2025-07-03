# ✅ 8. **Top Student (Maksimal yosh)**

import json

with open("students.json","r+") as file:
    content = json.load(file)
    
    #  olds = max(map(lambda x: x["age"], content))
    #  print(f"Eng katta yosh bu {olds!")
    olds = []
    
    for i in content:
        olds.append(int(i["age"]))
        
    max_age = max(olds)
    print(f"Eng katta yosh bu {max_age}!")
    
    