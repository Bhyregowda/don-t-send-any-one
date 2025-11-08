#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Load the CSV file into a DataFrame
data = pd.read_csv(r"C:\Users\SM\Desktop\AI&ML\emp1.csv")
print(data)
#Bar plot: Department vs Length of Service
plt.figure(figsize=(15,5))
sns.barplot(x=data['department_name'],y=data['length_of_service'])
plt.xticks(rotation=45)
plt.show()
#Scatter plot: Length of Service vs Age
plt.figure(figsize=(8,5))
sns.scatterplot(x=data['length_of_service'],y=data['age'])
plt.show()
#Count plot: Status Year with Status as Hue
plt.figure(figsize=(10,5))
sns.countplot(x=data['status_year'],hue=data['status'])
plt.show()