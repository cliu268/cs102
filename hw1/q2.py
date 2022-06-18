# Calculate A+B(5)
# https://xjoi.net/contest/4356/problem/2

# 【 Description 】  
# Your task is to compute A plus B.  
# The input contains multiple test cases, one row per use case.  Each case starts with an integer n, and then n integers 
# follow on the same line.  (All data in int range)  

# 【Sample input】
# 4 1 2 3 4
# 5 1 2 3 4 5

# 【Sample output】
# 10
# 15
while True:
    l= list(map(int, input().split()))
    sum=0
    x= l[0]
    for i in range(1, x+1):
        sum+= l[i]
    print(sum)