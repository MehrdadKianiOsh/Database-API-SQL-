import json

with open("data.pick", "r") as f:
    newd=json.load(f)
    
print(newd, type(newd))