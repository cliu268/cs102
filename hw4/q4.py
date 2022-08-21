# double-sort sequence
# https://xjoi.net/contest/4464/problem/4

# Description:
# A double-sort sequence is defined as following:
# Assuming there are n (n <= 1000) integers, to make a double-sort sequence, the 1st number of the sequence is the largest in 
# all of the numbers, and 2nd number is the smallest, and 3rd number is the second largest, and the 4th number is the second 
# smallest, and so on. Each number can be taken only once. Do this until all numbers have been used exactly once..
# Please program to output the double-sort sequence of these n integers.

# Input format:
# The first line: an integer n
# next n lines: n integers, one integer per line

# Output format:
# n lines, one integer per line, containing the double-sort sequence.

# Sameple input:
# 5
# 10
# -1
# 3
# 3
# -9

# Sample output:
# 10
# -9
# 3
# -1
# 3

# Constraints:
# 1 <= n <= 1000
n= int(input())
l= [int(input()) for i in range(n)]
l.sort()
for i in range(n):
  if i%2==0:
    print(l.pop(-1))
  else:
    print(l.pop(0))