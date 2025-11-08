#represent the data in an 8*2 array
data=[
[1,6012],
[2,4072],
[3,6386],
[4,5230],
[5,7800],
[6,8900],
[7,5679],
[8,9800]]
#write a pogram in python o filter steps walked more than 7000
high_steps_days=[day for day, steps in data if steps > 7000]
print("days with steps>7000:",high_steps_days)
#print an array containing steps walked in sorted order
sorted_data=sorted(data,key=lambda x:x[1])
print("sorted data by steps walked:")
print(sorted_data)
#use pandas to add 1000 steps to all observations
import pandas as pd
df=pd.DataFrame(data, columns=['day', 'steps'])
df['steps'] +=1000
print("updated dataframe with 1000 steps added:")
print(df)
# day on which he walked more than 8000 steps using pandas
high_steps_days_pandas=df[df['steps']>8000]['day'].tolist()
print("days with steps>8000 using pandas:", high_steps_days_pandas)