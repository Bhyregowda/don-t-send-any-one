#import necessary libraries
import pandas as pd
#create the data frame
data={
'name': ['alice','bob', 'charlie','david', 'eve'],
'department': ['hr', 'engineering', 'engineering', 'hr','marketing'],
'experience': [5,10,3,8,2],
'salary': [50000,80000,60000, 70000,55000]
}
#print the data
df=pd.DataFrame(data)
print("original dataframe:")
print(df)
#pivot table for average salary department
pivot_avg_salary=df.pivot_table(values='salary', index='department',aggfunc='mean').reset_index()
print("\naverage salary by department:")
print(pivot_avg_salary)
#pivot table for sum and mean salary of each employee
pivot_sum_mean_salary=df.groupby('name').agg(total_salary=('salary','sum'),average_salary=('salary',
'mean')).reset_index()
print("\nsum and mean salary of each employee:")
print(pivot_sum_mean_salary)