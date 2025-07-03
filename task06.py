# ✅ 6. **JSONdan boshqa CSV formatga o‘tkazish**

import json
import csv

with open("students.json","r+") as file:
    content = json.load(file)
    
with open("students.csv" , "w+") as file02:
    fieldnames = ['name','surname','age']
    result = csv.DictWriter(file02 , fieldnames=fieldnames)
    result.writeheader()
    result.writerows(content)