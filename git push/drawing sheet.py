#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
#creating the dataset
data={
'number': [1,2,3],
'pencil': [300,350,400],
'textbook': [250,350,400],
'drawing sheet':[100,125,190],
'total': [700,1075,1320],
'profit': [80000,9500,12890]
}
print(data)
df=pd.DataFrame(data)
#check the statistical information of the dataset
print("statistical information")
print(df.describe())
#plotline showing total profit on y-axis and number column on x-axis
plt.figure(figsize=(10,6))
plt.plot(df['number'], df['profit'], marker='o',color='pink', linestyle='-')
plt.title('total profit vs number')
plt.xlabel('number')
plt.ylabel('total profit')
plt.grid(True)
plt.show()
#finding the missing values
print("\nmissing values:")
print(df.isnull().sum())
#find the sum of total profit
total_profit_sum=df['profit'].sum()
print("\n sum of the total profit:",total_profit_sum)
#find the maximum values from the drawing sheet column
max_drawing_sheet=df['drawing sheet'].max()
print("\n maximum values from drawing sheet column: ",max_drawing_sheet)