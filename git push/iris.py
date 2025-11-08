#import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris=pd.read_csv(r"C:\Users\SM\Desktop\AI&ML\iris.csv")
#print 5 records
print("first 5 records:")
print(iris.head(5))
#print size of the dataset
print("\nsize of the dataset(rows,columns) ")
print(iris.shape)
#use scatterplot to comapre petal_length and width
plt.figure(figsize=(8,6))
sns.scatterplot(x='petal_length',y='petal_width',data=iris, hue='variety')
plt.title("scatterplot of petal length and petal width")
plt.show()
#check for missing values
print("\nmissing values in the dataset:")
print(iris.isnull().sum())