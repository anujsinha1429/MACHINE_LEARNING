import numpy as np

a=np.array([[1,2,3],[4,5,6]])
print(np.sum(a))

# axis =0 means we want to sum along the columns
print(np.sum(a,axis=0))

# axis =1 means we want to sum along the rows
print(np.sum(a,axis=1))

# because 
# 1+4=5
# 2+5=7
# 3+6=9
# and in the second case
# 1+2+3=6
# 4+5+6=15