# Given probabilities
Pr_A = 1/2
Pr_B = 1/3
Pr_A_and_B = 1/4

# Calculate conditional probabilities
Pr_A_or_B = Pr_A + Pr_B - Pr_A_and_B
Pr_A_given_B = Pr_A_and_B / Pr_B
Pr_B_given_A = Pr_A_and_B / Pr_A
Pr_A_complement_given_B = 1 - Pr_A_given_B
Pr_A_complement_given_B_complement = (1 - Pr_A_or_B)/(1 -Pr_B)

# Display results
print(" Pr(A|B) =", Pr_A_given_B)
print(" Pr(B|A) =", Pr_B_given_A)
print(" Pr(A' | B) =", Pr_A_complement_given_B)
print(" Pr(A' | B') =", Pr_A_complement_given_B_complement)

# Bernoulli random variable simulation
import random

# Define a function to simulate a Bernoulli random variable with a given probability p
def bernoulli_simulation(p):
    return 1 if random.random() < p else 0

simulated_A_given_B = [bernoulli_simulation(Pr_A_given_B) for _ in range(10000)]
simulated_Pr_A_given_B = sum(simulated_A_given_B) / len(simulated_A_given_B)
simulated_B_given_A = [bernoulli_simulation(Pr_B_given_A) for _ in range(10000)]
simulated_Pr_B_given_A = sum(simulated_B_given_A) / len(simulated_B_given_A)
simulated_A_complement_given_B = [bernoulli_simulation(Pr_A_complement_given_B) for _ in range(10000)]
simulated_Pr_A_complement_given_B = sum(simulated_A_complement_given_B) / len(simulated_A_complement_given_B)
simulated_A_complement_given_B_complement = [bernoulli_simulation(Pr_A_complement_given_B_complement) for _ in range(10000)]
simulated_Pr_A_complement_given_B_complement = sum(simulated_A_complement_given_B_complement) / len(simulated_A_complement_given_B_complement)

print("Simulated Pr(A|B) =", simulated_Pr_A_given_B)
print("Simulated Pr(B|A) =", simulated_Pr_B_given_A)
print("Simulated Pr(A' | B) =", simulated_Pr_A_complement_given_B)
print("Simulated Pr(A' | B') =", simulated_Pr_A_complement_given_B_complement)
