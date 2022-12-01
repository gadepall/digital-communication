#Code released under GNU/GPL
#Potukuchi Siddhartha
#June 19,2020
#Revised by 
#GVV Sharma
#June 19, 2020

#Generating points uniformly within a rectangle
#Finding the probability of those points  lying inside a circle
from itertools import product
import matplotlib.pyplot as plt
import math 
import numpy as np

#if using termux
import subprocess
import shlex
#end if

#Rectangle 
leng = 3 #length
breadth = 2 #breadth
rect_area = leng*breadth #area

# Circle 
rad = 0.5 #radius

circ_area = np.pi*rad**2 #Area

#Sample size, points randomly generated inside the rectangle
sample=int(1e4)

def preprocess(p, x, y, n): 
    for i in range(n): 
        p[i] = x[i] * x[i] + y[i] * y[i]
    p.sort() 

#Checking for points inside the circle
def query(p, n, rad): 
  
    start = 0
    end = n - 1
    while ((end - start) > 1): 
        mid = (start + end) // 2
        tp = math.sqrt(p[mid]) 
  
        if (tp > (rad * 1.0)): 
            end = mid - 1
        else: 
            start = mid 
  
    tp1 = math.sqrt(p[start]) 
    tp2 = math.sqrt(p[end]) 
  
    if (tp1 > (rad * 1.0)): 
        return 0
    elif (tp2 <= (rad * 1.0)): 
        return end + 1
    else: 
        return start + 1
  
if __name__ == "__main__": 
    #Generating points uniformly within a rectangle	centred at the origin
    x = np.random.uniform(low=-leng/2, high=leng/2, size=sample)
    y = np.random.uniform(low=-breadth/2, high=breadth/2, size=sample)
   #Generating a circle centred at the origin with radius 0.5
    circle = plt.Circle((0, 0), 0.5, color='red',fill=False)
    n = len(x) 
    p = [0] * n 
    preprocess(p, x, y, n) 

#Probability of points lying inside the circle
    event_size=query(p, n, rad)
    prob=event_size/sample

#Simulation vs analysis
    print(prob, circ_area/rect_area)
    fig, ax = plt.subplots()
    ax.add_artist(circle)
    ax.axis('equal')
    plt.scatter(x,y,rad)
#    plt.show()

    #if using termux
    plt.savefig('./figs/stochastic/rectangle.pdf')
    plt.savefig('./figs/stochastic/rectangle.png')
    subprocess.run(shlex.split("termux-open ./figs/stochastic/rectangle.pdf"))
    #else
    #plt.show()






