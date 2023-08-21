import numpy as np

m=10000
count1=0
count2=0
for i in range(m):
    h10=np.random.randint(1,50)
    count1+=1
    if h10==30:
        count2+=1
prob1=count2/count1
print(prob1)


count3=0
count4=0
for i in range(m):
    club=np.random.randint(1,50)
    count3+=1
    if club in range(5,16):
        count4+=1
prob2=count4/count3
print(prob2)
