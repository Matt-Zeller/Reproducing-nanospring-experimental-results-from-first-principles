from math import *
import matplotlib.pyplot as plt
import numpy as np

#function to be plotted
def hemi1(x,r,h):
    f=sqrt((r**2)-((x-h)**2))
    return f

# def hemi2(x,r,h):
#     f=-sqrt((r**2)-((x-h)**2))
#     return f

def plotter(f,a,b,h):
#takes function of variable 'x',lower bound and upper bound a,b, step h
#then plots it

    #first point function f is eval'd at
    x=a
    #array size
    arSize=int(np.abs((a-b)/h))
    #init array of function values
    F=np.zeros((arSize,1))
    #fill array of func values at all x in a,b
    for i in range(arSize):
        F[i,0]=f(x,1.,0.)
        x=x+h
    #make x axis array, plot f(x)
    X=np.arange(a,b,h)
    
##############################

    print(F)
    print(X)
    

##############################
    
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot()
    ax.set_xlim(-1.,1.)
    ax.set_ylim(-1.,1.)
    ax.plot(X,F)
    F=np.negative(F)
    ax.plot(X,F)

#type function of x here... right now it is set to plot 
#for x=[0,3] at increments of 0.01


plotter(hemi1,-1.,1.,0.01)
# plotter(hemi2,-1.,1.,0.01)