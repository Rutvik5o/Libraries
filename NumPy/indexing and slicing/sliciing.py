'''
array[index] #1d array
array[row,column] #2d

'''

import numpy as np

arr = np.array([1,2,3,4,54,30])
print("performing indexing")
print(arr[0])
print(arr[2])
print(arr[-1])


print("performing slicing")
'''
array[start:stop:step]  exclude

arr[start:end], start to end -1

nvagative step, -1 reverse
'''

print(arr[1:5]) #index 1 to 4
print(arr[:4]) #index 0 to 3
print(arr[::2]) #every second element
print(arr[::-1]) #reverse

