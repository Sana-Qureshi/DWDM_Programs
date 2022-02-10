
from math import sqrt
# calculate manhattan distance
def manhattan_distance(a, b):
	return sum(abs(e1-e2) for e1, e2 in zip(a,b))
# calculate euclidean distance
def euclidean_distance(a, b):
	return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))
row1 = [10, 20, 15, 10, 5]
row2 = [12, 24, 18, 8, 7]
print("Input Data :\n")
print(row1)
print(row2)
# calculate distance
dist = euclidean_distance(row1, row2)
print("Euclidean distance is : ",dist)

manhattanDist = manhattan_distance(row1, row2)
print("Manhattan distance is :", manhattanDist )
print()