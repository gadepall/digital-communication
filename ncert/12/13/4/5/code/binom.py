import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
n = 2
p1 = 0.333
p2 = 0.166
k = np.arange(0, n+1)
binom_1 = binom.pmf(k,n,p1)
binom_2 = binom.pmf(k,n,p2)

simlen = 10000      # Number of trials
dice_out = np.arange(1,6+1)     # Dice throw possible outcomes
dice_exp = np.random.choice(dice_out, (simlen, n)) # Uniformly choose from 6 dice outcomes for n throws repeated 'simlen' trials

# For every trial, count number of dice greater than 4 and store in dice_cnt
dice_cnt = np.zeros(simlen)
for i in range(0, n):
    # dice_exp[:,i]>4 return array of True, False values according to comparison
    # .astype(int) converts True, False to 0,1
    # For every throw, if comparison is True, adds 1 for that trial
    dice_cnt += (dice_exp[:,i]>4).astype(int)  
values, counts = np.unique(dice_cnt, return_counts=True)
binom_1_sim = counts/simlen

# For every trial, count number of dice equal to 6 and store in dice_cnt
dice_cnt = np.zeros(simlen)
for i in range(0, n):
    dice_cnt += (dice_exp[:,i]==6).astype(int)
values, counts = np.unique(dice_cnt, return_counts=True)
binom_2_sim = counts/simlen

print(binom_1, binom_1_sim)
print(binom_2, binom_2_sim)

plt.stem(k,binom_1,use_line_collection=True)
plt.plot(k,binom_1_sim, 'o', markerfacecolor="None", markeredgecolor="orange", markeredgewidth=2)
plt.legend(["Simulation", "Theory"])
plt.grid()
plt.xlabel('$k$')
plt.ylabel('$p_X(k)$')
plt.savefig('/home/user/Probability/12.13.4.5/code/bfig1.pdf')
plt.show()
plt.close()

plt.stem(k,binom_2,use_line_collection=True)
plt.plot(k,binom_2_sim, 'o', markerfacecolor="None", markeredgecolor="orange", markeredgewidth=2)
plt.grid()
plt.xlabel('$k$')
plt.ylabel('$p_X(k)$')
plt.legend(["Simulation", "Theory"])
plt.savefig('/home/user/Probability/12.13.4.5/code/bfig2.pdf')
plt.show()
