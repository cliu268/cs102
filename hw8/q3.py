# Array-Minesweeper
# https://xjoi.net/contest/4733/problem/3

# Description
# Minesweeper is a very classic PC game. Given a m*n board, some positions have one mine. At the beginning players can not see 
# the mines. When players click a position, it will show a number n which means there are n mines around it in all eight 
# neighboring positions.
# Now given the exact position of every mine. Please calculate the number in every position that has no mine.

# Input
# the first line includes two integers n,m.  1<=n,m<=100
# The next n lines,each line input a string of length m.
# Only two charcter can be used:'*','?'. ? means there is no mine in this position,* means there is one mine in this position.

# Output
# the output includes n lines,each line contains m characters. Use '*' to represent the position with a mine, and use a number 
# to represent the number of mines around this position. 

# Sample Input1
# 3 3
# *??
# ???
# ?*?

# ​Sample Output1
# *10
# 221
# 1*1

# Sample Input2
# 2 3
# ?*?
# *??

# ​Sample Output2
# 2*1
# *21
x, y=input().split()
x=int(x)
y=int(y)
mine=[]
count=0
for i in range(int(x)):
    mine.append(input())
for i in range(x):
    for j in range(y):
        if mine[i][j]!='*':
            for a in range(-1,2):
                for b in range(-1, 2):
                    if(a==0 and b==0):
                        continue
                    if i+a<0 or j+b<0 or i+a>=x or j+b>=y:
                        continue
                    if mine[i+a][j+b]=='*':
                        count+=1
            mine[i]=mine[i][:j]+ str(count) + mine[i][j+1:]
            count=0
print(*mine, sep='\n')