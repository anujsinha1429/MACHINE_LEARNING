import pandas as pd 
data = {
    "name":["ANUJ","RAHUL","SHIVAM","amit","sumit"],
    "study_hours":[3,5,2,6,4],
    "sleep":[7,6,8,5,7],
    "marks":[65,80,50,90,70]
}
# to print the data in tabular format we can use pandas dataframe.
df = pd.DataFrame(data)
print(df)

# column selection 
print(df["name"])

# mutiple column selection
print(df[["name","study_hours"]])

# filtering data
print(df[df["study_hours"]>3])

# dataset summary
print(df.describe())

# features and labels 
x=df[["study_hours","sleep"]]
y=df["marks"]
print(x)
print(y)