

import pickle
with open("file.out", "rb") as fic:
    d=pickle.load(fic)
    
print(d, type(d))