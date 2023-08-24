import numpy as np

#Let 1 denote non-defective bulbs and 0 denote defective bulbs 
p=6/24 #probability of occurence of zero

#Simulating 1s and 0s in random order with the given probability
sim_len=24
sim=np.random.choice([0,1],size=sim_len,p=[p,1-p])

#probability of selecting non-defective bulb
not_defec=np.array(sim==1)
p_nd=np.sum(not_defec)/sim_len 

#probability of selecting a defective bulb after a defective bulb is removed
p_new=5/24 #new probability of occurence of zero
defec=np.array(sim==0)
p_d=(np.sum(defec)-1)/(sim_len-1)

print(f"the probability of selecting non-defective bulb-obtained:{p_nd},actual:{1-p}")
print(f"the probability of selecting defective bulb after one defective bulb is removed-obtained:{p_d},actual:{p_new}")
print(f"simulation:{sim}")
