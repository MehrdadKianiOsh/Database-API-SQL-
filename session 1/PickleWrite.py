
d={"name":"Jean", "values":[56,78,89], "flag": True}
print(d)

for e in d:
    print(e, "=>", d[e])
    
import pickle

with open("data.pick", "wb") as f:
    pickle.dump(d, f)