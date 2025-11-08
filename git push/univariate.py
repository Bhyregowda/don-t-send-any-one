#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Read the CSV file into a DataFrame
data = pd.read_csv(r"C:\Users\SM\Desktop\AI&ML\emp1.csv")
#Display the first 5 rows of the dataset
print(data.head(5))
#Plot a histogram to show the distribution of 'age'
sns.histplot(data['age'])
x = data['status_year'].value_counts()
print(x)
print(x.values)
print(x.index)
plt.pie(x.values,labels = x.index,autopct='%1.1f%%')
plt.show()