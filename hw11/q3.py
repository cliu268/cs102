# Seek for prime factors
# https://xjoi.net/contest/4888/problem/3?locale=en

# Give many integers. For each integer X, return the number of different prime factors of X.
# For example, if the number is 252, and 252 = 2 x 2 x 3 x 3 x 7, the different factors are 2,3,7, The count is 3

# Input Format
# The first line is an integer of q, which means that there is a q group query.
# For next q rows, each row contains one positive integer X, indicating one query.

# Output Format
# A total of q rows, each contain an integer representing the answer to a group of queries.

# Sample Input
# 2
# 48
# 252

# Sample Output
# 2
# 3
def prime(x):
    sum=0
    for i in range(2, x):
        if is_prime(x):
            return sum+1        
        if x%i==0 and is_prime(i):
            sum+=1
            while x%i==0:
                x //= i
    return(sum)

def is_prime(x):
    h=int(x**(1/2))
    if x==1:
        return False
    if x==2:
        return True
    if x%2==0 and x!=2:
        return False
    
    for i in range(3, h+1):
        if x%i==0:
            return False
    return True

import time
n= int(input())
#sm = int(round(time.time() * 1000))
for i in range(n):
    a=int(input())
    print(prime(a))
# em = int(round(time.time() * 1000))
# print(em-sm)    