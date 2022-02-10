import statistics
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print(lst)
print("Mean : "+str(statistics.mean(lst)))
print("Mode : "+str(statistics.mode(lst)))
print("Median : "+str(statistics.median(lst)))