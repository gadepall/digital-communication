import numpy as np
from math import comb
#simulation length
s = 10000
#probability of winning 
ps = 10/10000
#probability of losing
qs = 1-ps
#number of tickets
n= int(input())
count = 0
for i in range(s):
    trail = np.random.choice([0,1],n,p=[qs,ps])
    if(np.count_nonzero(trail)>0):
        count +=1
prob = count/s
#total probability of not wining a prize
print(1-prob)


#theoritical
x = s-10
if(n==0):
    prob = 0
if(n<=x):
    prob = comb(x,n)/comb(s,n)
if((n>x) and (n<=s)):
    prob = 1
print(prob)
