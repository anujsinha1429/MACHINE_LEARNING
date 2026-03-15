# to read csv file we use pandas library
import pandas as pd
# read csv file, here we are reading a file named "data.csv" which is in
# the same directory as this script, if the file is in a different directory, 
# we need to provide the path to the file
df=pd.read_csv("data.csv")
print(df)

# first 5 rows of the dataframe
print(df.head())


