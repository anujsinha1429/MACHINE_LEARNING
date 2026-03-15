import pandas as pd

# basic statistics 
df=pd.read_csv("data.csv")
print(df.describe())

# output
#              AGE
# count   3.000000
# mean   23.000000
# std     1.000000
# min    22.000000
# max    24.000000
