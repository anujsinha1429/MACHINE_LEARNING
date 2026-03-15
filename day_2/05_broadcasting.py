# broadcasting
# different size of arrays are intelligently operated without manually 
# reshaping them
import numpy as np
a= np.array([1,2,3])
b=10
print(a+b)
# in this case, the scalar value 10 is added to each element of the array a,
#  resulting in a new array [11, 12, 13].

# broadcasting with matrix 

a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([10,20,30])
print(a+b)

# broadcasting possible when dimentions is same or one of them is 1

