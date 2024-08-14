# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 04:30:23 2024

@author: mattz
"""

def circle(r,h,N):
    circ_array = np.zeros((2,N))
    for x in range(N):
        y = -m.sqrt((r**2)-((x-h)**2))
        circ_array[0,x]=x
        circ_array[1,x]=y
    return circ_array[0],circ_array[1]