import numpy as np

a=np.array([1,2,3,4,5,6])
b=np.reshape(a,(2,3))
print(b)

# flatten the array b
print(b.flatten())
# flatten is used to convert a multi-dimensional array into a one-dimensional 
# array. In this case, it takes the 2D array b and flattens it back into a 1D 
# array, which is the same as the original array a.