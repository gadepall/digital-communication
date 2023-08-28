#CODE BY Muzaan Mohammed Faizel A P
#EE22BTECH11036
import numpy as np

# Array representing the number of members in the council
council=np.array(['M','M','M','M','F','F','F','F','F','F'])
#Simulating the array council in a random order
sim=np.random.choice(council,size=10,replace=False)
sim_len=10
# Calculate the total number of females using NumPy
women =np.array(sim=='F')
probability_women =np.sum(women)/sim_len
print("Probability that the selected student is not from A, B, or C:",np.sum(women),'/',sim_len,'=',probability_women)
print(f"simulation{sim}")
