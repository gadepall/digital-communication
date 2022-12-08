#!/usr/bin/env python

#This program compares the simulation and anlalytical BER in Nakagami-m
#fading for noninteger m

#The following command brings everything from sage to python
import sys
#from sage.all import *

#Importing numy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import scipy.stats as sp
#from scipy.integrate import quad
#import scipy.integrate as spint
import matplotlib.pyplot as plt
import subprocess



x = np.linspace(0,4,20)#points on the x axis
simlen = 1e5 #number of samples
err = [] #declaring probability list


for i in range(0,20):
	n = np.random.normal(0,1,simlen)
	err_ind = np.nonzero(n > x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x.T,err)#plotting the Q-function
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$Q(x)$')
plt.show() #opening the plot window
