import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data={
    "hours":[3,5,2,6,4],
    "marks":[65,80,50,90,70]
}
df=pd.DataFrame(data)

x=df[["hours"]]
y=df[["marks"]]

model=LinearRegression()
model.fit(x,y)

predicted= model.predict(x)

plt.scatter(df["hours"],y,color="blue",label="actual data")
plt.plot(df["hours"],predicted,color ="red",label="model line ")

plt.xlabel("hours studied")
plt.ylabel("marks")
plt.title("hours vs marks")

plt.legend()
plt.show()
