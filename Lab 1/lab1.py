# Let's create a vector. We can do this as a Python built-in type: the list
vector1 = [1, 2, 4, 78, 93] # we declare the vector as a list of elements

print(vector1)
print("The vector has %d elements" % len(vector1))

# Let's add a number to every element of the vector.
## Exercise: create a function that, given a vector and a number,
## returns the addition of that number to each element of the vector
def vector_plus_num(vector, number):
    
    #<------------INSERT CODE HERE------------>
    for index in range(len(vector)):
        vector[index] = vector[index] + number
    
    return vector
    
# Let's test your function:
print(vector_plus_num(vector1, 5))
print(vector_plus_num(vector1, -33))

def vector_mean(vector):
    
    #<------------INSERT CODE HERE------------>
    sumOfVector = 0

    for index in range(len(vector)):
        sumOfVector += vector[index]
    
    sumOfVector /= len(vector)

    return sumOfVector

print(vector_mean(vector1))

# Now let's create a new vector, called vector2, of the same length as vector1.
# We will then look at operations with multiple vectors, 
# such as adding and subtracting them, and vector multiplications.
vector2 = vector1 #<------------INSERT CODE HERE------------>

assert len(vector1) == len(vector2), "The vectors are not of the same length"

def add_two_vectors(vec1, vec2):
    sumVec = []
    index = 0
    while index < len(vec1):
        sumVec.append(vec1[index] + vec2[index])
        index += 1
    return sumVec

# Let's test your function:
print(add_two_vectors(vector1, vector2))
#print(add_two_vectors(vector1, [1, 2, 3]))
# If the second print resulted in an error, don't worry about it for now!

def scalar_product(v1, v2):
    #<------------INSERT CODE HERE------------>
    dotprod = []
    index = 0
    while index < len(v1):
        dotprod.append(v1[index] * v2[index])
        index += 1

    scalarProduct = sum(dotprod)

    return scalarProduct

# Test your function
#<------------INSERT CODE HERE------------>
print(scalar_product(vector1, vector2))

# Create a function that receives two matrices as input and returns the matrix multiplication of the two
# If you don't know how to multiply two matrices, check:
# https://en.wikipedia.org/wiki/Matrix_multiplication#Definition

def matrix_multiplication(matrix1, matrix2):
    
    #<------------INSERT CODE HERE------------>

    #get number of columns
    #get number of rows

    return 0#multipl_result

# And let's test your function:
# NOTE: some of the tests below will give errors. Don't worry about them!
matrixA = [[1, 2, 3], [1, 2, 3]]
matrixB = [[5, 6, 7], [5, 6, 7], [5, 6, 7]]
matrixC = [[8, 9], [8, 9], [8, 9], [8, 9]]
matrixD = [[10, 11], [10, 11], [10, 11]]

print(matrix_multiplication(matrixA, matrixB))
print(matrix_multiplication(matrixA, matrixC))
print(matrix_multiplication(matrixD, matrixA))