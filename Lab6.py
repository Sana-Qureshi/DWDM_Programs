#lab of data transformation using min-max, z-score, decimal scaling
import statistics
import pandas as pd

def minMaxNormal(num,list):
    minNum=int(input("Enter Minimun Setting:\t"))
    maxNum = int(input("Enter Maximum Setting:\t"))
    ans=round(((num-min(list))/(max(list)-min(list))*(maxNum-minNum))+minNum,2)
    return ans

def zNormal (num,mean,stdDv):
    return round((num-mean)/stdDv,2)

def zNormalMAD (num,mean,abMeanDiv):
    return round((num-mean)/abMeanDiv,2)

def decNormal(num,maxNum):
    digit=len(str(maxNum))
    div=pow(10,digit)
    return num/div
data = list(int(num) for num in input("Enter the data:").strip().split())[:5]

# data=[200, 300, 400, 600, 1000]

num=int(input("Enter an item from data :"))

print("Min-max normalization :",minMaxNormal(num,data))

print("Z-score normalization :", zNormal(num,statistics.mean(data),statistics.stdev(data)))

df = pd.DataFrame(data)
print("Modified z-score normalization : ", zNormalMAD(num,statistics.mean(data),df.mad()))

print("Decimal scaling normalization :", decNormal(num,max(data)))