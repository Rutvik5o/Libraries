import numpy as np

#using normal list

# temp=[34.34,35.35,35.24,66,4]

# total=0

# for x in temp:
#     total += x

# ans=total/len(temp)
# print(ans)


temprature = np.array([34.34,35.35,35.24,66,4])
avg = np.mean(temprature)
print("Average is => ", avg)

