import numpy as np

#Simulating numbers from 1 to 100 in a random order 
sim=np.random.choice(np.arange(1,101),size=100,replace=False)
sim_len=100

#probability of occurence of even number
even_num=np.array(sim%2==0)
pr_even=np.sum(even_num)/sim_len

#probability of occurence of odd number 
odd_num=np.array(sim%2!=0)
pr_odd=np.sum(odd_num)/sim_len

print(f"the probability of occurence of even number is {pr_even}")
print(f"the probability of occurence of odd number is {pr_odd}")
print(f"simulation:{sim}")
