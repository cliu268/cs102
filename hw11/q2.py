# Verify Goldbach's conjecture
# https://xjoi.net/contest/4888/problem/2

# Please help verify the Goldbach's conjecture, which is the following. Every even number greater than 2 is the sum of two prime 
# numbers. Enter the even number N (N>=4), please output an expression of N that proves Goldbach's conjecture. Please see the 
# examples below.

# 4=2+2
# 6=3+3
# 8=3+5
# 10=3+7
# 12=5+7
# 100=47+53

# Sample input:
# 4

# Sample output:
# 4=2+2

# time limit:
# 1000

# memory limit:
# 65536

# Hint:
# Requirement: Please output the expression with the smallest prime number possible. In the expression, please put the 
# smaller number first.
def prime(x):
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
 
x= int(input())
for i in range(1, (x//2)+1):
  if prime(i):
    if prime(x-i):
      a= min(i, x-i)
      b= max(i, x-i)
      print(x, '=', a, '+', b, sep='')
      break