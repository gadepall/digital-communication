import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
turns = int(10000)
possible=[1,2,3,4,5,6]
prob = [1/6,1/6,1/6,1/6,1/6,1/6]
random_A = np.random.choice(possible,turns,p=prob)
random_B = np.random.choice(possible,turns,p=prob)
W = random_A + random_B
sumlt6=[]
for i in range(turns):
	if(W[i] < 6):
		sumlt6.append(W[i])
sumeq3=[]
for i in range(len(sumlt6)):
	if(sumlt6[i] == 3):
		sumeq3.append(sumlt6[i])
# probability of getting 3 as sum when given sum is lessss than 6
probability = len(sumeq3)/len(sumlt6)
print(probability)
plt.figure(figsize=(8, 6))
plt.stem(np.unique(W), np.bincount(W)[np.unique(W)] / turns, markerfmt='ro', basefmt=' ', linefmt='k-')
plt.title('Stem Plot of W = X + Y ')
plt.xlabel('W (Sum of X and Y)')
plt.ylabel('Probability')
plt.xticks(np.arange(2, 13))
plt.grid(True)
plt.savefig('/home/sameer/12.13.3.82/figs/Z.png')
