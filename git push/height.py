#import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\SM\Desktop\AI&ML\height.csv')
print(df)
#ax=sns.boxplot(x=df['age'])
#ax=sns.boxplot(x=df['age'],y=df['height'])
#ax.set_title('boxplot')
#ax.set_xlabel('age')
#ax.set_ylabel('height')
h1=df["age"].quantile(.25)
print(h1)
h2=df["age"].quantile(.75)
print(h2)
h3=h1-h2
print(h3)
lw=h1-1.5*h3
print(lw)
uw=h2+1.5*h3
print(uw)
hu=df[(df.age<=lw)&(df.age>=uw)]
print(hu)
#bx=sns.boxplot(x=hu['age'],y=hu['height'])
#bx=sns.boxplot(x=hu['age'])
h4=df["height"].quantile(.25)
print(h4)
h5=df["height"].quantile(.75)
print(h5)
h6=h4-h5
print(h6)
lw1=h4-1.5*h6
print(lw1)
uw1=h5+1.5*h6
print(uw1)
hu1=df[(df.height<=lw1)&(df.height>=uw1)]
print(hu1)
cx=sns.boxplot(x=hu['age'],y=hu1['height'])
#cx=sns.boxplot(x=hu1['height'])