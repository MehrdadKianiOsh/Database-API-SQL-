
d={"name":"Jean", "values":[56,78,89], "flag": True}
print(d)

for e in d:
    print(e, "=>", d[e])
    
import json

with open("data.pick", "w") as f:
    json.dump(d, f)