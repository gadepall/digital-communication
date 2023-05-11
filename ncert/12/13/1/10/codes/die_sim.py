import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

simlen = 10000

pX = pY = np.ones(6)
pX = pY = pX/6
pZ = np.array([ 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36 ])
possible = np.arange(1,7)
possible_Z = np.arange(2, 13)
X= np.random.choice(possible, simlen, p=pX)
Y= np.random.choice(possible, simlen, p=pY)
cdfY = np.cumsum(pY)
Z = X + Y

simX, simpX = np.unique(X , return_counts= True)
simZ, simpZ = np.unique(Z , return_counts= True)
simY, simpY = np.unique(Y , return_counts= True)

simpX = simpX/simlen
simpY = simpY/simlen
simpZ = simpZ/simlen

simp_cdfY = np.cumsum(simpY)
# for Question1,
p1theo = cdfY[5] - cdfY[3]
p1sim = simp_cdfY[5] - simp_cdfY[3]

print("Theoretical value of probability of getting sum > 9 given X>5 is: " + str(p1theo))
print("Actual value of probability of getting sum > 9 given X>5 is: " + str(p1sim))


print("----------")
#for Question2,
p2theo = (pX[2]*pY[4] + pX[1]*pY[5])/cdfY[3]
p2sim = (simpX[2]*simpY[4] + simpX[1]*simpY[5])/simp_cdfY[3]

print("Theoretical value of probability of getting sum = 8 given Y < 4 is: " + str(p2theo))
print("Actual value of probability of getting sum = 8 given Y < 4 is: " + str(p2sim))

#plotting

fig,axes = plt.subplots(2,figsize = (12,20))

possible1 = possible.reshape(1,6)
eq9X = np.repeat(possible1,3, axis = 1)

pos = np.array([[1,2,3]])
eq9Y = np.repeat(pos , 6 , axis = 0)
#plot-1
axes[0].set_title("Plot for verifying current problem")
axes.flat[0].set(xlabel = 'Questions' , ylabel = 'Answers')
axes[0].stem([1, 2] , [p1theo,p2theo] , label = 'Actual', markerfmt = 'ro' , basefmt = 'g-' ,linefmt = 'b')
axes[0].set_xticks([1,2])
axes[0].plot([1, 2] , [p1sim, p2sim], 'yo',label = 'Theoretical')
axes[0].legend()

validX = np.repeat(possible,6).reshape(6,6)
validY = np.repeat(possible1,6 ,axis = 0)
print(validX)
print(validY)
#plot-2
axes[1].set_title("X+Y = 8 | Y < 4")
axes.flat[1].set(xlabel = 'X' , ylabel = 'Y')
axes[1].set_xlim(-0.2 , 7)
axes[1].set_ylim(-0.2 , 7)
axes[1].add_patch(Rectangle((0.6, 0.6), 5.8,5.8 , edgecolor = '#000000',facecolor = '#00000020' ,fill =True , label = 'Valid region for die roll results'))
axes[1].add_patch(Rectangle((0.8, 0.8), 5.4,2.4 , edgecolor = 'blue',facecolor = '#0000f020' ,fill =True ,label = 'Y<4'))
axes[1].scatter(validX,validY ,c = 'black' ,label = 'Integral points (X,Y)')
axes[1].scatter(eq9X,eq9Y , label = 'Integral points where Y<4')

axes[1].plot(possible[1:],8-possible[1:],'yo-' , label ='X+Y = 8')
axes[1].legend()

plt.show()



