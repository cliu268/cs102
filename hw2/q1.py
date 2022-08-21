# Find out numbers
# https://xjoi.net/contest/4388/problem/1

# Description
# Output all the numbers between 1 and n which can be divided by 3 left 2 and divided by 5 left 3 and divided by 7 left 2.

# Input
# One integer.  1<=n<=100000

# Output
# Each line contains a number which satisfies the conditions.

# Sample Input
# 200

# Sample Output
# 23
# 128
n=int(input())
print(*[i for i in range(0,n+1) if i%3==2 and i%5==3 and i%7==2])
