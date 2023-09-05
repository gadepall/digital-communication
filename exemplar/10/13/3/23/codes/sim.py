import numpy as np
import matplotlib.pyplot as plt

#sample size
simlen = 10000
#Possible outcomes
n = range(2,10)
# Generate X1 and X2
y1 = np.random.randint(1,7, size=(1, simlen))
y2 = np.random.randint(1,4, size=(1, simlen))
#Generate X
X = np.add(y1,y2)
#Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
#print the probability
print("the possible sum values are:", unique)
print("the probabiliteis of these sum values are:", counts/simlen)
prob = counts/simlen

#Theoretical probability
n1 = range(2,5)
n2 = range(5,8)
n3 = range(8,10)
panal1 = (n1 -np.ones((1,3)))
panal2 = (3*np.ones((1,3))+n2-n2)
panal3 = (10*np.ones((1,2))-n3)
panal = np.concatenate((panal1,panal2,panal3),axis=None)/18

#Plotting
plt.stem(n,panal, linefmt='b-',use_line_collection=True)
plt.stem(n,prob, linefmt='g',use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.title("Theoretical vs Simulated")
plt.legend(['Theoretical', 'Simulated'])
plt.savefig("figs/pmf.png",bbox_inches='tight')
