import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

simlen = 100000

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


ar1 = (Z == 4)
ar2 = (X!=Y)
# for Question,
ptheo = (2/36)/(5/6)
pxy = np.count_nonzero(ar2)/simlen

psim =  (np.count_nonzero(ar1&ar2)/simlen)/(pxy)

print("Theoretical value of probability of getting sum  =4 given X != Y is: " + str(ptheo))
print("Actual value of probability of getting sum  =4 given X != Y  is: " + str(psim))



#plotting


possible1 = possible.reshape(1,6)
eq9X = np.repeat(possible1,3, axis = 1)

pos = np.array([[1,2,3]])
eq9Y = np.repeat(pos , 6 , axis = 0)

validX = np.repeat(possible,6).reshape(6,6)
validY = np.repeat(possible1,6 ,axis = 0)


#plot
figure,axes = plt.subplots(1)
axes.set_title("X+Y = 8 | Y < 4")
axes.set(xlabel = 'X' , ylabel = 'Y')
axes.set_xlim(-0.2 , 7)
axes.set_ylim(-0.2 , 7)
axes.add_patch(Rectangle((0.6, 0.6), 5.8,5.8 , edgecolor = '#000000',facecolor = '#00000020' ,fill =True , label = 'Valid region for die roll results'))

axes.scatter(validX,validY ,c = 'black' ,label = 'Integral points (X,Y)')

axes.plot(np.arange(1,4) , 4 - np.arange(1, 4) , 'ro-' , label = 'X + Y = 4 ')
axes.plot(np.arange(1,7),np.arange(1,7),'bo-' , label ='X != Y')

axes.legend()

plt.show()



