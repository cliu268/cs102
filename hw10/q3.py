# Class of mathematics
# https://xjoi.net/contest/4845/problem/3

# A teacher defines 3 numbers:

# PRM number: Numbers that satisfies both the condisions below.
# 1. It is an odd number;
# 2. It is a prime number

# BCL number: Numbers that satisfies both the condisions below.
# 1. If it can not be divided by 100 exactly, and it has a remainder of 1 when divided by 4.
# 2. If it can be divided by 100 exactly, it can be divided by 400 with the remainder as 1, 
# and it can be divided by 3200 with the remainder not as 1.

# MDN number: Numbers that satisfies both the condisions below.
# 1. The number's only common divisor with 654729075 is 1 (coprime).
# 2. Not a PRM number

# The teacher will provide N numbers as the input. Please calculate the sum of all PRM, BCL, and MDN numbers respectively, 
# and print them out.
# Each number can be classified into multiple types of numbers defined above.

# Input Format
# The first line is a number N, and the next line is a number in each row.

# Output Format
# A total of three lines, followed by the sum of all PRM, BCL and MDN numbers.

# Sample Input
# 5
# 15
# 26
# 5
# 28
# 8

# Sample Output
# 5
# 5
# 8
PRM=0
BCL=0
MDN=0
 
def prm(x):
  h=int(x**(1/2))
  if x==1:
    return False
  if x%2==0:
    return False
   
  for i in range(3, h+1):
    if x%i==0:
      return False
  return True
 
def bcl(x):
  if x %100 != 0 and x%4 == 1 or x%100 == 0 and x%400 > 1 and x% 3200 < 1:
    return True
  else:
    return False
 
def mdn(x):
  if prm(x):
    return False
  if x%3==0 or x%5==0 or x%7==0 or x%11==0 or x%13==0 or x%17==0 or x%19==0:
      return False
  else:
    return True
 
n=int(input())
for i in range(n):
  a=int(input())
  if prm(a): PRM+=a
  if bcl(a): BCL+=a
  if mdn(a): MDN+=a
 
print(PRM)
print(BCL)
print(MDN)