import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print(arr)

# Dimension of array
print("Dimension of array",arr.ndim)

#Shape of the array number of rows and columns
print("Shape of an array",arr.shape)

#Size of an array
print("Size of an array",arr.size)

#for knowing data type of an array
print("Data type of an array",arr.dtype)

#Creating array from list of data
a= np.array([[1,3,0],[7,5,6]])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Array a:")
print(a)
print("Shape of array a:", a.shape)
print("Dimension of array a:", a.ndim)
print("data type of array a", a.dtype)


print("Array b:")
print(b)
print("Shape of array b:", b.shape)
print("Dimension of array b:", b.ndim)
print("data type of array b", b.dtype)

# Creating numpy array using function
# it will create an array from 1 to 10 with step size of 2
print("Array from with step of 2",np.arange(1,30,2))

# it will create an array from 1 to 10 with 5 elements  
print(np.linspace(1,10,1))

# Prininting array of zeros and ones
print("Array of zeros",np.zeros((3,4)))
print("Array of ones",np.ones((3,4)))

#Printing array of using indentity matrix
print("Identity matrix",np.eye(3))

#To print selected elements of an array
a[:, 0]	  # All rows, first column
a[:, 1]	  # All rows, second column
a[1, :]	  # All columns, second row
a[0:2, :] # First two rows, all columns

#Arithmatic operations on array
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1**2)
print(arr2**2)

#Comparision operations on array
print(arr1>1)

#Square root of an array
print(np.sqrt([16,9,25]))

print(np.exp([10,12,14]))