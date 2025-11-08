#Import necessary libraries
import pandas as pd
from sklearn import linear_model
#Read CSV file (make sure path is correct)
df = pd.read_csv(r"C:\Users\SM\Desktop\AI&ML\ccs.csv")
print(df)
#Define features (independent variables) and target (dependent variable)
x = df[["cie1","cie2","cie3"]] # Independent variables
y = df["see"]# Target variable (dependent)
reg = linear_model.LinearRegression()
#Fit (train) the model
reg.fit(x,y)
pre = reg.predict([[24,23,26]])
print("With comparison of cie1 to cie3, the person will score SEE:",pre)