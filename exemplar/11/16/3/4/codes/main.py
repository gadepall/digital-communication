import numpy as np
import matplotlib.pyplot as plt

# Sample size
simlen = 10000
X = {1, 2, 3, 4}
Y = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
Z = {1, 2}

# Generate X, Y, and Z without explicit loops
x = np.random.randint(1, 5, size=(1, simlen)) #X = {1, 2, 3, 4}
y = np.random.randint(1, 14, size=(1, simlen)) #Y = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
z = np.random.randint(1, 3, size=(1, simlen)) #Z = {1, 2}

# Find the frequency of each outcome
uniquex, countsx = np.unique(x, return_counts=True)
uniquey, countsy = np.unique(y, return_counts=True)
uniquez, countsz = np.unique(z, return_counts=True)

# Simulated probability
psimx = countsx / simlen
psimy = countsy / simlen
psimz = countsz / simlen

print(f"The probability that the card is an ace of spades = {psimx[1]*psimy[1]}")
print(f"The probability that the card is an ace = {psimy[1]}")
print(f"The probability that the card is black card = {psimz[1]}")

# Theoretical Probability
sample_space = 52
no_of_spades = 13
no_of_aces = 4
no_of_blackcards = 26
P_AOS = (no_of_aces/sample_space)*(no_of_spades/sample_space) #Prob of choosing ace of spade 
P_A = (no_of_aces/sample_space) #Prob of choosing ace  
P_bl = (no_of_blackcards/sample_space) #Prob of Black card
print(f"The probability that the card is an ace of spades = {P_AOS}")
print(f"The probability that the card is an ace = {P_A}")
print(f"The probability that the card is an ace = {P_bl}")

X_values = ['P_AOS', 'P_A', 'P_bl']
psim = [psimx[1]*psimy[1], psimy[1], psimz[1]]
theo_probs = [P_AOS, P_A, P_bl]

# Plotting
plt.stem(X_values, psim, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Simulation')
plt.stem(X_values, theo_probs, markerfmt='o', linefmt='C1-', use_line_collection=True, label='Analysis')
plt.xlabel('$X-axis$')
plt.ylabel('$Y-axis$')
plt.legend()
plt.grid()
plt.show()

