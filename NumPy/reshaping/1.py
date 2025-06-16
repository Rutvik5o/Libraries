'''

reshape(rows,columns) specify new shape
if dimensions match

'''


import numpy as np

arr = np.array([1,2,3,4,5,6])

reshaped_arr = arr.reshape(2,3) #-> two column three row

print(reshaped_arr) #reshaping does not create copy , its return view


"""
flattering

"""
#for using :multidimension converting into 1 dimensional array
 
"""
.revel() -> view , its affect original to modify
.flatten-> copy, does not affect original

"""
print("Performing flattering")

arr = np.array([[1,2,3],[4,5,6]])

print(arr.ravel())
print(arr.flatten())