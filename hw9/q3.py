# Circular matrix
# https://xjoi.net/contest/4773/problem/3

# 【Description】
# Read in an n*n matrix and print the circular matrix.

# 【Input】
# The first row contains an integer n.(1<=n<=100)

# 【Output】
# The output consists of N lines, each line contains n positive integers separated by spaces, and each positive integer 
# occupies two characters in width.

# 【Sample input1】
# 4

# 【Sample output2】
# 1 1 1 1 
# 1 2 2 1 
# 1 2 2 1 
# 1 1 1 1

# 【Sample input2】
# 5

# 【Sample output2】
# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1
n= int(input())
l=[ [0]*n for i in range(n) ]
max=1

if n%2==0:
    max=n/2
else:
    max= (n//2)+1

for i in range(n):
    for j in range(n):
        if i < max:
            if j < max:
                if j<(i+1):
                    print(j+1, end=' ')
                else:
                    print(i+1, end=' ')
            else:
                if (n - j) > (i+1):
                    print(i+1, end=' ')
                else:
                    print(n-j, end=' ')
        else: # i >= max
            if j < max:
                if j < (n - i):
                    print(j+1, end=' ')
                else:
                    print(n - i, end=' ')
            else:
                if (n - j) > (n - i):
                    print(n-i, end=' ')
                else:
                    print(n-j, end=' ')            
    print()