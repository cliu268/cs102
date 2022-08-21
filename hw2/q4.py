# Height of plants
# https://xjoi.net/contest/4388/problem/4

# Description
# Once upon a time there were n small plants in a row. A farmer wanted them to grow faster, so he helped by pulling up a given 
# range of plants a given height every day. Now ask you the final height of each plant after given days.

# Input
# The first line enters an integer n, representing the number of the plants.
# The second line enters n numbers, representing the initial height of each of the plants.
# The third line enters an integer m, representing the total days that the farmer pulls up the plants
# In the next m lines, each line enters three integers a,b,c, representing that from the range of plant a to the plant b, 
# to increase the height c.

# Output
# One line, including n integers, separated by spaces, representing the final height of the plants.

# Sample Input
# 4
# 1 2 3 4
# 3
# 1 2 1
# 2 3 1
# 4 4 1

# Sample Output
# 2 4 4 5
n= int(input())
l=list(map( int, input().split()))
m= int(input())
while m>0:
  a,b,c= map( int, input().split())
  for i in range(a-1, b):
    l[i] += c
  m-=1
print(*l)