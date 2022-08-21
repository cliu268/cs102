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
def clear_all(mine, n, m, i, j):
    for x in range(n):
        for y in range(m):
            if x != i and y != j and mine[x][y] == '*':
                return False
    return True

T = int(input())
while (T):
    n, m = map( int,input().split())
    mine = []
    for i in range(n):
        mine.append(input())
    # found = False
    # for i in range(n):
    #     if found: break
    #     for j in range(m):
    #         if clear_all(mine, n, m, i, j):
    #             print("YES")
    #             print(i+1, j+1)
    #             found = True
    #             break
    # if found == False:
    #     print("NO")
    row = 0
    col = 0
    rc = 0
    cc = 0
    for i in range(n):
        for j in range(m):
            if mine[i][j] == '*':

    T -= 1
