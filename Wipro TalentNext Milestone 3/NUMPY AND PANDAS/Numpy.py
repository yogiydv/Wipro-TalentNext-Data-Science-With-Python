# Exercise 1: Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr[:2, :2])

# Exercise 2: Create one dimensional array and perform ndim,shape, reshape  operation on it.

arr1d = np.array([1, 2, 3, 4, 5, 6])
print(arr1d)
print(arr1d.ndim)
print(arr1d.shape)
arr2d = arr1d.reshape(2, 3)
print(arr2d)