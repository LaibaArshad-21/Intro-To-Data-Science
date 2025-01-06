import pandas as pd

# Load the uploaded dataset to examine it
file_path = '/mnt/data/Iris.csv'
iris_data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
iris_data.head()
# Locate missing data
missing_data_summary = iris_data.isnull().sum()

# Display the number of missing values for each column
missing_data_summary





# Task 2: Data Integrity and Transformation

# Step 1: Remove duplicate records
duplicates_before = iris_data.duplicated().sum()
iris_data_cleaned = iris_data.drop_duplicates()
duplicates_after = iris_data_cleaned.duplicated().sum()

# Step 2: Feature engineering for total_area
# Calculate sepal area and petal area
iris_data_cleaned['SepalArea'] = iris_data_cleaned['SepalLengthCm'] * iris_data_cleaned['SepalWidthCm']
iris_data_cleaned['PetalArea'] = iris_data_cleaned['PetalLengthCm'] * iris_data_cleaned['PetalWidthCm']

# Calculate total_area
iris_data_cleaned['TotalArea'] = iris_data_cleaned['SepalArea'] + iris_data_cleaned['PetalArea']

# Step 3: Inspect for missing values after transformations
missing_data_after_transform = iris_data_cleaned.isnull().sum()

# Drop rows with missing values if any
iris_data_final = iris_data_cleaned.dropna()

# Results summary
{
    "duplicates_before": duplicates_before,
    "duplicates_after": duplicates_after,
    "missing_data_after_transform": missing_data_after_transform,
    "final_row_count": iris_data_final.shape[0]
}
