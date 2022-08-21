# Symmetrical Numbers
# https://xjoi.net/contest/4600/problem/5

# Input a n * n matrix. If two different points A(x1, y1), B (x2, y2) satisfy x1 + x2 = n + 1, y1 + y2 = n + 1, and the number 
# at positions A and B are the same, then we say the pair (A, B) is called a symmetric pair. Find the number of symmetric pairs. 
# In this problem, both x and y starts with 1. 
# Hint: (1) How will you adjust the problem to be 0 indexed? (2) x1 = n+1 - x2

# Input format:
# The first line has an integer n
# Then n rows, n integers between 0 and 100 per row

# Output format:
# An integer that represents the answer.

# Sample input:
# 5
# 3 3 3 4 1
# 2 0 0 3 1
# 0 3 1 4 1
# 3 4 3 3 1
# 1 0 3 3 1

# Sample output:
# 3

# Number limit:
# 1<=n<=500
n = int(input())
l = []
count = 0
for i in range(n):
    l.append(list(map(int, input().split())))
    
for i in range(n//2):
    for j in range(n):
        if l[i][j] == l[n-1-i][n-1-j]:
            count += 1
print(count)