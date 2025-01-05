import numpy as np

array_1d = np.arange(1, 21)

# Step 2: Reshape it into a 4x5 2D array
array_2d = array_1d.reshape(4, 5)

# Step 3: Replace all elements in the last column with zeros
array_2d[:, -1] = 0

# Step 4: Flatten the array back to 1D
flattened_array = array_2d.flatten()

flattened_array


# Generate a 2D array of random integers between 10 and 50 with a shape of 5x5
random_2d_array = np.random.randint(10, 50, size=(5, 5))

# Calculate and print the mean, sum, min, and max for each row
row_means = np.mean(random_2d_array, axis=1)
row_sums = np.sum(random_2d_array, axis=1)
row_mins = np.min(random_2d_array, axis=1)
row_maxs = np.max(random_2d_array, axis=1)

# Calculate and print the mean, sum, min, and max for each column
col_means = np.mean(random_2d_array, axis=0)
col_sums = np.sum(random_2d_array, axis=0)
col_mins = np.min(random_2d_array, axis=0)
col_maxs = np.max(random_2d_array, axis=0)

print("Task 2 Results:")
print("Array:\n", random_2d_array)
print("Row Means:", row_means)
print("Row Sums:", row_sums)
print("Row Minimums:", row_mins)
print("Row Maximums:", row_maxs)
print("Column Means:", col_means)
print("Column Sums:", col_sums)
print("Column Minimums:", col_mins)
print("Column Maximums:", col_maxs)




# Create an identity matrix of size 4x4
identity_matrix = np.eye(4)

# Add a constant (e.g., 5) to each element in the diagonal
identity_matrix[np.diag_indices_from(identity_matrix)] += 5

# Replace the last row with a row of ones
identity_matrix[-1, :] = 1

print("Task 3 Result:\n", identity_matrix)



# Generate a 1D array of 15 random integers between 0 and 20
random_1d_array = np.random.randint(0, 21, size=15)

# Count the occurrences of each unique value in the array
unique_values, counts = np.unique(random_1d_array, return_counts=True)
occurrences = dict(zip(unique_values, counts))

# List the indices of elements greater than 10
indices_greater_than_10 = np.where(random_1d_array > 10)[0]

print("Task 4 Results:")
print("Array:", random_1d_array)
print("Occurrences:", occurrences)
print("Indices of elements > 10:", indices_greater_than_10)




# Create a 3x4 array filled with random floating-point numbers between 0 and 1
float_array = np.random.rand(3, 4)

# Round each element to two decimal places
float_array = np.round(float_array, 2)

# Replace the elements in the second column with 0.5
float_array[:, 1] = 0.5

print("Task 5 Result:\n", float_array)