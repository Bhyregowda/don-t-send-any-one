import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Sample data
data = {'BP': [120, 140, 130, 150, 110],
 'Sugar': [5, 6, 7, 8, 9],
 'Age': [40, 50, 35, 45, 55],
 'Gender': ['M', 'F', 'M', 'M', 'F'],
 'Cholesterol': [180, 200, 220, 240, 260],
 'Heart_Disease': [0, 1, 1, 1, 0]}
df = pd.DataFrame(data)
# Encode 'Gender'
df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})
# Split the data
X = df[['BP', 'Sugar', 'Age', 'Gender', 'Cholesterol']]
y = df['Heart_Disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Sample data
data = {'BP': [120, 140, 130, 150, 110],
 'Sugar': [5, 6, 7, 8, 9],
 'Age': [40, 50, 35, 45, 55],
 'Gender': ['M', 'F', 'M', 'M', 'F'],
 'Cholesterol': [180, 200, 220, 240, 260],
 'Heart_Disease': [0, 1, 1, 1, 0]}
df = pd.DataFrame(data)
# Encode 'Gender'
df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})
# Split the data
X = df[['BP', 'Sugar', 'Age', 'Gender', 'Cholesterol']]
y = df['Heart_Disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
