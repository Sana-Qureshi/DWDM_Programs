#linear regression find value of width and slope
import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

train=pd.read_csv('train.csv')
print(train)

trainprice= train['price']
traindata=train.drop('price', axis='columns')
model=linear_model.LinearRegression()
model.fit(traindata,trainprice)

test_data=pd.read_csv('test.csv')
testprice=model.predict(test_data)

test_data['price']=testprice
test_data.to_csv('prediction.csv', index=False)

print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)
