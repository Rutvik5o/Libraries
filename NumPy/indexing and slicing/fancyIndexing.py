#fancy indexing
#for getting non sequence values from array & extracing multiple values from that 
#-> Creating copy of that, doesn't modify the original array

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[[0,2,4]])