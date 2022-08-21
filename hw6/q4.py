# Binary Matrix
# https://xjoi.net/contest/4600/problem/4

# Description:
# Input an n*m matrix, with the only allowed values being 0 and 1. Given one of these, please count how many times a "1" appears 
# in each column.

# Input:
# The first row is two integers n and m.
# Then n rows, each with m integers per row of value 0 or 1

# Output:
# m integers, one per line. Each number represents the count of 1 in the corresponding column.

# Sample input 1:
# 3 5
# 0 0 1 1 0
# 0 1 1 0 1
# 1 0 0 1 0

# Sample output 1:
# 1
# 1
# 2
# 2
# 1

# Sample input 2:
# 5 8
# 1 1 1 0 0 1 0 1
# 0 0 1 1 1 0 1 1
# 1 0 0 1 1 0 1 0
# 0 0 0 0 1 1 1 1
# 0 0 1 1 1 1 1 0

# Sample output 2:
# 2
# 1
# 3
# 3
# 4
# 3
# 4
# 3

# Constraints:
# 1<=n, m<=500
n,m = map( int, input().split())
l=[]
count=0
for i in range(n):
  l.append(list(map(int, input().split())))
 
for i in range(m):
  for j in range(n):
    if l[j][i]==1:
      count+=1
  print(count)
  count=0