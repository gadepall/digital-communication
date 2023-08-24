import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
  
#Radius and centre of the circumcircle
#of triangle ABC
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.block([[n1],[n2]])
  O=np.linalg.solve(N,p)
  r = np.linalg.norm(A -O)
  return O,r



def dir_vec(A,B):
  return B-A



#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
	
fig = plt.figure()
ax = fig.add_subplot(111)

A=np.array([0,0])
B=np.array([-1,0])
C=np.array([1,0])
D=np.array([0,1])

#Generating all lines
x_AB = line_gen(A,B)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D)

#Generating the circumcircle
[O,R] = ccircle(B,C,D)
x_circ= circ_gen(O,R)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],"blue")
plt.plot(x_CA[0,:],x_CA[1,:],"blue")
plt.plot(x_AD[0,:],x_AD[1,:],"blue")

#Plotting the circumcircle
plt.plot(x_circ[0,:],x_circ[1,:],"blue")

# Adding text without box on the plot.
ax.text(-0.45, 0.45, '1')
ax.text(0.45, 0.45, '2')
ax.text(0, -0.5, '3')





plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')


# image = mpimg.imread('tri_sss.png')
# plt.imshow(image)
plt.show()

