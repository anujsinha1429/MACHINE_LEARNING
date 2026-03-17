import pandas as pd

data={
    "name":["anuj","rahul","shivam"],
    "age":[22,None,24],
    "sleep_hours":[7,8,None]

}
df=pd.DataFrame(data)
# print(df)
print(df.isnull()) #this give output in boolean format.

print(df.isnull().sum()) # this give the count of null values in each column.

print(df.dropna()) # this will drop the rows which have null values.

# if we want to fill the null values with some value, we can use fillna() method.
print(df.fillna(0)) # this will fill the null values with 0.
df["age"]=df["age"].fillna(df["age"].mean()) # this will fill the null values in age column with the mean of age column.
print(df)

# duplicate remove
df=df.drop_duplicates()
print(df)