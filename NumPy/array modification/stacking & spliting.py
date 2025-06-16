"""
stacking-> combine array -> vertically, hozrizontally
vstack() : row wise
hstack() : column wise

"""



import numpy as np

arr1= np.array([1,2,3])

arr2= np.array([4,5,6])

print(np.vstack(((arr1,arr2)))) #vertically stacking

print(np.hstack(((arr1,arr2)))) #horizontally stacking


"""
spliting-> making multiple subset of entire array, or can equal part

np.split()
np.hsplit()
np.vsplit()
"""

arr3=np.array([1,34,3,36,3,2])

print(np.split(arr3,3))