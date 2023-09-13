import numpy as np
import random

simlen = 10000

#A and B represent two bags. 0 represents White ball, 1 represents Black ball
A = [0]*4 + [1]*5
B = [0]*9 + [1]*7

random.shuffle(A)
random.shuffle(B)
#Drawing a ball from the first bag
draw_A =  np.random.choice(A, size=simlen)
#Transferring the ball to the second bag and then drawing a ball from it.
draw_B = list(map( lambda k : np.random.choice(B + [draw_A[k]]), range(0,simlen)))

p_white = draw_B.count(0)/simlen
p_black = draw_B.count(1)/simlen
print("Probability through Simuation")
print("Probability of drawing white ball:" , p_white)

print("Theoretical Probability")
p_A = [4/9, 5/9]
p_th = (10/17) * p_A[0] + (9/17)* p_A[1]
print("Probability of drawing white ball:", p_th)
