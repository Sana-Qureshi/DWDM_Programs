import pandas as pd 
from scipy.spatial.distance import hamming
df=pd.read_csv('Hospital.csv')
print("****** Categorical Data ********")
print(df)

dummies1=pd.get_dummies(df["gender"])
dummies2=dummies1.drop(['F'], axis='columns')
dummies3=dummies2.rename(columns={'M': 'gender'})

dummies4=pd.get_dummies(df["fever"])
dummies5=dummies4.rename(columns={'Y': 'fever'})

dummies6=pd.get_dummies(df["cough"])
dummies7=dummies6.drop(['N'], axis='columns')
dummies8=dummies7.rename(columns={'P': 'cough'})

dummies9=pd.get_dummies(df["test1"])
dummies10=dummies9.drop(['N'], axis='columns')
dummies11=dummies10.rename(columns={'P': 'test1'})

df2=df.drop(['gender','fever','cough','test1'], axis='columns')
new=pd.concat([df2,dummies3,dummies5,dummies8,dummies11], axis='columns')
print("****Binary data******")
print(new)

Row_list =[]
for index, rows in new.iterrows():
    my_list =[rows.gender, rows.fever, rows.cough, rows.test1]
    Row_list.append(my_list)

dist = hamming(Row_list[0],Row_list[1])
print("Dissimilarity between jack and mary ",dist)

dist1 = hamming(Row_list[0],Row_list[2])
print("Dissimilarity between Jack Jim ",dist1)

dist2 = hamming(Row_list[1],Row_list[2])
print("Dissimilarity between Mary Jim ",dist2)

if(dist>dist1 and dist>dist2):
        print("Jack and Mary have most dissimilar diseases")

if(dist1>dist and dist1>dist2):
        print("Jack and Jim have most dissimilar diseases")

if(dist2>dist1 and dist2>dist):
        print("Mary and Jim have most dissimilar diseases")