# Interesting jump
# https://xjoi.net/contest/4936/problem/7

# In a number sequence of n numbers, if the absolute gap between all adjacent forms the sequence 1~n-1 after sorting, this 
# number sequence is called having "interesting jump". For example, the gaps of adjacent numbers in sequence 1, 4, 2, 3 are 
# 3, 2, 1, or 1, 2, 3 after sorting, which indicates that this number sequence has "interesting jump".
# Now you are given a number sequence, please judge if it has "interesting jump". 

# Input:
# First line an integer n. n <= 100000.
# Next line enters n numbers, each <= 100000.

# Output:
# "yes" if there's "interesting jump", "no" otherwise.

# Sample input:
# 4
# 1 4 2 3

# Sample output:
# yes

# Constraints:
# 1<=n<=100000
n= int(input())
l=list(map( int, input().split()))
a=[]
for i in range(0, n):
  if i==n-1:
    break
  x= abs(l[i]-l[i+1])
  a.append(x)
a.sort()
for i in range(1,n):
  if a[i-1]!=i:
    print("no")
    break
  elif i==n-1 and a[i-1]==i:
    print("yes")
    break