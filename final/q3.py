# Beautiful matrix
# https://xjoi.net/contest/4936/problem/6

# Here is a 3*3 matrix.
# 2  3  3
# 2  3  3
# 2  3  3

# Now input a 5*5 matrix, in this matrix only one cell is 1, all the other cells are 0. We call a matrix  "beautiful" if the 
# center of the matrix (the position is row 3,column 3) is 1 while the others are 0. Every time you can exchange two numbers 
# with the two adjacent positions. Please calculate how many steps are required to make a matrix "beautiful".

# Input:
# A 5*5 matrix.Each number is separated by spaces. In your input, only one position is 1, while the other positions are 0.

# Output:
# One integer represent the least number of exchanges needed to make the matrix beautiful..

# Sample Input:
# 0 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

# Sample Output:
# 3

# Hint:
# It takes 3 steps from the position of 1 to the center. 
l=[]
for i in range( 5):
  l.append(list(map(int, input().split())))
 
for i in range( 5):
  for j in range( 5):
    if l[i][j]==1:
      print(abs(i-2)+abs(j-2))