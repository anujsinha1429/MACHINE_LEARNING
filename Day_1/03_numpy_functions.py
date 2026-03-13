import numpy as np

a=np.zeros((3,3)) # creates a 3x3 array of zeros
b=np.ones((2,2)) # creates a 2x2 array of ones
c=np.arange(0,10) # creates an array of numbers from 0 to 9
print(a)
print(b)
print(c)

d=np.random.randint(0,10,(3,3)) # creates a 3x3 array of random integers between 0 and 10
print(d)

e=np.random.rand(3) # creates an array of 3 random floats between 0 and 1
print(e)

# numpy internally use:

# 1) features matrix
# 2) weights matrix
# 3) matrix multiplication