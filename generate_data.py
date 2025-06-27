import pandas as pd
import numpy as np


#setting random seed for redproducibility
np.random.seed(42)

num_rows = 1000

#generate data

data = {
    'camera':np.random.randint(8,201,size=num_rows), #megaPixel 8 - 200
    'age':np.random.randint(0,4,size=num_rows), #age in years
    'RAM': np.random.choice([4,6,8,12,16],size=num_rows), #RAM in GB
    'CPU_Score': np.random.randint(40,101,size=num_rows), #CPU BenchMark
    'Slot_SD': np.random.randint(0,2,size=num_rows), #SD SLOT 0-> no
    'Sims' : np.random.choice([1,2],size = num_rows), #Number of sims
    'price': np.random.randint(8000,70001,size=num_rows) #Price in INR

}


#Creating DataFrame
df = pd.DataFrame(data)

name_of_file = str(input("Enter the name of file:"))

df.to_csv(f"{name_of_file}.csv",index=False)
print("File Generated Succesfully\n----------------------------\n")

#Display First Few Rows
print(df.head())