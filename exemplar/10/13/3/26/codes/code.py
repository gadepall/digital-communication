import numpy as np
import matplotlib.pyplot as plt

#sample size
simlen = 10000
#Possible outcomes
n = range(-5,6)
# Generate X1 and X2
y1 = np.random.randint(1,7, size=(1, simlen))
y2 = np.random.randint(1,7, size=(1, simlen))
#Generate X
X = np.subtract(y1,y2)
#Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
#print the probability
print("the possible difference values are:", unique)
print("the probabiliteis of these difference values are:", counts/simlen)
prob = counts/simlen

#Theoretical probability
pArray = [1/36, 1/18, 1/12, 1/9, 5/36, 1/6, 5/36, 1/9, 1/12, 1/18, 1/36]

#Plotting
plt.stem(n,pArray, markerfmt='bo', linefmt='b-',use_line_collection=True)
plt.stem(n,prob, markerfmt='ro', linefmt='g',use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$p_{Z}(n)$')
plt.title("Theoretical vs Simulated")
plt.legend(['Theoretical', 'Simulated'])
plt.savefig("../figs/z.png",bbox_inches='tight')
