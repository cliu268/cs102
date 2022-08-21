# Absolute Matrix
# https://xjoi.net/contest/4600/problem/1

# Description:
# Given a n*m matrix, output its absolute matrix. An absolute matrix is defined as a matrix in which each element is the absolute 
# value of the orignal element in the input matrix.

# Input:
# The first row contains two integers n, m representing the dimensions of the input matrix.
# In the next N rows, each row has m columns, representing the matrix elements. Each number in the matrix is in the range of 
# -100 to 100.

# Output:
# A matrix whose elements are the absolue value of the original input matrix. This is a so-called absolute matrix.

# Sample input:
# 5 5
# 22 62 -39 -15 37
# -34 95 -85 26 -57
# 8 33 -36 69 -4
# -36 -55 -92 96 -70
# 79 -93 -42 -44 66

# Sample output:
# 22 62 39 15 37
# 34 95 85 26 57
# 8 33 36 69 4
# 36 55 92 96 70
# 79 93 42 44 66

# Constraints:
# 1<=n, m<=500
n, m = map( int, input().split())
for i in range (n):
  x=list(map( int, input().split()))
  for j in range (m):
    print (abs(x[j]), end=' ')
  print('\n')