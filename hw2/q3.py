# Tree Planting
# https://xjoi.net/contest/4388/problem/3

# Description of the topic:
# There is a road with length n. The endpoints are 0 and n respectively. There are a total of m tree planting operations, 
# each time the each integer point between l and r is planted a tree. Ask how many integer points having trees after each 
# tree planting operation?

# Input format:
# The first line is an integer n indicating the length of the road.
# The second line is an integer m indicating the number of tree planting operations.
# The next m lines are two integers l, r per line.

# Output format:
# A total of m lines, one integer per line, indicating how many integer points have trees after each tree planting.

# Sample input:
# 3
# 2
# 1 2
# 0 1

# Sample output:
# 2
# 3

# Note: n, m does not exceed 1000
n=int(input())
m=int(input())
tree=0
l=[0]*(n+1)
while m>0:
  a,b= map( int, input().split())
  for i in range(a, b+1):
    if l[i]==0:
      l[i]=1
      tree+=1
  print(tree)