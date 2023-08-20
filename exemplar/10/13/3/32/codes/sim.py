import numpy as np

#Simulating numbers from 2 to 101 in a random order 
sim=np.random.choice(np.arange(2,102),size=100,replace=False)
sim_len=100

#probability of occurence of even number
even_num=np.array(sim%2==0)
pr_even=np.sum(even_num)/sim_len

#probability of occurence of square number 
sqrt=np.sqrt(sim)
sq_num=np.array(sqrt==np.floor(sqrt))
pr_sq=np.sum(sq_num)/sim_len

print(f"the probability of occurence of even number is {pr_even}")
print(f"the probability of occurence of square number is {pr_sq}")
print(f"simulation:{sim}")
