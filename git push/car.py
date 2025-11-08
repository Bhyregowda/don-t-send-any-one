#import neccesary libraries
import pandas as pd
#read csv file
df=pd.read_csv(r"C:\Users\SM\Desktop\AI&ML\car.csv")
print(df)
#2 get all cars with 8 cylinder
cars_with_8_cylinders = df[df['cylinders']==8]
print("cars with 8 cylinders:")
print(cars_with_8_cylinders)
#3.get the number of cars manufactured in each year
cars_per_year=df['model-year'].value_counts().sort_index()
print("number of cars manufactured each year:")
print(cars_per_year)