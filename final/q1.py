# Simple matrix of Tangent
# https://xjoi.net/contest/4936/problem/3

# Tangent has a matrix of N * M size. She wants to know the sum of values in each row of the matrix, and hopes to find the 
# row number where the maximum sum is located.

# Please help her with the program.

# Input：
# The first line of input has two numbers, N and M, indicating the size of the matrix.
# Next N lines, each line will give M numbers.

# Output：
# The output includes N + 1 lines.
# The first n rows output the sum of the values in the first n rows of the matrix .
# Line n + 1 outputs the line number of the largest sum in the first n lines. If the sum is the same, the line number with the 
# smaller line number should be output.

# sample input：
# 4 5
# -1 0 1 2 3
# 1 2 3 4 5
# 5 4 3 2 1
# 0 0 2 3 -2

# sample output：
# 5
# 15
# 15
# 3
# 2

# Note：
# 1<=n，m<=100.The maximum number in the matrix is 1000000000
n,m = map( int, input().split())
l=[]
sum=0
sums=[]
for i in range(n):
  l.append(list(map(int, input().split())))
for i in range(n):
  for j in range(m):
    sum+=l[i][j]
  print( sum)
  sums.append( sum)
  sum=0
 
for i in range(n):
  h=max(sums)
  if sums[i]==h:
    print(i+1)
    break