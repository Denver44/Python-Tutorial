import numpy

# # This Function is used to find determinant.
# print(numpy.linalg.det([[1,2],[2,1]]))
# print(numpy.linalg.eig([[1,2],[2,1]]))
# print(numpy.linalg.inv([[1,2],[2,1]]))

n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
numpy.set_printoptions(legacy='1.13')  # important work as Setting Precision.
print(numpy.linalg.det(a))
