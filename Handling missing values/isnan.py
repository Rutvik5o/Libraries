#NoN : Not a Number

#np.isnan(array)

import numpy as np
#using to find missing values
arr = np.array([1,2,np.nan,4,5,np.nan])

print(np.isnan(arr))

#InterView:Question
#can you compre np.nan directly?Na:explain

print(np.nan == np.nan)
