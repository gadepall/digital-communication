import numpy as np
import matplotlib.pyplot as plt
import random as rand

# np.set_printoptions(threshold=np.inf)

# Using dice rolls
n =10000
choices = [0,1,6]
weights = [0.167,0.5,0.333]
def dice_roll():
	dice = np.array(rand.choices(choices, weights,k=n))         
	return dice
die_X = dice_roll()                                  
die_Y = dice_roll() 
#print(die_X)                        
sum_die = die_X + die_Y
print(sum_die,"\n")
values, sim_count = np.unique(sum_die, return_counts=True)
#x_1 = np.array(x_1)
pmf_sum_sim = np.array(sim_count)/n
print("value =",values,"\n","probability =",pmf_sum_sim)
thry_count = [n/36,n/6,n/4,n/9,n/3,n/9]

# Create a stem plot
plt.stem(values, sim_count, basefmt=' ', linefmt='-b', markerfmt='ob', use_line_collection=True)
plt.stem(values, thry_count, linefmt='none', markerfmt='go')

# Customize the plot (optional)
plt.title('PMF of sum')
plt.xlabel('Sum')
plt.ylabel('PMF')

# Show the plot
plt.legend(['Simulated', 'Theoretical'])
plt.savefig('/home/lancelot/Latex/EE2102/10.13.3.39/figs/plot.png')
plt.show()









