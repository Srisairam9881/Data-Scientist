import numpy as np

# Sample data for two variables X and Y
X = np.array([2, 4, 6, 8, 10])
Y = np.array([1, 3, 5, 7, 9])

# Step 1: Calculate the means
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Step 2: Compute the differences
diff_X = X - mean_X
diff_Y = Y - mean_Y

# Step 3: Multiply the differences
products = diff_X * diff_Y

# Step 4: Sum the products
covariance = np.sum(products) / (len(X) - 1)

print(f"Covariance between X and Y: {covariance:.2f}")
