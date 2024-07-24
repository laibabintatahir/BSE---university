import numpy as np

class Perceptron:
    def __init__(self, size, n=0.5, T=0.5):
        self.w = np.array([0.6,0.6])  # Initialize weights randomly
        self.n = n  # Learning rate
        self.T = T  # Threshold for activation

    def activation_function(self, x):
        return 1 if x >= self.T else 0

    def predict(self, x):
        z = self.w.T.dot(x)
        return self.activation_function(z)

    def train(self, X, y):
        for epoch in range(5):  # Iterate for a fixed number of epochs
            print(f"Epoch {epoch + 1}")
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = y[i] - prediction
                self.w += self.n * error * X[i]
                print(f"Updated weights: {self.w}")

# Define the inputs and outputs for the OR gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 1, 1, 1])

# Initialize the Perceptron
perceptron = Perceptron(size=2, n=0.5, T=1)

# Train the Perceptron
perceptron.train(X, y)

# Test the Perceptron
print("Testing the Perceptron on OR gate inputs:")
for x in X:
    print(f"Input: {x}, Predicted Output: {perceptron.predict(x)}")
