
import numpy as np
from sklearn.neural_network import MLPClassifier

# Input and output data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])

# Create Feed Forward Neural Network
model = MLPClassifier(hidden_layer_sizes=(4,),
                      max_iter=5000, random_state=1)

# Train the network
model.fit(X, y)

# Test the network
print("Predicted output:", model.predict([[1, 1]])[0])
