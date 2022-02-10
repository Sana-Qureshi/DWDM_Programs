#lab of CHI-square test
from scipy.stats import chi2_contingency

# defining the table
data = [[int(input("Enter input for observed data: ")) for _ in range(2)] for _ in range(2)]
# data = [[250,200], [50,1000]]
stat, p, dof, expected = chi2_contingency(data)
print('\nObserved value:',data)
print('Expected value :\n',expected)
v = 0
for i in range(len(data)):
    for j in  range(len(expected)):
        v = v + (data[i][j]-expected[i][j])**2/expected[i][j]
        
print("\nValue Of P = ", v)       






# # interpret p-value
# alpha = 0.05
# print("p value is ", p)
# if p <= alpha:
# 	print('Dependent (reject H0)')
# else:
# 	print('Independent (H0 holds true)')
