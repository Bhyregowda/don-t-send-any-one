#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Dataset
data = {
 'Experience': [1, 2, 3, 4, 5],
 'Salary': [40, 45, 60, 70, 75]
}
df = pd.DataFrame(data)
X = df[['Experience']] # Independent variable (2D array)
y = df['Salary'] # Dependent variable
# Model training
model = LinearRegression()
model.fit(X, y)
# Coefficients
intercept = model.intercept_
slope = model.coef_[0]
print(f"Intercept (b0): {intercept}")
print(f"Slope (b1): {slope}")
print(f"Equation: Salary = {intercept:.2f} + {slope:.2f}*Experience")
# Prediction
y_pred = model.predict(X)
# Plot
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary ($1000s)')
plt.title('Experience vs Salary (Linear Regression)')
plt.legend()
plt.show()