import numpy as np
numb=np.array(np.random.randint(0,4,size=10000))
r=np.sum(numb==2)
c1=np.sum(numb==1)
c2=np.sum(numb==3)
print((c1+c2)/(10000-r))

