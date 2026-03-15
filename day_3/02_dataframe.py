# dataframe is a 2D data structure in pandas

# dataframe creation, here data is a dictionary, where keys are column names 
# and values are lists of column data:

import pandas as pd 
data={
    "NAME":["ANUJ","RAHUL","SHIVAM"],
    "AGE":[22,23,24],
    "CITY":["DELHI","MUMBAI","KOLKATA"]

}
df=pd.DataFrame(data)
# print(df)
# print(df.head())

# specific column data
# print(df["NAME"])

# data informtaion 
print(df.info())