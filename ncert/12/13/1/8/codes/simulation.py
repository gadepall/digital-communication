import numpy as np


simlen=10000000

#let roll[i] represent the rolling of a dice i.

roll1 = np.random.choice([1,2,3,4,5,6],size=simlen) #for 1st born child 
roll2 = np.random.choice([1,2,3,4,5,6],size=simlen) #for 1st born child 
roll3 = np.random.choice([1,2,3,4,5,6],size=simlen) #for 1st born child 

#count1 is outcomes of 6 on first roll .
#count 2 is outcomes with 6 and 5 respectively (event F).
#count 3 is outcomes event EF.
count_1 = (roll2 ==6).sum()
count_2 = ((roll1 ==5).sum())*count_1
count_3 = ((roll3 ==4).sum())*count_2

experimental=count_3/count_2
experimental=experimental/simlen

print("calculated = ",1/6)
print("experimental =",experimental)

