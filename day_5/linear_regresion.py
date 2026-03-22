import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data={
    "hours":[3,5,2,6,4],
    "sleep":[7,6,8,5,7],
    "marks":[65,80,50,90,70]
}
df=pd.DataFrame(data)

X=df[["hours","sleep"]]
y=df["marks"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

predictions=model.predict(X_test)
print("Predictions:",predictions)

new_data=[[5,6]]
print("Predicted marks:",model.predict(new_data))
