#when there is multiple data
#for knowing structrue of data like how rows and column
import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3],
                  [4,5,6]])
arr_3d = np.array([[[1,2.14],[3.4,4],[5,6.47],[7.41,8]]])

print(arr_2d.shape)
#for knowing total number in elements in array->size

print(arr_2d.size)
#for knowing number of dimensions

#for knowing number of dimensions
print("Priting number of dimensions")
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

#for knowing data type of element
print("Datetype of element")
print(arr_3d.dtype)

#for performing type conversion of data
print("Type Conversion")
int_arr =  arr_3d.astype(int)
print(int_arr)
print(int_arr.dtype)

#for perfroming mathematical operations
print("Performing mathematical operations")
print(arr_3d + 50)
print(arr_2d * 4)
print(arr_1d - 23)
print(arr_3d / 4)
print(arr_2d ** 2)



