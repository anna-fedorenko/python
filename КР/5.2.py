import numpy as np

# Set seed for reproducibility
np.random.seed(0)

# Create two 4x4 arrays with random integers in the range from -10 to 10
A = np.random.randint(-10, 11, (4, 4))
B = np.random.randint(-10, 11, (4, 4))

# Find indices of all negative elements in matrix A
negative_indices_A = np.argwhere(A < 0)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Indices of negative elements in A:\n", negative_indices_A)

