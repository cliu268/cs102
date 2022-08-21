# Sum of string digits
# https://xjoi.net/contest/4442/problem/4

# Description:
# Given an integer N, please find the sum of all the digits of N.
# Try to calculate it with string processing.

# Input:
# An integer N.

# Output:
# An integer.

# Sample input 1:
# 12345

# Sample output 1:
# 15

# Constraints:
# The length of N is less than or equal to 100.
a=list(input())
sum=0
for i in a:
  sum+=int(i)
print( sum)