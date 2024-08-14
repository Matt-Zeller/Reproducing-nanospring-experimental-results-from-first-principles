# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:52:28 2024

@author: Matt E. Zeller
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:43:50 2024

@author: Matt E. Zeller
"""

from math import *

def refract(theta1, n1, n2):
    theta2 = asin((n1/n2)*sin(theta1))
    return theta2

#incident ray meets circle at polar angle alpha1
alpha1=pi/3

#ray refracts at angle theta2 measured from the line normal to glass surface
theta2=refract(pi/5, 1.0, 1.4)

#refracted ray meets interior side of circle at alpha2
alpha2=alpha1+pi-2*theta2

#ray reflects from alpha2 and meets opposite interior surface at alpha3
alpha3=alpha2+2*theta2

#reflected ray refracts back into air
theta3=refract(theta2, 1.4, 1.0)