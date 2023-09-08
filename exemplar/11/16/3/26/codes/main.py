import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Sample size
simlen = 10000
k_values = np.arange(0,2)
# Possible outcomes
string = "PROBABILITY"

# Generate X1 and X2 without explicit loops
y = np.random.choice(list(string), size=(simlen))

# Find the frequency of each outcome
unique, counts = np.unique(y, return_counts=True)
print(unique)
# Simulated probability
psim = counts / simlen
probs = []
probs.append(1-(psim[0]+psim[2]+psim[4])) #Addition of probs except vowels 
probs.append(psim[0]+psim[2]+psim[4]) #Addition of probs of vowels 

#Theoretical Probability
p = 4/11 
n = 1    
#We can use binom to create binomial distribution
rv = binom(n, p)

#Make the list combinations with rv.pmf function
combinations = rv.pmf(k_values)

X_axis = ["Prob of pulling a non-vowel","Prob of pulling a vowel"]

# Plotting
plt.stem(X_axis, probs, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Simulation')
plt.stem(X_axis, combinations, markerfmt='o', linefmt='C1-', use_line_collection=True, label='Analysis')
plt.xlabel('$k$')  # Use 'k' instead of 'n'
plt.ylabel('$p_{X}(k)$')  # Use 'k' instead of 'n'
plt.legend()
plt.grid()

# Save or display the plot
plt.savefig('/home/karthikeya/Desktop/Probability/New_assignment4/figs/figure1.png')
plt.show()




#Theoretical Probability
#string_ = list(string)
#sample_space = len(string_)

#unique2, counts2 = np.unique(string_, return_counts=True)

#prob = list(counts2 / sample_space)
#print(unique2)
#print(counts2)
#probability_dict = dict(zip(unique2, prob))

#print(f"Therefore the probability of choosing a vowel is {probability_dict['A'] + probability_dict['I'] + probability_dict['O']}")
