# Integer parity sort
# https://xjoi.net/contest/4582/problem/4

# 【describe】
# Given the sequence of 10 integers, it is required to reorder them. Sorting requirements:
# 1. Odd numbers come first and even numbers come last;
# 2. Odd numbers are sorted from large to small;
# 3. Even numbers are sorted from small to large.

# 【input】
# Enter a line containing 10 integers separated by a space. The range of each integer is greater than or equal to 0 and less than 
# or equal to 30000.

# 【output】
# Output a row after sorting as required, including the sorted 10 integers, separated by a space between numbers.

# 【sample input】
# 4 7 3 13 11 12 0 47 34 98

# 【sample output】
# 47 13 11 7 3 0 4 12 34 98
l=list(map(int, input().split()))
even=[]
odd=[]
for i in l:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
 
odd.sort(reverse=True)
even.sort()
print(*odd, *even)