import numpy as np
import matplotlib.pyplot as plt

#sample size
simlen = 10000
#Possible outcomes
n = range(2,13)
# Generate X1 and X2
y1 = np.random.randint(1,7, size=(1, simlen))
y2 = np.random.randint(1,7, size=(1, simlen))
#Generate X
X = np.add(y1,y2)
#Find the frequency of each outcome
uniques, count = np.unique(y1, return_counts=True)
unique, counts = np.unique(X, return_counts=True)
#print the probability
print("The possible values in a die are:", uniques)
print("The probabilities of these sum values are:", count/simlen)
print("The probability of not getting 5:",1-(count[4]/simlen))

print("The possible sum values are:", unique)
print("The probabilities of these sum values are:", counts/simlen)
prob = counts/simlen

#Theoretical probability
n1 = range(2,7)
n2 = range(7,13)
panal1 = (n1 -np.ones((1,5)))
panal2 = (13*np.ones((1,6))-n2)
panal = np.concatenate((panal1,panal2),axis=None)/36

#Plotting
plt.stem(n,panal, linefmt='b-',use_line_collection=True)
plt.stem(n,prob, linefmt='g',use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.title("Theoretical vs Simulated")
plt.legend(['Theoretical', 'Simulated'])
#plt.show()
