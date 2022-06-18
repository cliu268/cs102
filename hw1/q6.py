# Counting problem
# https://xjoi.net/contest/4356/problem/6

# Title Description:
# How many times does the number x (0 ≤ x ≤ 9) appear in all integers from 1 to n? For example, 
# in 1-11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, the number 1 appears four times.

# Input format:
# Two integers n, x, separated by a space

# Output format:
# An integer representing the number of times x occurs.

# Sample input:
# 11 1

# Sample output:
# 4

# Note: 1<=n<=1000000,0<=x<=9.
n,x = map( int, input().split())
answer=0
for i in range(1, n+1):
    j = i
    while (j > 0):
        z = j % 10
        if z == x:
            answer+=1
        j //= 10
print(answer)