import numpy as np

# Sample data
data = np.array([2, 4, 6, 8, 10])

# variance_np = np.var(data, ddof=1)  # Set ddof=1 for sample variance
# print(f"Variance (using NumPy): {variance_np:.2f}")

# Step 1: Calculate the mean
mean = np.mean(data)

# Step 2: Compute the differences
differences = data - mean

# Step 3: Square the differences
squared_differences = differences ** 2

# Step 4: Sum the squared differences
variance = np.sum(squared_differences) / (len(data) - 1)

print(f"Variance: {variance:.2f}")
