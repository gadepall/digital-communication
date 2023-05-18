import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import uniform
simlen=10000000
n =  2  
p = 0.5

experiment=np.zeros(4)
actual=np.zeros(4)
data_binom = binom.rvs(n,p,size=simlen)  #Simulating the event of jumping 10 hurdles
heads,simulation_coin = np.unique(data_binom , return_counts= True)
simulation_coin = simulation_coin/simlen


dice_outcomes = uniform.rvs(loc=1, scale=6, size=simlen).astype(int)
dice_out,simulation_dice = np.unique(dice_outcomes , return_counts= True)
simulation_dice = simulation_dice/simlen


actual[0] = binom.pmf(2,2,0.5)
actual[1] = binom.pmf(0,2,0.5)
actual[2] = binom.pmf(1,2,0.5)
actual[3] = 1/2

experiment[0] = simulation_coin[2]
experiment[1] = simulation_coin[0]
experiment[2] = simulation_coin[1]
experiment[3] = simulation_dice[0] + simulation_dice[2] + simulation_dice[4]

print("For X=2 the Simulation Probability is " + "{0:.7f}".format(experiment[0]) + " and the Theoritical Value is " + "{0:.7f}".format(actual[0]))
print("For X=0 the Simulation Probability is " + "{0:.7f}".format(experiment[1]) + " and the Theoritical Value is " + "{0:.7f}".format(actual[1]))
print("For X=1 the Simulation Probability is " + "{0:.7f}".format(experiment[2]) + " and the Theoritical Value is " + "{0:.7f}".format(actual[2]))
print("For Y=Odd the Simulation Probability is " + "{0:.7f}".format(experiment[3]) + " and the Theoritical Value is " + "{0:.7f}".format(actual[3]))