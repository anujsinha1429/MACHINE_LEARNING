import pandas as pd
from sklearn.model_selection import train_test_split

data={
    "hour_studied":[3,5,2,6,4],
    "sleep_hours":[7,6,8,5,7],
    "marks":[65,80,50,90,70]
}
df=pd.DataFrame(data)
print(df)

x=df[["hour_studied","sleep_hours"]]
y=df["marks"]

# split the data into training and testing sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
print("Training set:")
print(x_train)
print(y_train)
print("Testing set:")
print(x_test)
print(y_test)