#that value  exceed the python value called->inifite
#np.isinf(array) 10^1000

import numpy as np

arr = np.array([1,2,np.inf,4,-np.inf,6])

print(np.isinf(arr))


#Replacing infinite value

clearned_arry = np.nan_to_num(arr,posinf=1000,neginf=1000) #Positive infnitfy, and neg

print(clearned_arry)