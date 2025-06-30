#ML model doesn't process NaN value
#np.nan_to_num(array,nan=value) default - 0

import numpy as np

arr = np.array([1,2,np.nan,4,5,np.nan])

cleaned_arr = np.nan_to_num(arr,nan=100)

print(cleaned_arr)

#Replacing NaN value to Particular Number
#if did not pass then by take default 0 value