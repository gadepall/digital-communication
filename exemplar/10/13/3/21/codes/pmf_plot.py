import numpy as np
import matplotlib.pyplot as plt
import math as mt
def F_y(y):
    if y < 1:
        return 0
    elif y>=1 and y<=6:
        return mt.floor(y)/6
    else:
        return 1;
def func(n):
    sum=0
    for j in range(mt.floor(n/6)+1,7):
        sum=sum+F_y(n/j)
    return sum
        
pmf_1=[]
for i in range(1,37):
    pmf_1.append((mt.floor(i/6)+func(i))/6-(mt.floor((i-1)/6)+func(i-1))/6)

#the pmf list is made
#make it numpy array and proceed
pmf_2=np.array(pmf_1)
plt.stem(np.arange(1,37),pmf_2)
plt.title('pmf_Z(Z=n)')
plt.xlabel('n')
plt.ylabel('pmf')
plt.show()
