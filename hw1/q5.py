# Maoge Number
# https://xjoi.net/contest/4356/problem/5

# Description of the topic
# The maoge defines x as maoge number if and only if the sum of the digits of x is equal to x / 2 rounded down. 
# Now maoge wants to know how many maoge numbers among the divisors of n.

# Input format
# Enter a number n

# Output format
# Output the number of maoge numbers in the divisors of n

# Sample input
# 34

# Sample output
# 1

# data range
# n <= 100000
n= int(input())
number=0
for i in range(1, n+1):
    if n % i == 0:
        if sum(map(int, str(i))) == (i//2):
            number+=1
    else:
        continue
print(number)