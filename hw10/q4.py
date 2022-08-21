# passing two-dimensional matrix
# https://xjoi.net/contest/4845/problem/4

# Description:
# Enter two n*n matrices and output a matrix representing the sum of the two matrices.

# Use a function to calculate the sum of the two matrices and save them in another matrix.

# Please think about how lists are passed into functions when writing your solution.

# Input 
# Enter a $n$ in the first line
# Next, enter a matrix for the $n*n$ line.
# Then enter another matrix in $n*n$ lines

# Output :
# Output a matrix representing the sum of the two matrices.

# Sample input:
# 2
# 1 2
# 3 4
# 5 6
# 7 8

# Sample output:
# 6 8
# 10 12
n= int(input())
a=[]
b=[]
c=[ [0]*n for i in range(n) ]
for i in range(n):
  a.append(list(map(int, input().split())))
for i in range(n):
  b.append(list(map(int, input().split())))
 
for i in range(n):
  for j in range(n):
    c[i][j]=a[i][j]+b[i][j]
 
for i in range(n):
  print(*(c[i]))
