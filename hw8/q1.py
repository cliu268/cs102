# Count the number of 1's
# https://xjoi.net/contest/4733/problem/1

#【Description】
# Can you count the number of 1's that are surrounded completely by 0's in a n*m binary matrix? 
# (from the north, south, east, west directions).

# Input】
# The first row contains two integers n, m(3<=n,m<=100)
# Then n rows, m integers between 0 and 1 per row

#【Output】
# An integer that represents the answer.

#【Sample input】
# 4 4
# 1 0 1 1
# 0 1 0 0
# 1 0 1 0
# 0 0 0 1

#【Sample output】
# 2
a,b = map( int,input().split())
li = []
count = 0
for i in range(a):
  li.append(list(map(int,input().split())))
for i in range(1,a-1):
  for q in range(1,b-1):
    if li[i][q] == 1:
      if li[i-1][q] == 0 and li[i+1][q] == 0 and li[i][q-1] == 0 and li[i][q+1] == 0:
        count += 1
print(count)