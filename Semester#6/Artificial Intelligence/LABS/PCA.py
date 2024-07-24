import numpy as np

# Define the data
data = np.array([[8, 11], [10, 5], [13, 7], [7, 14], [5, 6], [7, 6]])

# Step-01 : calculate Mean
mean = np.mean(data, axis=0)
print("-----------------------------")
print("\t Mean : ", np.round_(mean, 2))
print("-----------------------------")

# Step-02 : center data
centered_data = data - mean

# Step-03 : Covariance Matrix
cov_matrix = np.cov(centered_data, rowvar=False)
print("Covariance matrix : \n", np.round_(cov_matrix, 2))
print("----------------------------------------")

# Step-04 : eigen values
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("EigenValues: ", np.round(eigenvalues, 2))
print("----------------------------------------")

# Step-05 : eigen vectors
print("EigenVectors : \n", np.round(eigenvectors, 2))
print("----------------------------------------")

# Step-06 Transform data (corrected)
transformed_data = np.dot(centered_data, eigenvectors[:, ::-1])
print("Transformed Data (Principal Components):\n", np.round(transformed_data, 2))
print("----------------------------------------")

# Step 7: Reduce dimensionality
principalComponent_1_corrected = transformed_data[:, 0]
print("Principal Component 1: \n", np.round(principalComponent_1_corrected, 2))
print("-----------------------------------------")


