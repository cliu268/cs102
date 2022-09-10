# Round to the nearest ten
# https://xjoi.net/contest/4936/problem/5

# Given an integer, round it to the nearest ten.
# 12344-> 12340
# 12399 -> 12400

# System function such as round is not allowed !

# Input:
# A integer N where 1 <= N <= 10^9

# Output:
# The rounded integer n where 1 <= n <=10^9

# Sample Input:
# 99

# Sample Output:
# 100
n=int(input())
if (n%10)<5:
  print((n)-(n%10))
else:
  x=10-(n%10)
  print((n)+(x))