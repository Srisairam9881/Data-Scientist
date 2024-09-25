import numpy as np

# Define the expected returns for each asset (in percentage)
expected_returns = np.array([0.08, 0.12, 0.10])  # Asset A, Asset B, Asset C

# Define the weights of each asset in the portfolio
weights = np.array([0.5, 0.3, 0.2])  # 50% in A, 30% in B, 20% in C

# Define the covariance matrix (risk)
covariance_matrix = np.array([
    [0.0004, 0.0002, 0.0001],  # Variance and covariance for Asset A
    [0.0002, 0.0005, 0.0003],  # Variance and covariance for Asset B
    [0.0001, 0.0003, 0.0004]   # Variance and covariance for Asset C
])

# Calculate the expected portfolio return
expected_portfolio_return = np.dot(weights, expected_returns)
print(f"Expected Portfolio Return: {expected_portfolio_return:.2%}")

# Calculate the portfolio risk (standard deviation)
portfolio_variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
portfolio_risk = np.sqrt(portfolio_variance)
print(f"Portfolio Risk (Standard Deviation): {portfolio_risk:.2%}")

# Example of optimizing weights (simple reallocation)
# This is just a demonstration and not an actual optimization
new_weights = np.array([0.4, 0.4, 0.2])  # Change to 40% A, 40% B, 20% C
expected_new_return = np.dot(new_weights, expected_returns)
new_portfolio_variance = np.dot(new_weights.T, np.dot(covariance_matrix, new_weights))
new_portfolio_risk = np.sqrt(new_portfolio_variance)

print("\nAfter reallocating weights:")
print(f"New Expected Portfolio Return: {expected_new_return:.2%}")
print(f"New Portfolio Risk (Standard Deviation): {new_portfolio_risk:.2%}")