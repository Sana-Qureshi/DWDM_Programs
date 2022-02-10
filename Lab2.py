import matplotlib.pyplot as plt
ages = []
n = int(input("Enter number of peoples to enter their ages : "))
print("Enter the ages : ")
for i in range(0, n):
            ele = int(input())
            ages.append(ele)
n1 = int(input("Enter number of ages_group : "))
age_group=[]
print("Enter age-groups : ")
for i in range(0, n1):
            ele = int(input())
            age_group.append(ele)
plt.hist(ages,age_group,rwidth=0.8)
plt.xticks(age_group)
plt.yticks(range(0,10,1))
plt.title('Linnear Regression')
plt.xlabel('age_group')
plt.ylabel('Number of people in respective ages')
plt.show()


