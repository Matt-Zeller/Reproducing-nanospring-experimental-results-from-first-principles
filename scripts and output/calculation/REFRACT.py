# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 02:54:48 2024

@author: Matt E. Zeller
"""
from math import *

def refract(angle1, n1, n2):
    
    angle2 = m.asin((n1/n2)*m.sin(angle1))
    
    return angle2

for i in range(8):
    print('angle2 =',refract(i*pi/,1,1.4))
    print('')