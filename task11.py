# 🔥 11. **Fayl mavjud bo‘lmasa yaratish**

import os
import json

file_name = 'data.json'
if not os.path.exists(file_name):
    with open("file_name","w") as jsonfile:
        json.dumps([], jsonfile)

