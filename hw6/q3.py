# Matrix exchange
# https://xjoi.net/contest/4600/problem/3

# Title Description:
# Read in an n*m matrix, perform Q number of exchanges of specified two rows, and output the final matrix.

# Input format:
# The first row has three integers n, m, Q
# Followed by the matrix
# Then Q lines, two integers X and Y in each row, and represent exchanging X and Y lines of the matrix.

# Output format:
# A matrix representing the answer.

# Sample input 1:
# 5 5 5
# 21 63 94 12 82
# 16 4 13 82 34
# 37 65 42 52 3
# 78 99 9 65 18
# 7 78 79 99 79
# 4 5
# 4 5
# 3 5
# 2 1
# 2 1

# Sample output 1:
# 21 63 94 12 82
# 16 4 13 82 34
# 7 78 79 99 79
# 78 99 9 65 18
# 37 65 42 52 3

# Appointment:
# 1 <= n, m <= 2000, Q <== 1000000
n,m,Q= map( int, input().split())
l=[]
for i in range(n):
  l.append(list(map(int, input().split())))
 
for i in range(Q):
  f,s=map( int, input().split())
  temp=l[f-1]
  l[f-1]=l[s-1]
  l[s-1]=temp
 
for i in range(n):
  print("\n")
  for j in range(m):
    print(l[i][j], end=' ')