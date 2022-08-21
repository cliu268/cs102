# Diagonal matrix traversal
# https://xjoi.net/contest/4773/problem/2

# 【Description】
# Read in an n*n matrix and print all the diagonals of the matrix.For the bottom left to top right diagonal.

# 【Input】
# The first row contains an integer n.(3<=n<=100)
# Then n rows, n integers between 0 and 100 per row

# 【Output】
#  print all the diagonals of the matrix

# 【Sample input】
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# 【Sample output】
# 1 
# 4 2 
# 7 5 3 
# 8 6 
# 9
num  = int(input())
mat = []
for i in range(num):
    mat.append(list(map(int,input().split())))
for i in range(num):
    for j in range (0, i+1):
        print(mat[i-j][0+j],end=" ")
    print()
for i in range (1,num,1):
    for j in range (0,(num-i)):
        print(mat[num-1-j][i+j],end=" ")
    print()
