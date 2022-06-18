# Calculate A+B(2)
# https://xjoi.net/contest/4356/problem/1 

# 【 Description 】  
# Your task is to compute A plus B.  
# The input will consist of A pair of integers A and B, separated by Spaces, one pair of integers per line. 
# The input here is multiple, infinite.  (All data in int range)  

# 【Sample input】
# 1 5
# 10 20

# 【Sample output】
# 6
# 30
while True:
    a,b = map( int,input().split())
    print(a+b)