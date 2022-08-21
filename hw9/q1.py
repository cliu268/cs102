# Matrix diagonals
# https://xjoi.net/contest/4773/problem/1 

# 【Description】
# Read in an n*n matrix and print the two diagonals of a square matrix.

# 【Input】
# The first row contains an integer n.(3<=n<=100)
# Then n rows, n integers between 0 and 100 per row

# 【Output】
# The first line of output represents the value of the upper left to lower right diagonal.
# The second line of output represents the value of the bottom left diagonal to the top right diagonal.

# 【Sample input】
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# 【Sample output】
# 1 5 9
# 7 5 3
n=int(input())
l=[]
d2=[]
 
for i in range(n):
  l.append(list(map(int, input().split())))
 
for i in range(n):
  for j in range(n):
    if i==j:
      print(l[i][j], end=' ')
print()
 
for i in range(n):
  for j in range(n):
    if (i+j)==(n-1):
      d2.append(l[i][j])
d2=reversed( d2)
print(*d2)