
from sklearn.tree import DecisionTreeClassifier

# Training data
X = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = [1, 1, 0, 0]

# Create and train the decision tree
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict the output
prediction = model.predict([[1, 0]])

print("Predicted output:", prediction[0])
