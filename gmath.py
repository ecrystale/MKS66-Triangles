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
    a=polygons[i]
    b=polygons[i+1]
    c=polygons[i+2]
    one=[c[0]-a[0],c[1]-a[1],c[2]-a[2]]
    two=[b[0]-a[0],b[1]-a[1],b[2]-a[2]]
    cross=[one[1]*two[2]-one[2]*two[1],one[2]*two[0]-one[0]*two[2],one[0]*two[1]-one[1]*two[0]]
    return cross
