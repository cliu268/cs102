# Transpose matrix
# https://xjoi.net/contest/4600/problem/2

# Description:
# Given an n*m matrix and output its transpose matrix.
# https://en.wikipedia.org/wiki/Transpose

# Input format:
# The first line contains two integers n, m
# Then enter n lines with m integers per line.

# Output:
# A matrix of m*n, which represents the answer.

# Sample input:
# 5 4
# 3 3 3 4
# 2 0 0 3
# 0 3 1 4
# 3 4 3 3
# 1 0 3 3

# Sample output:
# 3 2 0 3 1
# 3 0 3 4 0
# 3 0 1 3 3
# 4 3 4 3 3

# Constraints:
# 1<=n, m<=500
n,m = map( int, input().split())
a= [ [0]*m for i in range(n) ]
for i in range(n):
  a[i]= list(map( int, input().split()))
for j in range(m):
  for i in range(n):
    print(a[i][j], end=' ')
  print(end='\n')