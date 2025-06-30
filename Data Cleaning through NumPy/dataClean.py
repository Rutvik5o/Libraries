import pandas as pd
import numpy as np


pd.set_option('display.max_columns',None) #Show all columns

df = pd.read_csv(r'E:\Data Science\Projects-remain\NumPy\Final Project\indian_employee_data_large.csv')

print(df.head())

#checking the missing values
print("Missing value in each column")
print(df.isnull().sum()) #give in each column how many missing values

#Replaceing Value
df['Salary_INR'] = df['Salary_INR'].fillna(df['Salary_INR'].mean())
df['Experience_Years'] = df['Experience_Years'].fillna(df['Experience_Years'].median())
df['Age'] = df['Age'].fillna(df['Age'].median())


#Replaceing Infinite values into mean
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Then fill missing numeric values only
df.fillna(df.select_dtypes(include='number').mean(), inplace=True)





#Remove Duplicate Records
df.drop_duplicates(inplace=True)

#Replace Nagative Salaries
df['Salary_INR'] = np.where(df['Salary_INR']<0,df['Salary_INR'].mean(),df['Salary_INR'])


salary_mean = df['Salary_INR'].mean()
salary_std = df['Salary_INR'].std()
Lower_Bound = salary_mean - ( 3 * salary_std)
Upper_Bound = salary_mean + ( 3 * salary_std)


#Remove rows where salary is too high or too low

df = df[(df['Salary_INR'] >= Lower_Bound) & (df['Salary_INR'] <= Upper_Bound)]


df.to_csv('Cleaned_Indian_Employee_data.csv',index=False)

print("Data Cleaning Succesfully")
print(df.isnull().sum())