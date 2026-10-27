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

# it will create an array from 1 to 10 with step size of 2
print("Array from with step of 2",np.arange(1,30,2))

# it will create an array from 1 to 10 with 5 elements  
print(np.linspace(1,5,10)) 