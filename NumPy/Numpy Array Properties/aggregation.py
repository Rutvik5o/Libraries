import numpy as np

arr_3d = np.array([[[1,2.14],[3.4,4],[5,6.47],[7.41,8]]])

print("Perfroming aggregation operations")

print(np.sum(arr_3d))
print(np.min(arr_3d))
print(np.max(arr_3d))
print(np.mean(arr_3d))
print(np.std(arr_3d)) #perform standard deviation
print(np.var(arr_3d)) #perform variance