

d={"Geneva":{"Date":"12/02/2001", "temperature":23.4},
   "Lausanne":{"Date":"14/02/2001", "temperature":29.2},
   "Nyon":{"Date":"14/02/2001", "temperature":20.4}
   }

import pickle
with open("file.out", "wb") as fic:
    pickle.dump(d,fic)