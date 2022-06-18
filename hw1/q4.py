# Calculate A+B(3)
# https://xjoi.net/contest/4356/problem/4

# 【 Description 】  
# Your task is to compute A plus B.  
# The input contains multiple test cases.  Each test case contains a pair of integers A and B, one pair per row.  
# When you  input "0 0",the program will end.  (All data in int range)  

# 【Sample input】
# 1 5
# 10 20
# 0 0

# 【Sample output】
# 6
# 30
while True:
    a,b = map( int, input().split())
    if a!=0 and b!=0:
        print(a+b)
    else:
        break