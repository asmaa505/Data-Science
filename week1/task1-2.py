'''
اسماء احمد اسماعيل مارية
ID: 811634546

'''

# TASK 1
# 1. How do you efficiently generate a diagonal matrix from a 1D array
import numpy as np

arr = np.array([1, 2, 3, 4])
diag_matrix = np.diag(arr)

print(diag_matrix)



# 2. How do you find the indices of the top k largest elements in an array
arr = np.array([10, 50, 20, 40, 30])
k = 3

top_k_indices = np.argsort(arr)[-k:]

print(top_k_indices)



# 3. How do you efficiently normalize a NumPy array?
arr = np.array([1, 2, 3, 4, 5])

normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(normalized)




# 4. Write a Python script using NumPy to analyze a dataset of student grades.
np.random.seed(42)

grades = np.random.randint(0, 101, size=(10, 5))
print(f"Grades:\n{grades}")


mean = np.mean(grades, axis=0)
median = np.median(grades, axis=0)
std = np.std(grades, axis=0)

print("Mean:", mean)
print("Median:", median)
print("Std:", std)


high_scores = grades > 80
students_idx = np.where(np.sum(high_scores, axis=1) >= 3)

print("Students indices:", students_idx[0])


min_val = grades.min()
max_val = grades.max()

normalized_grades = (grades - min_val) / (max_val - min_val)
print("Normalized Grades:\n", normalized_grades)


reshaped = normalized_grades.reshape(5, 2, -1)
print("Reshaped Shape:", reshaped.shape)


correlation_matrix = np.corrcoef(grades, rowvar=False)
print("Correlation Matrix:\n", correlation_matrix)


#######################################################################

# TASK 2

# 1.Use an appropriate reader function from pandas to read this file and show the first 10 rows
import pandas as pd
df = pd.read_csv("data/GenomicData_orig.csv")
print(df.head(10))



# 2.What are the labels of the first column (index 0) and 20th column 
print(df.columns[0])
print(df.columns[19])



# 3.Drop the first two columns 
cols_to_drop = [df.columns[0], df.columns[1]]
df = df.drop(columns=cols_to_drop)



# 4.How many missing values are in this dataset
missing_values = df.isnull().sum().sum()
print("Number of missing values:", missing_values)



# 5.Fill missing values using fillna and prove no missing values now
df_filled = df.fillna(df.mean())
print(df_filled.isnull().sum().sum())