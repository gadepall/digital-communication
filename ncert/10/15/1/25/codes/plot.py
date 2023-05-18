import matplotlib.pyplot as plt
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

plt.figure(figsize=(16,10))
plt.xlabel('X')
plt.ylabel('Probabilities')
plt.ylim(0 , 1)
plt.xlim(-1, 4)
print(experiment[0])
plt.stem(np.arange(0,3) , [experiment[0],experiment[1],experiment[2]] , markerfmt = 'ro' , linefmt = 'b' , basefmt = 'g--' , label = 'Simulation')
plt.plot(np.arange(0,3) , [actual[0],actual[1],actual[2]] , 'yo' , label = 'Theoretical')
plt.legend()
plt.show()


plt.figure(figsize=(16,10))
plt.xlabel('Y')
plt.ylabel('Probabilities')
plt.ylim(0.15 , 0.17)
plt.xlim(-1, 7)
plt.stem([1,3,5] , [simulation_dice[0],simulation_dice[1],simulation_dice[2]] , markerfmt = 'ro' , linefmt = 'b' , basefmt = 'g--' , label = 'Simulation')
plt.plot([1,3,5] , [1/6,1/6,1/6] , 'yo' , label = 'Theoretical')
plt.legend()
plt.show()