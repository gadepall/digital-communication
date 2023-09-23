import numpy as np
#let X and Y be the two bernoulli random variables where 

pX = 1/2 #basically its x it can be changed 
pY = 1/6 #basically its y it can be changed 

pXY = pX * pY #Given that they are independent
pXunionY = pX + pY 

if (pXY==0):
	print("X and Y are mutually exclusive")
else:
	print("X and Y are not mutually exclusive")
if (pXunionY!=1):
	print("It is not necessary that probability of X + Y is 1")




