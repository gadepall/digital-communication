import numpy as np
import matplotlib.pyplot as plt


def pdf_fun(y):
    for x in range(-1,4):
        if(x==0):
            y.append(1/6)
        elif(x==1):
            y.append(1/3)
        elif(x==2):
            y.append(1/2)
        else:
            y.append(0)
    return y

x =np.arange(0,4)
pdf=[]
cdf = []                   
pdf = pdf_fun(pdf)
print(pdf)
sum=0
for i in pdf:
    sum = sum + i
    cdf.append(sum)
print(x)
print(cdf)
plt.step(x,cdf[1:],where = 'post',color='r')
x = np.arange(-1,4)
plt.stem(x,pdf)
plt.grid()          
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.legend(["cdf","pdf"])
plt.savefig('/home/divya/fwc-2/probability/12.13.4.9/codes/fig.pdf')
plt.savefig('/home/divya/fwc-2/probability/12.13.4.9/codes/fig.pdf')
plt.show() 
