import numpy as np
import matplotlib.pyplot as plt
import math as mt

def cdf_Y(k) :
  if np.all(k < 1):
   cdf=0
   return cdf/6
  if np.any(np.logical_or.reduce([k == i for i in range(1, 7)])):
   cdf=k/6
   return cdf/6
  elif np.all((k < 6) & (k > 1)):
   cdf=mt.floor(k)/6
   return cdf/6
  elif np.all(k>6):
   cdf=1
   return cdf/6

N = np.linspace(0, 36, 100000).astype(float)

i=0
cdf_xy=[]
while i<100000:
  cdf_xy.append(cdf_Y(N[i])+ cdf_Y(float(N[i])/2.0) + cdf_Y(N[i]/3) + cdf_Y(N[i]/4)+ cdf_Y(N[i]/5)+cdf_Y(N[i]/6))
  i=i+1


plt.xlabel('N')
plt.ylabel('cdf(Z)')
plt.plot(N,cdf_xy,'r')
plt.show()
