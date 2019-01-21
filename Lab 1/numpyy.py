import numpy as np
from numpy import random

# Other types of arrays

zeros = np.zeros((10, 10))
print(zeros)
# print the shape of zeros
#<------------INSERT CODE HERE------------>
print(zeros.shape)
ones = np.ones((4, 4))
print(ones)
# print the shape of ones
#<------------INSERT CODE HERE------------>
print(ones.shape)

print(ones.reshape(2, 8))
# print the shape of ones
#<------------INSERT CODE HERE------------>
print(ones.shape)

# We can also use numpy to generate random values.
randn = np.random.randn(1, 1000)
# print the shape of randn
#<------------INSERT CODE HERE------------>
print(randn.shape)

# print the first 10 elements of randn. What happens if you re-run this code? Its valus change.
#<------------INSERT CODE HERE------------>
i = 0
while i < 10:
    i += 1
    print(randn[0][i])

np.random.seed(23)

# Generate a new array of random numbers, this time of shape (3, 2) and print it.
# What happens when you re-run the code now?
# TIP: you might want to save the result to compare the previous and the new one

#<------------INSERT CODE HERE------------>
arr_rnd_no = np.random.randn(3, 2)

print(arr_rnd_no)

# Think: what does np.seed() do? (Use Google if you don't know!)

arr1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
arr2 = np.array([[5, 6, 7, 8], [5, 6, 7 , 8]])

# Print the shapes of arr1 and arr2 and cat after each of the types of concatenations.
# Concatenating arrays is a very common operation. Make sure you understand it!
# TIP: it might help you to print the actual cat array after each type of concatenation too

#<------------INSERT CODE HERE------------>
print(arr1)
print(arr2)
print(arr1.shape)
print(arr2.shape)

# concatenate along the row
cat = np.concatenate((arr1, arr2), axis=0)
#<------------INSERT CODE HERE------------>
print(cat)
print(cat.shape)

# concatenate along the column
cat = np.concatenate((arr1, arr2), axis=1)    
#<------------INSERT CODE HERE------------>
print(cat)
print(cat.shape)

# stack arrays vertically
cat = np.vstack((arr1, arr2))
#<------------INSERT CODE HERE------------>
print(cat)
print(cat.shape)
# stack arrays horizontally
cat = np.hstack((arr1, arr2))
#<------------INSERT CODE HERE------------>
print(cat)
print(cat.shape)

#Let's create a couple of vectors using numpy
v1 = np.array([20, 30, 40, 50])
v2 = np.arange(4)

#And a couple of matrices
mat1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
mat2 = mat1.T # this is the transpose of mat1

# Add a number to an array of 1-D (i.e., a vector)
print(5 + v1)
# Compare the line above to your function vector_plus_num(vector, number) from Part 1.

# Does your function work with matrices?

# How do you add a number to a np.array object? Try adding 2367 to mat1

#<------------INSERT CODE HERE------------>
mat1.add(mat1, 2367)
