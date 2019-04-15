import numpy as np
nummers = np.arange(0,13,1)
tabel = np.zeros((13,13))


for i in range(13):
    tabel[i]=nummers
    tabel[i]=np.multiply(tabel[i],i)
    
print(tabel)


