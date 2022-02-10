# Binning method for data smoothing
import numpy as np
n = int(input("Enter number of elements : "))

l = sorted(list(map(int,input("\nEnter the numbers : ").strip().split())))[:n]
bins = int(input("Enter number of Bins : "))
bin_list = []
size_of_bin = int(len(l)/bins)
for i in range(bins):
    bin_list.append(l[i*size_of_bin:(i+1)*size_of_bin])
    print(f'Bin {i+1} : {bin_list[i]}')
print('Smoothing by bin means : ')
bin_means = []
for i in range(bins):
    mn = int(np.mean(bin_list[i]))
    bin_means.append([mn]*size_of_bin)
    print(f'Bin {i+1} : {bin_means[i]}')
print('Smoothing by bin boundaries : ')
bin_boundaries = []
for i in range(bins):
    L = bin_list[i][0]
    R = bin_list[i][len(bin_list[i])-1]
    temp = [L]
    for j in range(1,len(bin_list[i])-1):
        if(bin_list[i][j] - L <= R - bin_list[i][j]):
            temp.append(L)
        else:
            temp.append(R)
    temp.append(R)
    bin_boundaries.append(temp)
    print(f'Bin {i+1} : {bin_boundaries[i]}')





# 4 8 9 15 21 21 24 25 26 28 29 34