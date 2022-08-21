# Code Your Function 1
# https://xjoi.net/contest/4845/problem/2

# Please write a function to pass the parameters of two non-negative INT types A, B, allowing it to return the value of 
# an INT type of C, and C = max( A mod B, B mod A).

# Input Format:
# The first line is an integer of N, which means that there are a total of N calls.
# For next N row, there are two positive INT per row A, B, representing the parameter of a call.

# Output Format:
# A total of N rows, one integer per row, represents the return value of the function.

# Sample Input
# 3
# 2 5
# 18 27
# 192 79

# Sample Output
# 2
# 18
# 79

# Data range
# 1 <= N <= 10^5 
# 1 <= A, B <= 10^31
# 1S, 256M
def mod_bigger(a, b):
  a_mod = a%b
  b_mod = b%a
  if a_mod > b_mod:
    return a
  else:return b
n = int(input())
for i in range(n):
  a, b = map( int, input().split())
  print(mod_bigger(a,b))