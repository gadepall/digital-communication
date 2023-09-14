import numpy as np

P_0 = 5/9 #probability of first draw being blue
P_1 = 4/9 #probability of first draw being red
P_00 = 1/2 #second ball being blue after first ball is blue
P_01 = 5/8 #second ball being blue after first ball is blue

Pfinal = (P_0)*(P_00)+(P_1)*(P_01)

print("The actual probability is: ", Pfinal)

#simulation
simlen = 10000

sim1 = np.random.choice([0,1],size = simlen, p=[P_0,1-P_0])

blue = np.array(sim1==0)
red = np.array(sim1==1)
p_blue = np.sum(blue)/simlen
p_red = np.sum(red)/simlen

sim2 = np.random.choice([0,1],size = simlen, p=[P_00,1-P_00])

bb = np.array(sim2==0)
p_bb = np.sum(bb)/(simlen-1)

sim3 = np.random.choice([0,1],size = simlen, p=[P_01,1-P_01])

br = np.array(sim3==0)
p_br = np.sum(br)/(simlen-1)

p_sim = (p_blue)*(p_bb)+(p_red)*(p_br)

print("The simulated probability is: ",p_sim)

