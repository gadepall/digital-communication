import numpy as np
import matplotlib.pyplot as plt

# np.set_printoptions(threshold=np.inf)

# Simulated Values - Using 10000 dice rolls
def dice_roll():
        dice = np.array(np.random.randint(1, 7, size=10000))         
        return dice

# Dice rolls generation - 2 sets for Apoorv and 1 set for Peehu                                                 
apoorv_1 = dice_roll()                                  
apoorv_2 = dice_roll()                                  
peehu = dice_roll()                                                                                             
pmf_apoorv_sim = [0]*36                                    
pmf_peehu_sim = [0]*36

# Calculating products and squares and counting them  
prod = np.multiply(apoorv_1, apoorv_2)
sq = np.multiply(peehu, peehu)

x_1, pmf_apoorv_sim = np.unique(prod, return_counts=True)
x_2, pmf_peehu_sim = np.unique(sq, return_counts=True)
x_1 = np.array(x_1)
x_2 = np.array(x_2)
pmf_apoorv_sim = np.array(pmf_apoorv_sim)/10000
pmf_peehu_sim = np.array(pmf_peehu_sim)/10000

# Theoretical Values
x = np.arange(1,37)
y = np.arange(1,7)
m1 = np.where(np.mod.outer(x, y) == 0, 1, 0)            # m1 is a matrix of order 36 x 6 which shows condition of k%i==0 being true or false
m2 = x[:,np.newaxis]/y[np.newaxis,:]                    
m2 = np.where(m2 <= 6, 1, 0)                            # m2 is a matrix of order 36 x 6 which shows condition of k/i<=6 being true or false
pmf_apoorv_theoretical = np.diagonal(m1@np.transpose(m2))/36
pmf_peehu_theoretical = np.isin(x, np.arange(1,7)**2)/6

# Cumulative Distribution Functions
cdf_apoorv_sim = np.cumsum(pmf_apoorv_sim)
cdf_peehu_sim = np.cumsum(pmf_peehu_sim)
cdf_apoorv_theoretical = np.cumsum(pmf_apoorv_theoretical)
cdf_peehu_theoretical = np.cumsum(pmf_peehu_theoretical)

# Plotting 
plt.stem(x, pmf_apoorv_theoretical, linefmt='b-', markerfmt='bo')
plt.stem(x_1, pmf_apoorv_sim, linefmt='none', markerfmt='go')
plt.xlabel('Product of Dice Rolls')
plt.ylabel('PMF')
plt.title("Apoorv's PMF")
plt.legend(['Theoretical', 'Simulated'])
plt.show()
 
plt.stem(x, cdf_apoorv_theoretical, linefmt='b-', markerfmt='bo')
plt.stem(x_1, cdf_apoorv_sim, linefmt='none', markerfmt='go')
plt.xlabel('Product of Dice Rolls')
plt.ylabel('CDF')
plt.title("Apoorv's CDF")
plt.legend(['Theoretical', 'Simulated'])
plt.show()
 
plt.stem(x, pmf_peehu_theoretical, linefmt='b-', markerfmt='bo')
plt.stem(x_2, pmf_peehu_sim, linefmt='none', markerfmt='go')
plt.xlabel('Square of Dice Rolls')
plt.ylabel('PMF')
plt.title("Peehu's PMF")
plt.legend(['Theoretical', 'Simulated'])
plt.show()
 
plt.stem(x, cdf_peehu_theoretical, linefmt='b-', markerfmt='bo')
plt.stem(x_2, cdf_peehu_sim, linefmt='none', markerfmt='go')
plt.xlabel('Square of Dice Rolls')
plt.ylabel('PMF')
plt.title("Peehu's CDF")
plt.legend(['Theoretical', 'Simulated'])
plt.show()