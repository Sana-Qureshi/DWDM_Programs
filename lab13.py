number_of_clusters = int(input('enter no of clusters : '))
ans = []
for _ in range(number_of_clusters): 
    number_of_obj = int(input('enter no of obj : '))
    print('enter postion of each obj : ')
    linear_sum1 = 0
    linear_sum2 = 0
    sqr_sum1 = 0
    sqr_sum2 = 0
    t = (number_of_obj,)
    for _ in range(number_of_obj): 
        x,y = map(int,input('x y : ').split(' '))
        linear_sum1 += x
        linear_sum2 += y
        sqr_sum1 += x**2
        sqr_sum2 += y**2
    t2 = (linear_sum1,linear_sum2)
    t3 = (sqr_sum1,sqr_sum2)
    t = (t) + (t2,)
    t = (t) + (t3,)
    ans.append(t)

print('cluster feature if each cluster')
for i in range(len(ans)): 
    print(f'{i+1} : {ans[i]}')