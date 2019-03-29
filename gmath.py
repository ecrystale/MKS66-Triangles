import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    x=vector[0]
    y=vector[1]
    z=vector[2]
    unit=(x**2+y**2+z**2)**0.5
    vector=[x/unit,y/unit,z/unit]

#Return the dot porduct of a . b
def dot_product(a, b):
    prod=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    return prod
    
#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    return None
