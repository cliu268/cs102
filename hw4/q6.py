# Array Rearrangement
# https://xjoi.net/contest/4464/problem/6
 
# Description
# Given a sequence of n numbers, please rearrange them to be x1, x2, x3,, xn-1,xn, to maximize the value of 
# (x1-x2)+(x2-x3)+...+(xn-1-xn), and also please keep the 2nd number to the second last number sorted in increasing order.

# Input
# The first line is a integer n.
# The second line input n integers.  2<=n<=100 |ai|<=1000

# Output
# Rearranged list of numbers that can maximize the value of  (x1-x2)+(x2-x3)+...+(xn-1-xn), and please keep the 2nd number to 
# the second last number sorted in increasing order.

# Sample Input
# 5
# 100 -100 50 0 -50

# ​Sample Output
# 100 -50 0 50 -100
n=int(input())
l=list(map(int, input().split()))
l.sort()
l[0],l[-1] = l[-1],l[0]
print(*l)