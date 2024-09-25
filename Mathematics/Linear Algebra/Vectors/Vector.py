# What is a Vector?
# A vector is simply a way to represent data. Imagine a vector as an ordered list of numbers.
# For example, if you have a dataset about houses, a vector could represent one house's features like this:
# Size: 2000 sq ft
# Bedrooms: 3
# Bathrooms: 2
# This could be represented as a vector [2000,3,2].
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.Data Organization-
# Example: Imagine you have a dataset of cars, and each car has features like:
# Horsepower: 150
# Weight: 3000 lbs
# Miles per Gallon (MPG): 25
# You can represent each car as a vector:
# Car1=[150,3000,25] This helps you keep the data organized, making it easier to process.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2.Calculating Distances-
# Example: Suppose you want to find out how similar two cars are.
# You can use the Euclidean distance formula. For two cars:
# car1:[150,3000,25]
# car2:[200,2800,30]
# You can calculate the distance between them to understand how similar their features are.
# A smaller distance indicates more similarity.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.Machine Learning Models-
# Example: In a model predicting car prices, each car’s features are the input vectors. For instance:
# car1:[150,3000,25] might correspond to a price of $20,000.
# car2:[200,2800,30] might correspond to $25,000.
# The model learns from these vectors to predict prices for new cars based on their features.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4.Transforming Data-
# Example: Using PCA to reduce dimensions, you might have a dataset with many features (like horsepower, weight, and MPG).
# PCA transforms these features into a smaller set of new features (principal components) while retaining important information.
# Each car can then be represented as a vector in this reduced space, simplifying analysis.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5.Natural Language Processing-
# Example: In text analysis, words can be represented as vectors. For instance, the words “king” and “queen” might be represented as:
# king:[0.2,0.8,0.5]
# queen: [0.3,0.9,0.4]
# You can then measure the similarity between these vectors to understand relationships between words.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6.Efficient Computation-
# Example: When using a library like NumPy to process large datasets of cars, you can perform operations on entire arrays (vectors) at once.
# If you want to calculate the average horsepower of a fleet of cars:
# horsepower=[150,200,180]
# This efficiently computes the average without needing to loop through each value manually.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Summary:
# These examples illustrate how vectors help in organizing data, measuring similarities, training models,
# transforming data, analyzing language, and performing computations efficiently in data science.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# np.array() creates an array for each car’s features.
# car1 - car2 computes the difference between the two vectors.
# np.linalg.norm() calculates the Euclidean distance by applying the formula.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
# cars =np.array([
#     [150, 3000, 25],  # Car 1: [Horsepower, Weight (lbs), MPG]
#     [200, 3200, 20],  # Car 2
#     [120, 2800, 30],  # Car 3
# ])
# print(cars[2])
car1=np.array([150,3000,25])
car2=np.array([200,2800,30])
print("vector 1: ",car1)
print("vector 2: ",car2)
# Vector addition
vector_sum = car1 + car2
print("Sum of A and B:", vector_sum)

# Vector subtraction
vector_difference = car1 - car2
print("Difference of A and B:", vector_difference)

# Dot product
dot_product = np.dot(car1, car2)
print("Dot product of A and B:", dot_product)

# Euclidean distance
distance = np.linalg.norm(car1 - car2)
print("Euclidean distance between A and B:", distance)

horsepower = np.array([150, 200, 180])

Mean=np.mean(horsepower)
print("Mean: ",Mean)

median=np.median(horsepower)
print("Median: ",median)

Max=np.max(horsepower)
print("Max: ",Max)

Min=np.min(horsepower)
print("Min: ",Min)

avg=np.average(horsepower)
print("Average: ",avg)


