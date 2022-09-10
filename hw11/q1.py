# greatest common divisor and least common multiple
# https://xjoi.net/contest/4888/problem/1

# Pelase take two integers as the input, and use the brute-force method to find their greatest common divisor and their 
# least common multiple.

# Sample input:
# 4 6

# Sample output:
# 2
# 12

# time limit:
# 1000

# memory limit:
# 65536
def gcd(a, b):
  while b!=0:
    a, b = b, a%b
  return(a)
 
def lcm(a, b):
  return(int((a*b)/(gcd(a,b))))
 
x,y =map( int, input().split())
print(gcd(x,y))
print(lcm(x,y))