import numpy as np

x=np.array([2,4,6,8])
y=np.array([30,50,70,90])

# split the data into training and testing sets
# training data:
x_train=x[:3]
y_train=y[:3]

# testing data:
x_test=x[3:]
y_test=y[3:]

print ("training data:",x_train,y_train)
print ("testing data:",x_test,y_test)