# Array-bomb
# https://xjoi.net/contest/4733/problem/4

# Description
# In a dark and stormy night, you are given a explosion mission. Given a n*m area, where some places have a wall. 
# If you put a bomb at position (i,j), then the wall in i-th row and j-th column would all be destroyed. 
# Now you want to know whether all the walls can be destroyed using only one bomb.

# Input
# The first line is an integer T representing the number of groups of testing data.
# For each group of testing data, the first line enters two numbers n, m representing a n*m area.
# The next n lines, each line contains m characters of '*' representing the wall and '.' representing space.  1<=n,m<=1000

# Output
# In the first line, there's way to destroy all walls by only one bomb, output "YES", otherwise output "NO".
# If the answer is "YES", please output the positon of bomb x,y in the second line separated by space.

# Notice:If you have several ways to solve the problem, output the one who has the smallest row number, then, if there are 
# still several ways, output the one which has the smallest column number. 

# Sample Input
# 2
# 3 4
# .*..
# ....
# .*..

# 3 3
# ..*
# .*.
# *..

# ​Sample Output
# YES
# 1 2
# NO

#### brute force solution that runs TLE when data input is large ####
# def clear_all(mine, n, m, i, j):
#     for x in range(n):
#         for y in range(m):
#             if x != i and y != j and mine[x][y] == '*':
#                 return False
#     return True

# T = int(input())
# while (T):
#     n, m = map( int,input().split())
#     mine = []
#     for i in range(n):
#         mine.append(input())
#     found = False
#     for i in range(n):
#         if found: break
#         for j in range(m):
#             if clear_all(mine, n, m, i, j):
#                 print("YES")
#                 print(i+1, j+1)
#                 found = True
#                 break
#     if found == False:
#         print("NO")
#     T -= 1

#### Good solution that loop through mines ####
def clear_all(mine, i, j):
    for x in mine:
        if i != x[0] and j != x[1]:
            return False
    return True

T = int(input())
while (T):
    n, m = map( int,input().split())
    mine = []
    rows = []
    for i in range(n):
        rows.append(input())
    for i in range(n):
        for j in range(m):
            if rows[i][j] == '*':
                mine.append([i, j])

    found = False
    for i in range(n):
        if found: break
        for j in range(m):
            if clear_all(mine, i, j):
                print("YES")
                print(i+1, j+1)
                found = True
                break
    if found == False:
        print("NO")
    T -= 1

# # XC220068
# T=int(input())
# for z in range(T):
#   n, m=map(int, input().split())
#   x, y=[], []
#   for i in range(n): x.append([t for t in input()])
#   for i in range(n):
#     for j in range(m):
#       bomb=0
#       if x[i][j]=='*': y.append([i, j])
#   for i in range(n):
#     for j in range(m):
#       bomb=0
#       for k in range(len(y)):
#         if i==y[k][0] or j==y[k][1]:
#           continue
#         else:
#           bomb+=1
#           break   
#       if bomb == 0: 
#         print('YES')
#         print(i+1, j+1)
#         break
#     if bomb==0:break
#   if bomb!=0:
#     print('NO')

# # XC220297
# num = int(input())
# for i in range (num):
#     n,m = map(int,input().split())
#     lst,x,y,total =[],[0]*n,[0]*m,0
#     flag = False
#     r,c = -1,-1
#     for j in range (n):
#         lst.append(list(input()))
#         for k in range (m):
#             if lst[j][k]=='*':
#                 x[j]+=1
#                 y[k]+=1
#                 total+=1
#     for j in range (n):
#         for k in range (m):
#             temp =0
#             if lst[j][k]=='*':
#                 temp = 1
#             if x[j]+y[k]-temp  == total:
#                 flag = True
#                 r = j
#                 c = k
#                 break
#         if flag==True:
#             break
#     if flag==False:
#         print("NO")
#     else:
#         print("YES")
#         print(r+1,c+1)

# # XC220013
# T = int(input())
 
# for i in range(T):
#   n, m = map(int, input().split())
#   lst = []
#   walls = 0
#   x = 0
#   wallCoordinates = []
 
#   for j in range(n):
#     string = str(input())
#     sublst = []
#     for i in string:
#       sublst.append(i)
#       if (i == '*'):
#         walls += 1
#     lst.append(sublst)
 
#   for j in range(n):
#     for k in range(m):
#       if (lst[j][k] == '*'):
#         wallRow = j
#         wallColumn = k
 
#   # for j in range(n):
#   #   for k in range(m):
#   #     if (lst[j][k] == '*'):
#   #       walls += 1
 
#   for j in range(n):
#     for k in range(m):
#       if (j == wallRow or k == wallColumn):
#         countOfWalls = 0
#         if (lst[j][k] == '*'):
#           countOfWalls = -1
           
#         for L in range(n):
#           if (lst[L][k] == '*'):
#             countOfWalls += 1
   
#         for L in range(m):
#           if (lst[j][L] == '*'):
#             countOfWalls += 1
   
#         if (countOfWalls == walls):
#           if (x == 0):
#             print('YES')
#             print(str(j + 1), str(k + 1))
#           x = 1
#           break
   
#       if (x == 1):
#         break
 
#   if (x == 0):
#     print('NO')