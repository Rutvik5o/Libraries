"""
np.insert(array,index,value,asix=None)
array- original array
index -
value
axis = 
axis = 0 means its data rows wise, for 1 -> column wise
"""
#Insertion-> Adding element in specific position
#Append-> adding element in the last position


import numpy as np


arr = np.array([102,30,4,35,52,3])

new_arr = np.insert(arr,2,100,axis=0) #bydefault -> axis = 0 means row wise
print(new_arr)


#insertion in 2d array
print("2D array")

arr_2d = np.array([[1,2],[3,4]])
#insert a new at index 1
print(arr_2d)

new_arr2 = np.insert(arr_2d,1,[5,7],axis=None) #for 2d array inserting axis paramter is compulsary
#if pass None: -> insertion in flattern version
print(new_arr2)


#append: adding at the end

print("Performing append operations")

arr2=np.array([24,35,22])
new_arr= np.append(arr,[40,50,59])

print(new_arr)

#concating of two arrays: adding two array

"""
np.concatenate((array1,array2),axis = 0)

axis 0 > vertical stacking
axis 1 > horizontal stacking
"""


arr3=np.array([1,2,3])
arr4=np.array([4,5,6])

new_arr = np.concatenate((arr3,arr4))

print(new_arr)

#removing elements from array

"""
np.delete(array,index,axis=None)
axis None -> flatten array -> 1d array
"""
print("Perforimg Deleting Operations")
new_a=np.delete(arr,2)
print(new_a)

print("Perfoming on 2d array")

arr_3 = np.array([[1,2,3],[4,5,6]])

new_a4 = np.delete(arr_3,0,axis=0)
#0-> it will delete 1,2,3
#axis 0 -> delete row


#numpy doesn't support like adding, update,delete on existin array,it 
#always return new array