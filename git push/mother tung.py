import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Read CSV file
ds = pd.read_csv(r"C:\Users\SM\Desktop\AI & ML\de.csv")

print("Original Dataset:")
print(ds)

# Map all unique values in 'mothertang' column
mothertang_map = {
    'kannada': 1,
    'English': 2,
    'Chinese': 3,
    'Hindi': 4,
    'Spanish': 5,
    'Korean': 6,
    'German': 7
}
ds['mothertang'] = ds['mothertang'].map(mothertang_map)

print("\nAfter encoding 'mothertang':")
print(ds)

# Map all unique values in 'going' column
going_map = {'y': 1, 'n': 0}
ds['going'] = ds['going'].map(going_map)

print("\nAfter encoding 'going':")
print(ds)

# Check for any remaining NaNs
print("\nRows with NaNs:")
print(ds[ds.isna().any(axis=1)])

# Drop any rows with NaN values (if any)
ds = ds.dropna()

# Prepare features and target
features = ["age", "noexp", "mothertang"]
X = ds[features]
y = ds["going"]

print("\nFeatures (X):")
print(X)
print("\nTarget (y):")
print(y)

# Train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=features, class_names=["No", "Yes"], filled=True)
plt.title("Decision Tree Classifier")
plt.show()
