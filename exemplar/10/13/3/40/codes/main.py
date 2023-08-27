import numpy as np 
 
P_1=7/8 #probability of picking a good mobile 
 
simlen=1000 
sim1=np.random.choice([0,1],size=simlen,p=[P_1,1-P_1]) 
 
good=np.array(sim1==0) 
p_good=np.sum(good)/simlen 
 
 
print('the simulated probability: ',p_good,"vs, the actual probability :", P_1) 
 
P_2=1/16 #probability that the mobile has major defects 
 
sim2=np.random.choice([0,1],size=simlen,p=[P_2,1-P_2]) 
 
traderbuy=np.array(sim2==1) 
p_trader=np.sum(traderbuy)/simlen 
 
print('the simulated probability: ',p_trader,'vs, the actual probability :',1- P_2)
