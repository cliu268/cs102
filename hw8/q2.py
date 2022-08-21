# Friendly Pair
# https://xjoi.net/contest/4733/problem/2

# Read in an n*m matrix and define two numbers as friendly if and only if they are adjacent (left, right, up or down) 
# and have the same value. Find the number of friendly pairs.

# Input format:
# The first row contains two integers n, m
# Then n rows, m integers between 0 and 100 per row

# Output format:
# An integer that represents the answer.

# Sample input:
# 5 4
# 3 3 3 4
# 2 0 0 3
# 0 3 1 4
# 3 4 3 3
# 1 0 3 3

# Sample output:
# 7

# Number limit:
# 1<=n, m<=500
x,y=input().split()
m=[]
count=0
for i in range(int(x)):
    m.append(list(map(int, input().split())))
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]==m[i-1][j] and i!=0:
            count+=1
        if i!=int(x)-1 and m[i+1][j]==m[i][j]:
            count+=1       
        if j!=0 and m[i][j-1]==m[i][j]:
            count+=1
        if j!=int(y)-1 and m[i][j+1]==m[i][j]:
            count+=1
print(count//2)