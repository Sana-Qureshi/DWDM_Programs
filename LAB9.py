#using model in prediction
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = pd.read_csv("houses.csv")
# print(data.head(10))
# print(data.columns)
# print(data.shape)
#data visulaization
print("Is there any missing/null value?\n",data.isnull().sum())
#modeling
print(data.head(5))
train=data.drop('price', axis='columns')
test = data['price']
x_train, x_test , y_train, y_test = train_test_split(train,test, test_size=0.3, random_state=2)
regr = LinearRegression()
regr.fit(x_train, y_train)
pred= regr.predict(x_test)
print("\nPrediction")
print(pred)
print("\nAccuracy",regr.score(x_test, y_test))




# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# pred = regr.predict(x_test)
# print(confusion_matrix(y_test, pred))
# print(classification_report(y_test, pred))
