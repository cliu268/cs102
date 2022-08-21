# Insertion sort
# https://xjoi.net/contest/4503/problem/1

# Description:
# Input n numbers. Use insertion sorting algorithm to sort these numbers.
# At each step, take the first number in unsorted section and insert into the sorted section. 
# Repeat until all the numbers in sequence s are sorted.
# Output it from small to big. 

# Input:
# The first line: one integer N.
# The second line contains N numbers.  1<=N<=1000 0<=ai<=109  

# Output:
# N integers.

# Sample Input:
# 5
# 1 4 2 3 5

# Sample Output:
# 1 2 3 4 5
n= int(input())
l= list(map(int, input().split()))
for i in range(1,n):
  key=l[i]
  j=i-1
  while j>=0 and key<l[j]:
    l[j+1]=l[j]
    j-=1
  l[j+1]=key
print(*l)