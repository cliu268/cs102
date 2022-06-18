# Print number triangle
# https://xjoi.net/contest/4356/problem/3

# Description
# Print number triangle.Output begin with 1.The ith line output i integers.Every number in triangle account for 4 positions,
# align right.
# (In C,you can use "%4d" to complete the task:account for 4 positions,allign right)

# Input
# An integer n. 1<=n<=1000

# Output
# N lines,the ith line contains i number.Every number in triangle account for 4 positions,align right.

# Sample Input
# 4

# Sample Output
#    1
#    2   3
#    4   5   6
#    7   8   9  10
n= int(input())
x=0
for i in range(1,n+1):
    for j in range(1, i+1):
        print('%4d'%(x+j), end='')
    print("\n")
    x+=i